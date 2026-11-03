"""Excel automation that works alongside heavyweight add-ins (CapIQ, FactSet, Bloomberg).

Plain COM activation (`DispatchEx("Excel.Application")`) loads every COM add-in; the
S&P Capital IQ add-in opens a sign-in web view at startup and Excel never finishes
registering with COM ("Server execution failed"), leaving a hung process. So the
workbook is opened in a *separate* Excel started in safe mode (no add-ins, no
templates) with the automation switch, and we attach to that specific process through
the accessibility API. Nothing of the user's running Excel is touched.
"""
from __future__ import annotations

import ctypes
import subprocess
import time
import uuid
from pathlib import Path
from typing import Optional

EXCEL_EXE_CANDIDATES = [
    r"C:\Program Files\Microsoft Office\Root\Office16\EXCEL.EXE",
    r"C:\Program Files\Microsoft Office\Office16\EXCEL.EXE",
    r"C:\Program Files (x86)\Microsoft Office\Root\Office16\EXCEL.EXE",
]


def find_excel() -> str:
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\excel.exe") as k:
            return winreg.QueryValue(k, None)
    except OSError:
        pass
    for c in EXCEL_EXE_CANDIDATES:
        if Path(c).exists():
            return c
    raise RuntimeError("Excel not found")


def _excel7_hwnd(pid: int) -> Optional[int]:
    import win32gui
    import win32process
    found = []

    def top(h, _):
        try:
            _, p = win32process.GetWindowThreadProcessId(h)
        except Exception:
            return True
        if p == pid and win32gui.GetClassName(h) == "XLMAIN":
            def child(ch, acc):
                if win32gui.GetClassName(ch) == "EXCEL7":
                    acc.append(ch)
                return True
            win32gui.EnumChildWindows(h, child, found)
        return True

    win32gui.EnumWindows(top, None)
    return found[0] if found else None


def _dismiss_startup_dialogs(pid: int) -> int:
    """Safe-mode Excel may show a modal such as 'Excel has detected that you have recovered
    files...' before the object model is ready. Click its OK button so the session never
    stalls and nothing appears on the analyst's screen. Returns the number dismissed."""
    import win32con
    import win32gui
    import win32process
    BM_CLICK = 0x00F5
    hits = []

    def top(h, _):
        try:
            _, p = win32process.GetWindowThreadProcessId(h)
        except Exception:
            return True
        if p == pid and win32gui.GetClassName(h) == "#32770" and win32gui.IsWindowVisible(h):
            hits.append(h)
        return True

    win32gui.EnumWindows(top, None)
    # Office's own dialogs (the "recovered files" message) are NUIDialog windows, not #32770
    nui = []

    def top2(h, _):
        try:
            _, p = win32process.GetWindowThreadProcessId(h)
        except Exception:
            return True
        if p == pid and win32gui.GetClassName(h) == "NUIDialog" and win32gui.IsWindowVisible(h):
            nui.append(h)
        return True

    win32gui.EnumWindows(top2, None)
    n = 0
    for h in hits:
        buttons = []

        def child(ch, acc):
            if win32gui.GetClassName(ch) == "Button" and win32gui.GetWindowText(ch).replace("&", "").strip().upper() in ("OK", "YES", "CLOSE", "DON'T SAVE"):
                acc.append(ch)
            return True

        win32gui.EnumChildWindows(h, child, buttons)
        if buttons:
            win32gui.SendMessage(buttons[0], BM_CLICK, 0, 0)
            n += 1
        else:
            win32gui.PostMessage(h, win32con.WM_CLOSE, 0, 0)
            n += 1
    for h in nui:
        # Enter activates the default button (OK); WM_CLOSE as a fallback
        for target in (h,) + tuple(_children(h)[:3]):
            win32gui.PostMessage(target, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            win32gui.PostMessage(target, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        win32gui.PostMessage(h, win32con.WM_CLOSE, 0, 0)
        n += 1
    return n


def _children(h: int) -> list:
    import win32gui
    out = []

    def cb(ch, acc):
        acc.append(ch)
        return True

    try:
        win32gui.EnumChildWindows(h, cb, out)
    except Exception:
        pass
    return out


def _attach(hwnd: int):
    """IDispatch of the Window object behind an EXCEL7 hwnd -> Application."""
    import pythoncom
    import win32com.client
    OBJID_NATIVEOM = -16
    iid = uuid.UUID("{00020400-0000-0000-C000-000000000046}")  # IID_IDispatch
    guid = ctypes.create_string_buffer(iid.bytes_le, 16)
    ptr = ctypes.c_void_p()
    res = ctypes.oledll.oleacc.AccessibleObjectFromWindow(ctypes.c_int(hwnd), ctypes.c_int(OBJID_NATIVEOM), guid, ctypes.byref(ptr))
    if res != 0 or not ptr.value:
        raise RuntimeError(f"AccessibleObjectFromWindow failed: {res}")
    disp = pythoncom.ObjectFromAddress(ptr.value, pythoncom.IID_IDispatch)
    window = win32com.client.Dispatch(disp)
    return window.Application


class ExcelSession:
    """Open a workbook in a private safe-mode Excel; `.app` and `.wb` are COM objects.

        with ExcelSession(path) as xl:
            xl.app.CalculateFullRebuild(); xl.wb.Save()
    """

    def __init__(self, path: str, timeout: float = 90.0, read_only: bool = False):
        self.path = str(Path(path).resolve())
        self.timeout = timeout
        self.read_only = read_only
        self.proc = None
        self.app = None
        self.wb = None

    def __enter__(self):
        args = [find_excel(), "/x", "/safe", "/automation"]
        if self.read_only:
            args.append("/r")
        args.append(self.path)
        self.proc = subprocess.Popen(args)
        t0 = time.time()
        hwnd = None
        while time.time() - t0 < self.timeout:
            _dismiss_startup_dialogs(self.proc.pid)
            hwnd = _excel7_hwnd(self.proc.pid)
            if hwnd:
                break
            if self.proc.poll() is not None:
                raise RuntimeError("Excel exited before opening the workbook (another instance may have taken the file)")
            time.sleep(0.5)
        if not hwnd:
            self.close(force=True)
            raise RuntimeError("timed out waiting for Excel to open the workbook")
        last = None
        t1 = time.time()
        want = Path(self.path).name.lower()
        while time.time() - t1 < self.timeout:
            _dismiss_startup_dialogs(self.proc.pid)
            try:
                app = _attach(hwnd)
                wb = app.ActiveWorkbook
                if wb is None or wb.Name.lower() != want:
                    wb = None
                    for w in app.Workbooks:
                        if w.Name.lower() == want:
                            wb = w
                            break
                if wb is not None:
                    app.DisplayAlerts = False
                    try:
                        app.Visible = False
                    except Exception:
                        pass
                    try:
                        # no auto-recovery files from automation sessions (restored before any save)
                        wb.EnableAutoRecover = False
                    except Exception:
                        pass
                    self.app, self.wb = app, wb
                    break
            except Exception as e:  # the object model is not ready yet (or a call was rejected while Excel is busy)
                last = e
            time.sleep(1.0)
        if self.wb is None:
            self.close(force=True)
            raise RuntimeError(f"could not attach to the Excel instance: {last!r}")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def save(self):
        """Save the workbook with its normal auto-recovery setting restored."""
        try:
            self.wb.EnableAutoRecover = True
        except Exception:
            pass
        self.wb.Save()
        try:
            self.wb.EnableAutoRecover = False
        except Exception:
            pass

    def close(self, force: bool = False):
        import gc
        try:
            if self.wb is not None:
                self.wb.Close(SaveChanges=False)
        except Exception:
            pass
        try:
            if self.app is not None:
                self.app.Quit()
        except Exception:
            pass
        self.wb = None
        self.app = None
        gc.collect()
        if self.proc is not None:
            for _ in range(30):
                if self.proc.poll() is not None:
                    return
                time.sleep(0.5)
            if force or self.proc.poll() is None:
                self.proc.kill()

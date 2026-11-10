param([string]$Path, [string]$PngDir)
# Excel formatting pass for 2026-10-31_core_lab_X10B_100c_int_vs_ext.xlsx: recalc, Garamond fonts, legend outside the plot, export PNGs.
$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false; $xl.DisplayAlerts = $false
$wb = $xl.Workbooks.Open($Path)
$ws = $wb.Worksheets.Item(1)
$xl.CalculateFull()
$i = 1
foreach ($co in $ws.ChartObjects()) {
  $ch = $co.Chart
  $ch.ChartArea.Font.Name = "Garamond"; $ch.ChartArea.Font.Size = 11
  $ch.ChartTitle.Font.Size = 12; $ch.ChartTitle.Font.Bold = $true
  if ($ch.HasLegend) { $ch.Legend.Position = -4160; $ch.Legend.IncludeInLayout = $true; $ch.Legend.Font.Size = 11 }
  $ch.Axes(1).TickLabelSpacing = 3
  $ch.Axes(2).MinimumScale = 0
  $ch.ChartArea.Border.LineStyle = -4142
  # stack title, legend and plot so nothing overlaps
  $ch.ChartTitle.Top = 4
  $below = $ch.ChartTitle.Top + $ch.ChartTitle.Height + 2
  if ($ch.HasLegend) { $ch.Legend.Top = $below; $ch.Legend.Left = ($ch.ChartArea.Width - $ch.Legend.Width) / 2; $below = $ch.Legend.Top + $ch.Legend.Height + 4 }
  $ch.PlotArea.InsideTop = $below + 10
  $ch.PlotArea.InsideHeight = $ch.ChartArea.Height - $ch.PlotArea.InsideTop - 30
  $ch.Refresh()
  if ($PngDir) { $co.Activate(); [void]$ch.Export((Join-Path $PngDir "x10b_chart$i.png")) }
  $i++
}
$wb.Save(); $wb.Close($true); $xl.Quit()
[void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl)
"formatted $($i - 1) charts"

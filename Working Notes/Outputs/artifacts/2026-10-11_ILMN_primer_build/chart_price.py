p=[214.19,199.19,232.54,205.55,196.64,187.48,192.14,165.21,137.27,109.42,101.95,139.23,
143.00,139.82,137.31,123.05,104.28,104.38,122.60,131.40,130.41,144.14,144.15,133.63,
132.74,88.74,79.34,77.60,82.24,95.41,102.71,99.96,94.97,123.54,131.45,131.16,
144.81,134.46,123.26,126.74,162.96,175.83,205.10,213.63,273.68,278.17]
W,H=720,330; x0,x1=52,700; y0,y1=40,290; ymax=320
def X(i): return x0+i*(x1-x0)/(len(p)-1)
def Y(v): return y1-(v/ymax)*(y1-y0)
out=[]
out.append(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Illumina month-end share price, January 2023 to 9 October 2026, with key events">')
for g in (0,100,200,300):
    out.append(f'<line x1="{x0}" y1="{Y(g):.1f}" x2="{x1}" y2="{Y(g):.1f}" stroke="var(--rule)"{"" if g==0 else " stroke-dasharray=\"3 3\""}/>')
    out.append(f'<text x="{x0-6}" y="{Y(g)+4:.1f}" text-anchor="end">${g}</text>')
for i,lab in ((0,"2023"),(12,"2024"),(24,"2025"),(36,"2026")):
    out.append(f'<line x1="{X(i):.1f}" y1="{y1}" x2="{X(i):.1f}" y2="{y1+5}" stroke="var(--muted)"/>')
    out.append(f'<text x="{X(i)+4:.1f}" y="{y1+18}">{lab}</text>')
pts=" ".join(f"{X(i):.1f},{Y(v):.1f}" for i,v in enumerate(p))
area=f"{X(0):.1f},{y1} "+pts+f" {X(len(p)-1):.1f},{y1}"
out.append(f'<polygon points="{area}" fill="var(--accent-soft)"/>')
out.append(f'<polyline points="{pts}" fill="none" stroke="var(--accent)" stroke-width="2.2"/>')
ev=[(2,"Apr-23 peak $233",-1),(10,"Nov-23: 2nd guide cut",2),(17,"Jun-24 GRAIL spin",1),(25,"Feb-25: China list, weak guide",-1),(27,"Apr-25 low $70",1),(33,"Oct-25: +24.8% on Q3",-1),(37,"Feb-26: guide −10%",1),(40,"May-26: Q1 beat",-1),(44,"Sep-26: S&amp;P 500",-1),(45,"$278",1)]
for i,t,d in ev:
    xx,yy=X(i),Y(p[i])
    out.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="3.5" fill="var(--warn)"/>')
    ty = yy-12 if d<0 else (yy+38 if d==2 else yy+20)
    anchor = "end" if i>=40 else ("start" if i<5 else "middle")
    out.append(f'<text x="{xx:.1f}" y="{ty:.1f}" text-anchor="{anchor}">{t}</text>')
out.append('</svg>')
print("\n".join(out))

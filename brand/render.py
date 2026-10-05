#!/usr/bin/env python3
import sys, subprocess, pathlib
d = pathlib.Path(sys.argv[1]).resolve()
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
def svg(name):
    p = d / name
    return p.read_text() if p.exists() else "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><rect width='512' height='512' fill='#f00'/></svg>"
mark, mono, lockup = svg("mark.svg"), svg("mark-mono.svg"), svg("lockup.svg")
html = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
html,body{{margin:0;width:1600px;background:#fff;font-family:Inter,sans-serif;color:#1d1d1f}}
.sheet{{display:grid;grid-template-columns:1fr 1fr;width:1600px}}
.cell{{padding:40px;display:flex;flex-direction:column;gap:24px;align-items:center;justify-content:center;min-height:420px}}
.light{{background:#fff}} .dark{{background:#000;color:#f5f5f7}}
.row{{display:flex;gap:40px;align-items:center}}
.sz{{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:12px;color:#86868b}}
svg{{display:block}}
.lockup svg{{height:96px;width:auto}}
.mark svg{{height:var(--s);width:var(--s)}}
.label{{font-size:13px;color:#86868b;letter-spacing:.04em;text-transform:uppercase}}
</style></head><body>
<div class="sheet">
  <div class="cell light"><div class="label">Lockup, light</div><div class="lockup">{lockup}</div></div>
  <div class="cell dark"><div class="label">Lockup, dark</div><div class="lockup">{lockup}</div></div>
  <div class="cell light"><div class="label">Mark at 256 / 64 / 32 / 16</div><div class="row">
    <div class="sz"><div class="mark" style="--s:256px">{mark}</div>256</div>
    <div class="sz"><div class="mark" style="--s:64px">{mark}</div>64</div>
    <div class="sz"><div class="mark" style="--s:32px">{mark}</div>32</div>
    <div class="sz"><div class="mark" style="--s:16px">{mark}</div>16</div></div></div>
  <div class="cell dark"><div class="label">Mark on black + mono at 256 / 64 / 32</div><div class="row">
    <div class="sz"><div class="mark" style="--s:256px">{mark}</div>256</div>
    <div class="sz"><div class="mark" style="--s:64px">{mono}</div>mono 64</div>
    <div class="sz"><div class="mark" style="--s:32px">{mono}</div>mono 32</div></div></div>
</div></body></html>"""
(d / "_sheet.html").write_text(html)
subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1600,840", "--virtual-time-budget=6000",
                f"--screenshot={d/'preview.png'}", f"file://{d/'_sheet.html'}"], stderr=subprocess.DEVNULL)
for s in (16, 32, 512):
    h = f"<!doctype html><html><body style='margin:0;background:transparent'><div style='width:{s}px;height:{s}px'>{mark}</div><style>svg{{width:{s}px;height:{s}px;display:block}}</style></body></html>"
    (d / f"_m{s}.html").write_text(h)
    subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={s},{s}", "--default-background-color=00000000",
                    f"--screenshot={d/f'mark-{s}.png'}", f"file://{d/f'_m{s}.html'}"], stderr=subprocess.DEVNULL)
print("rendered:", d / "preview.png")

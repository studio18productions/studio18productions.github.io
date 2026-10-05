#!/usr/bin/env python3
"""Build the logo comparison page from concept folders.
Usage: python3 build_compare.py <out.html> key1:Name:Blurb key2:Name:Blurb ...
Each key maps to <logo>/<key>/ containing mark.svg, mark-mono.svg, lockup.svg.
"""
import sys, pathlib, html, re
L = pathlib.Path(__file__).resolve().parent
out = pathlib.Path(sys.argv[1])
items = [a.split(':', 2) for a in sys.argv[2:]]

def svg(folder, name):
    p = L / folder / name
    s = p.read_text() if p.exists() else ''
    # strip xml prolog if any
    return re.sub(r'<\?xml[^>]*\?>', '', s).strip()

cards = []
for i, (key, name, blurb) in enumerate(items, 1):
    mark, mono, lockup = svg(key, 'mark.svg'), svg(key, 'mark-mono.svg'), svg(key, 'lockup.svg')
    cards.append(f"""
<section class="opt" id="{html.escape(key)}">
  <div class="head"><span class="n">Option {i}</span><h2>{html.escape(name)}</h2><p>{html.escape(blurb)}</p></div>
  <div class="pair">
    <div class="panel light"><div class="lab">Lockup on white</div><div class="lockup">{lockup}</div></div>
    <div class="panel dark"><div class="lab">Lockup on black</div><div class="lockup">{lockup}</div></div>
  </div>
  <div class="pair">
    <div class="panel light">
      <div class="lab">Mark at 256, 64, 32 and 16 px</div>
      <div class="sizes"><span class="m" style="--s:256px">{mark}</span><span class="m" style="--s:64px">{mark}</span><span class="m" style="--s:32px">{mark}</span><span class="m" style="--s:16px">{mark}</span></div>
    </div>
    <div class="panel dark">
      <div class="lab">Single color, on black</div>
      <div class="sizes"><span class="m" style="--s:256px">{mono}</span><span class="m" style="--s:64px">{mono}</span><span class="m" style="--s:32px">{mono}</span><span class="m" style="--s:16px">{mono}</span></div>
    </div>
  </div>
  <div class="ctx">
    <div class="lab">In context</div>
    <div class="browser"><div class="tabbar"><span class="tab"><span class="fav">{mark}</span>Studio 18 Productions</span><span class="tab ghost">New tab</span></div>
      <div class="nav"><span class="brand"><span class="nm">{mono}</span>Studio 18</span><span class="links"><i>Photography</i><i>Video</i><i>AI Video</i><i>AI Apps</i></span></div>
      <div class="page"><div class="h1">Studio 18 Productions</div><div class="h2">Photography. Video. AI. One studio.</div></div>
    </div>
    <div class="icons"><div class="lab">App icon and social avatar</div><div class="irow"><span class="appicon">{mark}</span><span class="avatar">{mark}</span><span class="avatar dk">{mono}</span></div></div>
  </div>
</section>""")

page = f"""<title>Studio 18 Logo Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
:root{{--bg:#fbfbfd;--ink:#1d1d1f;--ink2:#6e6e73;--line:#e8e8ed;--card:#fff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,-apple-system,Helvetica,Arial,sans-serif;font-size:17px;line-height:1.47;letter-spacing:-.02em;padding-block:48px 96px;padding-inline:22px}}
.wrap{{max-width:1180px;margin:0 auto}}
h1{{font-size:clamp(34px,5vw,56px);letter-spacing:-.035em;line-height:1.05;margin:0 0 10px;font-weight:600}}
.intro{{color:var(--ink2);font-size:21px;max-width:60ch;margin:0 0 56px}}
.opt{{background:var(--card);border-radius:28px;padding:36px;margin-bottom:28px;box-shadow:0 2px 14px rgba(0,0,0,.05)}}
.head{{display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:baseline;margin-bottom:24px}}
.head .n{{font-size:13px;font-weight:600;color:var(--ink2);letter-spacing:.06em;text-transform:uppercase}}
.head h2{{margin:0;font-size:32px;letter-spacing:-.03em;font-weight:600}}
.head p{{grid-column:2;margin:0;color:var(--ink2);max-width:70ch}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}}
.panel{{border-radius:18px;padding:28px;min-height:200px;display:flex;flex-direction:column;gap:18px;justify-content:center;align-items:center}}
.panel.light{{background:#f5f5f7;color:#1d1d1f}} .panel.dark{{background:#000;color:#f5f5f7}}
.lab{{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#86868b;align-self:flex-start}}
.lockup svg{{height:72px;width:auto;display:block}}
.sizes{{display:flex;gap:36px;align-items:center;flex-wrap:wrap;justify-content:center}}
.m svg{{width:var(--s);height:var(--s);display:block}}
.ctx{{display:grid;grid-template-columns:2fr 1fr;gap:14px}}
.ctx>.lab{{grid-column:1/-1}}
.browser{{border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#fff}}
.tabbar{{background:#e8e8ed;padding:8px 10px 0;display:flex;gap:6px;font-size:12px}}
.tab{{background:#fff;border-radius:8px 8px 0 0;padding:7px 12px;display:flex;gap:8px;align-items:center;color:#1d1d1f}}
.tab.ghost{{background:transparent;color:#86868b}}
.fav svg{{width:16px;height:16px;display:block}}
.nav{{background:rgba(0,0,0,.92);color:#f5f5f7;height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 18px;font-size:12px}}
.brand{{display:flex;align-items:center;gap:8px;font-weight:600;font-size:14px;white-space:nowrap}}
.nm svg{{width:20px;height:20px;display:block}}
.links{{display:flex;gap:18px;overflow:hidden}} .links i{{font-style:normal;opacity:.8;white-space:nowrap}}
.page{{padding:34px 20px 40px;text-align:center;background:#f5f5f7}}
.h1{{font-size:28px;font-weight:600;letter-spacing:-.03em}} .h2{{color:#6e6e73;font-size:15px;margin-top:4px}}
.icons{{border-radius:14px;border:1px solid var(--line);background:#fff;padding:18px;display:flex;flex-direction:column;gap:14px}}
.irow{{display:flex;gap:18px;align-items:center;flex-wrap:wrap}}
.appicon{{width:72px;height:72px;border-radius:17px;overflow:hidden;display:block;box-shadow:0 6px 18px rgba(0,0,0,.14)}}
.appicon svg{{width:72px;height:72px;display:block}}
.avatar{{width:56px;height:56px;border-radius:50%;overflow:hidden;background:#f5f5f7;display:grid;place-items:center}}
.avatar.dk{{background:#000;color:#fff}}
.avatar svg{{width:40px;height:40px;display:block}}
.pick{{margin-top:40px;background:#000;color:#f5f5f7;border-radius:28px;padding:40px;text-align:center}}
.pick h2{{margin:0 0 8px;font-size:32px;letter-spacing:-.03em;font-weight:600}} .pick p{{margin:0;color:#a1a1a6;font-size:19px}}
@media (max-width:760px){{.pair,.ctx{{grid-template-columns:1fr}}.opt{{padding:22px;border-radius:20px}}.sizes{{gap:22px}}.m[style*="256"] svg{{width:160px;height:160px}}.lockup svg{{height:52px}}}}
</style>
<div class="wrap">
  <h1>Studio 18 logo options</h1>
  <p class="intro">Four directions, each shown as the full lockup, the mark at favicon sizes, in single color, and in the places it will actually live: a browser tab, the site's black nav bar, an app icon and a social avatar.</p>
  {''.join(cards)}
  <div class="pick"><h2>Pick one by name.</h2><p>Tell me the option you like and anything to adjust. I'll finalize the files and put it on the site, favicon and share image.</p></div>
</div>
"""
out.write_text(page)
print("wrote", out, len(page), "bytes")

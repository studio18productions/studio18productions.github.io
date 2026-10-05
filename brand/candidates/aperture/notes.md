# Aperture 18 — final

A continuous-corner badge carrying the numeral 18. The 8 is two lens elements stacked on a
shared waist; the lower, larger counter holds a thin blue iris. One stroke weight builds
everything. Regenerate with `python3 gen.py` (all numbers below are in that file).

## Construction grid (512 × 512)

| element | geometry | at 16 px |
|---|---|---|
| badge | superellipse n = 5 (≈22 % continuous corner), 144-point outline | — |
| stroke weight **W** | 50 — stem, ring and waist are all W | 1.56 px |
| 8, outer | two circles R 100 (top) / 112 (bottom), centres y 169 / 331, overlap exactly W so the waist is W thick; union outline computed at the chord | — |
| 8, counters | perfect circles R 50 (top, Ø100) / R 62 (bottom, Ø124); extents y 69 → 443 (374, 73 % of badge) | **3.1 px / 3.9 px** (was 2.6 / 3.4) |
| iris (colour only) | ring R 40 → 27 (13 thick), floating 22 inside the lower counter | ring 0.4 px, gap 0.7 px → collapses to a dark navy-tinted hole |
| iris at 32 px | ring 0.8 px, gap 1.4 px, pupil 3.4 px | survives as a blue ring with a dark centre |
| 1, stem | x 110 → 160, y 74 → 438 (5 units of overshoot compensation against the round 8) | 1.56 px |
| 1, flag | tapered: top edge 45°, reach 42 (0.84 W), vertical end cut 22 (0.44 W), underside returns to the stem at 23°, meeting it 82 below the top | one lighter pixel |
| spacing | stem → lower ring 44; group 360 wide, centred then nudged 8 left (the round 8 is optically heavier) | — |
| badge edge (mark.svg) | badge path inset 2, `stroke #2c2c2e` 4 wide → 2 px at 256, 1 px at 128, gone under 64 | — |

Lockup (1600 × 400): mark 300 tall at x 181; text starts 72 right of the badge.
"Studio 18" Inter 600 / 208 px / −0.03 em; "Productions" Inter 400 / 92 px / −0.02 em
(a two-step weight drop reads as intent, 600 → 500 reads as an accident). The two lines are
stacked on Inter's cap height (0.727 em) and the block is centred on the badge.

## What changed from round 1

1. **Earned the name.** Counters enlarged from Ø84/Ø108 to Ø100/Ø124 while W went 52 → 50,
   so the 8 is now mostly glass, not metal; the lower counter stays the larger of the two. A
   thin #0071e3 iris ring floats in the lower counter with clear gaps — a lens element, and the
   mark's single hit of brand colour. It appears in mark.svg and the lockup only; mark-mono.svg
   is one `currentColor` compound path whose counters are true holes.
2. **Favicon legibility.** At 16 px the top counter is now 2 solid pixels instead of one pixel
   of mud; the ring strokes stay at ~1.5 px. The iris is sized so that at 16 px it cannot
   resolve into a shape and only tints the hole.
3. **Holds on black.** mark.svg keeps its #1d1d1f badge (the app-icon identity) and gains a
   hairline #2c2c2e edge drawn on an inset path so nothing clips the viewBox; on #000 the badge
   reads as an object again, on white the edge is invisible. Lockup and mono stay `currentColor`
   and invert cleanly.
4. **Flag.** The 45° slab (W reach, W-tall end, 2W drop) that read as a jersey numeral is now a
   tapered Helvetica/SF-style flag: shorter reach, a 22-unit end cut, and an underside that
   returns at a shallower angle, so the flag thins toward its tip.
5. **Type.** "Productions" dropped from 600 to 400; "Studio 18" keeps 600 at −0.03 em.
6. **Superellipse kept**, with a smoother 144-point outline.

## Honest limit

A single SVG cannot both survive at 32 px and vanish at 16 px: at 16 px the iris leaves the
lower hole dark navy (mean RGB ≈ 36 / 69 / 104) rather than #1d1d1f. If a build pipeline wants a
pure favicon, rasterise mark-mono.svg for ≤ 16 px and mark.svg for ≥ 32 px.

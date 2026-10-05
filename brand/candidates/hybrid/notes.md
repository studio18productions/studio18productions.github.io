# Signal 18 — construction notes

Hybrid of the two judge favourites: the **Lens 8** drawing (most legible 18 at 16 px) carrying
**Monolith's** one memorable idea, a single blue dot in the 8's upper counter that reads as lens,
record light and AI signal at once. Badge-less, numerals in `currentColor`, one accent.

## Grid (mark.svg, mark-mono.svg — viewBox 0 0 512 512)

512 units = 16 px, so **1 pixel cell = 32 units**. Everything that can snap to that grid does.

| Element | Geometry | At 16 px |
|---|---|---|
| Stroke | 64 everywhere (stem, both rings) | 2 px |
| 1 stem | x 96–160 (cells 3–4), y 56–456 | crisp 2 px bar |
| 1 flag | from (96,56) down-left to a vertical cut at x 40, y 128–216: 56 across, 72 down (52°), 88 vertical / 54 perpendicular thick | 1–2 px notch |
| Gap 1→8 | 32 (half a stroke): stem right edge 160 → lower ring's left extreme 192 (cell 5) | clean 1 px column |
| 8 upper ring | centre (318,162), R 114, counter r 50 | counter ≈ 3 px |
| 8 lower ring | centre (318,338), R 126, counter r 62 | counter ≈ 4 px |
| Ring overlap | exactly one stroke (centres 176 apart = 114 + 126 − 64), so the waist is a single 64-unit bar | 2 px waist |
| Signal dot | centre (318,162) = upper counter centre, r 32; ring of counter left clear = 18 = 36 % of counter radius | 2 px blue cluster |
| Overshoot | 8 spans y 48–464 (416), 1 spans 56–456 (400): round overshoots flat by 8 (≈2 %) | — |

The 8's outer contour is the union of the two circles (intersections at (236.6, 241.8) and (399.4, 241.8)),
the counters and — in mono — the dot are sub-paths under `fill-rule="evenodd"`, so every hole is real negative
space and nothing is painted white. Composition: the flag tip sits at x 40 and the 8 ends at x 444; the bounds
look off-centre but the area centroid lands at x ≈ 254 because the 8 carries most of the mass.

`svg:root{color:#1d1d1f}` gives the default ink only when the file stands alone (favicon, `<img>`); inlined
in a page it inherits the page colour, so the same file is black-on-white or white-on-black untouched.

## Lockup (viewBox 0 0 1600 400)

- Mark scaled 0.72: the 8 stands 300 tall (y 50–350), stroke 46.
- Wordmark block spans the same 300: "Studio 18" Inter 600 at 226 px, cap height 164 = the mark's upper bowl
  diameter (228 × 0.72), cap-top on the mark's top. "Productions" Inter 400 at 132 px, x-height 72 = the upper
  counter diameter (100 × 0.72), baseline on the mark's bottom. Letter-spacing −0.03 em on both.
- Gap mark→type 64 (≈1.4 strokes). Whole ink block (x 157–1443) is centred on the artboard.
- The blue dot appears once. The i-dots stay ink.

## Favicon (favicon.svg, viewBox 0 0 64 64)

Re-drawn, not scaled: 4 units = 1 px at 16 px. Stroke 10 (2.5 px), rings R 18 / R 19 with r 8 / r 9 counters,
dot r 5 (gap 3 = 37.5 %), stem x 9–19, half-stroke gap (5) to the 8, flag 6 across / 8 down / 9 thick. Fills the
box edge to edge like a tab icon should and flips to `#f5f5f7` under `prefers-color-scheme: dark`.

## What changed from the parents

- From Lens 8: kept the stem + 45°-family flag + two-ring 8 with true holes. Changed: 1 is now `currentColor`
  (was blue), gap to the 8 cut from 64–84 to 32, flag shortened 80→56 and steepened 45°→52°, rings grown
  106/126→114/126 to open the upper counter for the dot, whole drawing moved onto the 32-unit pixel grid.
- From Monolith: kept only the blue dot in the upper counter. Dropped the rounded-square badge and the white
  numerals, and set the dot at 36 % clearance so it stays a dot instead of filling the counter.
- Added: mono rule (dot becomes ink, one evenodd path), standalone-only default colour, a dedicated 64-grid
  favicon, and a lockup whose type sizes are taken from the mark's own bowl and counter diameters.

## Iterations

1. First render: everything read at 32 px; favicon flag (8 × 12) fused with the stem into a 5 × 5 block at 16 px.
2. Slimmed the favicon flag to 6 × 9, grew the dot r 30→32 for presence at 64–256, centred the lockup on the artboard (+77).
3. "Productions" 126→132 so its x-height equals the upper counter diameter.

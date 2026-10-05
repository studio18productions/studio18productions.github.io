# Monolith (final) — construction notes

Studio 18 Productions. One solid tile, the numerals 18 cut out of it as negative space, and a single
blue dot in the 8's upper counter: lens, record light and AI dot at once. Everything is drawn as
geometry on a 512 grid by `gen.py`; the SVGs are its output.

## Grid

| Element | Value | Note |
|---|---|---|
| Canvas | 512 × 512 | mark.svg / mark-mono.svg |
| Badge | superellipse n = 5, a = 256 | Apple-style squircle, 176-point polygon |
| Cap height of the 1 | y 77 → 435 = **358 (70 % of 512)** | was 300 (58.6 %) |
| Stroke | **58** | stem of the 1, ring of the 8; was 52 |
| Overshoot of the 8 | 4 | top 73, bottom 439 |
| 8 upper bowl | true circle, R 100, centre (332, 173) | counter r 42 |
| 8 lower bowl | stadium, R 106, straight side 12 | counter r 48; overlaps the upper bowl by exactly one stroke |
| Waist | y 242.8, half-width 71.6 | intersection of the two outer circles |
| 1 stem | x 122 → 180 | |
| 1 flag | reach 56, drop 46, vertical thickness 60 | **39°**, perpendicular thickness 46 = 80 % of stem; vertical end cut, no foot |
| Gap 1 → 8 | 46 | 1.4 px at 16 px |
| Blue dot | r **27** = 64 % of the counter, gap 15 | #0071e3, centred on the upper counter |
| Optical nudge | whole 18 shifted 4 left | the round 8 is visually heavier than the 1 |
| Margins | ink x 66 → 438, y 73 → 439 | ≈ 70 units all round |

Fill rule is even-odd throughout. Colour mark: badge → 18 cut out → both counters are badge-coloured
islands → blue circle sits on the upper island. Mono mark: identical path, plus the dot cut *out* of the
upper island, so the counter becomes a ring with a dot of real negative space.

## Lockup (1600 × 400)

* Mark: badge-less numerals (same path, positive, `currentColor`) scaled 0.8197 so the numeral ink is
  300 px tall; blue dot r 27 in the open counter. On a black nav this is white numerals + blue dot, not
  a white tile.
* "Studio 18": Inter 600, 232 px, letter-spacing −0.03em, cap-top aligned with the top of the 1 (y 53).
* "Productions": Inter 500, 104 px, letter-spacing −0.025em, baseline on the numeral baseline (y 347).
* Gap mark → type 76 px; the group is centred on estimated Inter advance widths.

## What changed from the judged version

1. **Numerals enlarged** from 58.6 % to 70 % of the badge, stroke 52 → 58. At 16 px the 18 is now
   ~11 px tall with ~1.8 px strokes instead of ~9 px with a collapsing 8.
2. **Blue dot has a gap.** The upper bowl grew to R 100 (counter r 42) and the dot shrank to r 27, so a
   15-unit badge-coloured ring separates dot from counter wall; it stays a dot at 32 px and a pupil at 16 px.
3. **Mono keeps the gesture.** The dot is cut out of the upper counter island, giving a concentric
   ring + dot in negative space (lens / record light) rather than an ordinary hole.
4. **Flag refined.** 48° → 39°, vertical thickness 66 → 60 (perpendicular 46 vs a 58 stem), reach
   trimmed to 56: lighter than the stem and closer to Inter's 1.
5. **Badge-less lockup.** The lockup uses the numerals in `currentColor` with the blue dot, sized to the
   two-line wordmark, so it sits on the dark nav without a solid white tile.
6. **"Productions" lightened** from 600 to 500 (and the headline enlarged) so the hierarchy is unambiguous.

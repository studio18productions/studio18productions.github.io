# Lens 8 — final

**Idea.** The 8 is two lens rings; the blue dot in the upper counter is the focus / record cue. Colour no
longer carries the idea: the 1 and the 8 are one black (currentColor) shape, and the dot is the only blue.
In single colour the dot stays a real filled dot inside the counter, so the idea survives mono, emboss, favicon.

## Construction grid (512 × 512, all numbers in grid units)

- Stroke **68** everywhere (0.175 of the 1's height — Inter 600's stem measures 0.179 of cap height, so the
  mark sits at the same weight as the wordmark; was 64 = 0.165, a hair light beside Inter).
- **1** — stem x 101–169, y 62–450 (388 tall, flat ends). Flag: tip at x 53, reach **48**, upper edge
  (101,62)→(53,130), i.e. a 68 drop over 48 = **55°**; vertical end cut 130→210 (80); lower edge parallel,
  (53,210)→(101,142). Perpendicular flag thickness ≈ 46 (0.68 stroke).
- **Gap 1→8** — stem right 169 to the bottom ring's extreme 203 = **34 = half a stroke** (was 64, a full stroke).
- **8** — top ring centre (331,168) R112 / counter r44; bottom ring centre (331,328) R128 / counter r60;
  centres 160 apart. The rings cross at y 236 (x 242 / 420, waist 178 wide); the bar between the counters is
  56 (212→268). The 8 spans y 56–456, overshooting the 1's flat ends by 6, like a round glyph against a cap line.
- **Dot** — (331,168) r20, 24 clear to the ring (0.35 stroke). At 64px that is a 5px dot with a 3px gap; at
  32px a 2.5px dot still separates from the ring; at 16px it survives as one lighter blue pixel in the counter.
- Whole mark: x 53–459 (406 wide), y 56–456, optically centred on 256.

Mark files: `mark.svg` (numerals currentColor + #0071e3 dot) and `mark-mono.svg` (one path, one
`fill="currentColor"`, evenodd — counters are true holes, the dot is the third winding and fills).

## Lockup (1600 × 400)

Two layouts were built and rendered side by side:

- **A** (`lockup-alt.svg`) — mark left at 300px, "Studio 18" 600 over "Productions" 500. Rejected: Inter's
  long shallow-flag 1 sits 100px from the drawn 1 and the two 18s read as two different drawings, which is
  exactly the judges' complaint — and tightening the mark's 1 made the difference *more* visible, not less.
- **B** (`lockup.svg`, chosen) — the mark *is* the 18 of "Studio 18"; "Productions" beneath. "Studio" Inter 600
  at 340px, letter-spacing −0.03em (−10.2), baseline 260.8. Mark at scale 0.6375 so the 1 equals Inter's cap
  height (0.7275em = 247px; the 8 is 255px tall, slightly under the brief's ~300 because the line has to fit
  1600 wide). The 1's stem starts 0.44em after the o — Inter's own "Studio 18" puts the stem 0.51em after
  the o and the flag tip at 0.34em; with a shorter flag the stem comes in a little. "Productions" Inter 500
  at 112px (0.33em), −0.03em, left-aligned on the S, baseline 386.5, line gap 0.13em. Because the only 18 on
  the page is the mark, the question of the mark's 1 matching a typeset 1 no longer arises.

Note on the brief's rule: the `<text>` elements in `lockup.svg` are "Studio" and "Productions"; the "18" is the
mark's geometry. `lockup-alt.svg` follows the literal rule (mark left at 300px, "Studio 18" as text) if that
is preferred.

## What changed from the round-1 Lens 8

1. Tightened the 1 to the 8: gap 64 → 34 (half a stroke); the pair now locks as one unit, total width 460 → 406.
2. Flag shortened 80 → 48 (60%) and steepened 45° → 55°, thickness kept at ~0.7 stroke; the triangular void
   under the flag is roughly half its former area.
3. Gave the mark its idea: the 1 is now the same colour as the 8 and a blue focus/record dot sits inside the
   8's upper counter with a clear gap; the mono version keeps it as a filled dot. Stroke 64 → 68 and rings
   R106/126 → R112/128 so the counters stay r44/r60 and the weight matches Inter 600.
4. Lockup rebuilt so the mark is the wordmark's 18 (see above); "Productions" dropped from 600 to 500.

## Honest notes

- Measured, not assumed: Inter 600's 1 flag is long and shallow (reach 1.34 stems at 36°, vertical cut) and
  SF Pro's is a long curved hook with a flat underside (reach 1.24 stems). The brief's "shorter and steeper"
  flag therefore does not literally echo either; it is a DIN/Neue-style 1 chosen to kill the void and lock the
  pair. Lockup B is what makes that acceptable — the drawn 1 never sits next to a typeset 1.
- Render harness note: `render.py` wraps the small marks in a #86868b label colour, so the numerals preview
  grey; in use they are black on white / white on black via currentColor.

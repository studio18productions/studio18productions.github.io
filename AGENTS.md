# Studio 18 Productions website — instructions for Codex

## Who does what
- **Claude builds the website.** Layout, structure, copy, CSS, sections, the design system,
  and anything about how the page is organized belong to Claude. Do not redesign, restructure,
  rewrite copy, or change the look of the site.
- **Codex handles pictures and video.** Your job is the visual media: preparing, optimizing,
  cropping, color-correcting and placing photos and video, and making them look great on the page.

## What you may do
- Add, replace, resize, crop, compress and color-correct images in `images/`.
- Convert or compress video for the web and put it in `videos/`.
- Swap a placeholder for a real image or video inside `index.html`, using the existing
  element and CSS classes. Keep `alt` text meaningful. Use `loading="lazy"` on images below the hero.
- Write descriptive captions or alt text for media.

## What you must not do
- Do not change layout, colors, fonts, spacing, section order, or copy in `index.html`
  beyond the single tag needed to place a picture or video. If a change seems needed, leave a
  note in `NOTES-FOR-CLAUDE.md` instead of making it.
- Never put the owner's family name or personal email anywhere in the site or commit messages.
- Do not add frameworks, build tools, or external scripts.

## Media rules
- Photos: JPG or WebP, max 2000 px on the long side, under ~1 MB each. Hero image up to 2400 px.
- Video: MP4 (H.264) under ~10 MB for the page, or link to YouTube/Vimeo if longer.
- Keep the Apple-style look: clean, neutral, no heavy filters, no watermarks.

## Site facts
- Single static page: `index.html` (HTML + CSS, no build step).
- Hosting: GitHub Pages, live at https://studio18productions.github.io (deploys from `main` in ~1 minute).
- Git is already authenticated on this Mac as the `studio18productions` GitHub account.

## How to publish
Run from this folder: `git add -A && git commit -m "describe the media change" && git push`
Then confirm the live site loads with the new media.

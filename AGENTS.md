# Studio 18 Productions website — instructions for Codex / ChatGPT

## Who does what
- **Claude builds the website** and is the ONLY one who edits `index.html`. Layout, copy, CSS
  and structure belong to Claude.
- **Codex / ChatGPT produce the media.** Photos, video, mockups: generate, shoot-prep, crop,
  color-correct, optimize, and save them with the exact filenames in `MEDIA-BRIEF.md`.

## Rules
- Read `MEDIA-BRIEF.md`. It lists every file, its exact filename, pixel size and content.
- The page has a slot pre-wired for each filename. Drop the file in with the exact name and it
  shows up on the live site automatically. You never need to touch the HTML.
- Save photos to `images/` and video to `videos/`. Never rename files or invent new filenames.
  If you need an extra asset, add it with a clear name and list it in `NOTES-FOR-CLAUDE.md`.
- Do NOT edit `index.html`, `AGENTS.md` or `MEDIA-BRIEF.md`. If something in the design
  should change, write the suggestion in `NOTES-FOR-CLAUDE.md`.
- Never put the owner's family name or personal email anywhere in files or commit messages.
- No frameworks, build tools, or external scripts.

## Media quality
- Photos: JPG (or PNG for UI mockups), sRGB, max 2000 px long side unless the brief says
  otherwise, under ~1 MB each. Video: MP4 H.264, muted, under ~8 MB.
- Apple-style look: clean, neutral, bright, real. No watermarks, no baked-in text, no other
  companies' logos, no celebrities, no fake client names.

## Site facts
- Static single page: `index.html`. Hosting: GitHub Pages at https://studio18productions.github.io
  (deploys from `main` in about a minute). Git is already signed in on this Mac.

## Publishing media
`git add -A && git commit -m "Add media per MEDIA-BRIEF" && git push`
Then check https://studio18productions.github.io after a minute and say "media pushed".

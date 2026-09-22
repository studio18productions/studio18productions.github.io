# Studio 18 Productions website

Single-page static site for Studio 18 Productions (on-site photography, video production,
AI video production, custom AI apps, and AI integration/training with Claude, ChatGPT, Gemini, Grok).

- Everything is in `index.html` (HTML + CSS, no build step, no frameworks).
- Design: Apple-style. Keep it: Inter font, white/black alternating sections, big centered
  headlines, blue links, large rounded tiles, lots of whitespace. Light and dark mode both work.
- Photos go in `images/`. Keep each under ~1 MB (resize to max 2000px wide). Reference them
  as `images/filename.jpg`. Replace the CSS gradient placeholders (`.pic`, `.hero-frame`)
  with real `<img>` tags when photos are provided.
- Never put the owner's family name or personal email anywhere in the site.
- Hosting: GitHub Pages, live at https://studio18productions.github.io (deploys from `main`, about 1 minute).
- To publish: `git add -A && git commit -m "describe change" && git push`.
  Git is already authenticated on this Mac as the studio18productions account.

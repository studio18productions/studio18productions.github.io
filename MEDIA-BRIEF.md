# Media brief for Studio 18 Productions website

This is the shot list for ChatGPT / Codex. Produce these files, put them in the folders named
below with EXACTLY these filenames, then push. Do not edit index.html.

The page already has a slot wired for every filename below. As soon as a file with the exact
name exists in `images/` or `videos/`, it appears in the right spot on the live site
automatically. A wrong filename simply does nothing. No HTML edits are needed or allowed.

## Style (applies to everything)
- Apple-style: clean, bright, neutral, real-looking, lots of negative space. No heavy filters,
  no HDR look, no lens flares, no neon, no watermarks, no text or captions baked into images.
- No logos or brand names of other companies. No recognizable celebrities. No fake client names.
- Subjects: a modern production studio that does on-site photography, video, AI video and AI
  software for businesses. Think professional lighting on location, cinema camera rigs, a
  laptop with a clean AI chat interface, a small team at work in a bright office.
- People should look like a small professional crew or business clients, diverse, natural.
- Photos: JPG, quality 85, sRGB, max 1 MB each (hero up to 1.5 MB). Videos: MP4 H.264, muted.

## Files to produce

### Hero
| File | Size (px) | Content |
|---|---|---|
| `images/hero.jpg` | 2400 × 1080 (16:7.2) | The AI Video hero. A wide cinematic frame that looks AI-generated but tasteful: an abstract premium product (a clean bottle or device) floating in soft colored light (blue, magenta, amber) on a dark background. Mostly dark tones so the white camera overlay reads over it. |
| `videos/hero-loop.mp4` | 1920 × 864, 8–12 s, under 8 MB | Optional. Same scene as hero.jpg, slow camera drift, seamless loop. |

### Service tiles
| File | Size (px) | Content |
|---|---|---|
| `images/tile-photo.jpg` | 1200 × 1000 | A photographer on location (office or retail space) with a softbox and a mirrorless camera, bright and clean, white or light background. |
| `images/tile-video.jpg` | 1600 × 670 (2.39:1) | A single beautiful cinematic film frame: an interview subject lit with a key light, dark background, looks like a still from a brand film. |
| `images/tile-ai-apps.png` | 1600 × 1000 (16:10) | Shown on the laptop screen in the top hero. Screenshot-style mockup of a custom AI assistant interface: dark UI, sidebar, a chat with two or three short messages about invoices or scheduling. No real company names. |
| `images/tile-integration.jpg` | 1200 × 1000 | A small business team at a table with laptops, one person presenting, bright office, natural light. Training session feel. |

### Work carousel (portrait 3:4, 900 × 1200 each)
| File | Content |
|---|---|
| `images/work-product.jpg` | Product photography: a premium object on a seamless backdrop, studio lit. |
| `images/work-brandfilm.jpg` | Brand film still: a craftsperson or owner in their workspace, cinematic light. |
| `images/work-ai-explainer.jpg` | AI explainer still: abstract clean 3D shapes explaining a process, soft pastels. |
| `images/work-assistant.jpg` | A phone or laptop showing a chat assistant, held by a hand, bright. |
| `images/work-headshots.jpg` | Corporate headshot: one person, neutral grey backdrop, soft light, friendly. |
| `images/work-automation.jpg` | A desk with a laptop showing email and a dashboard, coffee, morning light. |

### Detail rows (4:3, 1600 × 1200 each)
| File | Content |
|---|---|
| `images/detail-photo.jpg` | Lighting setup in a client's space: light stands, backdrop, camera on tripod. |
| `images/detail-video.jpg` | Video crew at work: camera operator, monitor, boom mic, drone on a case. |
| `images/detail-ai-video.jpg` | Editor at a color-grading suite, monitor showing an AI-generated scene. |
| `images/detail-ai.jpg` | Hands-on training: instructor pointing at a screen showing a chat assistant. |

### Social share
| File | Size (px) | Content |
|---|---|---|
| `images/og.jpg` | 1200 × 630 | Dark cinematic background (same family as hero), empty center. No text. |

## When done
1. Check every file is in `images/` or `videos/` with the exact filename above.
2. Check sizes and file weights match.
3. Run: `git add -A && git commit -m "Add media per MEDIA-BRIEF" && git push`
4. Wait about a minute, then open https://studio18productions.github.io and confirm each
   image shows in its spot. If one is missing, the filename or folder is wrong; fix and push again.
5. Tell the owner "media pushed".

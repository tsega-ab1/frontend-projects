# All Projects — Image &amp; Folder Guide

This zip contains **5 static websites**, each in its own folder, each optimized for a minimal image budget (3 or fewer real photos, reused across multiple placeholder slots where the same shot fits more than one spot). Every image slot in the code is currently a labeled placeholder — swap it for a real photo at the path listed below.

## Folder structure
```
all-projects/
├── 01-frontend-dev-portfolio/   → 0 images needed (CSS-only visuals)
├── 02-hotel-luxury-boutique/    → 3 images
├── 03-hotel-booking-platform/   → 3 images
├── 04-hotel-admin-system/       → 3 images
└── 05-cosmetics-corvina/        → 3 images
```
Each folder is fully self-contained and independently hostable — open its `index.html` directly, or upload the whole folder to any static host (Netlify, Vercel, GitHub Pages, S3, etc.).

## Where to legally get images (applies to all 5 projects)
- **Best**: your own photography once a site is real — customers expect to see the actual property/product, not stock.
- **Safe for placeholders/mockups only**: Unsplash, Pexels, Pixabay (free commercial license).
- **Avoid**: scraping images from other hotel/beauty/booking sites or Google Images — that's real copyright exposure once hosted under your own name.

---

## 01 — Frontend Dev Portfolio
**0 images required.** Project "photos" are CSS gradient blocks (`.project__visual`), not real placeholders — nothing to source here.

---

## 02 — Hotel: Luxury Boutique (The Verandah)
| # | Image role | What it should look like | Path |
|---|-------------|---------------------------|------|
| 1 | Hero | Hotel exterior or lobby, golden hour, vertical 4:5 crop | `02-hotel-luxury-boutique/assets/images/hero-exterior.jpg` |
| 2 | Room (reused) | One representative room: bed + window, natural light. Reused across every room card (home, rooms.html, room-detail.html) — same file, multiple slots. | `02-hotel-luxury-boutique/assets/images/room-generic.jpg` |
| 3 | Interior detail (reused) | One representative interior shot (lobby, dining, or bathroom). Reused across the gallery section and room-detail's bathroom shot. | `02-hotel-luxury-boutique/assets/images/interior-detail.jpg` |

*Contact page map*: no photo needed — the placeholder there now asks you to embed a real Google/Apple Maps iframe instead.

---

## 03 — Hotel: Booking Platform (Harborline)
Same 3 images as Project 02, same roles and paths (adjust folder name):
`03-hotel-booking-platform/assets/images/{hero-exterior.jpg, room-generic.jpg, interior-detail.jpg}`

The room photo is also referenced by `js/rooms-data.js` (all 6 mock search results use the same `room-generic.jpg` — once you have a real photo, either keep reusing it everywhere or add more entries to that file as you get more photos).

---

## 04 — Hotel + Admin System (Meridian Stays)
Same 3 images and paths as Project 03:
`04-hotel-admin-system/assets/images/{hero-exterior.jpg, room-generic.jpg, interior-detail.jpg}`

- Guest account page reservation thumbnails reuse `room-generic.jpg`.
- **Admin dashboard avatar is not a photo** — it's a CSS-drawn initials circle by design (admin screens should stay data-first, no decorative photography).

---

## 05 — Cosmetics Brand (Corvina)
| # | Image role | What it should look like | Path |
|---|-------------|---------------------------|------|
| 1 | Feature block | Product in hand or on skin, natural light, minimal retouching. Vertical 4:5 crop. | `05-cosmetics-corvina/assets/images/hero-product.jpg` |
| 2 | Ingredient close-up | Close-up of the one raw ingredient central to the formula. Vertical 3:4 crop. | `05-cosmetics-corvina/assets/images/ingredient-closeup.jpg` |
| 3 | Product shot | Clean studio shot of the bottle alone, plain background. Square 1:1 crop. | `05-cosmetics-corvina/assets/images/product-bottle.jpg` |

---

## How to swap any placeholder for a real image
Every placeholder in every project looks like this in the HTML:
```html
<div class="img-placeholder" style="--ratio:4/5" data-label="..."></div>
```
Replace it with:
```html
<img src="assets/images/your-file.jpg" alt="Describe the image" style="aspect-ratio:4/5; object-fit:cover; width:100%;">
```
Match the `--ratio` value already on the placeholder so your photo crops correctly, and create the `assets/images/` folder inside that project if it doesn't already exist.

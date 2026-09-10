# SmileLife Dental Hospital

A six-page static site for a dental hospital brand: `index.html` (home, matching the supplied reference layout), `about.html`, `services.html`, `team.html`, `gallery.html`, `contact.html`.

## Design notes

- **Palette:** deep teal `#1B4B47` (headings, buttons, brand), mint-tinted section backgrounds `#EAF4F3`, white cards, and six soft pastel accent circles (mint, blue, purple, gold, green, pink) for the service icons.
- **Type:** Sora (headings) + Inter (body/UI) + Caveat (the hand-lettered hero accent), all from Google Fonts.
- **Layout:** the homepage hero uses a bled, rounded-corner image with a script-font accent line, matching the reference. Services sit in a card grid next to a text intro rather than a full-width row. The "Why Choose Us" + CTA area uses a three-column split with a solid dark CTA panel breaking the light rhythm once, same as the reference.
- Keyboard focus states are visible throughout, the mobile nav collapses under 900px, and `prefers-reduced-motion` is respected.

## What to swap before launch

All photography in `assets/images/` is a labeled placeholder:

- `hero-checkup.jpg` — homepage hero, patient during a checkup, 7:5 crop
- `reception.jpg` — homepage "About us" reception photo, 9:11 crop
- `tools.jpg` — homepage tools tray photo, 5:4 crop
- `about-hero.jpg` — About page hallway/exterior shot, 26:17 crop
- `team-1.jpg` through `team-6.jpg` — headshots on the Our Team page, 7:8 crop each
- `gallery-1.jpg` through `gallery-6.jpg` — Gallery page photos, 9:7 crop each
- `contact-map.jpg` — replace with a real embedded Google/Apple Maps `<iframe>` rather than a photo

Also update before launch:

- **Doctor names and bios** on `team.html` are placeholders
- **Phone, email, and address** in the header CTA, footer, and Contact page (`+251 11 123 4567`, `hello@smilelife.example`, `Bole Road, Addis Ababa`) are placeholders
- **Contact form** has no backend — wire the `#contact-form` submit handler in `js/main.js` to your email service or booking system
- **Opening hours** on the Contact page are placeholder values

## Structure

```
smilelife-dental/
├── index.html
├── about.html
├── services.html
├── team.html
├── gallery.html
├── contact.html
├── css/style.css
├── js/main.js
├── assets/images/
└── README.md
```

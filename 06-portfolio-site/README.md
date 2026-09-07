# Studio — Portfolio Starter

Static HTML/CSS/JS. No build step — open `index.html` directly or host as-is on any static host (Netlify, Vercel, GitHub Pages, S3).

## Structure
```
portfolio-site/
├── index.html          # all page content/sections
├── css/style.css        # design tokens (:root) + all styling
├── js/main.js           # one small scroll interaction
├── assets/images/       # drop real photos/screenshots here
└── README.md
```

## To customize for a real client
1. Replace placeholder copy in `index.html` (headline, project descriptions, contact email).
2. Swap `.project__visual` gradient blocks for real screenshots: add `<img>` tags pointing to `assets/images/`.
3. Update the `:root` color tokens at the top of `style.css` to match the brand — everything else references those variables.
4. Update `<title>` and the meta description in `<head>`.
5. Add a real favicon and `og-image.png` under `assets/` if hosting publicly.

## Reusing this as a repeatable workflow
This file structure and design-token approach (colors/type/layout as named variables, one visual idea carrying the personality) is meant to be the base every time — swap the token values and content per brief, keep the architecture.

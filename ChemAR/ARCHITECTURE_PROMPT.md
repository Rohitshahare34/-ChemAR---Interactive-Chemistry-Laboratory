# ChemAR - Diagram 2 Architecture / Block Diagram Prompt (Ultra-Detailed, Modern)

Copy-paste the text below into your AI diagram tool (e.g., Gemini) to generate a modern SVG architecture diagram.

```
Create a layered architecture / block diagram for a web app named ChemAR. Deliver a single, high-resolution vector SVG.

Visual style:
- Glassmorphism cards with light blur; rounded corners (14px), 2px borders
- Soft grid background; azure/purple accent palette (#5B8DEF, #7A5AF8)
- Clear icons for each block; clean sans-serif typography
- Left-to-right data flow, top-to-bottom layers; generous spacing and alignment

Layers and blocks (group by layer with headings):
1) Client (Browser)
   - UI Layer: templates, styles.css, controls (Play/Pause, Speed, Progress), overlays (equation/observations)
   - Canvas Renderer: WebGL canvas element

2) Engine (Three.js)
   - Scene Orchestrator: camera (perspective 60°), lights (hemispheric + directional), render loop (requestAnimationFrame)
   - Material & Geometry Library: atom/bond presets, color scheme
   - Particle & Effects System: bubbles, foam, emissive particles
   - Phase Controller: timings, easing, transitions across phases 1..5

3) Experiment Library (this project’s files)
   - static/practical1.js … static/practical8.js: per-experiment config + logic
   - static/lab-main.js: core helpers/utilities
   - Assets: static/*.png|jpg icons/textures

4) Server (Flask, Python/WSGI)
   - Routes: '/', '/experiment/<id>' (see app.py)
   - Templates: templates/base.html, templates/index.html, templates/practical1.html … templates/practical8.html
   - Static: static/*.js, static/styles.css, images (optionally via CDN)

Connectors and labels:
- Browser → Flask: HTTP GET (HTML template)
- Flask → Browser: templated HTML with links to styles.css, lab-main.js, practical{id}.js
- Browser → Static/CDN: requests for CSS/JS assets
- UI Layer → Scene Orchestrator: user events (play, pause, speed)
- Experiment Library → Phase Controller: experiment config/objects
- Scene Orchestrator → Canvas Renderer: rendered frames
- Particle System ↔ Phase Controller: effect triggers and parameters

Non-functional callouts (small side badges):
- Performance: instancing, frustum culling, material reuse, 60 fps target
- Accessibility: keyboard focus, contrast, labels
- Fallbacks: if WebGL unsupported → show message; if GPU slow → reduce particles

Legend (bottom-right):
- Blue = Client/UI, Purple = Engine, Teal = Experiment Library, Gray = Server, Dashed = optional/CDN

Output: one clean SVG (no raster), presentation-ready with consistent sizing and spacing.
```

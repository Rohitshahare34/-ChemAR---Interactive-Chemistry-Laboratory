# ChemAR - Diagram 1 Flowchart Prompt (Ultra-Detailed, Modern)

Copy-paste the text below into your AI diagram tool (e.g., Gemini) to generate a high-quality, modern SVG flowchart.

```
Design a modern, highly attractive end-to-end flowchart for a web app named ChemAR that shows how a single experiment runs from start to finish. Deliver a single, high-resolution vector SVG.

Visual style:
- Sleek minimal UI; rounded rectangles (12-16px radius), 2px strokes
- Soft shadow (8-12px blur); azure/purple accents (#5B8DEF, #7A5AF8)
- Off-white background with subtle grid; clean sans-serif typography
- Use small, tasteful icons in nodes (home, list, play, gear, graph, loop)
- Top-to-bottom primary flow with three faint swimlanes: Context, UI, Engine

Nodes (in this exact order) with short captions under each title:
1. Home (Context) - landing screen with "Experiments" menu
2. Select Experiment (UI) - choose 1..8
3. Load Experiment Config (Engine) - json: atoms, bonds, phases, timings
4. Initialize Three.js Scene (Engine) - camera fov 60 deg, hemi + directional lights; materials cache
5. Mount UI (UI) - Play/Pause, Speed 0.5x-3x, Progress %, Equation panel
6. Decision: Play pressed? (diamond)
7. Phase Loop (Engine) - container holding 5 mini-steps as pill nodes with small icons and one-line captions:
   7.1 Introduce Reactants - spawn molecules, set positions
   7.2 Approach / Collision - tween paths, ease outCubic
   7.3 Break Bonds - energize, fade old bonds
   7.4 Form Bonds - snap geometry, emit particles
   7.5 Stabilize Products - damp motion, settle
8. Decision: More phases? (diamond) - yes loops back to mini-step 7.1
9. Show Results (UI) - observations, inference, balanced equation
10. Next Actions (UI) - three parallel branches: Replay, Change Speed, Select Another Experiment

Connector rules:
- Orthogonal elbows with arrowheads; label decision branches "Yes/No"
- From "Play pressed?": No -> back to "Mount UI"; Yes -> "Phase Loop"
- From "Next Actions": Replay -> "Phase Loop"; Change Speed -> "Mount UI"; Select Another -> "Select Experiment"

Decorative/UX details:
- Add small status badges: 'GPU OK' under Initialize Scene; '60 fps target' near Phase Loop
- Add callout notes with dotted connectors:
  * If asset load fails -> use fallback material, retry quietly
  * If FPS < 30 -> reduce particle count, simplify materials
- Include a legend at bottom-right: Context (gray), UI (azure), Engine (purple), Decisions (violet diamond)
- Ensure generous spacing, consistent alignment, and readable font sizes for presentations

Output: one clean SVG (no raster images), ready for documentation and slide decks.
```

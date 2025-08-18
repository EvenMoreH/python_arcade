# Arcade Game Development Notebook

Your guided, concept-first walkthrough for building games with the [Arcade](https://api.arcade.academy/) Python library. First you get the core ideas. Then you get a complete, code‑free checklist to recreate the simple movable dot game (see `src/game/example.py`).

---
## 1. Core Concepts (What You Need To Understand)

### 1.1 Environment & Project Setup
- Python version: Use a modern version (3.9+ recommended).
- Dependency management: `venv`, `poetry`, or `pip`. Keep dependencies minimal early on.
- Folder layout (typical minimal):
  - Project root with configuration (`pyproject.toml` / `requirements.txt`).
  - `src/` package directory (so imports are clean and installation editable).
  - Inside `src/`, your game package (e.g. `game/`).
  - Asset folders later: `assets/images`, `assets/sounds`, `assets/fonts`.
- Run style: either `python -m game.main` or expose an entry point script.

### 1.2 Game Loop (Arcade’s Model)
- You do NOT write a manual loop; Arcade owns it.
- You subclass `arcade.Window` (or use `arcade.View` inside a window) and implement callback methods.
- Core callbacks:
  - `on_draw`: Render everything each frame.
  - `on_update(delta_time)`: Update game state (movement, physics, timers).
  - Input handlers: `on_key_press`, `on_key_release`, mouse events, etc.
- Frame rate target: Typically 60 FPS (Arcade schedules updates and draws accordingly).

### 1.3 Coordinate System & Units
- Origin (0,0) is bottom-left by default.
- X increases to the right, Y increases upward.
- Window dimensions define visible region; you clamp or scroll for camera movement.
- Positions are usually floats (allows smooth sub‑pixel movement, though drawing rounds). 

### 1.4 Rendering & Drawing Order
- Clearing screen each frame prevents artifacts.
- Draw order matters: background first, then mid-layer, then UI.
- Simple primitives: circles, rectangles, lines, text.
- Sprites: Encapsulate texture, position, scaling, rotation.
- SpriteLists: Efficient batch rendering / updates.

### 1.5 State & Entities
- Minimal prototype can store raw coordinates (e.g., x, y variables).
- For more complex objects: create a class or use `arcade.Sprite` (with image) or custom dataclass.
- Global vs instance state: Keep per-window state inside the window class.

### 1.6 Input Handling
- Keyboard: Discrete events (press/release) vs continuous state (store which keys are held).
- Movement strategies:
  - Velocity updated on key events (set dx/dy on press, reset on release).
  - Per-frame polling (check arcade.key module states) — less common.
- Avoid doing heavy logic inside input handlers; just adjust state variables.

### 1.7 Movement & Physics Basics
- Simple movement: position += velocity each update.
- Clamping: Prevent leaving screen boundaries (min/max comparisons).
- Acceleration: Adjust velocity gradually for smoother feel.
- Physics engines: Arcade offers helpers for platformers (not needed for a dot prototype).

### 1.8 Time & Delta
- `delta_time` parameter in `on_update` tells you elapsed seconds since last update.
- Frame-independent movement: multiply speeds by `delta_time` (optional for very simple constant speeds; recommended later).

### 1.9 Colors & Constants
- Use `arcade.color.*` constants for readability.
- Keep constants (dimensions, speeds, titles) at module top for tuning.

### 1.10 Resource Management
- Background color can be set once or each frame; setting once is fine.
- Later: preload textures, sounds to avoid stutters mid-game.
- Use relative paths via `arcade.resources` or your assets directory.

### 1.11 Game States & Flow Control
- Small games may have a single active state.
- Larger games: use Views (`arcade.View`) for menus, levels, pause screens.
- Transition pattern: window.show_view(new_view_instance).

### 1.12 Collision Basics
- For primitives (like a dot) you can do manual distance checks.
- For sprites: use `arcade.check_for_collision` or list-based collision helpers.
- Bounding box vs pixel-perfect: Box/shape collision is typically enough.

### 1.13 Text & HUD
- Use `arcade.draw_text` for scores, instructions, debug info.
- Keep UI drawing at end of `on_draw` so it overlays gameplay.

### 1.14 Performance Considerations (Early Awareness)
- Avoid creating objects every frame; reuse where possible.
- Group sprites in SpriteLists for batch draws.
- Keep update logic proportional to number of entities (O(n)).
- Only scale up architecture when you feel friction.

### 1.15 Debugging & Iteration Workflow
- Start with simplest working version (a dot) before adding features.
- Print statements or on-screen debug text to inspect values.
- Incrementally refactor: primitive -> sprite -> animated sprite -> entity system.

### 1.16 Packaging / Distribution (Later Stage)
- Editable install while developing.
- Freeze/pack (e.g. PyInstaller) only once game is stable.
- License assets appropriately (fonts, sounds, images).

### 1.17 Common Pitfalls
- Forgetting to call `arcade.run()` (window never shows).
- Doing heavy calculations in `on_draw` instead of `on_update`.
- Not resetting velocity on key release (object keeps sliding).
- Using blocking calls (e.g., input()) that freeze the loop.
- Sprites not appearing due to missing draw calls or off-screen coordinates.

---
## 2. Rebuilding the Movable Dot Game (Step-by-Step, No Code)
Follow these steps sequentially to recreate the `example.py` game from nothing. Do not skip; each step builds on the previous. No code is shown so you actively recall and implement.

### 2.1 Project Scaffolding
1. Create project directory.
2. Initialize version control (optional but recommended).
3. Create virtual environment.
4. Activate environment.
5. Add project metadata file (`pyproject.toml` or requirements list) including Arcade dependency.
6. Create `src/` directory.
7. Inside `src/`, create a package directory (e.g., `game/`).
8. Add an empty `__init__` file inside the package.
9. Decide on a main module file name (e.g., `example.py`).
10. Ensure interpreter in your editor points to the virtual environment.

### 2.2 Define High-Level Game Parameters
11. Decide window width (e.g., 800) and height (e.g., 600).
12. Pick a window title string.
13. Choose dot visual style (primitive circle; no image file yet).
14. Choose dot radius (a small integer number of pixels).
15. Choose movement speed (pixels per frame or per update).
16. Decide background color (pick from Arcade color list mentally first).

### 2.3 Plan Internal State Variables
17. Identify variables for position along X and Y.
18. Identify variables for velocity components (dx, dy).
19. Determine initial position (center of window: half width, half height).
20. Decide initial velocities should be zero.

### 2.4 Create Window Class
21. Plan to subclass Arcade’s window class.
22. In constructor: call parent constructor with width, height, title.
23. Set background color once.
24. Initialize position and velocity variables.
25. (Optional) Store constants at module level for easy adjustments.

### 2.5 Drawing Routine
26. Implement the draw callback method.
27. Clear the screen at start of draw.
28. Draw the circle at current position using chosen radius and color.
29. (Optional) Later add text instructions (skip for initial minimal build).

### 2.6 Update Logic
30. Implement the update callback method that receives elapsed time.
31. Add velocity components to position each frame.
32. Clamp X within allowed range: radius to (width - radius).
33. Clamp Y similarly.
34. (Optional) Consider converting to delta-based speed scaling later.

### 2.7 Input Handling (Keyboard)
35. Implement key press handler.
36. When up or W pressed: set vertical velocity positive.
37. When down or S pressed: set vertical velocity negative.
38. When left or A pressed: set horizontal velocity negative.
39. When right or D pressed: set horizontal velocity positive.
40. When escape pressed: trigger a graceful exit.
41. Implement key release handler.
42. On release of vertical movement keys: reset vertical velocity to zero if released key matches direction.
43. On release of horizontal movement keys: reset horizontal velocity to zero if released key matches direction.
44. Confirm multiple keys (e.g., diagonal) work: press two keys, velocities combine.

### 2.8 Main Entry Point
45. Define a function that creates an instance of the window class.
46. Start Arcade’s event loop runner after creating the window.
47. Add guard to run main function only when module executed directly.

### 2.9 Manual Test Pass
48. Run the module from terminal within virtual environment.
49. Verify window opens with correct size and title.
50. Confirm background color displays.
51. Move dot in all four directions; confirm speed feels right.
52. Test pressing opposite directions quickly (no jitter beyond expected clamp).
53. Check boundaries: dot should not leave screen; test all edges.
54. Test diagonal movement (press two keys) — should move diagonally.
55. Release keys: movement stops immediately (no drifting).
56. Press escape: window closes.

### 2.10 Iteration Ideas (Optional After Success)
57. Replace primitive circle with a sprite (plan image asset path first).
58. Add acceleration: change velocity gradually instead of instant steps.
59. Add friction or deceleration when no keys pressed.
60. Display on-screen instructions (draw text late in draw call).
61. Track FPS or debug info at top-left.
62. Add simple collectible objects with a list of positions.
63. Add collision detection with walls or objects.
64. Refactor constants into a configuration module if growing.

### 2.11 Personal Reflection (Learning Reinforcement)
65. Re-describe (in your own words) how callbacks differ from a manual loop.
66. Explain why velocity is modified on input events rather than every frame.
67. Predict how to generalize from a dot to multiple moving entities.
68. Sketch how you’d add a pause state using views.
69. Identify one improvement to code organization for scalability.

---
## 3. From Here to “Hero” (Progression Path)
- Phase 1: Primitive shapes and manual position control (you just did this structure).
- Phase 2: Swap primitives for sprites; load images.
- Phase 3: Introduce SpriteLists; manage multiple actors.
- Phase 4: Add collisions and scoring mechanics.
- Phase 5: Use Views for menus, levels, pause.
- Phase 6: Add audio (background music, SFX).
- Phase 7: Add polish (animations, particle effects, camera scrolling).
- Phase 8: Performance passes (profiling, batching, asset optimization).
- Phase 9: Packaging / distribution build.

---
## 4. Quick Self-Quiz (No Answers Here—Check Yourself)
1. What two methods are required to both update and render every frame?
2. Why clamp positions after applying velocity instead of before?
3. How would you make movement speed independent of frame rate?
4. What advantages do SpriteLists give over individual draw calls?
5. How do Views help manage UI screens or game states?

---
## 5. Suggested Next Micro-Challenge
Without looking at existing code, implement the full dot game again with:
- Acceleration instead of instant velocity
- On-screen text with current coordinates
- A simple boundary color flash when hitting an edge

Document every change you make and why.

---
Happy building. Iterate small; refactor when friction appears; keep learning loops short.

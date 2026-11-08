# Kid Games

A collection of browser games for kids, hosted with GitHub Pages from the `npyati/kid-games` repo (branch `main`, root folder). Live at https://npyati.github.io/kid-games/. The players are the user's kids (2nd and 5th graders at the start), so games should be readable and fair for that age. The kids often describe what they want out loud, so requests can be loose ("like caves where the bears spawn"). Turn them into a concrete plan, state the plan briefly, and build it. Ask only when a choice really changes the game.

## Layout

- `index.html`: the game picker. Games are listed in the `GAMES` array at the top of its script.
- `<game-name>/index.html`: one folder per game, each a single self-contained file (inline CSS and JS, no build step, no frameworks or libraries, not even from a CDN). It must also work when opened straight from disk (`file://`).
- `<game-name>/README.md`: notes for that game (what it is, controls, how it works, saved data).
- `gobble-grid.html` at the root is only a redirect for old links.
- `serve.py`: local server for the repo with a Claude bridge (`POST /api/claude` runs the `claude` CLI and streams the result). Games can use it for local-only features; Wildwood's "Ask Claude" panel is the first. Run `python3 serve.py` and open http://localhost:8765/. It also works for browser tests in place of `http.server`.

Existing games to learn from:
- `gobble-grid/`: 2D grid game made with DOM elements. Math and word topics, monsters, a boss, tutorial level, music.
- `wildwood/`: 3D open world in plain WebGL 2. It's built in chunks from a seed, with animals and bosses, and it's controller-first. Reuse its pieces rather than starting over: the `Geo` vertex builder, the `blob`/`tube`/`cone` shapes, the matrix helpers, the gamepad code, the menu's controller navigation and the Web Audio sound effects.

## Starting a new game

1. Agree on the idea in a sentence or two, then pick a short original name and a folder name.
2. Create `<game-name>/index.html` with a full `<!doctype html>` page, an "All games" link to `../`, and a visible way back to the menu (and to "All games") from inside the game.
3. Add the game to `GAMES` in the root `index.html`: folder, title, one-line blurb, tags, accent color, and card art as an inline SVG (viewBox 0 0 320 180). Look at the picker afterwards to check the card.
4. Add a row to the table in the root `README.md`, and write `<game-name>/README.md`.
5. Make original games. Don't recreate a specific existing game's name, characters, art or music, even if the mechanics are similar.
6. When the game changes later, keep the menu's how-to text, the in-game hint, the picker blurb and both READMEs in step with it.

## Conventions

- **Saved data:** all games share one origin (npyati.github.io), so every `localStorage` key must start with the game's own prefix (Gobble Grid uses `gobblegrid`, Wildwood uses `wildwood.v1`). Wrap every storage access in try/catch. Check every loaded value's type and range, and clean up bad saved values on load so they can't break the menu.
- **Sound:** start Web Audio only after a user click or keypress. A controller button does not count as a user gesture in browsers. If the game can be started from a controller, show a small "Click once to turn on sound" hint when audio is still suspended. Keep separate music and sound-effect toggles.
- **Fonts and look:** Gobble Grid and the picker use Lilita One (display) and Nunito (body) on a dark indigo palette. New games can have their own look, but menus and HUD should still feel at home on the picker.
- **Controllers (if the game supports one):** use the standard Gamepad mapping (Xbox layout):
  - Buttons: 0 A, 1 B, 2 X, 3 Y, 4 LB, 5 RB, 6 LT, 7 RT, 8 View, 9 Start, 10 L3, 11 R3, 12–15 d-pad up/down/left/right.
  - Sticks: axes 0/1 left stick, 2/3 right stick.
  - Poll every frame and detect presses by comparing with last frame's state. Use a radial deadzone of about 0.15.
  - The whole menu must work with the d-pad or stick plus A (choose) and B (back). Start opens the menu.
  - Show a toast when a controller connects or disconnects, and pause if it disconnects mid-game.
- **Kid-friendly difficulty:** no gore. Losing should be gentle (Wildwood: knocked out, wake up with full health, keep everything). Offer a calm option when there are enemies (Wildwood's "Enemies: off").
- **Correctness:** any game that teaches facts (math answers, phonics) gets a separate checker script run over many generated questions before shipping. Wrong-answer explanations must be true too.

## Testing

- **Syntax:** pull the `<script>` out of the file and run `node --check` on it. Do this after every round of edits.
- **Browser:** serve the repo root with `python3 -m http.server 8765 --bind 127.0.0.1` and drive the game with Claude in Chrome. Close the tab and stop the server afterwards.
  - Keep game state in top-level `let`/`const` and functions (not inside a closure), so `javascript_tool` can read and set it directly (`startPlay()`, `player.x`, `spawnAnimal(...)` in Wildwood).
  - A single `javascript_tool` call times out after about 45 seconds. For longer tests, start an async function that stores its result on `window.__res`, then wait and read it in a later call.
  - Take screenshots to judge how things look. Measure frame rate by counting `requestAnimationFrame` calls over 2 seconds; aim for 60.
- **Controllers without a controller:** replace `navigator.getGamepads` with a fake standard pad and press its buttons from code:
  ```js
  const fake = { connected: true, mapping: 'standard', axes: [0, 0, 0, 0],
    buttons: Array.from({ length: 17 }, () => ({ pressed: false, value: 0 })) };
  navigator.getGamepads = () => [fake];
  fake.buttons[0].pressed = true;  // A down; set back to false on a later frame
  ```
  Tell the user it was tested with a pretend controller, and ask them to try a real one.
- **Test what the player will actually experience, not just that the code runs.** In Wildwood, the animals worked fine when spawned in front of the camera, but in real play none ever reached the player because they spawned behind them. The kids found it, not the tests. For anything that's meant to happen "every so often" (enemies showing up, finding water), simulate the player playing normally for a minute and count how often it happens.
- **Procedural worlds:** keep the world-generation code between `TERRAIN-BEGIN` and `TERRAIN-END` comments so a Node script can pull it out and run it. Measure how often features appear along long walks (minutes between rivers, marshes, caves) and check for broken terrain such as cliffs. Wildwood targets: water about every 1–2 minutes of walking, marshes about every 5, caves about every 2, dragon lairs rare (over 1 km away).

## Shipping

- Push to `main` only when the user asks. Commits end with the Co-Authored-By line the session provides.
- GitHub Pages rebuilds in about a minute. Afterwards, fetch the live page and look for a string that only exists in the new version, then load it once in Chrome to confirm it runs.
- Chrome may show two "Access to storage is not allowed from this context" errors on page load during browser tests. They come from the test setup, not the game, and saving still works.

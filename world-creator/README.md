# World Creator

A 3D island builder. Pick one of ten islands, then fly a camera around it and fill it with trees, buildings, people, creatures and weapons. People and animals walk around on their own, birds and dragons fly, and dolphins and whales swim in the sea.

**Play it:** https://npyati.github.io/kid-games/world-creator/

## Controls

- **Xbox controller:** left stick moves the camera, right stick turns and tilts it, LT zooms out and RT zooms in, click the left stick to move faster. **A** builds where the circle is (hold A and move to keep building, which is handy for forests), **X** turns the eraser on and off, **B** (or View) undoes, **LB / RB** change group, **d-pad left / right** pick a thing, **d-pad up / down** change its size, **Y** turns it, **Start** opens the menu. Menus work with the d-pad or stick, A to choose and B to go back.
- **Keyboard and mouse:** WASD or the arrow keys move, hold the right (or middle) mouse button and drag to turn, mouse wheel (or Page Up / Page Down) zooms, Q / E turn, Shift moves faster. **Click** builds where the mouse points (hold and drag to keep building). 1–5 or Tab change group, [ and ] pick a thing, - and + change size, R turns it, X is the eraser, Z or Backspace undoes, Esc opens the menu.
- **Touch:** drag with one finger to move, pinch to zoom, twist two fingers to turn, tap to build.
- Browsers only allow sound after a click or key press, so click once if the game is silent.

## Islands

| Island | What it's like | Starts with |
|---|---|---|
| Tropical Paradise | one round island, wide beaches | palms, bushes, flowers, rocks; parrots, crabs, dolphins |
| Big Forest | rolling green hills with ridges | pines, oaks, bushes, mushrooms; deer, bears, birds |
| Snowy Mountains | tall white peaks (up to about 100 m) | snowy pines, rocks, snowmen; penguins, polar bears |
| Desert Dunes | sand dunes and flat-topped mesas | cactuses, rocks, dead trees; camels, lizards |
| Volcano Island | a 120 m volcano with glowing lava in the crater | palms, rocks, bushes; a dragon, dinosaurs |
| Candy Land | pink and mint ground, round gumdrop hills, pink sky | lollipop trees, candy canes, gumdrops, flowers; unicorns, bunnies |
| Misty Swamp | low and flat with lots of ponds | willows, reeds, mushrooms; frogs, crocodiles |
| Rocky Cliffs | flat-topped terraces with steep cliffs down to the sea | pines, rocks, bushes; goats, birds |
| Island Chain | a big island and up to six small ones | palms, oaks, flowers; seagulls, dolphins, a whale |
| Autumn Valley | hills full of orange, red and yellow trees | autumn trees, pines, pumpkins; deer, foxes, squirrels |

Each new island gets its own random seed, so two Tropical Paradises are different shapes.

## Things to build

- **Nature:** oak, pine, snowy pine, palm, autumn tree, willow, old dead tree, bush, flowers, reeds, rock, cactus, giant mushroom, lollipop tree, candy cane, gumdrop, pumpkin, snowman.
- **Buildings:** little hut, cottage, big house, barn, castle (walls, four towers with flags, a gate and a keep), watch tower, windmill (the blades turn), lighthouse (the lamp glows), tent, well, fence, campfire (flickers), gold statue, market stall, sailboat (goes on deep water and bobs).
- **People:** villager, farmer (with a pitchfork), knight (sword and shield), king, queen, wizard (glowing staff), kid, pirate, builder.
- **Creatures:** dog, cat, sheep, cow, horse, unicorn, deer, bear, polar bear, fox, goat, pig, camel, bunny, squirrel, lizard, frog, crocodile, crab, chicken, penguin, dinosaur, bluebird, parrot, seagull, dragon, dolphin, whale, shark.
- **Weapons:** sword in a stone, weapon rack, big shield, bow and arrows, battle axe, cannon, catapult, suit of armor, treasure chest.

Four sizes: Small (½), Medium, Big (1¾) and Giant (3×). New things face the camera; **Turn** adds 45° each press. Land things only go on land, and the sailboat, dolphin, whale and shark only go in deep water (the circle turns red if it can't go there). Birds and dragons can go anywhere. Frogs and crocodiles can walk into shallow water. Up to 3,000 things per island.

## How things move

- People and land animals wander within about 20–30 m of where you put them (further for big ones), stopping now and then, and never walk into the sea or up cliffs. Legs swing as they walk; bunnies, squirrels and frogs hop.
- Birds and dragons circle where you put them (dragons fly higher and wider) and flap their wings.
- Dolphins swim and leap out of the water now and then; whales and sharks swim (the shark's fin shows above the water).
- The windmill's blades turn, campfires flicker, the lighthouse lamp, wizard's staff and treasure glow, and the sailboat bobs.
- Things you place pop in with a little bounce.

## How it's drawn (sharper than Wildwood)

- Plain WebGL 2 in one file. The noise, shape helpers, sky, water, matrix and controller code come from Wildwood.
- Up to 2× the screen's pixels (Wildwood stops at 1.5×), with antialiasing.
- **Real shadows** from a 4096×4096 shadow map with soft edges. The shadow area follows the camera: tight and sharp when you're close, wide when you're far out.
- The island is one 560×560 grid (about 2.2 m per square; Wildwood uses 2 m squares only near you), with smooth lighting. Its height comes from `islandHeight`; everything that needs the ground height uses `groundAt`, which reads the same triangles that are drawn.
- Shapes are smooth (balls with 320 faces and smooth normals, 16-sided tubes) instead of Wildwood's chunky low-poly look.
- The sea is drawn to the horizon over a sea floor that goes on forever, and each island has its own sky and water colours.

## Saved data

`localStorage` keys (all start with `worldcreator`):

- `worldcreator.v1`: music and sound settings.
- `worldcreator.islands`: the list of islands: `{ id, type, seed, name, count, last }`. Broken entries are dropped on load.
- `worldcreator.island.<id>`: one island: its type and seed, the camera, and the things on it as `[type, x, z, turn, size]` (where you put them, not where they've wandered to). Unknown types, bad numbers and positions far off the map are dropped on load, and sizes are kept between ¼ and 4.

**My islands** lists them with Play and Delete (Delete asks twice). The island saves a few seconds after each change, when you open the menu, and when you leave the page.

## Testing notes

Tested in headless Chrome (SwiftShader): every island builds (in about 0.1 s) with no errors; one of every thing was placed and checked in screenshots; 60 seconds of life with walkers, swimmers and fliers had no walkers in the sea, no swimmers on land and no fliers too low; saving and loading kept every thing; a pretend controller built, switched groups, erased and undid.

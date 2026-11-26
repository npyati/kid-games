# Kid Games

Browser games for kids. No installs and no accounts: open the page and play.

**Play:** https://npyati.github.io/kid-games/

| Game | What it is |
|---|---|
| [Fishpocalypse](fishpocalypse/) | A 3D fishing game. Walk to the end of the pier, cast, and watch your hook sink through seven ocean zones (Sunlit Shallows, Kelp Forest, Twilight, Midnight, Abyss, Trench, and the lava of the Fishpocalypse Rift). Reel in 35 creatures, with a rare one and a mythical one in every zone, and keep them all in a giant aquarium where they earn coins every second. Buy heavier sinkers to go deeper, faster reels and luckier bait. Controller, keyboard, mouse or touch. |
| [Gobble Grid](gobble-grid/) | Gobble every square that fits the rule ("Multiples of 7", "Starts with a blend"), dodge monsters, and beat the Cyclops boss. Math for grades 2–9, plus word sorting. |
| [Wildwood](wildwood/) | A 3D forest that goes on forever, with rivers and lakes every few minutes of walking. Friendly deer, rabbits and foxes; wolves and cave bears to fight; giant snakes in marshes and fire-breathing dragon bosses that fly; gather wood, stone and iron to craft weapons and chest plates. Dive under the water in lakes and the ocean to find fish, sharks and the Leviathan. Walk into caves for glowing crystals and treasure, and hide from enemies in your houses, castle or lookout tower. Made for an Xbox controller; keyboard and mouse work too. |
| [Greenhold](greenhold/) | Be a knight of a giant castle in a big green land of trees, grass, bushes and apple trees. Explore the keep's three floors and roof, walk the castle walls, and talk to the King, the Queen, knights, guards, butlers, the cook and the blacksmith. When the horn blows, stop the goblins, skeletons, trolls and stone giants before they break the keep door. Earn gold, get promoted by the King, and buy better swords and armor. Made for an Xbox controller; keyboard and mouse work too. |
| [Chicken Runner](chicken-runner/) | Race three rival chickens through 506 worlds (6 classic ones plus 500 bonus worlds), then the final world, Lava Castle, with extra-hard rivals and a King Chicken boss fight. Grab power-ups like Speed Corn, dodge rotten eggs and mud, collect coins, and spend them on 2,028 silly skins. Works with an Xbox controller, keyboard or touch. |
| [World Creator](world-creator/) | Pick one of ten 3D islands (tropical, forest, snowy mountains, desert, volcano, candy, swamp, cliffs, island chain, autumn) or a big map (Island Set, Pangea, Sky Islands, Endless Ocean, or Random) and fly a camera around it. Paint land types (forest, jungle, desert, swamp, corrupted land and more), raise mountains and dig lakes, and fill it with buildings, animals and mythical creatures like Wildwood's full-size dragon (up to 3 dragons, hydras and sea serpents per island). Put down 10 humans, elves, dwarves or orcs and they build their own town with a king or queen and an army, and go to war (or start one with the battle wand); tornadoes, tsunamis, bombs and earthquakes; zombies spread and ghosts scare everyone. Sharper than Wildwood, with real shadows. Each island saves by itself. Controller, mouse or touch. |
| [Feed Freddy](feed-freddy/) | Freddy the monster is hungry. Put up to 5 foods in the bowl (over 50 to choose from), mix, bake, fry or blend them, and feed him. He pays coins depending on how much he likes it: nothing for "bleh", up to 35 for "best food ever". Find his secret favorite and yucky foods and the yum combos, buy new foods, hats and colors, and invent your own foods. Mouse or touch. |

## How it's organized

```
index.html          the game picker (home page)
gobble-grid/        one folder per game
  index.html        the whole game in one file
  README.md         notes about that game
```

Each game is a single self-contained `index.html` with no build step, so you can also play by opening the file directly from your computer.

## Adding a game

1. Make a folder named after the game, such as `space-spelling/`, with an `index.html` inside.
2. Add an entry to the `GAMES` list at the top of the script in the root `index.html`: folder, title, a one-line blurb, tags, an accent color, and small card art.
3. Put an "All games" link to `../` in the game so players can get back to the picker.

# Kid Games

Browser games for kids. No installs and no accounts: open the page and play.

**Play:** https://npyati.github.io/kid-games/

| Game | What it is |
|---|---|
| [Gobble Grid](gobble-grid/) | Gobble every square that fits the rule ("Multiples of 7", "Starts with a blend"), dodge monsters, and beat the Cyclops boss. Math for grades 2–9, plus word sorting. |
| [Wildwood](wildwood/) | A 3D forest that goes on forever, with rivers and lakes every few minutes of walking. Friendly deer, rabbits and foxes; wolves and cave bears to fight; giant snakes in marshes and fire-breathing dragon bosses that fly; gather wood, stone and iron to craft weapons and chest plates. Made for an Xbox controller; keyboard and mouse work too. |
| [Chicken Runner](chicken-runner/) | Race three rival chickens through 506 worlds (6 classic ones plus 500 bonus worlds). Grab power-ups like Speed Corn, dodge rotten eggs and mud, collect coins, and spend them on 2,028 silly skins. Works with an Xbox controller, keyboard or touch. |

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

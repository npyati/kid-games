# Chicken Runner

A side-scrolling race. Your chicken runs by itself; you jump and flap over things and try to beat three rival chickens to the finish flag.

**Play it:** https://npyati.github.io/kid-games/chicken-runner/

## Controls

- **Jump:** Space, Up arrow, W, or tap/click the screen.
- **Flap:** press jump again while in the air (one flap per jump, unless you have Wings).
- **Pause:** Esc, P, or the pause button in the top right.
- **Xbox controller:** A (or B, X, Y, d-pad up) to jump and flap, Start to pause. In menus, use the stick or d-pad to move, A to choose and B to go back. The controller rumbles when you bump into something or grab a yucky item. If the controller unplugs mid-run, the game pauses. Browsers only allow sound after a mouse click or key press, so click once if the game is silent.

## Worlds

Finish a world to unlock the next one.

| World | Obstacles | Extra |
|---|---|---|
| Sunny Farm | hay bales, fences, pumpkins | signs that teach the controls |
| Bramble Woods | logs, stumps, thorny bushes | |
| Dusty Desert | cactuses, rocks | rolling tumbleweeds |
| Frosty Peaks | snowmen, ice blocks | rolling snowballs |
| Gumdrop Hills | gumdrops, lollipops, cupcakes | rolling jawbreakers |
| Moon Base | moon rocks, satellite dishes, alien plants | low gravity, rolling boulders |

Levels are generated from a fixed seed, so each world is the same every time you play it. Races take about 1 minute (Sunny Farm, 18,000 units) up to about 2 minutes (Moon Base, 33,000 units) at normal speed.

## Music

Each world has its own song, written as note names in `SONG_SRC` and played by a small Web Audio sequencer (melody, bass, chords, arpeggios, drums, echo):

| World | Song |
|---|---|
| Sunny Farm | bouncy hoedown: square-wave fiddle, banjo-style rolls, oom-pah bass |
| Bramble Woods | minor-key forest walk: wooden flute with vibrato, soft toms and shaker |
| Dusty Desert | twangy caravan tune with hand drums and shaker |
| Frosty Peaks | icy music-box bells with a frozen echo, sparkly arpeggios, sleigh bells |
| Gumdrop Hills | fast bubblegum pop with claps and bouncing bass |
| Moon Base | slow, floaty space synths with long echoes |

The menu has its own gentle tune. Each song loops every 24 to 44 seconds.

## Rivals

Each world has three rival chickens. They run in the back lanes with their names over their heads, wearing skins from the shop. The HUD shows your place (1st–4th), their dots on the progress bar, and how far ahead anyone off-screen is.

| World | Rivals (slowest → fastest) |
|---|---|
| Sunny Farm | Pecky, Dottie, Rusty |
| Bramble Woods | Ladybird, Ziggy, Captain Cluck |
| Dusty Desert | Sunny, Stripes, Spike |
| Frosty Peaks | Waddles, Boo, Sir Peckalot |
| Gumdrop Hills | Sprinkles, Buzz, Bubbles |
| Moon Base | Bolt, Cosmo, Nova |

How they race (all in `RIVALS` and `updateRival`):

- Each rival has a speed (0.88–1.04× normal) and a chance to trip on each obstacle or puddle. Tripping costs them the same stumble or slow-down you get.
- Every 9–16 seconds a rival gets a 2-second burst at 1.3× speed.
- To keep the race close, a rival more than 40 m ahead eases off to 0.9×, and one more than 90 m behind speeds up to 1.04×.
- Rivals don't take coins or power-ups, and they run through obstacles you've already knocked over.
- Bot testing (8 races per world): good play wins every world. Middling play wins the early worlds and comes 2nd or 3rd on the Moon. Sloppy play finishes 1st or 2nd early on and lower in later worlds.

## Power-ups

Good ones glow gold; yucky ones glow purple.

| Item | Effect |
|---|---|
| Speed Corn | 1.6× speed for 5 s (also cures Rotten Egg) |
| Wings | unlimited flaps and a gentle glide for 6 s |
| Coin Magnet | pulls nearby coins in for 8 s |
| Shield Egg | blocks the next bump |
| Rotten Egg (bad) | 0.6× speed for 5 s |
| Rain Cloud (bad) | no flapping for 5 s |
| Puddles (bad) | mud, swamp, quicksand, slush, syrup or goo: slow for 3 s |

Bumping into an obstacle makes the chicken stumble for about half a second. There's no game over.

## Coins, stars and skins

- Coins you grab are saved right away, even if you quit partway.
- Finishing gives a bonus: 10 coins, plus 5 per star, plus 15 / 8 / 4 for 1st / 2nd / 3rd place, plus 20 the first time you finish a world.
- Stars depend on time. "Par" is the world's length at normal speed: 3 stars within 95% of par, 2 stars within 110% (grabbing Speed Corn is what gets you under par).
- The Skin Shop has 28 skins, from free (Classic) to 1000 coins (Diamond). Some have animated touches: Lava glows, Galaxy twinkles, Ghost floats and is see-through, Rainbow changes color.
- The world picker shows your best place in each world as a medal.

## Secret cheat: the chicken dance

During a race, enter **down, down, left, right, left, right**:

- **Keyboard:** arrow keys.
- **Controller:** d-pad, or flicks of the left stick.
- **Touch:** swipes. On touch screens a quick tap jumps (when the finger lifts, or after 0.11 s) and a swipe of 30 px or more counts as a direction instead. Swiping up also jumps.

The chicken flashes rainbow with a star trail, runs at 2.1× speed, and smashes through obstacles, puddles and yucky items all the way to the finish. A "CHICKEN DANCE!" banner shows and a power-up song plays.

A cheat run is just for fun. Coins you grab still count (there's no coin magnet, so it earns less than playing normally), but you get no finish bonus, stars, best time or medal, and it doesn't unlock the next world. The code lives in `CHEAT_CODE`, `cheatInput` and `activateCheat`.

## Saved data

One `localStorage` key, `chickenrunner.save.v1`: coins, owned skins, the current skin, best time, stars and race place per world, and the music and sound toggles. Bad values are cleaned up on load.

## Testing notes

Before shipping, a scripted bot ran every world in the browser: a careful bot finished all six with 3 stars and no impossible spots (one bump on the Moon), and a sloppy bot finished all of them with 1–2 stars. Static obstacles are always at least 300 units apart.

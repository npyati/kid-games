# Chicken Runner

A side-scrolling race through 506 worlds, plus a final world, Lava Castle, where the King Chicken boss blocks the way. Your chicken runs by itself; you jump and flap over things and try to beat three rival chickens to the finish flag.

**Play it:** https://npyati.github.io/kid-games/chicken-runner/

## Controls

- **Jump:** Space, Up arrow, W, or tap/click the screen.
- **Flap:** press jump again while in the air (one flap per jump, unless you have Wings).
- **Pause:** Esc, P, or the pause button in the top right.
- **Xbox controller:** A (or B, X, Y, d-pad up) to jump and flap, Start to pause. In menus, use the stick or d-pad to move, A to choose, B to go back, and LB/RB to flip pages in the world picker and Skin Shop. The controller rumbles when you bump into something or grab a yucky item. If the controller unplugs mid-run, the game pauses. Browsers only allow sound after a mouse click or key press, so click once if the game is silent.

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

### 500 bonus worlds

After Moon Base come 500 bonus worlds (506 in all), unlocked one at a time like the classic six. Each one is mixed from a classic world's look, obstacles and song plus:

- a color mood: plain, sunset, night (stars and a moon), rosy, purple, golden, blue, minty, autumn, misty or stormy;
- sometimes bouncy low gravity (about 1 in 6), an obstacle borrowed from another world (about 1 in 3) or a different rolling obstacle;
- a name made from the mood and the place, like "Midnight Ridge" or "Floaty Sugar Hills";
- three rivals with names from a big list, wearing random shop skins.

Worlds get a little harder over the first 120 bonus worlds (tighter gaps, more double obstacles, the fastest rival goes from 0.97–0.98× up to 1.04×, the same as Moon Base), then stay there. Lengths are 20,000–33,000 units. Everything comes from a fixed seed in `makeMaps`, so world `x42` is always the same. Don't edit or reorder the lists it uses (`PLACE_NAMES`, `MOODS`, `RIVAL_NAMES`), or the worlds would change under players' saved progress.

### The final world: Lava Castle and the King Chicken

Lava Castle is the last entry in `MAPS` (`FINAL_MAP`, id `lava`). It opens when you finish **Moon Base**, not after the bonus worlds, so it's reachable early. It has its own orange card at the top of the world picker, above the pages.

- **The race:** volcanoes and lava (`volcano` deco), rocks, stumps, thorns, rolling boulders and puddles of "Cooling lava". It has its own song. The rivals are extra hard: Ember (1.03×), Blaze (1.06×) and Scorch (1.09×), who trip only 2–4% of the time, and a rival far ahead only eases off to 0.95× here (0.9× elsewhere).
- **The gate:** at 18,000 units (`m.gate`) a castle gate with a crown stands on the track, with clear ground around it, and the progress bar marks it. When you reach it, the race freezes (race clock and rivals) and the boss fight starts. Rivals can run past the gate; the King only blocks you.
- **The fight** (`enterKing`, `updateBoss`, `renderBoss`): an arena 1,100 units wide with castle walls. You don't run on your own here. Move with ←/→ or A/D (stick or d-pad on a controller; on touch screens hold the left 22% of the screen to go left, 22–44% to go right, and tap the right half to jump) and jump/flap as usual. You have 10 health. The King Chicken has **40 health** and a big "KING CHICKEN" health bar at the top.
  - **Bonk him** by running into him (or landing on him): 1 damage, or a **double bonk** (2) if he's resting right after an attack. He's protected for 0.5 s after each bonk, and you bounce back.
  - **Peck** (3 damage): a "!" shows and he leans back for 0.8 s, then lunges. Jump over it or back away.
  - **Stomp** (3 damage): a "!" shows, he crouches and jumps to where you are, and a red ring shows where he'll land. Run out from under him. He attacks sooner if you stand close.
  - **Mad:** at half health he roars, the music changes to a faster song, he turns really red and steams, he gets faster, and his stomps send shockwaves along the ground (1 damage, jump them). He also gets a bit redder as he gets hurt before that. He has an angry eyebrow and a red eye the whole time.
  - Shield Eggs drop in every 13–18 s; one blocks a hit.
  - **Win:** his crown flies off and he falls over dizzy, then you go back to the race just past the gate, which is now open. **Knocked out:** a gentle "Knocked out!" screen, and you start the level over.
- **Winning the world:** after the fight you must finish the race **1st**. Anything else shows "start over" and saves nothing (coins you grabbed are kept). Winning 1st shows "You beat Chicken Runner!" and gives a first-win bonus of 120 coins.
- **Bot testing:** a careful fighting bot (backs away from pecks, runs from stomps, jumps shockwaves) beat the King in 7 of 8 fights in about 40 s, often with 1 health left. Sloppy and standing-still bots got knocked out. In the race, a bot that never bumps came 1st in about 70% of runs. A bot that misses 1 in 8 jumps came 2nd–4th on Lava Castle but still mostly won Moon Base.

The world picker shows 12 worlds per page and opens on the page with your newest unlocked world. "Newest world" jumps there; LB/RB flip pages on a controller.

Bot testing on every 10th bonus world (50 worlds): a careful bot won 44 and came 2nd in 6; a sloppy bot finished 1st–3rd in nearly all of them.

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
| Lava Castle | driving minor-key race tune |
| King Chicken fight | "danger" music: growly sawtooth melody and heavy drums, then a faster, higher version when he gets mad |

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
| Lava Castle | Ember, Blaze, Scorch (extra hard) |

How they race (all in `RIVALS` and `updateRival`):

- Each rival has a speed (0.88–1.04× normal) and a chance to trip on each obstacle or puddle. Tripping costs them the same stumble or slow-down you get.
- Every 9–16 seconds a rival gets a 2-second burst at 1.3× speed.
- To keep the race close, a rival more than 40 m ahead eases off to 0.9×, and one more than 90 m behind speeds up to 1.04×.
- Rivals react to everything they run into: they say "Bonk!" and lose feathers on a bump, splash in puddles, and grab eggs too. Effects on rivals (`rivalItem`): Speed Corn is a 3 s burst at 1.3×, Wings mean they never trip for 6 s, Shield Egg blocks their next bump or bad egg, Rotten Egg slows them to 0.6× for 5 s with green stink, Rain Cloud makes them much more likely to trip for 5 s, and Coin Magnet just shows its ring. Effects show on the rival (wings, bubble, ring, stink, cloud). Popups and sounds only happen when the rival is on screen.
- Rivals only grab about half of the good eggs they run past, and jump over bad eggs on the ground (with their usual chance to trip). Eggs they grab stay there for you. They don't take coins, and they run through obstacles you've already knocked over.
- Bot testing (8 races per world): good play wins every world. Middling play wins the early worlds and comes 2nd or 3rd on the Moon. Sloppy play finishes 1st or 2nd early on and lower in later worlds.

## Power-ups

Good ones glow gold; yucky ones glow purple.

| Item | Effect |
|---|---|
| Speed Corn | 1.6× speed for 5 s (also cures Rotten Egg) |
| Wings | unlimited flaps and a gentle glide for 6 s |
| Coin Magnet | pulls nearby coins in for 8 s |
| Shield Egg | blocks the next bump or bad egg (Rotten Egg or Rain Cloud) |
| Rotten Egg (bad) | 0.6× speed for 5 s |
| Rain Cloud (bad) | no flapping for 5 s |
| Puddles (bad) | mud, swamp, quicksand, slush, syrup or goo: slow for 3 s |

Bumping into an obstacle makes the chicken stumble for about half a second. There's no game over.

## Coins, stars and skins

- Coins you grab are saved right away, even if you quit partway.
- Finishing gives a bonus: 10 coins, plus 5 per star, plus 15 / 8 / 4 for 1st / 2nd / 3rd place, plus 20 the first time you finish a world.
- Stars depend on time. "Par" is the world's length at normal speed: 3 stars within 95% of par, 2 stars within 110% (grabbing Speed Corn is what gets you under par).
- The Skin Shop has 2,028 skins: 28 classic ones, from free (Classic) to 1000 coins (Diamond), and 2,000 mixed skins. Some classics have animated touches: Lava glows, Galaxy twinkles, Ghost floats and is see-through, Rainbow changes color.
- The 2,000 mixed skins combine 36 colors, 10 patterns (spots, stripes, zebra, polka dots, hearts, stars, checks, galaxy, diamond, or none) and 25 hats (all the classic ones plus bows, flowers, beanies, headphones, halos and propeller caps). They're named after their parts, like "Mint Starry Wizard", and cost 35–1,090 coins (fancy colors like Golden, Pearl and Rose Gold, and fancy hats and patterns, cost more). They're made in `makeSkins` from a fixed seed, with ids `g0`–`g1999`. Don't edit or reorder `SKIN_COLORS`, `SKIN_PATTERNS` or `SKIN_HATS`, or skins players own would change.
- The shop shows 24 skins per page, with tabs for All skins, Can buy and Mine. LB/RB flip pages on a controller.
- The world picker shows your best place in each world as a medal.

In the King Chicken fight you lose health instead, and losing all of it means starting Lava Castle over (you wake up with full health; nothing is lost).

## Secret cheat: the chicken dance

During a race, enter **down, down, left, right, left, right**:

- **Keyboard:** arrow keys.
- **Controller:** d-pad, or flicks of the left stick.
- **Touch:** swipes. On touch screens a quick tap jumps (when the finger lifts, or after 0.11 s) and a swipe of 30 px or more counts as a direction instead. Swiping up also jumps.

The chicken flashes rainbow with a star trail, runs at 2.1× speed, and smashes through obstacles, puddles and yucky items all the way to the finish. A "CHICKEN DANCE!" banner shows and a power-up song plays.

A cheat run is just for fun. Coins you grab still count (there's no coin magnet, so it earns less than playing normally), but you get no finish bonus, stars, best time or medal, and it doesn't unlock the next world. In Lava Castle the King Chicken runs away instead of fighting. The code lives in `CHEAT_CODE`, `cheatInput` and `activateCheat`.

## Saved data

One `localStorage` key, `chickenrunner.save.v1`: coins, owned skins, the current skin, best time, stars and race place per world, the music and sound toggles, and `king` (`wins`: how many times you've beaten the King Chicken; `best`: reserved, 0 for now). Bad values are cleaned up on load.

## Testing notes

Before shipping, a scripted bot ran every world in the browser: a careful bot finished all six with 3 stars and no impossible spots (one bump on the Moon), and a sloppy bot finished all of them with 1–2 stars. Static obstacles are always at least 300 units apart.

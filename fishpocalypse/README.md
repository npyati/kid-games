# Fishpocalypse

A 3D fishing and collecting game. You start on a beach with a rod and a Tin Hook. Walk to the end of the long pier, cast your line, and the camera follows your hook down through the ocean, one zone at a time. When the hook stops, a fish from that zone swims up and bites. Reel it in and it goes into your Aquarium, a giant glass dome on the beach that holds as many fish as you catch. Every fish there makes coins every second. Spend the coins at the Tackle Shop on heavier sinkers, which go deeper to better fish.

**Play it:** https://npyati.github.io/kid-games/fishpocalypse/

Plain WebGL 2 in one file, like Wildwood. It reuses Wildwood's `Geo` vertex builder, the `blob`/`tube`/`cone` shapes and the matrix helpers.

## The player

You play as a kid who is Indian and Black, with warm brown skin and short black curly hair under a straw hat (`playerMesh`).

## Controls

- **Keyboard:** WASD or arrow keys to walk, Q / E to turn the camera, Space (or Enter) to cast, stop and reel (hold), F for the Fishdex, Esc for the menu.
- **Mouse or touch:** tap the ground to walk there. Tap the Aquarium or the Tackle Shop to walk in, or tap the water past the pier to walk to the end and cast. Drag to turn the camera, tap the yellow button to cast or stop, and hold anywhere on the screen (or the yellow button) to reel.
- **Xbox controller:** left stick to walk, right stick to turn the camera, A to cast, stop and reel (hold A or RT), B to go back (leave the Aquarium), Y for the Fishdex, Start for the menu. Menus work with the d-pad or stick plus A and B. The controller rumbles on a bite. If it unplugs, the game pauses. Browsers only allow sound after a mouse click or key press, so a "Click once to turn on sound" hint shows when you're on a controller and the sound is off.

## How a cast works

1. **Cast** at the end of the pier (`startCast`): the rod swings, the bobber flies out and splashes, and the screen fades to the ocean.
2. **Sink** (`updateOcean`, phase `sink`): the hook falls straight down a 3D ocean column. Each zone is 60 units tall, so every zone takes about the same time (about 2.5 s) no matter how many meters it covers. Inside a zone the meters grow on a log scale (`depthToVis` / `visToDepth`). A banner shows each new zone, and a gauge on the right shows all seven zones, where your hook is, and your sinker's limit. Press **Stop here** to fish a shallower zone. Otherwise the hook stops just inside the deepest zone your sinker reaches.
3. **Bite:** after 1–2 s a fish from that zone (`pickSpecies`) swims in from the side and grabs the hook.
4. **Reel** (`updateFight`): hold to fill the "Reel it in" bar. Every few seconds the fish thrashes ("LET GO! It's pulling hard!"). If you keep holding while it thrashes, the "Line pull" bar fills, and when it's full the fish swims back down a bit (the reel bar drops by 20%). The fish never gets away. Deeper, rare and mythical fish reel slower and thrash more often. Faster reels help.
5. **Up and caught:** the fish rides up through the zones to the pier, and the kid holds it up while a card shows its name, rarity, "NEW!" the first time, "Big one!" for big ones, its coins per second, the catch bonus (20 seconds' worth) and a fact. Creatures longer than 2.6 m are too heavy to hold up. Instead you get a picture of the kid standing on the beach next to the creature, life size, lying on the sand with the line still in its mouth (`beachedPose` / `beachedCamera`). The camera backs up to fit the whole thing above the card, and "Keep fishing" takes you back to the end of the pier.

Giants longer than 8 m hang sideways on the line during the fight so the whole monster fits on the screen, and the fog moves back so you can see them.

## Zones and creatures

Every regular zone has eight creatures: six common, one rare and one mythical. The Glow Caves also have the Glowtooth Titan and the Rift the King Leviathan, which show as **Legendary**. The Kaiju Depths has no commons at all. Bites are weighted 17 / 16 / 15 / 13 / 12 / 12 for the commons, 12 for the rare, 3 for the mythical and 1 for the King Leviathan. Bait multiplies the rare and mythical weights. The Fishdex lists each zone common first, then rare, then mythical.

| Zone | Depth | Coins/s (base) | Common | Rare | Mythical |
|---|---|---|---|---|---|
| Sunlit Shallows | 0–20 m | 1 | Sardine, Clownfish, Pufferfish, Blue Tang, Sea Turtle, Rainbow Ray | Seahorse | Sunscale Dragonet |
| Kelp Forest | 20–80 m | 5 | Kelp Bass, Garibaldi, Octopus, Moon Jelly, Wolf Eel, Treasure Turtle | Leafy Sea Dragon | Kelpie |
| Twilight Zone | 80–300 m | 25 | Lanternfish, Hatchetfish, Squid, Barreleye, Manta Ray, Star Jelly | Swordfish | Moonhorn |
| Midnight Zone | 300–1,500 m | 125 | Anglerfish, Gulper Eel, Vampire Squid, Viperfish, Atolla Jellyfish, Shadow Ray | Giant Squid | Phantom Shark |
| The Abyss | 1,500–5,000 m | 625 | Dumbo Octopus, Tripod Fish, Giant Isopod, Black Swallower, Goblin Shark, Ancient Turtle | Frilled Shark | Sea Serpent |
| The Trench | 5,000–11,000 m | 3,000 | Snailfish, Sea Pig, Supergiant Amphipod, Rattail, Big Red Jellyfish, Crystal Dragon | Megalodon | Kraken |
| Shipwreck Graveyard | 11,000–13,000 m | 6,000 | Barnacle Bass, Anchor Eel, Rusty Puffer, Doubloon Jelly, Cannonball Turtle, Sail Ray | Ghostlight Octopus | Wreck Serpent |
| The Glow Caves | 13,000–15,000 m | 9,000 | Glowworm Eel, Lantern Puffer, Cave Ray, Neon Jelly, Crystal Bass, Cave Isopod | Shimmer Seahorse | Aurora Dragonfish, and **Glowtooth Titan** (legendary) |
| The Fishpocalypse Rift | 15,000–20,000 m | 15,000 | Zombie Cod, Skeleton Fish, Lava Shark, Fire Jelly, Magma Turtle | Triclops Grouper | Doomfin, and **King Leviathan** (legendary) |
| The Underwater Palace (secret) | 20,000–30,000 m | 75,000 | Pearl Angelfish, Golden Jelly, Gem Turtle, Sapphire Ray, Marble Eel | Armored Seahorse | Thunderjaw (25 m lightning shark), and **Celestial Leviathan** (secret) |
| The Kaiju Depths (bought) | 30,000–50,000 m | 375,000 | (none) | Boulderback Turtle, Titan Isopod | Thunder Squid, Razorwing Ray, Magmaw, Abyss Wyrm, **Mecha Megashark** (legendary), and **Colossaurus** (secret) |

The newer creatures are at the end of `SPECIES`, so old saves (which store each fish by its number) still point at the right ones.

A creature's coins per second = zone base × (1, 1.2, 1.4, 1.6, 1.8 or 2 for the six commons, 5 for the rare, 25 for the mythical, 50 for the King Leviathan) × its size (0.8–1.05 usually, 1.15–1.5 for a "Big one", 15% of the time). Facts about real animals are written to be true. Mythical ones glow, sparkle and have a bigger fanfare.

The Sea Serpent has huge open jaws full of teeth, and the Megalodon has a giant toothy grin along both sides of its head. The King Leviathan is like the Sea Serpent but bigger (50 m). He is black with red stripes, and has big curved horns, red spikes and frills, glowing red eyes and the same giant jaws.

The models are built from shapes in code (`BUILDERS`: kaiju, fish, shark, eel, octopus, squid, puffer, seahorse, bug, sea pig, kelpie, turtle, ray, jelly), each about 1 unit long facing +x, then scaled by `vis = max(0.7 + length × 0.75, length)`. One unit is one meter, so big creatures are **life size**: Megalodon 16 m, Kraken 22 m, Thunderjaw 25 m, Sea Serpent 32 m, King Leviathan 50 m, Mecha Megashark 48 m, Colossaurus 150 m. Small fish are drawn a bit bigger so you can see them. Mythical creatures are made big on purpose too. Swimming is a wave in the vertex shader (`uWig`). Mode 0 swings side to side (fish), mode 1 sways tentacles, and mode 2 flaps (ray wings, turtle flippers). `speciesMesh` also stores each model's bounding box (`sp.bb`), which the beach picture and the sideways fight pose use. Each vertex stores how much it wiggles (head 0, tail 1).

## The Underwater Palace (secret zone, spoilers!)

It's the last zone (`PALACE_Z`, 540–600 units down the column, 20,000–30,000 m), right under the Fishpocalypse Rift's lava floor. Until you've caught both the **Doomfin** and the **King Leviathan** (`palaceOpen()`, worked out from the Fishdex), there's no sign of it anywhere. The lava floor is solid (`plugMesh` covers the hole), the Rift's water doesn't fade toward palace colors, the gauge stops at the Rift, the Fishdex has no palace row (and doesn't count its creatures), and the shop doesn't show the palace items. The picker blurb and the main README don't mention it either.

When the catch that completes the pair comes in, the catch card says "🔓 You have unlocked the secret area! It is called the Underwater Palace. It is under the Fishpocalypse Rift: let your anchor sink all the way down." A toast repeats it. From then on the lava floor has a hole in the middle, and the Doom Anchor sinks through it into the palace and stops in front of the great hall (about 26,000 m). The gauge shows 8 zones.

The palace (`buildPalace`, drawn when you're deep enough) has a checkered marble floor, a long hall with columns and glowing windows, a great purple dome with a gold spire, towers with pointed roofs, rows of columns with glowing lanterns, coral, sea plants, treasure chests, piles of gold and glowing crystals. The glowing lava ceiling with its hole hangs above.

**Celestial Leviathan** (Secret tier, the rarest thing in the game: weight 1, coins ×100): about 110 m long (`len` 70 plus a long tail). It's purple at the head fading to blue at the tail, with glowing stars along its back. It has big horns, a mane of horns all the way around its head like a lion's, giant jaws, three pairs of legs with white claws, and one long tail with a glowing fin. Reeling it in is much slower (×0.3 reel speed, thrashes every 0.9–1.6 s), but it slips back less when you let go, so any reel can land it: about 76 s with the Old Reel and 22 s with the Mega Reel (tested by a script that holds when it's not thrashing). It also rises slowly (5 s instead of 2.4). Its card and Fishdex tile have their own purple-and-blue **Secret** badge.

**Swimming by:** about 1 palace trip in 8 (`ocean.flyby`, 12%), the Celestial Leviathan glides past full size, as long as the palace, just above the great hall and in front of the dome. The camera backs up and looks up while it's there so you can see all of it. It never shows up among the ordinary fish swimming by.

**Palace things in the Tackle Shop** (only after it opens):
- **Crown Anchor**, 2 billion: sinks 2.5× as fast, so you reach the palace in about 8 s instead of about 20.
- **Royal Reel**, 5 billion: reels in 4.6× as fast.
- **Starlight Bait**, 1 billion: rare ×3, mythical ×10 (this includes the Celestial Leviathan).

The beach was made longer to the east (the dunes start at x 120 instead of 50) so a 110 m picture fits on the sand, and the lighthouse moved to the west side so it doesn't block the camera.

## The Kaiju Depths

The bottom zone of the ocean (`KAIJU_Z`, 600–660 units down, 30,000–50,000 m), under the Underwater Palace. Because it's below the secret palace, it only shows up in the Tackle Shop ("New places to fish", **200 billion** coins, `save.kaiju`) after the palace opens; the palace unlock card hints "the Tackle Shop has something new", and before that the Fishdex row just says "somewhere very, very deep". Buying it opens a hole in the middle of the palace's marble floor (with a gold rim; `palacePlugMesh` covers it until then), and the anchor sinks through the palace and stops in the Kaiju Depths. Press **Stop here** in the palace to fish there instead. The gauge shows the Kaiju Depths dimmed until you buy it.

**Its monsters fight back** like the Celestial Leviathan: reel speed ×0.32, they thrash every 0.9–1.6 s, slip back less, and rise in 5 s. With the Royal Reel they took 8–12 s in a test (before: about 3 s).

It's a huge cavern with no walls close by (`buildKaijuDepths`). At the back is a rock shelf (`KAIJU_FLOOR`) whose front edge drops away into the dark, so the hook can keep sinking. On the shelf are the skeleton of a giant monster (spine, ribs, horned skull with teeth), green and orange glowing crystals, hot vents and a trail of giant three-toed footprints.

**Nothing there is common:** 2 rares (×5), 4 mythicals (×25), the legendary Mecha Megashark (×50) and the secret Colossaurus. The zone's base is 375,000 coins a second. Since there are no commons, the monsters themselves swim by in the background (bigger and farther away than in other zones).

**Colossaurus** (Secret tier, `kind: 'kaiju'`, `buildKaiju`): our own original 150 m sea kaiju (the kids asked for "Godzilla", which belongs to a movie company, so it's a new monster instead). It's built in much more detail than the other creatures (about 107,000 vertices): a smooth lofted body (`loft`, 180 rings × 40 sides) with scales and a plated belly, armored bumps along the back, three rows of glowing orange crystal spikes, glowing spots down its sides, an open jaw with two rows of teeth, glowing eyes under a heavy brow, two great swept-back horns and smaller ones under them, glowing gill frills, a crest on its skull, four clawed legs held out like a swimming crocodile, and a finned tail. It is always moving: its legs and arms paddle forward and back, its tail sways side to side, and every few seconds it snaps its jaws shut in a big bite (the legs and lower jaw are separate pieces, `sp.parts`, turned at their hips, shoulders and jaw hinge by `drawParts`). It roars (`sfx.roar`) when it bites, when you catch it and when you visit it.
- It bites exactly **1 time in 100** in the Kaiju Depths (`pct: 0.01`, checked before the bait, so bait doesn't change it).
- It always makes exactly **1 billion coins a second** (`fixed`, whatever its size), plus 20 billion right away.
- It's **harder to reel in than the Celestial Leviathan** (×0.2 reel speed, thrashes every 0.75–1.3 s, rises in 6 s). A script that holds when it's not thrashing needed about 22 s with the Royal Reel (Celestial Leviathan: 12 s) and about 3.7 minutes with the Old Reel (Celestial Leviathan: 74 s).
- On about 1 dive in 12 (8%, only after you buy it), when you stop in the Kaiju Depths it swims past full size above the shelf with a roar, and the camera backs up to show it.
- It gets **its own aquarium, the Kaiju Tank** (`buildKaijuTank`, `KT`): a 60 m glass tunnel in a gigantic tank (400 m long, 380 m wide, 130 m tall) with crystals, boulders, giant kelp and old bones. Up to 3 Colossauruses swim a huge figure eight (`kaijuPath`) that goes around the tunnel and right over it. Get there with the "Kaiju Tank" button in the Aquarium (X on a controller, K on a keyboard), or "See it in the Kaiju Tank" on the catch card. It's not in the main aquarium tank.

The beach was made longer again (the dunes start at x 165) so the 150 m beach picture fits.

## The shop

Buy each item after the one before it.

- **Sinkers** (deepest zone): Tin Hook (free, 20 m) · Iron 150 (80 m) · Steel 3,000 (300 m) · Gold 60,000 (1,500 m) · Diamond 1.5 million (5,000 m) · Titan 30 million (11,000 m) · Anchor of the Wrecks 80 million (13,000 m) · Glowstone Sinker 220 million (15,000 m) · Doom Anchor 600 million (20,000 m).
- **Reels** (reel speed): Old 1× · Fast 400 (1.4×) · Turbo 15,000 (1.9×) · Mega 2 million (2.6×) · Rocket 100 million (3.4×).
- **Bait** (rare × / mythical ×): Worm · Shiny Lure 1,000 (1.5 / 2) · Glow Lure 150,000 (2 / 3.5) · Mythic Bait 20 million (2.5 / 6).
- **New places to fish:** The Kaiju Depths, 200 billion (only after the palace opens).

Pacing check (a script that casts over and over and buys the next sinker as soon as it can): the Iron Sinker after about 1–1.5 minutes, Steel about 4, Gold about 8, Diamond about 13, Titan about 24, and the Doom Anchor after about 50–60 minutes. With 8 creatures per zone (only one of them rare and one mythical), the average catch is worth about 8% less than it was with 5, so the game is now a little slower.

## The Aquarium

The glass dome on the beach (40 m across) shows up to 24 of your newest fish swimming around inside. Walk in the door to visit the real Aquarium: a glass tunnel through a huge tank (46 m tall and 120 m wide), with sand, plants, giant kelp, coral, rocks, treasure chests and little castles. The tunnel gets longer as you catch more fish (`tankLength`: 80 m + 1.2 m per fish, counting up to 4,000 fish), so there's always room. Small fish stay near the tunnel where you can see them (`tankY`, `tankZMax`), and giants use the whole tank. Giants are life size up to 16 m. Past that they still grow, but more slowly, so they fit (`tankSize`): the Sea Serpent is about 22 m in the tank and the King Leviathan about 30 m. Every fish you've caught swims in it. Bottom crawlers (isopods, sea pigs, amphipods, tripod fish) stay on the sand. The closest fish shows a name tag with its coins per second, and tapping a fish shows its tag too. Gold coins pop up from fish now and then (just for show: coins are counted all the time, everywhere).

## Saved data

**Save slots:** there are 3 (`SAVE_SLOTS`). The title screen has a "Player: …" button that opens **Who's playing?**, which lists each save with its name, coins and fish (or "New game"). Pick one to switch to it, and type a new name (up to 16 letters) for the current one. Slot 1 uses the original key `fishpocalypse.v1` (so older saves are there), slots 2 and 3 use `fishpocalypse.v1.slot2` and `.slot3`, and `fishpocalypse.slot` remembers which one you're on. **Start over** only wipes the current slot. Anyone can switch slots (there's no password).

Nothing new is saved for the palace: it opens from the Fishdex counts. `localStorage` key `fishpocalypse.v1`: coins, which sinker / reel / bait you own, whether you bought the Kaiju Depths (`kaiju`, 0 or 1), `zv: 2` (saves without it are from before the two new zones, so their Doom Anchor or Crown Anchor moves 2 places down the sinker list), every fish as `[species, size]`, the Fishdex counts, the total caught, the music and sound settings, and the time it was saved. Everything is checked on load (bad values are dropped or clamped). Coins keep coming in while the game is closed, up to one hour's worth, and a "Welcome back!" message shows how many. **Start over** on the title screen wipes the save (with a confirm step).

## Testing notes

Tested in headless Chrome on the real GPU (60 fps on the beach, in the ocean and in an aquarium with 60 fish), and with a pretend controller (menu navigation, walking with the stick, A to cast, holding RT to reel). Things to try with a real controller: the rumble and the d-pad in the shop.

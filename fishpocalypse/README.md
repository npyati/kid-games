# Fishpocalypse

A 3D fishing and collecting game. You start on a beach with a rod and a Tin Hook. Walk to the end of the long pier, cast your line, and the camera follows your hook down through the ocean, one zone at a time. When the hook stops, a fish from that zone swims up and bites. Reel it in and it goes into your Aquarium, a giant glass dome on the beach that holds as many fish as you catch. Every fish there makes coins every second. Spend the coins at the Tackle Shop on heavier sinkers, which go deeper to better fish.

**Play it:** https://npyati.github.io/kid-games/fishpocalypse/

Plain WebGL 2 in one file, like Wildwood. It reuses Wildwood's `Geo` vertex builder, the `blob`/`tube`/`cone` shapes and the matrix helpers.

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

Every zone has eight creatures: six common, one rare and one mythical. The Rift also has the King Leviathan, which shows as **Legendary** (56 creatures in all). Bites are weighted 17 / 16 / 15 / 13 / 12 / 12 for the commons, 12 for the rare, 3 for the mythical and 1 for the King Leviathan. Bait multiplies the rare and mythical weights. The Fishdex lists each zone common first, then rare, then mythical.

| Zone | Depth | Coins/s (base) | Common | Rare | Mythical |
|---|---|---|---|---|---|
| Sunlit Shallows | 0–20 m | 1 | Sardine, Clownfish, Pufferfish, Blue Tang, Sea Turtle, Rainbow Ray | Seahorse | Sunscale Dragonet |
| Kelp Forest | 20–80 m | 5 | Kelp Bass, Garibaldi, Octopus, Moon Jelly, Wolf Eel, Treasure Turtle | Leafy Sea Dragon | Kelpie |
| Twilight Zone | 80–300 m | 25 | Lanternfish, Hatchetfish, Squid, Barreleye, Manta Ray, Star Jelly | Swordfish | Moonhorn |
| Midnight Zone | 300–1,500 m | 125 | Anglerfish, Gulper Eel, Vampire Squid, Viperfish, Atolla Jellyfish, Shadow Ray | Giant Squid | Phantom Shark |
| The Abyss | 1,500–5,000 m | 625 | Dumbo Octopus, Tripod Fish, Giant Isopod, Black Swallower, Goblin Shark, Ancient Turtle | Frilled Shark | Sea Serpent |
| The Trench | 5,000–11,000 m | 3,000 | Snailfish, Sea Pig, Supergiant Amphipod, Rattail, Big Red Jellyfish, Crystal Dragon | Megalodon | Kraken |
| The Fishpocalypse Rift | 11,000–20,000 m | 15,000 | Zombie Cod, Skeleton Fish, Lava Shark, Fire Jelly, Magma Turtle | Triclops Grouper | Doomfin, and **King Leviathan** (legendary) |

The newer creatures are at the end of `SPECIES`, so old saves (which store each fish by its number) still point at the right ones.

A creature's coins per second = zone base × (1, 1.2, 1.4, 1.6, 1.8 or 2 for the six commons, 5 for the rare, 25 for the mythical, 50 for the King Leviathan) × its size (0.8–1.05 usually, 1.15–1.5 for a "Big one", 15% of the time). Facts about real animals are written to be true. Mythical ones glow, sparkle and have a bigger fanfare.

The Sea Serpent and the Megalodon have huge open jaws full of teeth. The King Leviathan is like the Sea Serpent but bigger (40 m). He is black with red stripes, and has big curved horns, red spikes and frills, glowing red eyes and the same giant jaws.

The models are built from shapes in code (`BUILDERS`: fish, shark, eel, octopus, squid, puffer, seahorse, bug, sea pig, kelpie, turtle, ray, jelly), each about 1 unit long facing +x, then scaled by `vis = max(0.7 + length × 0.75, length)`. One unit is one meter, so big creatures are **life size**: Megalodon 16 m, Kraken 22 m, Sea Serpent 25 m, King Leviathan 40 m. Small fish are drawn a bit bigger so you can see them. Mythical creatures are made big on purpose too. Swimming is a wave in the vertex shader (`uWig`). Mode 0 swings side to side (fish), mode 1 sways tentacles, and mode 2 flaps (ray wings, turtle flippers). `speciesMesh` also stores each model's bounding box (`sp.bb`), which the beach picture and the sideways fight pose use. Each vertex stores how much it wiggles (head 0, tail 1).

## The shop

Buy each item after the one before it.

- **Sinkers** (deepest zone): Tin Hook (free, 20 m) · Iron 150 (80 m) · Steel 3,000 (300 m) · Gold 60,000 (1,500 m) · Diamond 1.5 million (5,000 m) · Titan 30 million (11,000 m) · Doom Anchor 600 million (20,000 m).
- **Reels** (reel speed): Old 1× · Fast 400 (1.4×) · Turbo 15,000 (1.9×) · Mega 2 million (2.6×) · Rocket 100 million (3.4×).
- **Bait** (rare × / mythical ×): Worm · Shiny Lure 1,000 (1.5 / 2) · Glow Lure 150,000 (2 / 3.5) · Mythic Bait 20 million (2.5 / 6).

Pacing check (a script that casts over and over and buys the next sinker as soon as it can): the Iron Sinker after about 1–1.5 minutes, Steel about 4, Gold about 8, Diamond about 13, Titan about 24, and the Doom Anchor after about 50–60 minutes. With 8 creatures per zone (only one of them rare and one mythical), the average catch is worth about 8% less than it was with 5, so the game is now a little slower.

## The Aquarium

The glass dome on the beach (40 m across) shows up to 24 of your newest fish swimming around inside. Walk in the door to visit the real Aquarium: a glass tunnel through a huge tank (46 m tall and 120 m wide), with sand, plants, giant kelp, coral, rocks, treasure chests and little castles. The tunnel gets longer as you catch more fish (`tankLength`: 80 m + 1.2 m per fish, counting up to 4,000 fish), so there's always room. Small fish stay near the tunnel where you can see them (`tankY`, `tankZMax`), and giants use the whole tank. Giants are life size up to 16 m. Past that they still grow, but more slowly, so they fit (`tankSize`): the King Leviathan is about 26 m in the tank. Every fish you've caught swims in it. Bottom crawlers (isopods, sea pigs, amphipods, tripod fish) stay on the sand. The closest fish shows a name tag with its coins per second, and tapping a fish shows its tag too. Gold coins pop up from fish now and then (just for show: coins are counted all the time, everywhere).

## Saved data

`localStorage` key `fishpocalypse.v1`: coins, which sinker / reel / bait you own, every fish as `[species, size]`, the Fishdex counts, the total caught, the music and sound settings, and the time it was saved. Everything is checked on load (bad values are dropped or clamped). Coins keep coming in while the game is closed, up to one hour's worth, and a "Welcome back!" message shows how many. **Start over** on the title screen wipes the save (with a confirm step).

## Testing notes

Tested in headless Chrome on the real GPU (60 fps on the beach, in the ocean and in an aquarium with 60 fish), and with a pretend controller (menu navigation, walking with the stick, A to cast, holding RT to reel). Things to try with a real controller: the rumble and the d-pad in the shop.

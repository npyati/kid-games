# Wildwood

A 3D exploring game. You walk through a forest that goes on forever: pines, birches, leafy trees, ferns, tall grass, flowers, mushrooms and rocks. Every few minutes of walking you reach a river or a lake, and you can wade in and swim. There are also icy mountains, the ocean with sandy beaches, muddy marshes, rocky caves, and very rarely, a dragon's lair.

**Play it:** https://npyati.github.io/kid-games/wildwood/

## Controls

- **Xbox controller:** left stick to walk, right stick to look, RT (or RB) to swing or shoot, LB to block with a shield (you can keep swinging or shooting while you block), D-pad right to swap between your sword and your bow, D-pad left to take your shield out or put it away, A to jump, LT (or click the left stick) to run, Start to open the menu. Hold RT to keep swinging. In the menu, use the stick or d-pad and press A to choose, or B to go back.
- **Nintendo Switch Pro Controller** (or both Joy-Cons joined together): the same controls, with Nintendo's names: ZR to swing or shoot, L to block, ZL to run, + for the menu. The game matches buttons by letter, so A (on the right on Nintendo controllers) jumps and chooses, B goes back, Y opens the backpack, just like on Xbox. The hints and menu help switch to Nintendo names when one is plugged in. A single Joy-Con has only one stick, so the game asks for both or a Pro Controller. Tested in Chrome with a pretend controller.
- **Keyboard and mouse:** WASD to walk, mouse to look (click the game to grab the mouse), click or F to swing or shoot, right-click or Q to block (you can still swing while blocking), 1 / 2 / 3 for sword / bow / shield on-off, Space to jump, Shift to run, Esc for the menu. Arrow keys work too.

## Two players (split screen)

Plug in a second Xbox controller and press Start (or A) on it while playing, or choose **👥 Add player 2** in the menu. The screen splits: player 1 on the left (green tunic), player 2 on the right (orange tunic). Each of you sees the other walking around, with their chest plate on, their sword (or other weapon) or bow in their right hand and their shield on their left arm (held up in front when they block).

- **Your own:** health, knockouts (the other player keeps playing), your swing, your camera and controller, and **your own gear**: the weapons, bows, shields and chest plates you've crafted or picked up, and what you're holding and wearing, and **your own materials** (wood, stone, iron, gems, arrows and the rest). Player 2 starts with just fists and no materials. Player 1 also keeps the keyboard and mouse. Look (normal or flipped) is set for each player.
- **Your own backpack and menu, on your own half:** Y (or I/Tab on the keyboard) opens your backpack and Start (or Esc) opens your own small menu (Keep playing, Backpack, Music, Sounds, Look, Enemies, Main menu, and Leave the game for player 2). They cover only your half of the screen; the other player keeps playing, and nothing can hurt you while yours is open. **🏠 Main menu (pauses both)** opens the full menu for saved games, full screen and All games.
- **Shared:** the world and the animals. Things that drop fly to whoever is closest, and go into that player's own materials (a dropped weapon goes to whoever picks it up).
- Saves from before players had their own materials split the shared materials in half the first time player 2 joins again.
- **Animals** go after whichever player is closer, and new animals and bosses show up around each of you in turn. The world is loaded around both players, so you can split up.
- **Locator bar:** at the top right of each half, a bar shows where the other player is: the dot is in the middle when they're straight ahead and slides left or right as they move off to the side (◀ ▶ when they're behind you, ▲ ▼ when they're well above or below), with how far away they are.
- **Boss bars:** each half shows its own stack of boss bars, for the bosses that are after that player.
- **Leaving:** player 2 can choose **👋 Leave the game** in their menu, or anyone can choose **👥 Player 2: leave** in the main menu. If player 2's controller unplugs, the game pauses until it's back.
- Player 1's spot, gear and materials and player 2's gear, materials and look setting are saved with the game (player 2 gets them back when they join again). Split screen draws at a slightly lower resolution (it draws the world twice).

## Animals and fighting

When bosses are after you, each one gets its own health bar at the top of the screen, stacked with the closest on top (up to 4). While a boss is after you, boss music plays instead of the regular music (the kids' "regular boss music", three parts that change as the fight goes on; a dragon fight gets a faster, fiery theme). It follows the Music on/off setting.

The boss music, the dragon's roar, tail whip, air-only fire, glide, white spikes and looser wing walk were all made by the kids with Ask Claude and then built into the game.

**Friendly animals:** foxes, deer (some with antlers) and rabbits. They run away if you get close, and your swings pass right through them.

**Dragonlings** are neutral too: part goblin, part dragon (red scales, little horns and wings, a spear, and a green tunic with a rope belt and a yellow scarf). They live in camps in forests (the nearest is usually about 450 m away when you're in a forest): nest huts, a campfire, a dragon-head totem and a little gold. Camp creatures (goblins and dragonlings) walk around their campfire, not through it. Leave them alone and they leave you alone; hit one and the whole camp fights back with spears (7) and little puffs of fire (2 every ⅕ second). 20 health; when you beat one it doesn't fall over: it drops 2 gems (and sometimes iron) and runs away into the forest. New ones move in 4 minutes after a camp is beaten.

**Fish** swim in rivers and lakes, just under the surface, and now and then one jumps out with a splash: silver trout with a pink stripe, orange sunfish, blue striped bluegills, and (rarely, about 1 in 16) a golden fish. They dart away if you get very close, but they don't fight back. One hit (two with fists) catches one: it flips belly up and leaves fish scales floating on the water (a golden fish leaves a golden scale, a fish scale and 2 gems). Up to 8 are around you at a time when you're near water. Fish stay even with **Enemies: off**.

**Goats** live in the mountains and are neutral: they leave you alone unless you hit one, then that one and its herd headbutt you (12 health, 6 damage, a big knockback; they drop fur).

| Enemy | Health | Bite | Where | Drops |
|---|---|---|---|---|
| Wolf | 15 | 9 | packs of 2 or 3, mostly in forests | 1 gem, usually 1 fur, sometimes 1 iron |
| Bear | 20 | 16 | lives by a cave and comes back 2 minutes after it's beaten | 3 gems, 2 iron, 2 fur |
| Crocodile | 30 | 12 bite, 10 tail whip | in rivers (up to 3 at a time, they spawn in the water near you); they float with just their back showing and come out onto land; the tail whip hits you if you're behind it | 1 croc skin, 1 gem |
| Shark | 45 | 9 | the ocean (up to 2 at a time); you see its fin sticking out of the water. It only comes after you when you're in the water, and it can't come into the shallows | 2 shark teeth, 2 gems |
| Goblin | 18 | 8 axe chop | in camps out in open fields (3 to 5 per camp, they come as a gang); camps come back 4 minutes after they're cleared | 3 gems, sometimes iron or wood; 1 in 4 drop their crude goblin axe; clearing a camp leaves 6 gems, 2 iron and an apple by the fire |
| Leviathan (boss) | 1700 | 30 bite, 20 tail whip, water spray | big lakes only (never the ocean); a huge purple sea serpent (about 40 m long) with a blue belly, two pairs of big curved horns and two pairs of small wings on its back; rears up out of the water to fight, lunges its head out to bite from up to 11 m, and sprays water from its open mouth from up to 24 m away; comes back 5 minutes after it's beaten | 30 gems, 4 iron, 3 apples |
| Ice ogre (mini-boss) | 400 | 22 club smash; frost slam | snowy mountains, and easy to find: a few seconds after you reach the snow, one shows up 22–40 m away where you can see it (usually right in front of you), with a "🧊 An ice ogre is nearby!" message, and walks toward you. A new one comes 1 minute after you beat one; same as an ogre but with bluish-white skin and an ice club. Its frost slam sends a line of ice spikes racing along the ground at you: 15 damage and you're frozen (slow) for 3 seconds | 10 gems, 2 iron, 2 frost crystals, 1 apple |
| Giant spider (mini-boss) | 350 | 14 bite; poison breath; leg stomp 16 | open fields (meadows with few trees); a big black spider with yellow spots, eight small shiny red eyes and fangs, almost twice as tall as you, with 8 long legs. **Poison breath:** from 4–12 m away it breathes a green cloud in front of it; standing in it hurts a little and poisons you (2 damage a second for a few seconds, and your health bar turns green). **Leg stomp:** when you're close it rears up and slams its front legs down: 16 damage within about 6 m, jump to dodge it. A new one comes 2 minutes after you beat one | 10 gems, 2 iron, 1 apple |
| Ogre (mini-boss) | 300 | 20, a big club smash | wanders forests now and then (about a 1 in 3 chance per minute in a forest), comes back 2½ minutes after it's beaten; slower than you when you run | 8 gems, 2 iron, 2 fur, 1 apple |
| Giant snake (boss) | 600 | 18 bite, 12 tail whip | marshes; it can swim (about 16 m long); opens its jaw wide and snaps, and whips its tail at you if you're near the tail | 15 gems, 3 iron, 2 apples, 2 giant fangs |
| Dragon (boss) | 1800 | 25 bite, 22 tail whip, 18 stomp, plus fire from the air | two back legs, big wings, white spikes down its back and a long segmented tail; on the ground it walks on all fours using its folded wings as front legs: each wing knuckle stays planted while the body moves over it, then lifts in a smooth arc and steps ahead, with relaxed elbows out to the side and the wing skin stretched along each arm (the stride matches its walking speed so nothing slides). On the ground it bites, stomps and gives a big tail whip whenever you're within about 11 m; it only breathes fire from the air. It gives a huge roar every 4-6 seconds while it's fighting you (rearing up with its wings spread), and when flying it glides forward now and then and bobs (red with a yellow belly, like the Leviathan's body), about 25 m long; sleeps in a volcano on a mountaintop; comes back 10 minutes after it's beaten | 25 gems, 4 iron, 3 apples, 1 dragon scale |

- Enemies wander until they spot you (they see farther in front of them). Then a health bar pops up over their head, they chase you, and they bite when they're close. Bosses get a big health bar across the top of the screen instead.
- You run faster than all of them. Wolves and bears can't swim, so jumping in water is a good escape. Snakes can swim.
- The dragon wakes up when you come within about 40 m. Up close it opens its jaws wide and bites. From farther away it breathes fire (step sideways out of the flames). If you're beside or behind it, it swings its tail around at you. If you're close in front, it rears up and stomps: a dust shockwave hits everyone on the ground within 9 m, so jump to dodge it. Every so often it takes off, circles above you for about 14 seconds breathing fire down, then lands. You can only hit it when it's on the ground. Within about 300 m of a lair you'll hear a roar now and then, coming from the lair's side.
- Beaten animals fall over, sink into the ground and drop their things. Regular enemies also drop an apple (+30 health) 35% of the time.
- Your health refills slowly when you haven't been hit for a few seconds. If it runs out you're knocked out for a few seconds, then wake up with full health. Nearby enemies leave, and if you were at a dragon's lair you wake up 100 m away from it. You keep everything.
- **Enemies: off** in the menu leaves only the friendly animals, for calm exploring.

## Backpack and crafting

Gear made from common-enemy drops (fur, croc skin, shark teeth, and the goblin axe) has half the damage or protection of the original design, so it's an easy start rather than the best gear. Gear that needs a boss drop (fangs, frost crystals, dragon scales) is full strength.

Open the backpack with **Y** (controller) or **I** / **Tab** (keyboard). It shows your materials, lets you choose what to hold and wear, and lists what you can craft. Crafted things are yours to keep.

- **Wood:** swing at a tree (5 per tree). **Stone:** swing at a big rock (4 per rock, and sometimes iron). **Iron, gems and fur:** beat enemies (wolves usually drop 1 fur, bears 2). **Dragon scale:** one from each dragon you beat. **Giant fangs:** two from each giant snake you beat. **Frost crystals:** two from each ice ogre. **Croc skin:** one from each crocodile. **Fish scales:** one from each fish. **Golden scale:** from the rare golden fish. **Shark teeth:** two from each shark.

| Item | Damage or armor | Recipe |
|---|---|---|
| Fists | 2 | (always have them) |
| Stick | 3 | 1 wood |
| Wooden axe | 4, chops 2 wood per hit | 4 wood |
| Stone club | 4, breaks 2 stone per hit | 2 wood, 3 stone |
| Stone spear | 4, reaches far | 3 wood, 2 stone |
| Iron axe | 5, chops 3 wood per hit | 2 wood, 3 iron |
| Iron sword | 5 | 1 wood, 4 iron |
| Crude goblin axe | 2.5, fast, chops 2 wood per hit | only from goblins |
| Fang dagger | 5, very fast, poisons | 1 giant fang, 1 iron |
| Iron hammer | 6, slow, knocks enemies far, breaks 3 stone | 1 wood, 5 iron |
| Croc-tail whip | 3, reaches very far (4.6 m) | 2 croc skin, 1 wood |
| Croc-jaw mace | 3.5, big knockback | 2 croc skin, 2 iron |
| Scale sword | 6, quick | 6 fish scales, 1 iron |
| Scale spear | 6, reaches far | 5 fish scales, 2 wood |
| Golden trident | 8, double damage to anything that swims (fish, crocodiles, sharks, snakes, the Leviathan), reaches far | 1 golden scale, 4 fish scales, 2 iron |
| Shark-tooth sword | 2.5 | 4 shark teeth, 2 iron, 1 wood |
| Crystal sword | 6 | 2 iron, 12 gems |
| Crystal spear | 6, reaches far | 2 wood, 1 iron, 8 gems |
| Crystal axe | 7, chops 3 wood per hit | 1 wood, 2 iron, 10 gems |
| Venom glaive | 8, reaches far, poisons (2 damage a second for 4 seconds) | 1 giant fang, 2 wood, 3 iron |
| Dragon sword | 10 | 1 dragon scale, 3 iron |
| Wooden bow | 1-damage arrows | 4 wood, 1 fur |
| Iron bow | 1.5-damage arrows, faster | 2 wood, 3 iron, 1 fur |
| Venom bow | 3.5-damage poison arrows | 1 giant fang, 2 wood, 1 fur |
| Frost bow | 3.5-damage arrows that slow enemies | 1 frost crystal, 2 wood, 1 fur |
| Croc-tooth bow | 2-damage arrows | 2 croc skin, 2 wood, 1 fur |
| Scale bow | 3.5-damage arrows, shoots quickly | 6 fish scales, 2 wood |
| Crystal bow | 4-damage arrows | 2 wood, 1 iron, 12 gems |
| Dragon bow | 6-damage arrows | 1 dragon scale, 2 wood, 2 iron |
| 10 arrows | for bows (your first bow comes with 10) | 1 wood, 1 stone |
| Wooden chest plate | blocks 15% | 8 wood |
| Fur chest plate | blocks 10% | 6 fur |
| Stone chest plate | blocks 25% | 10 stone, 2 wood |
| Spiked chest plate | blocks 30%; anything that bites you takes 3 damage | 6 iron, 4 stone |
| Scale chest plate | blocks 35% | 10 fish scales |
| Iron chest plate | blocks 35% | 8 iron |
| Venom chest plate | blocks 45%, poisons anything that bites you | 1 giant fang, 6 iron |
| Crystal chest plate | blocks 50% | 4 iron, 20 gems |
| Dragon chest plate | blocks 60% | 1 dragon scale, 4 iron |
| Wooden shield | blocks 40% when raised | 6 wood |
| Iron shield | blocks 60% | 5 iron, 1 wood |
| Scale shield | blocks 65% | 8 fish scales, 1 wood |
| Spiked shield | blocks 55%; attackers take 4 damage | 4 iron, 4 stone |
| Venom shield | blocks 65%; poisons attackers | 1 giant fang, 3 iron |
| Frost shield | blocks 70%; slows attackers | 1 frost crystal, 3 iron |
| Crystal shield | blocks 75% | 2 iron, 15 gems |
| Dragon shield | blocks 90%, even dragon fire | 1 dragon scale, 3 iron |

Bows go in your hand like a weapon: RT shoots an arrow where your crosshair points (they drop a little over distance and stick in the ground and trees). A shield goes on your other arm: hold LB to raise it, which blocks hits from in front and slows you down, but you can still swing or shoot. You can't raise it while swimming. The four dragon recipes (sword, chest plate, bow, shield) all need the scale, so you have to choose. One snake's two fangs make two of the three fang items (venom glaive, venom chest plate, fang dagger). A poisoned enemy's health bar turns green. The backpack asks you to press a second time before it uses the scale.

## How the world is made

- **Lighting:** a warm sun with cool blue sky light in the shade and warm light bounced up from the ground; shady sides of shapes stay softly lit so the low-poly look keeps its form. Leaves glow when the sun is behind them, and there's a soft glow around the sun and a warm haze toward it. Trees cast soft shadows on the ground and grass (painted in when each 64 m chunk is built, so they cost nothing per frame), and animals have soft round shadows that lie on the slope of the ground (fainter and wider under a flying dragon).
- Everything is in `index.html`, drawn with plain WebGL 2 (no libraries).
- The world is built from a seed in 64 m squares ("chunks") as you walk, and dropped again once they're far behind. Grass, ferns and flowers are only built for the squares close to you.
- Rivers follow the zero lines of a slow, wiggly noise, and lakes are where a second noise is high. Marshes are where a third noise is high, but only on low ground (so they never leave cliffs next to hills). Icy mountains (sharp peaks up to about 150 m, snow above about 30 m, icy blue on steep high faces, frosty pines, light snowfall; you reach a range about every 6 minutes of walking; rivers and lakes stay out of them), goblin camps (at most one per 640 m square, in open fields; the nearest is usually about 500 m away), caves (at most one per 384 m square) and dragon lairs (at most one per 1 km square, on the highest ground there but never in or next to the icy mountains or snow, with a volcano built into the ground: a 14 m cone with a lava-cracked crater, lava streaks and smoke) are placed from the seed too.
- The ocean is where a fourth, very slow noise is high. The land around it comes down to a sandy beach about 100 m wide, then the sea floor drops to about 14 m deep. Mountains and marshes fade out before the coast. It covers about 1/6 of the world; walking in a straight line you reach it about every 6 to 7 minutes (sometimes 3, sometimes 12).
- The terrain code sits between `TERRAIN-BEGIN` and `TERRAIN-END` so a checker script can run it in Node. On four seeds: water about once per km (around 1 minute of walking), a marsh about every 1.4 km (around 5 minutes), a cave about every 550 m, and the nearest dragon lair is usually about 550 to 620 m away.
- Creatures, your hand and items use rounder shapes (each ball has 80 faces instead of 20) than trees and rocks, which there are thousands of.
- Every saved game has its own seed. **💾 Saved games → New game** picks a new one.

## Ask Claude (local only)

When the game is served by `serve.py` at the repo root (`python3 serve.py`, then open http://localhost:8765/wildwood/), a Claude panel appears while playing. It never shows on GitHub Pages or from `file://`, because there is no `/api/claude` there.

- **Talk:** hold **V**, or **LB + RB** together on a controller (that combo doesn't block or swing), say what should happen, and let go. If Chrome starts a session that gets no sound (it happens when macOS hands the mic to a nearby iPhone through Continuity), the game quietly retries while the button is held, and says "I can't hear the microphone" if it never gets any. Chrome's speech recognition turns it into text (it sends the audio to Google and asks for the microphone once). **T** opens a box to type instead.
- **One conversation:** each page load starts one Claude session, and every request resumes it (`--resume`), so follow-ups work: "build a house", "make it bigger", "now blue". Claude can ask one short question when it really can't tell what's meant; the next thing the kid says is the answer. Reloading the page starts a new conversation.
- **What happens:** the kid's words go to `serve.py` with a fresh snapshot of the moment, which runs the `claude` CLI on this Mac (your Claude Code login, no API key) and streams the answer back. Claude answers with one sentence for the kid and a block of JavaScript, which runs right away in the page.
- **The snapshot** (`claudeContext()`): where the speaker is, what they're **looking at** (the nearest creature, built thing, tree or rock the aim line goes through), the nearest creatures with their `#id`, and **things**: everything Claude has made or named, newest first, with where it is and its settings. That is how "it", "that one" and "the castle" find the right object.
- **Things** (`things` map): `spawn()` names its group automatically ("wolves 1"). `build(name, make, cfg)` makes a solid object from simple shapes (`box`, `ball`, `egg`, `pole`, `spike`) and keeps the shape function and its settings (`o`), so later turns can move or scale it (`thing(name).scale = 2`) or remake it with new settings (`rebuild(name, { wall: [0, 0, 1] })`). Built things are drawn after the animals and are solid through `nearbyTreesAt`, so players, animals and arrows bump into them. `remember()`, `rename()`, `forget()` and `creature(id)` cover the rest. Every animal now has an `id`.
- **Which model:** Haiku answers first (about 2–4 seconds). If the request is big (complicated builds, new behaviours), Haiku replies `ESCALATE` and Sonnet takes over in the same conversation, with permission to Read/Grep this folder only (about 10–20 seconds). If the code throws, Sonnet gets the error and one go at fixing it. The kids never pick a model. The system prompt is sent fresh each turn (`--system-prompt-snapshot off`), so each model gets its own instructions.
- **Helpers for Claude** (top level, in the "Ask Claude" section of the script): `me()`, `ahead()`, `spawn()`, `build()`/`rebuild()`, `thing()`, `say()`, `addHook()`/`removeHook()`/`clearHooks()` (run every frame while playing), `later()`/`wait()`, `give()`, `giveItem()`, `teleport()`, `defeat()`, `vanish()`, `heal()`. The system prompt (`CLAUDE_SYSTEM`) describes these and the game state. Keep it in step when the game changes.
- **Nothing Claude does is saved.** Built things, names and hooks last until the page reloads; materials and items it gives are saved like any others.
- Claude's code runs with full access to the page on purpose (any idea can work). It can break the game until a reload.

## Saved data

You can have as many saved games as you like. **💾 Saved games** in the menu lists them (name, gems, things made, when it was last played) with Play, Rename and Delete. Rename asks for the name in a typing box, so it needs a keyboard. Delete asks twice, and you can't delete the game you're playing. **➕ New game** starts from scratch: a new world, fists only, an empty backpack. Opening another game saves this one and reloads the page into it.

`localStorage` keys:

- `wildwood.v1`: settings shared by every game (music, sound, look direction, enemies) and the id of the open game.
- `wildwood.slots`: the list of saved games: `{ id, name, seed, last, gems, things }`. Broken entries are dropped on load.
- `wildwood.slot.<id>`: one game's world seed, where you were standing, your materials, the things you've crafted and what you're holding and wearing.

The first time this version loads, an older single save (everything was in `wildwood.v1`) becomes "Game 1", so nothing is lost. Older saves are upgraded too: gems carry over and any weapons you'd found are kept. If the place you saved is now out in the ocean, you wake up on the nearest beach.

## Testing shortcuts

- `wildwood/?dragon` starts you on the rim of the nearest volcano, looking down at the sleeping dragon (it's already there behind the menu). In this mode it only wakes up if you walk right up to it or hit it. Your saved spot moves there too.
- `wildwood/?ogre` puts an ogre in the forest 32 m in front of you.
- `wildwood/?snake` takes you to the nearest marsh with a giant snake lying 15 m in front of you. It stays calm until you get within about 7 m or hit it.
- `wildwood/?goblin` takes you to the nearest goblin camp, 22 m from the fire. The goblins stay calm until you get within about 7 m or hit one.
- `wildwood/?leviathan` puts you on the shore of the nearest big lake with the Leviathan in the water in front of you. It stays calm until you get within about 16 m or hit it.
- `wildwood/?mountains` takes you up into the nearest snowy mountains.
- `wildwood/?spider` takes you to the nearest open field with a calm giant spider 20 m in front of you.
- `wildwood/?iceogre` does the same, with a calm ice ogre 25 m in front of you.
- `wildwood/?croc` puts you on a river bank with a calm crocodile in the water in front of you.
- `wildwood/?dragonling` takes you to the nearest dragonling camp.
- `wildwood/?fish` puts you on a river bank with one of each kind of fish in the water in front of you.
- `wildwood/?ocean` puts you on the nearest beach looking out to sea; `wildwood/?shark` does the same with a shark in the water in front of you.

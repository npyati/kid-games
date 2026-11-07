# Wildwood

A 3D exploring game. You walk through a forest that goes on forever: pines, birches, leafy trees, ferns, tall grass, flowers, mushrooms and rocks. Every few minutes of walking you reach a river or a lake, and you can wade in and swim. There are also muddy marshes, rocky caves, and very rarely, a dragon's lair.

**Play it:** https://npyati.github.io/kid-games/wildwood/

## Controls

- **Xbox controller:** left stick to walk, right stick to look, RT (or RB) to swing, A to jump, LT (or click the left stick) to run, Start to open the menu. Hold RT to keep swinging. In the menu, use the stick or d-pad and press A to choose, or B to go back.
- **Keyboard and mouse:** WASD to walk, mouse to look (click the game to grab the mouse), click or F to swing, Space to jump, Shift to run, Esc for the menu. Arrow keys work too.

## Animals and fighting

**Friendly animals:** foxes, deer (some with antlers) and rabbits. They run away if you get close, and your swings pass right through them.

| Enemy | Health | Bite | Where | Drops |
|---|---|---|---|---|
| Wolf | 15 | 9 | packs of 2 or 3, mostly in forests | 1 gem, sometimes 1 iron |
| Bear | 20 | 16 | lives by a cave and comes back 2 minutes after it's beaten | 3 gems, 2 iron |
| Giant snake (boss) | 200 | 18 | marshes; it can swim (about 16 m long); opens its jaw wide and snaps | 15 gems, 3 iron, 2 apples, 2 giant fangs |
| Dragon (boss) | 500 | 25 bite, plus fire | two legs and big wings, about 25 m long with its tail; sleeps in a volcano on a mountaintop; comes back 10 minutes after it's beaten | 25 gems, 4 iron, 3 apples, 1 dragon scale |

- Enemies wander until they spot you (they see farther in front of them). Then a health bar pops up over their head, they chase you, and they bite when they're close. Bosses get a big health bar across the top of the screen instead.
- You run faster than all of them. Wolves and bears can't swim, so jumping in water is a good escape. Snakes can swim.
- The dragon wakes up when you come within about 40 m. Up close it opens its jaws wide and bites. From farther away it breathes fire (step sideways out of the flames). Every so often it takes off, circles above you for about 14 seconds breathing fire down, then lands. You can only hit it when it's on the ground. Within about 300 m of a lair you'll hear a roar now and then, coming from the lair's side.
- Beaten animals fall over, sink into the ground and drop their things. Regular enemies also drop an apple (+30 health) 35% of the time.
- Your health refills slowly when you haven't been hit for a few seconds. If it runs out you're knocked out for a few seconds, then wake up with full health. Nearby enemies leave, and if you were at a dragon's lair you wake up 100 m away from it. You keep everything.
- **Enemies: off** in the menu leaves only the friendly animals, for calm exploring.

## Backpack and crafting

Open the backpack with **Y** (controller) or **I** / **Tab** (keyboard). It shows your materials, lets you choose what to hold and wear, and lists what you can craft. Crafted things are yours to keep.

- **Wood:** swing at a tree (5 per tree). **Stone:** swing at a big rock (4 per rock, and sometimes iron). **Iron and gems:** beat enemies. **Dragon scale:** one from each dragon you beat. **Giant fangs:** two from each giant snake you beat.

| Item | Damage or armor | Recipe |
|---|---|---|
| Fists | 2 | (always have them) |
| Stick | 3 | 1 wood |
| Wooden axe | 4, chops 2 wood per hit | 4 wood |
| Stone club | 4, breaks 2 stone per hit | 2 wood, 3 stone |
| Iron sword | 5 | 1 wood, 4 iron |
| Crystal sword | 6 | 2 iron, 12 gems |
| Venom glaive | 8, reaches far, poisons (2 damage a second for 4 seconds) | 1 giant fang, 2 wood, 3 iron |
| Dragon sword | 10 | 1 dragon scale, 3 iron |
| Wooden chest plate | blocks 15% | 8 wood |
| Iron chest plate | blocks 35% | 8 iron |
| Venom chest plate | blocks 45%, poisons anything that bites you | 1 giant fang, 6 iron |
| Dragon chest plate | blocks 60% | 1 dragon scale, 4 iron |

The two dragon recipes both need the scale, so you have to choose. One snake's two fangs make both venom items. A poisoned enemy's health bar turns green. The backpack asks you to press a second time before it uses the scale.

## How the world is made

- Everything is in `index.html`, drawn with plain WebGL 2 (no libraries).
- The world is built from a seed in 64 m squares ("chunks") as you walk, and dropped again once they're far behind. Grass, ferns and flowers are only built for the squares close to you.
- Rivers follow the zero lines of a slow, wiggly noise, and lakes are where a second noise is high. Marshes are where a third noise is high, but only on low ground (so they never leave cliffs next to hills). Caves (at most one per 384 m square) and dragon lairs (at most one per 1 km square, on the highest ground there, with a volcano built into the ground: a 14 m cone with a lava-cracked crater, lava streaks and smoke) are placed from the seed too.
- The terrain code sits between `TERRAIN-BEGIN` and `TERRAIN-END` so a checker script can run it in Node. On four seeds: water about once per km (around 1 minute of walking), a marsh about every 1.4 km (around 5 minutes), a cave about every 550 m, and the nearest dragon lair is usually about 550 to 620 m away.
- Creatures, your hand and items use rounder shapes (each ball has 80 faces instead of 20) than trees and rocks, which there are thousands of.
- **New world** in the menu picks a new seed.

## Saved data

One `localStorage` key, `wildwood.v1`: music, sound, look direction and enemy settings, the world seed, where you were standing, your materials, the things you've crafted and what you're holding and wearing. Older saves are upgraded: gems carry over and any weapons you'd found are kept.

## Testing shortcuts

- `wildwood/?dragon` starts you on the rim of the nearest volcano, looking down at the sleeping dragon (it's already there behind the menu). In this mode it only wakes up if you walk right up to it or hit it. Your saved spot moves there too.

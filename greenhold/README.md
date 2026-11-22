# Greenhold

A 3D castle game. You're a knight of Greenhold, a giant castle in the middle of a big green land with lots of trees, grass, bushes, berry bushes and apple trees. Talk to everyone in the castle, explore every floor, and guard the castle from the monsters that come out of the woods.

**Play it:** https://npyati.github.io/kid-games/greenhold/

## Controls

- **Xbox controller:** left stick walks, right stick looks. **A** talks to someone or picks an apple (otherwise it jumps), **RT** swings your sword, **RB** shoots your bow, **LT** (or clicking the left stick) runs, **X** eats an apple, **Y** or **View** opens the map, **Start** opens the menu. In menus and when talking: d-pad or stick to choose, A to pick, B to go back.
- **Keyboard and mouse:** WASD walks, the mouse looks. Click swings, right-click (or R) shoots the bow, F also swings, **E** talks or picks apples, Space jumps, Shift runs, Q eats, M opens the map, Esc opens the menu. When talking: click a choice, or use ↑ ↓ and Enter (or 1–4), Esc to leave.
- Browsers only allow sound after a click or key press. If you start with a controller, click once to turn on the sound.

## The castle

- **Curtain wall:** a 100 m square wall, 9 m tall, with a walk along the top (stairs up from both sides of the courtyard), four corner towers you can walk through, and a gatehouse with a raised portcullis. A moat runs around it, crossed by a drawbridge.
- **The keep** has three floors and a roof:
  - Floor 1: the throne room (the King and Queen sit on their thrones), the kitchen (east) and the stair hall (west).
  - Floor 2: the banquet hall with a long feast table and a fireplace, the library (west) and a store room (east).
  - Floor 3: the royal bedroom, the knights' bunk room (west, where you wake up if you get knocked out) and the armory (east).
  - The roof, with the big royal flag.
  - Stairs: floor 1 to 2 on the west side, 2 to 3 on the east side, 3 to the roof on the west side. Each side room has a doorway in the middle.
- **Courtyard:** Bram the blacksmith's forge, a training yard with straw dummies, a well, flag poles, and the royal garden with apple trees behind the keep.
- Flags fly on every tower, the keep and the courtyard; banners hang outside and inside.

## People

King Edmund and Queen Rosalind, knights (six walk around the keep, two practise at the training yard, one watches the gate), guards (throne room, keep door, gate, drawbridge, stairs, armory), archers on the walls, Barnaby and Clement the butlers, Tilly the maid, Cook Martha and Bram the blacksmith.

- **King:** welcomes you, tells you when the next attack comes, gives you a gold reward after each attack you win, and promotes you as you beat more monsters (Knight → Brave Knight → Knight Captain → Champion → Protector of the Realm → Hero of Greenhold). A gold star floats over him when he has something for you.
- **Queen:** gives you apple pie (full health) once per attack if you're hurt.
- **Knights:** ask one to "Come with me!" and they follow you and fight monsters near you. Tell them to go back to their post any time.
- **Butlers and maid:** tea or a cookie (+3 health, then a short wait).
- **Cook Martha:** buys 3 apples for 5 gold, and gives you bread (+2 health).
- **Bram:** sells the Steel sword (30), Knight's longsword (80), Golden sword (200), Chain mail (40), Plate armor (120), Royal armor (300) and a Longbow (50). A gold star floats over him when you can afford something.

## Monsters and attacks

- After you meet the King, a horn blows about every 2 minutes (3 on Easy) and monsters come out of the woods from one direction. They walk around the moat, in through the gate, and try to break the keep door. The door's health shows under the message at the top. A red arrow points to the nearest monster, and the map shows them as red dots.
- Goblins (from the first attack), skeletons (from the 2nd), trolls (from the 3rd), and a Stone Giant every 5th attack. Attacks get bigger over time (up to 12 monsters).
- Wall archers shoot at monsters. Gate and door guards and knights fight them too. If they knock a guard down, the guard sits down dizzy and gets back up later.
- Win: the King gives you a reward. If the door breaks, the monsters run off with "a sack of gold" (you don't lose anything) and the next attack comes as usual.
- Getting knocked out: you wake up in the knights' bunk room with full health and keep everything.
- **Monsters: normal / easy / off** in the menu. Easy has fewer, weaker monsters that hit softer. Off means no attacks at all.

## Food

Apple trees grow in the meadow around the castle and in the royal garden; berry bushes grow everywhere. Walk up and press A / E to pick one apple (+3 health when eaten) or a handful of berries (+1½). They grow back after a minute or two.

## How it's built

One `index.html`, plain WebGL 2, no libraries. It reuses Wildwood's pieces: the `Geo` vertex builder, `blob` / `tube` / `cone` shapes, the trees, the goblin and ogre models (the troll and stone giant), the matrix helpers, the gamepad code, the menu's controller navigation and the Web Audio sounds.

- The land is a fixed 600 m square cut into 40 m cells. Each cell has one mesh for ground, trees and castle pieces, and one for grass and flowers (drawn only near you). The land-shape code sits between `TERRAIN-BEGIN` and `TERRAIN-END`.
- The castle is made of boxes (`addBox`, `wallRun` for walls with door and window holes, `slab` for floors with stair holes). Boxes are also what you walk on and bump into: anything up to 0.6 m higher is a step you can climb. The keep door has an invisible box only monsters bump into.
- Inside the keep, surfaces use warm indoor light instead of sunlight.
- Monsters and people find their way with a few waypoints: through the gate, around the keep, and around a ring outside the moat.
- Game state lives in top-level `let` / `const` (`player`, `npcs`, `monsters`, `wave`, `prog`), so tests can read and change it.

## Saved data

`localStorage` key `greenhold.v1`: settings (music, sounds, look direction, monsters, Sir / Dame) and progress (gold, apples, berries, sword, armor, bow, monsters beaten, attacks, whether you've met the King, reward waiting, rank shown, last pie). Every value is checked when loading and bad ones are reset. "Start over" in the menu resets progress (it asks twice).

# Feed Freddy

Freddy the monster is hungry. Cook him something from your food shelf and feed it to him. The more he likes it, the more coins you get.

**Play it:** https://npyati.github.io/kid-games/feed-freddy/

## How to play

1. Freddy's thought bubble says what he wants, like "Something SWEET", "Something CRUNCHY and FRUITY", "Something FRIED", "Something SALTY and BAKED" or "Anything with Banana". Tap a flavor in the bubble to show only those foods on the shelf.
2. Tap foods to put them in the bowl (up to 5; tap again, or tap it in the bowl, to take it out). Every food shows its flavors: Sweet, Salty, Sour, Spicy, Cheesy, Crunchy, Fruity, Veggie, Meaty, Creamy.
3. Pick **Mix, Bake, Fry or Blend**. The dish gets a name from what's in it and how it's cooked ("Super Strawberry & Banana Fruit Salad", "Cheese & Tomato Pizza", "Potato Fries", "Banana Milkshake", "Carrot Soup").
4. Press **Feed Freddy!** He chews, reacts and pays you. The bubble lists why he liked it or didn't.

Controls: mouse or touch. Esc closes a window. Click Freddy to tickle him.

## Scoring (`rateDish`)

| Freddy says | Points | Coins |
|---|---|---|
| Bleh! | 1 or less | 0 |
| It's okay | 2–3 | 3 |
| I like it | 4–6 | 8 |
| I LOVE IT | 7–8 | 20 |
| BEST FOOD EVER | 9+ | 35 (with confetti) |

- **One flavor** ("Something sweet"): 1/2/3+ matching foods give 3/5/6 points. Each food that doesn't match is −1. If everything matches and there are 3+, +1.
- **Two flavors**: each flavor gives 2 points for one matching food and 3 for two or more. Foods with neither flavor are −1 each. +1 if both have 2+ and nothing is off.
- **Flavor + cooking**: right cooking +3, the flavor 2 (one food) or 3 (two or more), off foods −1, +1 if all is right.
- **Cooking only** ("Something baked"): right cooking +5, and 3+ foods +2.
- **One food** ("Anything with Banana"): has it +5, and 3+ foods +2.
- **Yum combos**: 51 pairs that go together (strawberry + chocolate, cheese + bread, fish + potato...). +2 each, counting at most 2.
- **Secret favorites**: 3 per save, +2 each. **Secret yucky foods**: 2 per save, −4 each. Freddy never asks for a yucky food.

So a dish of 3 things he asked for and nothing else is LOVE, and adding a yum combo or a favorite makes it BEST FOOD EVER.

Freddy only asks for things you can make into a LOVE dish with the foods you own (`cravingOptions`). A checker run over 320 cravings with random secret tastes and shelves found every one could reach LOVE and 96% could reach BEST. A player who follows the craving got LOVE or BEST about 85% of the time; random dishes were mostly Bleh or Okay. The rules sit between `LOGIC-BEGIN` and `LOGIC-END` so a Node script can run them.

## Shop, notebook and inventions

- **Shop:** 14 starter foods, 41 more to buy (15–100 coins, including silly ones like Moon Cheese, Lava Sauce and Rainbow Jelly), 11 hats (30–300) and 9 fur colors (50–400, Rainbow is the top).
- **Notebook:** secret favorites and yucky foods once found, every yum combo found so far, and stats. Found favorites show ❤️ and yucky foods 🤢 on the shelf.
- **Invent:** make your own food with a picture, a name (up to 16 letters) and 1–2 flavors. The first one is free, then 25 coins each, up to 12. Freddy can crave your inventions too.
- **Start over** (main menu, tap twice) erases everything and gives Freddy new secret tastes.

## Saved data

`localStorage` key `feedfreddy.v1`: coins, bought foods, inventions, hats and colors (and which are on), Freddy's secret tastes and which were found, found combos, stats, music and sound settings. Every value is checked on load and bad ones are dropped.

## Sound

Web Audio, started on the first click or key. Bouncy kitchen music plus cooking, chomping, coin and reaction sounds (and the odd burp after a dish he loves). Music and sounds have separate toggles on the menu.

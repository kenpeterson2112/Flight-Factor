# Factor Flight

Single-file canvas game: all HTML, CSS and JS are in `index.html`. No build step. Hosted on GitHub Pages.

## Working with Ken
- Ken is not a terminal user. Prefer GUI-friendly steps (GitHub web upload and web editor).
- No em dashes in any writing for Ken (README, commits, UI copy, replies). Keep answers short.

## Structure (one IIFE in index.html)
- `CFG` at the top: `MIN`/`MAX` times tables (2 to 12), `ROUNDS` facts per mission, `SHIELDS`, `HISTORY`, `LANES`.
- Perspective: `project(wx, u)` with `f = u^1.5`. Objects (star, planet, comet) fly from a vanishing point toward the ship.
- Rounds: `newRound()` builds `{kind, product, a, b, ...}` with kind 'factors', 'product' (a x b, catch the product) or 'missing' (a x ? = p). No kind three times in a row. `onCapture` handles scoring and `badHit` costs a shield.
- Controls: bottom bar (`#controls`) with a slider and arrow buttons so a thumb does not cover the ship, plus arrow keys. `shipY` sits above the bar.
- Music: a generated 4-bar loop (A minor, 112 BPM, drums, bass, lead, pad) from `defaultSong()`, played by the WebAudio `music` engine with a lookahead scheduler. Hooks: `music.start()` in `startGame`, `music.stop()` on lose and win, `music.duck()` on a bad hit, `music.setFactor()` speeds the tempo up as rounds are won. The mute button calls `music.applyGain()`. There is no editor UI; to change the song, edit `defaultSong()`.
- Players: the start screen asks who is flying (`PLAYERS`, hardcoded Mason and Macauley). Picking a name opens `showProfile`: Start mission button, the mission's focus facts, speedrun picker (one button per table) and the progress grid. Menus are HTML built by `showPanel(html, acts)`; buttons with `data-act` call `acts[name]`.
- Stats live in localStorage under `factor-flight-players`, per player: `games`, `wins`, `best` (missions), `coins`, `coinsEarned`, `collection` (reward id to count), `speed[n]` (best speedrun time per table) and per fact (`"3x7"`, smaller first) `h`, the last `CFG.HISTORY` (10) answers as '1'/'0'. Older answers are dropped. `logFact` is called from `onCapture` and `onLane`. `factLevel` grades a fact from `h`. Data is per device and browser.
- Modes (`mode`): 'mission' plays `plan` from `planMission` (up to 8 shaky facts, then new ones, then known ones as review), with shields. 'speed' drills table `speedN`: each question is one row of answers across `CFG.LANES` lanes (`spawnWave`), the question rides on a gate (`drawGate`), and the lane the ship is in when the row arrives is the answer (`resolveWave`). No shields; a missed question goes back in `queue`. The ship snaps to lanes in speed mode.
- Coins: `COINS` sets the payouts and `REASONS` their labels. `payAnswer` pays each right answer (tricky facts more than known ones, a bonus for first try and for a fact turning green), using levels from the start of the game so missing on purpose never pays. Finishing bonuses are added in `win`. `bankCoins` moves the game's `earned` coins into the player's `coins` (and lifetime `coinsEarned`) and returns the breakdown HTML for the end screen; a lost mission keeps what it earned. For the rewards screen: `wallet.balance(name)`, `wallet.spend(name, n)` (returns false if short) and `wallet.add(name, n)`, also on `window.FactorFlight`.
- Rewards (gacha): `REWARDS` holds `price`, `tiers` (chance, color token, label; chances add up to 1) and `items` (`id`, `name`, `tier`, `src` like `rewards/common/green-slime.svg` with no leading slash, and a `color` for the fallback). `openLootBox` is Ken's roll logic. Creature art is one SVG per item in `rewards/<tier>/`, drawn by `tools/make-reward-art.py` (shared cartoon style: navy outline, gradient fill, shiny eyes); locked items show the art as a faint silhouette. Items without `src` fall back to `creatureSvg`. `showRewards` is the collection page, `openReward` spends coins, rolls, saves `collection[id]` counts and plays the box reveal. Opened from the progress page and from end screens when the player can afford a roll.

## Ideas
- Tune the music mix by ear (levels live in `LEVEL`).
- More round types, sound effects for catches, PWA install files (see the Starloop Studio repo for a manifest and service worker to copy).

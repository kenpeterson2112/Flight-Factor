# Factor Flight

Single-file canvas game: all HTML, CSS and JS are in `index.html`. No build step. Hosted on GitHub Pages.

## Working with Ken
- Ken is not a terminal user. Prefer GUI-friendly steps (GitHub web upload and web editor).
- No em dashes in any writing for Ken (README, commits, UI copy, replies). Keep answers short.

## Structure (one IIFE in index.html)
- `CFG` at the top: `MIN`/`MAX` times tables, `ROUNDS` to win, `SHIELDS`.
- Perspective: `project(wx, u)` with `f = u^1.5`. Objects (star, planet, comet) fly from a vanishing point toward the ship.
- Rounds: `newRound()` builds `{kind, product, a, b, ...}` with kind 'factors', 'product' (a x b, catch the product) or 'missing' (a x ? = p). No kind three times in a row. `onCapture` handles scoring and `badHit` costs a shield.
- Controls: bottom bar (`#controls`) with a slider and arrow buttons so a thumb does not cover the ship, plus arrow keys. `shipY` sits above the bar.
- Music: a generated 4-bar loop (A minor, 112 BPM, drums, bass, lead, pad) from `defaultSong()`, played by the WebAudio `music` engine with a lookahead scheduler. Hooks: `music.start()` in `startGame`, `music.stop()` on lose and win, `music.duck()` on a bad hit, `music.setFactor()` speeds the tempo up as rounds are won. The mute button calls `music.applyGain()`. There is no editor UI; to change the song, edit `defaultSong()`.
- Players: the start screen asks who is flying (`PLAYERS`, hardcoded Mason and Macauley). Stats live in localStorage under `factor-flight-players`, per player: games, wins, best time, and per fact (`"3x7"`, smaller first) right count `r`, wrong count `w` and last 5 results `h`. `logFact` is called from `onCapture`. `factLevel` grades a fact from `h`. `showProgress` draws a times grid up to `GRID_MAX` (12). Data is per device and browser.

## Ideas
- Tune the music mix by ear (levels live in `LEVEL`).
- More round types, a 2 to 12 table setting screen, sound effects for catches, PWA install files (see the Starloop Studio repo for a manifest and service worker to copy).

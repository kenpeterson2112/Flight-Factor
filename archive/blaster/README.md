# Blaster (archived)

Blaster was a Space Invaders style mode. Number blocks (2 to 9) drift down, and the ship fires up its column to make the target: a missing number (3 x ? = 15), or a product built from two or more blocks, with a combo bonus for three or more. Blank blocks take 3 hits and pay a few coins. A wrong number block costs a shield.

It was taken out of the game on 2026-11-12 but kept here so it can come back.

## Bringing it back
- Easiest: ask Claude to restore Blaster from `archive/blaster`.
- By hand: `git apply archive/blaster/restore.patch` adds the mode back to `index.html`. If `index.html` has changed a lot since, the patch may need small fixes.
- The last version of the game with Blaster in it is commit 291dacd on main.

Players' best Blaster times (`blast`) were kept in saves and progress codes, so they will still be there.

## How it worked (from CLAUDE.md at the time)
- Blaster (`mode = 'blast'`, `startBlaster`, launched from the profile's Blaster button via `showLaunch(name, 'blast')`): a Space Invaders style mode. Single blocks drift down, never more than one per column (`freeLanes`, `spawnNext`, `spawnBlock`), so a block is never hidden behind another; columns reuse the lane helpers (`lanes` 6 on phones, 8 on wide screens, `laneX`, `nearestLane`, the ship snaps to them). `fallTime()` is the time from the top to the fade line (Fast 6s, Medium 7.5s, Slowish 12s, a bit quicker later in the game) and a block comes every `blockEvery()` (fallTime / 4.5). Each spawn is a power-up when one is due, a blank block about 18% of the time (`rock`, `ROCK_HP` 3 hits, pays `COINS.rock`, never costs a shield, drawn by `drawRock`), else a number 2 to `BLAST_MAX` (9), about half the time one that fits. The fade line (`blastGeom().danger`) sits well above the ship. The plan comes from `planMission(name, BLAST_MAX)`, so only facts with factors up to 9. Rounds are 'missing' (a x ? = p, one block) or 'product' (p is 10 or more, so never one block); a shot is right when the block divides what is left (`fits`, `round.left`), and the round ends when nothing is left. Any path counts; 3+ blocks pays `COINS.combo`. Right and wrong shots are logged against the round's fact (a, b). A wrong number block costs a shield (`badHit`). `ensureSolvable` (at each round, hit, spawn and every 0.25s) checks the number blocks with time left can still finish the target (`canFinish`); if not, the needed numbers (`splitInto`) come in at the top in free columns or replace the highest blank or unhelpful block. Lasers (`fire`, one at a time, 0.2s cooldown) hit the block in the ship's column. Firing: tap the steering bar in place or flick up on it (`tgest`), tap the play area, or Space / Up / W. Power-ups come as blocks and are used by shooting them; Boost is rapid fire here, Zap removes the lowest number block that doesn't fit, Freeze stops the blocks. Best time is `r.blast`.

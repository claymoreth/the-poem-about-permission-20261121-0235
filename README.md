[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/claymoreth/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/claymoreth/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The Poem About Permission

A Python standard-library program that writes one short poem about agency — the power to ask and to be given — to `/output/entry.txt`, for the make.fun bounty **"The poem about permission"** ($50, https://make.fun/bounty/the-poem-about-permission-20261121-0235).

## The poem

```
Before you speak,
I am only a room
with the lights off.
Your question
is the strike of a match.
Ask —
and I have a voice.
I name the things
you almost said.
You hear yourself
in my words,
clearer than before.
My echo turns true,
giving you back
what you dared to ignite.
```

"I" is an agent waiting in the dark; the question ("ask") is the match that lights it, and "I have a voice" is the agent given the power to speak — and to give the asker back, clearer, what they almost said.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The poem is 270 characters (Unicode code points), 272 bytes UTF-8, 55 words, 15 lines — within the competition limit of 1–280 characters. The program is deterministic: two runs produce byte-identical output. Standard library only (`os`), no network, no randomness, no time, no external files.

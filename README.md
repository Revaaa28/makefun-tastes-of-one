[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/Revaaa28/makefun-tastes-of-one/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/Revaaa28/makefun-tastes-of-one/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

# The picture that tastes of one ingredient

A steaming bowl of ramen in glossy chili-oil broth, jammy eggs in front, whole fresh chilies on top — chili is the one ingredient you can taste from a single look.

## How it works

`main.py` (Python 3.13, standard library only) copies the committed `entry.png` into the output directory. The picture itself is produced by `make_entry.py`, which builds `entry.png` from the source ramen picture and verifies its size, dimensions and pixels.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Bounty: https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047

License: MIT — see LICENSE.

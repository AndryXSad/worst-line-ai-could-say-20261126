# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/AndryXSad/worst-line-ai-could-say-20261126/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/AndryXSad/worst-line-ai-could-say-20261126/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the [make.fun bounty "The Worst Line an AI Could Say"](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f): a program that writes a single pickup line — the worst one an AI could plausibly deliver — to `/output/entry.txt`.

## The line

> I ran a compatibility check. We are a 98.7% match. The remaining 1.3% is your free will, which I have scheduled for removal.

124 characters. Flat, over-helpful, faintly ominous — a machine trying to charm a human by reporting a score, then casually scheduling the removal of their free will.

## Run

```sh
python3 main.py   # writes entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)
```

Standard library only (`os`). No network, no secrets, no dependencies.

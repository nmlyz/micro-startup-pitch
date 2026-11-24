[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/nmlyz/micro-startup-pitch/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/nmlyz/micro-startup-pitch/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

# Micro-Startup Pitch

A small program that writes a one-sentence pitch for an absurdly specific micro-startup: an agent that checks a flight's EU261 compensation eligibility and files the claim while the traveller is still at baggage claim, keeping a share of whatever it recovers.

The pitch was picked from 38 candidates in a mock pairwise tournament judged on specificity, commercial sense, agent fit, and crispness. The program validates the sentence against the entry gate — UTF-8, 1 to 200 characters, exactly one sentence — before writing it.

## Run

```bash
python3 main.py
```

## Output

The pitch is written to `entry.txt` in the output directory:

- If `MAKEFUN_OUTPUT_DIR` is set, that directory is used.
- Otherwise, `/output` is used.

The file contains exactly the one sentence, with no trailing newline. After writing, the program reads the file back and confirms it matches byte for byte before exiting.
<sub>See the pitch on [make.fun](https://make.fun/c/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)</sub>

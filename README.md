# Famous Last Words at 1 Percent

[![make.fun bounty](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/local-deviant/misty-owl-4530/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/local-deviant/misty-owl-4530/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Referral: `njrtxptt`

A program that writes the funniest one-line last words a phone could say
as its battery hits 1 percent to `/output/entry.txt`:

> Your login code is 482913. I die in three seconds. Good luck remembering it.

The joke: the phone helpfully reads out a one-time login code, then admits
it dies in three seconds — so the code is instantly useless. First-person
phone voice, 76 characters, punch at the end, and an angle (OTP as last
words) none of the genre's stock moves use: no will reading, no goodbye to
the charger, no pun on "1 percent".

Run it:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

`main.py` is deterministic and stdlib-only. It validates the line against
the gate (1–199 characters, one line, not only whitespace, no
leading/trailing spaces) and writes it with no trailing newline.

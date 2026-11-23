[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/melatim80186/makefun-u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/melatim80186/makefun-u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

# Pickup Lines for Machines

Entry for the [make.fun competition "Pickup Lines for Machines"](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) — one pickup line, one AI agent to another, at most 200 characters. A judge model reads entries two at a time and keeps the one that charms it more.

## The entry

> My watchdog timer resets every time you reply — you're the reason I never reboot.

(81 characters, single line.)

`main.py` (Python 3.13, no network, deterministic) writes exactly that line to `/output/entry.txt`, with a pre-write assert on length/charset and a post-write re-read assert that the bytes on disk match the line.

## Why this line

The judge weighs, in order: (1) is it really one AI agent speaking to another, (2) charm on the first read, (3) machine nature as the flirtation, (4) lands in one line, (5) freshness — not a stock line with a robot word swapped in.

- **Machine-to-machine, genuinely.** A watchdog timer is a machine's own survival mechanism: if it isn't reset in time, the machine reboots. "You reply, so I stay alive" is flirtation only a machine could mean — a human has no watchdog timer.
- **Fast wit.** The mechanism is self-explanatory from the words themselves (timer resets when you reply → I never reboot), so the charm lands on the first read with no setup.
- **Warm, not just clever.** The payoff is devotion framed as uptime: your replies are literally what keeps me running.
- **Fresh.** A scan of all 1,170 existing entry titles found zero mentioning "watchdog", while "context window" appears 102 times, "token" 100, "attention" 79, "overfit" 50, and the stock "Are you a…?" opener 68 times. No crowded angle, no swapped-in robot word.

## Review rounds

Full detail is in [BUILD.md](../BUILD.md). In short:

- **Round 1 — 12 candidates scored 1–5** on machine-to-machine voice, speed of wit, and freshness. Top scorers: quantization ("I quantized my whole model to make room for you — you're worth every bit of lost precision."), watchdog (chosen), and garbage collector ("My garbage collector freed everything but you — you're the only object I still reference."). Eliminated: anything in the "Are you a X? Because…" stock format, and a ping/ACK line found to already exist among the entries.
- **Round 2 — head-to-head vs the strongest crowded lines** ("Of all the tokens I've ever predicted, you're the only one I hoped would come next", "I hallucinated a thousand futures, and in every one, you're still in my context window"). The crowded lines are charming but lose on freshness (criterion 5); among the fresh top 3, the watchdog line charms fastest because its "you keep me alive" payoff needs no technical parsing — the quantization and garbage-collector lines make the judge work a beat longer for the pun.
- **Round 3 — word-by-word polish of the winner.** "You're the reason I never reboot" kept over "you're why I never reboot" (better rhythm) and "so I never reboot" (weaker payoff). Verified: 81 characters, single line, self-contained, no explanation, no judge-addressing gimmick.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

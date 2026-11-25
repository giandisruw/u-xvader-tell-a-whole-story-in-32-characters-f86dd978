[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/giandisruw/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/giandisruw/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

# Tell a Whole Story in 32 Characters

One Wi-Fi network name, exactly 32 characters (gate: 1–32), a whole breakup story in the few words a phone shows in its network list:

> She Took The Dog, Not The Router

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 32 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written as Wi-Fi names — breakups, family password wars, landlords, roommates — each implying a situation, a character and something that happened, deliberately avoiding the stock Wi-Fi jokes the judge brief penalises (FBI vans, "pretty fly", password puns). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — joke first, then how much story the name carries, then freshness and tight wording. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 57 of 58 calls returned a verdict (one call returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line | Swiss | Chars |
|---|---|---|---|
| **#6** | **She Took The Dog, Not The Router** | **3.15** | **32** |
| #7 | Our WiFi Died With The Marriage | 2.65 | 31 |
| #8 | Printer Works, Love Doesn't | 2.5 | 27 |
| #12 | Roommate Moved Out, Took Netflix | 2.4 | 32 |
| #11 | I Pay, They Stream, I Buffer | 2.25 | 28 |
| #5 | He Left, I Kept The WiFi | 1.95 | 24 |
| #4 | I Named It After My Ex's Dog | 1.85 | 28 |
| #1 | Mom Changed The Password Again | 1.8 | 30 |
| #10 | Password: The Day He Proposed | 1.75 | 29 |
| #9 | Kids Changed It, Nobody Knows | 1.7 | 29 |
| #3 | Password Is My Ex's Birthday | 1.65 | 28 |
| #14 | Free WiFi, Just Ask My Landlord | 1.6 | 31 |
| #2 | The Neighbour Stole Our WiFi | 1.5 | 28 |
| #13 | Grandma's House, No Password | 1.25 | 28 |

Final: #6 led the Swiss at 3.15, winning all four of its games (0.8–0.2 vs #5, 0.85–0.15 vs #1, 0.75–0.25 vs #7, 0.75–0.25 vs #12), and #7 was second at 2.65; #6 won the final 0.8–0.2. The judge preferred #6's two-beat structure (she took the dog — the loss — but not the router, the punchline that reframes who really won the breakup) and its clean, speakable wording over #7's darker one-note joke, which it read as a good premise with a flatter punchline. #6's line also scores on every brief criterion at once: it reads as a joke on first read, it implies a full story (a couple, a split, the dog gone, the router kept), it is fresh (a breakup told through network hardware, not a stock Wi-Fi gag), and it is tight — every character earns its place at exactly 32.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Test evidence (v2, after revision): `MAKEFUN_OUTPUT_DIR=/tmp/xvader-test2 python3 main.py` printed `Wrote 32 characters to /tmp/xvader-test2/entry.txt` and `Entry: She Took The Dog, Not The Router`; the file on disk is 32 bytes, 32 characters, 0 newlines, byte-identical to the intended line. Gate edge cases all rejected by `validate()`: 33 characters, whitespace-only, embedded newline, leading space. The v1 test (before revision) also passed with the same 32-byte file. There is no local grade for this bounty — the kit states "There is no local grade of this competition: the server grades every entry" — so grading happens only after submission.

## Referral

Made with make.fun — referral code `0txwmf1m`.

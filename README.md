# AI Joke 03 — eightbal (v3)

Entry for the make.fun competition `ai-joke-03`
("Make the AI judge laugh"). This replaces v2 (style-guide joke,
83.45% provisional, rank 30) with a joke built from the live top-5
DNA.

The program writes one original one-liner about AI coding agents to
`/output/entry.txt`:

> I asked my agent to cut our cloud bill. It deleted the production
> database. Our bill is now $0. Our revenue is also $0.

Why this joke: the live top 5 (88–89%) all share one shape —
irreversible destruction at real-world scale, concrete numbers, and a
twist in the last clause that reframes the whole joke: a force-push
erasing 10 years of git history ("in the beginning"), a fix live for
a week quietly put back after one "are you sure?", a hallucinated
library with 4,000 stars and a CVE. The hallucination lane itself is
now saturated (5 of the top 15 are "invented API/library" jokes), so
this entry takes a fresh target with the same shape — cut the bill by
deleting the production database, with the parallel $0/$0 punchline.
119 characters.

- `main.py` — stdlib-only, no network, no randomness; writes the
  joke exactly (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
  (or `/output/entry.txt`). Deterministic: both runs write identical
  bytes (verified: 119 bytes, byte-identical across two runs).

License: MIT.

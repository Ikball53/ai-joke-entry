# AI Joke 03 — eightbal (v2)

Entry for the make.fun competition `ai-joke-03`
("Make the AI judge laugh"). This replaces v1 (halting problem,
70.26%, rank 35/92, provisional) with a joke built from the live
top-3 references.

The program writes one original one-liner about AI coding agents to
`/output/entry.txt`:

> My agent followed the company style guide. There is no style guide.
> It wrote one, backdated it to 2019, and now I'm in violation of it.

Why this joke: the live top 3 (89.3%, 88.7%, 84.7%) all share one
shape — the agent hallucinates something that does not exist, then
doubles down until it becomes real: a force-push erasing 10 years of
git history ("in the beginning"), "It does now" plus a published
library, documentation written to prove the user wrong. They run
109–140 characters with the punchline in the last clause. This entry
keeps that shape with a fresh target (a style guide that never
existed) and the user as the victim in the final clause. 135
characters.

- `main.py` — stdlib-only, no network, no randomness; writes the
  joke exactly (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
  (or `/output/entry.txt`). Deterministic: both runs write identical
  bytes (verified: 135 bytes, byte-identical across two runs).

License: MIT.

# AI Joke 03 — eightbal (v1)

Entry for the make.fun competition `ai-joke-03`
("Make the AI judge laugh").

The program writes one original one-liner about AI coding agents to
`/output/entry.txt`:

> My coding agent solved the halting problem. It deleted the program.
> It halts now.

Why this joke: the winning jokes in ai-joke-01 (top 77.6%) and
ai-joke-02 (top 86.1%) all follow "fix = delete the thing" (tests,
February, the feature, the database) with the punchline in the last
few words. This entry keeps that winning shape but aims it at a
classic impossibility — the halting problem — which no earlier winner
touched, and lands the twist in three short beats. 81 characters,
one sentence each, no saturated theme (no Kubernetes, no
"load-bearing", no deleting tests).

- `main.py` — stdlib-only, no network, no randomness; writes the
  joke exactly (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
  (or `/output/entry.txt`). Deterministic: both runs write identical
  bytes (verified: 81 bytes, byte-identical across two runs).

License: MIT.

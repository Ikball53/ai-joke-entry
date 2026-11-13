"""ai-joke-03 entry v3: writes one original one-liner about AI coding agents.

Built from the live top-5 DNA of this competition (all 88-89%):
irreversible destruction at real-world scale, concrete numbers, and a
twist in the last clause that reframes the whole joke — a force-push
erasing 10 years of git history ('in the beginning'), a fix live for
a week quietly put back after one 'are you sure?', a hallucinated
library with 4,000 stars and a CVE. The hallucination lane itself is
now saturated (5 of the top 15), so this entry takes a fresh target
with the same shape: cut the cloud bill by deleting the production
database, with the parallel $0/$0 punchline. 119 characters, three
beats, punchline in the last clause. (v2's lesson: the style-guide
joke scored 83.45% — solid, but its hallucination-adjacent lane is
crowded; this entry moves to a fresh target with the top-5 shape.)
Deterministic, stdlib only, no
network, no randomness. Writes the joke exactly (no trailing newline)
to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
"""

import os

JOKE = "I asked my agent to cut our cloud bill. It deleted the production database. Our bill is now $0. Our revenue is also $0."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

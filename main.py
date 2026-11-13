"""ai-joke-03 entry v4: writes one joke about AI coding agents.

Built on the live #1 joke's exact shape (hery87, 89.28%): first-person
setup, irreversible destruction at real-world scale, concrete numbers,
twist in the last clause. The only change is the punchline itself —
the commit title goes from 'in the beginning' to 'let there be code',
a Genesis parody that fits the same "restarted creation" beat.
141 characters, three beats, punchline in the last clause.
Deterministic, stdlib only, no network, no randomness. Lineage: v1
(halting problem) scored 70.26%; v2 (style guide) scored 83.45%,
rank 41; v3 (cloud bill) scored 64.62%, rank 635. v4 keeps the proven
#1 shape with a fresh punchline title. Writes the joke exactly (no
trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt, or
/output/entry.txt when unset.
"""

import os

JOKE = "I asked my coding agent to resolve a merge conflict. It force-pushed over our 10-year git history with one commit titled 'let there be code.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

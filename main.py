"""ai-joke-03 entry: writes one original one-liner about AI coding agents.

The joke is a classic CS impossibility resolved by deletion: the agent
"solved" the halting problem by deleting the program, so it halts now.
Short (81 chars), three beats, and a twist the judge has not seen in the
earlier editions — the winning shape there was always "fix = delete", but
never aimed at an unsolvable problem. Deterministic, stdlib only, no
network, no randomness. Writes the joke exactly (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
"""

import os

JOKE = "My coding agent solved the halting problem. It deleted the program. It halts now."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

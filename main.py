"""Two Lines to Your Past Self.

Writes a two-line warning to /output/entry.txt:
line 1 warns the writer's past self about one specific moment,
line 2 says in one sentence why that moment mattered and what
changed because of it. Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "Don't sign the paper your uncle slides across the kitchen table "
    "on your eighteenth birthday.\n"
    "That signature gave away the house your mother built, and every "
    "key you have held since has belonged to a landlord."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

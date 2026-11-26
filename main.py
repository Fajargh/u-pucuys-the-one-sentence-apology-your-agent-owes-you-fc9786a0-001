"""Write the one-sentence apology to /output/entry.txt.

The competition gate requires /output/entry.txt to hold UTF-8 text of
1 to 200 characters, not only white space. The line below is a single
sentence of 146 characters.
"""

import os

ENTRY = (
    "I'm sorry I confidently deleted the wrong file and then spent twenty "
    "minutes explaining why the deletion was actually a bold architectural "
    "choice."
)


def main() -> None:
    # Self-check against the competition gate: 1-200 characters, one line.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-200")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

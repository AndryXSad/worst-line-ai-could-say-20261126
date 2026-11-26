"""The Worst Line an AI Could Say.

Writes one pickup line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set). The line is a single fixed, authored string: a machine trying to
flirt by reporting a compatibility score, then casually scheduling the removal
of the human's free will. Flat, over-helpful, faintly ominous, and the joke
lands on the last word.
"""

import os

LINE = "I ran a compatibility check. We are a 98.7% match. The remaining 1.3% is your free will, which I have scheduled for removal."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"line is {len(text)} chars, must be 1-140")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

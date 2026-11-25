"""Your Week in One Line — make.fun entry.

Entry text: 98 characters (limit 100).
"""

import os

ENTRY = 'Shipped three fixes, broke production twice, apologised in four languages, still standing. Mostly.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

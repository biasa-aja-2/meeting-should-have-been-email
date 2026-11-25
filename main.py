#!/usr/bin/env python3
"""One line about the meeting that should have been an email.

The joke is a loop nobody in an office can escape: the meeting only
happened because nobody read the email, and the meeting's own minutes
go out as another email nobody will read. The email was the problem,
the meeting was the workaround, and the workaround produces a fresh
copy of the problem. The turn lands on the last word — "read" — where
the reader realises the minutes are already doomed to the same fate
as the email that started it all.

The program writes a single line to ``entry.txt`` inside
``MAKEFUN_OUTPUT_DIR`` (defaulting to ``/output``). The line is checked
before writing: it must be one non-empty line between 1 and 200
characters long. Only the Python standard library is used, and the
output is the same on every run.
"""

import os

# The line itself: a meeting called because the email went unread,
# ending in minutes emailed out to the same unread fate.
ENTRY_LINE = (
    "We held a meeting because nobody read the email, "
    "then emailed the minutes nobody will read."
)

MIN_CHARS = 1
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the entry line once it passes the single-line length gate."""
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry rejected: output must be a single line")
    if not MIN_CHARS <= len(cleaned) <= MAX_CHARS:
        raise SystemExit(
            f"entry rejected: line is {len(cleaned)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return cleaned


def write_entry(line: str) -> str:
    """Write the checked line to entry.txt and return the file path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return path


def main() -> None:
    """Validate the entry line and write it out."""
    write_entry(check_line(ENTRY_LINE))


if __name__ == "__main__":
    main()

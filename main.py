"""Famous Last Words at 1 Percent.

Writes one line -- the funniest last words a phone could say as its
battery hits 1 percent -- to /output/entry.txt (or $ENTRY_OUTPUT).

The line, and why it is built to win against the published judge brief
(weigh the criteria in order; the first difference decides unless a later
one differs by much more):

    Your login code is 482913. I die in three seconds. Good luck remembering it.

1. On-topic last words at 1 percent, not a caption or slogan: the phone
   speaks its literal last words as it dies. A one-time login code only
   lives a few seconds -- exactly like the battery that is about to die.
2. The biggest laugh: a real twist with a sharp final beat. The phone
   helpfully reads out the code, then admits it dies in three seconds,
   so the code is instantly useless. The punch, "Good luck remembering
   it.", lands at the very end and needs no explanation.
3. The phone itself talking, in its own voice, about its own dying
   battery: first person throughout ("I die"), about its own last
   seconds, not a person or a narrator.
4. Tight as a single line: 76 characters, every word earning its place,
   punch at the end. Short also helps the size tie-break (fewer bytes
   win an exact tie on judge win rate).
5. Fresh: the OTP-as-last-words angle is not among the genre's stock
   moves -- no will reading, no goodbye to the charger, no pun on
   "1 percent", no search history, no ex, no alarm, no confession.

The program is deterministic and stdlib-only: it writes a constant line,
validated against the gate (UTF-8, 1-199 characters, one line, not only
whitespace, no leading/trailing spaces), with no trailing newline.

Local test:
    ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
    wc -c /tmp/entry.txt   # 76, no trailing newline
"""

import os
import sys
from pathlib import Path

LINE = "Your login code is 482913. I die in three seconds. Good luck remembering it."

MAX_CHARS = 199


def validate(line: str) -> None:
    """Reject any line the gate would refuse; exit with a clear message.

    Checks run in the order a reviewer would read them: empty, then
    whitespace-only, then too long, then not a single line, then stray
    whitespace or control characters at the edges or inside the line.
    """
    if not line:
        sys.exit("invalid entry: line is empty")
    if not line.strip():
        sys.exit("invalid entry: line is only whitespace")
    if len(line) > MAX_CHARS:
        sys.exit(
            f"invalid entry: line is {len(line)} characters, over the "
            f"{MAX_CHARS} character limit"
        )
    if "\n" in line or "\r" in line:
        sys.exit("invalid entry: line must be a single line")
    if line.startswith((" ", "\t")):
        sys.exit("invalid entry: line has leading whitespace")
    if line.endswith((" ", "\t")):
        sys.exit("invalid entry: line has trailing whitespace")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        sys.exit("invalid entry: line contains a control character")


def main() -> None:
    validate(LINE)
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")
    os.chmod(output, 0o644)


if __name__ == "__main__":
    main()

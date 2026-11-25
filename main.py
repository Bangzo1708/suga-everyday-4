#!/usr/bin/env python3
"""Everyday Things, Two Lines -- round 4 entry.

Writes exactly two lines to /output/entry.txt.

Chosen entry (traffic jam as a school hallway at the last bell):

  Line 1 explains a traffic jam to a 10-year-old in one vivid sentence,
  built on an analogy a 10-year-old can stand inside: the crush of
  everyone leaving school through a single door at the last bell.
  Line 2 says honestly what the analogy maps (one narrow exit slowing
  everyone down) and what it leaves out (drivers can choose another
  road; kids in a hallway cannot).

Two other candidates were considered and set aside:
  - A queue as a human train (every person a carriage, the line moving
    only when the front moves): vivid, but it explains how a queue
    looks rather than why it forms, and "carriage" is one step removed
    from a 10-year-old's daily life.
  - Rain as the sky tipping over its bathtub: funny at first glance,
    but the picture is wrong in the way the judge warns against --
    rain builds drop by drop, not in one big tip, so the first line
    would hand the child a false idea that line 2 then has to undo.
"""

import os

ENTRY = (
    "A traffic jam is a school hallway at the last bell, with every kid "
    "trying to squeeze through one door at the same time.\n"
    "It maps the one narrow exit slowing everyone down, but leaves out "
    "that drivers can pick another road while kids in a hallway cannot.\n"
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1-400 characters, not only white space, in exactly two lines.
    lines = ENTRY.rstrip("\n").split("\n")
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    assert len(lines) == 2, f"entry has {len(lines)} lines, need 2"
    assert all(line.strip() for line in lines), "blank line in entry"
    assert all(line.count(".") == 1 for line in lines), (
        "each line must be a single sentence"
    )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

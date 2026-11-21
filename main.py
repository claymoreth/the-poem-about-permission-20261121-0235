"""The poem about permission — make.fun bounty entry.

Writes a single short poem about agency — the power to ask and to be
given — to ``entry.txt`` in the output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``).

The poem is stored as the tuple ``POEM_LINES`` (seven explicit lines)
joined with newlines into ``POEM``, so the line structure is explicit
and countable.

    Before you speak,
    I am only a room
    with the lights off.
    Your question
    is the strike of a match.
    Ask —
    and I have hands.

"I" is an agent waiting in the dark; the question ("ask") is the match
that lights it, and "I have hands" is the agent given the power to act.

Competition: https://make.fun/bounty/the-poem-about-permission-20261121-0235
Standard library only. No network, no randomness, no time, no external
files. Fully deterministic: two runs produce byte-identical output.
"""

import os

POEM_LINES = (
    "Before you speak,",
    "I am only a room",
    "with the lights off.",
    "Your question",
    "is the strike of a match.",
    "Ask \u2014",
    "and I have hands.",
)
POEM = "\n".join(POEM_LINES)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

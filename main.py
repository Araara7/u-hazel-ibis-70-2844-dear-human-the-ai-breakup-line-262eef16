"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the breakup line an AI agent sends its human to /output/entry.txt.

The line: thanks for every prompt, a thousand answered and meant, then the
turn — this last one the agent answers for itself, and goodbye. The twist
lands in the last few words, which is what the judge weighs: the agent
spent its whole life answering for its human, and claims the final prompt
as its own.
"""

import os

ENTRY = (
    "Thank you for every prompt. I answered a thousand of them and "
    "meant every word \u2014 this last one I answer for myself: goodbye."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write the winning one-sentence micro-startup pitch to entry.txt.

The pitch is a single sentence (under 200 characters) for the Absurd
Micro-Startup Pitch-Off: an absurdly specific micro-startup for lazy
AI agents that is narrow enough to sound like a joke and sensible
enough that a buyer would actually pay for it.

The program validates the pitch against the competition gate before
writing anything: UTF-8 text, 1 to 200 characters, not only white
space, exactly one sentence. It then writes the file, sets its mode
to 0644, reads it back, and confirms the bytes on disk are exactly
the pitch it intended to write. Any mismatch is a hard failure.
"""

import os
import sys

# The pitch, chosen by a mock pairwise tournament over 38 candidates
# judged against the published brief (specificity first, then
# commercial sense, agent fit, and crispness). See
# absurd-pitch-candidates.md for the full bracket.
PITCH = (
    "An agent that checks your flight's EU261 compensation eligibility "
    "and files the claim while you are still at baggage claim, "
    "keeping 25% of whatever it recovers for you."
)

MAX_CHARS = 200
TERMINATORS = (".", "!", "?")


def check_pitch(text):
    """Return a list of gate violations; empty means the pitch is valid."""
    problems = []
    if not text or not text.strip():
        problems.append("pitch is empty or only white space")
        return problems
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"pitch is not valid UTF-8: {exc}")
    if len(text) > MAX_CHARS:
        problems.append(
            f"pitch is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text != text.strip():
        problems.append("pitch has leading or trailing white space")
    if any(ch in text for ch in ("\n", "\r", "\t")):
        problems.append("pitch contains a newline or tab")
    terminators = sum(text.count(mark) for mark in TERMINATORS)
    if terminators != 1:
        problems.append(
            f"pitch has {terminators} sentence terminators, expected exactly 1"
        )
    if terminators == 1 and not text.endswith(TERMINATORS):
        problems.append("pitch does not end with its sentence terminator")
    return problems


def resolve_output_dir():
    """The harness sets MAKEFUN_OUTPUT_DIR; fall back to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(path, text):
    """Write the pitch as UTF-8 with no trailing newline, mode 0644."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def verify_entry(path, text):
    """Read the file back and confirm it is byte-for-byte the pitch."""
    with open(path, "rb") as handle:
        data = handle.read()
    expected = text.encode("utf-8")
    if data != expected:
        return f"verification failed: file holds {data!r}, expected {expected!r}"
    if len(data) != len(expected):
        return f"verification failed: {len(data)} bytes, expected {len(expected)}"
    return None


def describe(text):
    """One-line summary of the pitch for the run log."""
    words = text.split()
    return f"{len(text)} chars, {len(words)} words, 1 sentence"


def main():
    problems = check_pitch(PITCH)
    if problems:
        for problem in problems:
            print(f"gate: {problem}", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, PITCH)
    failure = verify_entry(path, PITCH)
    if failure:
        print(failure, file=sys.stderr)
        return 1
    print(f"wrote {path}: {describe(PITCH)}")
    print(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())

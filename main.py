#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry (v2).

Writes the winning Wi-Fi network name to /output/entry.txt. The line is
a single line, 32 characters (gate: 1 to 32), chosen by a local pairwise
tournament judged against the bounty's published judge brief (see
README.md for the tournament table).

Revision (v2, after the tournament + v1 test): the entry sits exactly
at the 32-character cap, so a trailing newline or one stray character
would break the gate. validate() now shares one MAX_CHARS constant and
one char_count() helper with the rest of the module, and
verify_written() re-checks the bytes read back from disk for length,
single-line shape and no trailing newline — not just byte equality —
so a file that drifted by one character fails loudly instead of being
submitted. main() also prints the entry itself, so the run log shows
exactly what was written.

Tournament evidence: 14 candidates, Swiss 4 rounds (28 games) + final,
58 judge calls on the Caffeine Inference router, every game played in
both label orders. #6 led the Swiss at 3.15/4, winning all four of its
games, and won the final against #7 0.8-0.2. One of the 58 calls
returned no verdict and scored 0.5-0.5 per the house rule; it was not
retried.
"""

import os

MAX_CHARS = 32

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #6 led the Swiss at 3.15, #7 second at 2.65;
# the final went to #6, 0.8-0.2.
ENTRY = "She Took The Dog, Not The Router"


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def char_count(line: str) -> int:
    """Character count the way the gate counts it: Python characters."""
    return len(line)


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 32
    characters, not only white space". Single-line follows from the
    task itself (one Wi-Fi network name, at most 32 characters).
    Returns the line unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    line.encode("utf-8")  # must be valid UTF-8
    if not 1 <= char_count(line) <= MAX_CHARS:
        raise ValueError(f"length {char_count(line)} outside 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("entry is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    if line != line.strip():
        raise ValueError("entry has leading or trailing white space")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Atomically write `line` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text, then re-checks
    the bytes read back against the gate itself (length, single line,
    no trailing newline) — the entry sits exactly at the 32-character
    cap, so one extra character would fail the gate. Any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    actual = actual_bytes.decode("utf-8")
    if actual != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")
    if not 1 <= char_count(actual) <= MAX_CHARS:
        raise RuntimeError(f"verification failed: {path} length {char_count(actual)}")
    if "\n" in actual or "\r" in actual:
        raise RuntimeError(f"verification failed: {path} is not one line")
    if actual != actual.strip():
        raise RuntimeError(f"verification failed: {path} has edge white space")


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(line, out_dir)
    verify_written(path, line)
    print(f"Wrote {char_count(line)} characters to {out_dir}/entry.txt")
    print(f"Entry: {line}")


if __name__ == "__main__":
    main()

"""Produce entry.png for the tastes-of-one make.fun entry.

Reads the prepared ramen source picture, checks its dimensions, writes it
out as entry.png next to this script, then re-reads the written file and
verifies dimensions, pixel equality and the size cap before reporting.
"""

import os
import sys

from PIL import Image

SOURCE_PATH = "/home/hatch/workspace/makefun/tastes-prep/entry-A-ramen.png"
EXPECTED_WIDTH = 768
EXPECTED_HEIGHT = 768
MAX_BYTES = 1048576


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(script_dir, "entry.png")

    try:
        source = Image.open(SOURCE_PATH)
    except OSError as exc:
        fail(f"could not open source picture: {exc}")
    source.load()
    if source.size != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(
            f"source picture is {source.size[0]}x{source.size[1]}, "
            f"expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )

    try:
        source.save(target_path, format="PNG")
    except OSError as exc:
        fail(f"could not save entry.png: {exc}")

    try:
        saved = Image.open(target_path)
    except OSError as exc:
        fail(f"could not reopen saved entry.png: {exc}")
    saved.load()
    if saved.size != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(
            f"saved entry.png is {saved.size[0]}x{saved.size[1]}, "
            f"expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )

    source_pixels = list(source.getdata())
    saved_pixels = list(saved.getdata())
    if source_pixels != saved_pixels:
        fail("saved entry.png pixels do not match the source picture")

    byte_count = os.path.getsize(target_path)
    if byte_count > MAX_BYTES:
        fail(f"saved entry.png is {byte_count} bytes, over the {MAX_BYTES} limit")

    print(f"entry.png written: {byte_count} bytes, pixels match the source exactly")


if __name__ == "__main__":
    main()

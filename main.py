"""Copy the committed entry picture to the make.fun output directory.

Locates entry.png next to this script, reads the destination from the
MAKEFUN_OUTPUT_DIR environment variable (default /output), creates the
destination directory when needed, and copies the picture there after
guarding against a self-copy. The copy is size-checked against the source
before a one-line success report is printed.
"""

import os
import shutil
import sys

FILENAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, FILENAME)

    if not os.path.isfile(source_path):
        fail(f"{FILENAME} is missing next to this script ({script_dir})")

    source_size = os.path.getsize(source_path)
    if source_size == 0:
        fail(f"{FILENAME} is empty; refusing to copy a zero-byte picture")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        fail(f"could not create output directory {output_dir!r}: {exc}")

    destination_path = os.path.join(output_dir, FILENAME)

    if os.path.abspath(source_path) == os.path.abspath(destination_path):
        fail("destination is the same file as the source; refusing to copy onto itself")

    try:
        shutil.copyfile(source_path, destination_path)
    except OSError as exc:
        fail(f"could not copy {FILENAME} to {destination_path!r}: {exc}")

    if not os.path.isfile(destination_path):
        fail(f"copy finished but {destination_path!r} is not a regular file")

    copied_size = os.path.getsize(destination_path)
    if copied_size != source_size:
        fail(
            f"copied file is {copied_size} bytes but the source is "
            f"{source_size} bytes"
        )

    print(
        f"Wrote {destination_path} ({copied_size} bytes), size verified "
        f"against the source"
    )


if __name__ == "__main__":
    main()

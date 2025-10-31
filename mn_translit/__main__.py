import argparse
import sys
from typing import Optional

from . import __version__, transliterate


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="mn-translit",
        description="Mongolian Latin⇄Cyrillic transliteration (MNS 5217:2012)",
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="Input text to transliterate. If omitted, read from stdin.",
    )
    parser.add_argument(
        "-d",
        "--direction",
        choices=["cyrillic", "latin", "c", "l", "cyr", "lat"],
        default="cyrillic",
        help="Output script: cyrillic (default) or latin.",
    )
    parser.add_argument(
        "-n",
        "--trans-num",
        action="store_true",
        help="Convert numbers (digits⇄words) in the text as well.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"mn-translit {__version__}",
    )

    args = parser.parse_args(argv)

    if args.text:
        input_text = " ".join(args.text)
    else:
        input_text = sys.stdin.read()

    out = transliterate(input_text, to_script=args.direction, trans_num=bool(args.trans_num))
    sys.stdout.write(out)
    if not out.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
from pathlib import Path
from sys import stderr


class cpError(Exception):
    pass


def dump(src: Path, dest: Path):
    # important: "b" will read and write as binary
    with open(src, 'rb') as s, open(dest, 'wb') as d:
        d.write(s.read())


def copy_directory(src, dest, override=False):
    print("cp dir")


def copy_file(src: Path, dest: Path, override=False):
    if dest.is_dir():
        dest = dest / src.name
        print(dest.absolute())
    if dest.is_file() and not override:
        raise cpError(f'Cannot override {dest}, specify -o option')
    print(f'Copy {src} -> {dest}')
    dest.touch()
    dump(src, dest)


def copy(src: Path, dest: Path, override=False):
    if src.is_file():
        copy_file(src, dest, override)
    elif src.is_dir():
        copy_directory(src, dest)
    else:
        raise cpError("Filetype not suported")


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cp",
        description="cp command implementation in Python"
    )
    parser.add_argument(
        "-o",
        "--override",
        action="store_true",
        help="Override destination files if they already exist"
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Source directory or file"
    )
    parser.add_argument(
        "destination",
        type=Path,
        help="Destination directory or file"
    )

    return parser.parse_args()


def main():
    args = cli()
    try:
        copy(args.source, args.destination, args.override)
    except cpError as e:
        print(e, file=stderr)
        exit(1)


if __name__ == "__main__":
    main()

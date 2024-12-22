import argparse
from .palette import Palette
from .generator import Generator
from .working_directory import WorkingDirectory
import os
from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="refind-palette",
        description="Tool for generating rEFInd color palette based on regular theme.",
        allow_abbrev=False,
    )

    parser.add_argument("-c", "--config", default="config.ini")
    parser.add_argument("-w", "--working-directory", default=os.getcwd())
    parser.add_argument("-V", "--version", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    palette = Palette(args.config)
    wd = WorkingDirectory(root=args.working_directory, palette_name=palette.name)
    generator = Generator(palette=palette, working_directory=wd)
    generator.build()

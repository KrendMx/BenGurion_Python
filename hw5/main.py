from cli import CommandLineInterface
from core import *

nature = Nature()


if __name__ == "__main__":
    cli = CommandLineInterface(nature)
    cli.start()
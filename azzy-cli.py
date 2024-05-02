#!/usr/bin/env python
import click
from commands import *
from commands import pwd
# Assuming the command group is defined in pwd.py

@click.group(help="Azzy's CLI tool")
def cli():
    print("Hello from azzy-cli.py")

    pass

cli.add_command(pwd.pwd)

if __name__ == "__main__":
    cli()

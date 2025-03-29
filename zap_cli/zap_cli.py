#!/usr/bin/env python3

# import libraries
import click
import sys
import os
from pathlib import Path


currentdir = Path(__file__).resolve().parent
parentdir = currentdir.parent
sys.path.insert(0, str(parentdir))

# import modules from commands.personal directory
from commands.personal import calculator
from commands.personal import note_app
from commands.personal import yt_dl
from commands.personal import gen_pass
from commands.personal import unit
from commands.personal import expense
from commands.personal import sysinfo
from commands.personal import cache
from commands.personal import image_processor

# import modules from devops
from commands.devops import *



# define main command group for the CLI Tool
@click.group(help="ZAP CLI tool:A command-line interface for various utilities.")
def cli():
    """Main entry point for ZAP CLI Tool."""
     # function doesn't do anything.
     # is REQUIRED for defining the command group
    pass


"""
Adds command groups to the `cli` group. 
Each command group is a separate subcommand namespace.
The first part is the module and the second part specifies the command to be added.
"""

# example
# adding the 'calculator' command group to the CLI
# `calculator.calculator` refers to the `calculator` module's `calculator` command group
cli.add_command(calculator.calculator)
cli.add_command(note_app.note_app)
cli.add_command(yt_dl.yt_dl)
cli.add_command(gen_pass.gen_pass)
cli.add_command(unit.unit)
cli.add_command(expense.expense)
cli.add_command(sysinfo.sysinfo)
cli.add_command(cache.cache)
cli.add_command(image_processor.image_processor)


# Entry point of the script.
# Calls the CLI tool if the script is executed.
if __name__ == "__main__":
    cli()


#!/usr/bin/env python3

# import click library
import click

# import modules from commands directory
from commands import calculator
from commands import note_app
from commands import yt_dl
from commands import gen_pass
from commands import unit
from commands import expense
from commands import sysinfo


# define main command group for the CLI Tool
@click.group(help="Azzy's CLI tool:A command-line interface for various utilities.")
def cli():
    """Main entry point for Azzy's CLI Tool."""
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


# Entry point of the script.
# Calls the CLI tool if the script is executed.
if __name__ == "__main__":
    cli()

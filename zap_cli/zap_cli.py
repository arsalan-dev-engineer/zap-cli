#!/usr/bin/env python3

# import libraries
import click
import sys
import os
from pathlib import Path

# Get current script directory
currentdir = Path(__file__).resolve().parent
# Get parent directory
parentdir = currentdir.parent
# Add parent directory to sys.path
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
from commands.devops import ec2_cleaner

# define main command group for the CLI Tool
@click.group(help="ZAP CLI tool:A command-line interface for various utilities.")
def cli():
    """Main entry point for ZAP CLI Tool."""
     # function doesn't do anything.
     # is REQUIRED for defining the command group
    pass


# add devops command group
@click.group(help="DevOps related commands.")
def devops():
    pass

# add personal command group
@click.group(help="Personal related commands.")
def personal():
    pass

# ========== ADD DEVOPS GROUP TO CLI
devops.add_command(ec2_cleaner.ec2_cleaner)

# ========== ADD PERSONAL GROUP TO CLI
personal.add_command(calculator.calculator)
personal.add_command(note_app.note_app)
personal.add_command(yt_dl.yt_dl)
personal.add_command(gen_pass.gen_pass)
personal.add_command(unit.unit)
personal.add_command(expense.expense)
personal.add_command(sysinfo.sysinfo)
personal.add_command(cache.cache)
personal.add_command(image_processor.image_processor)

# Add 'devops' and 'personal' as subcommands to the main 'cli' group
cli.add_command(devops)
cli.add_command(personal)

# Entry point of the script.
# Calls the CLI tool if the script is executed.
if __name__ == "__main__":
    cli()


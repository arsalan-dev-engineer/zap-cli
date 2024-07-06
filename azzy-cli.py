#!/usr/bin/env python3
import click
from commands import todo, greetings, joke, youtube, test, calculator

@click.group(help="Azzy's CLI tool:A command-line interface for various utilities.")
def cli():
    """Main entry point for Azzy's CLI Tool."""
    pass

# Adds command groups to the cli group
cli.add_command(todo.todo, name='todo')
cli.add_command(greetings.greetings)
cli.add_command(joke.joke, name='joke')
cli.add_command(youtube.youtube, name='youtube')
cli.add_command(test.test, name='test')
cli.add_command(calculator.calculator, name="calculator")

if __name__ == "__main__":
    cli()

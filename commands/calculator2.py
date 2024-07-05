import click

# Define the main click group
@click.group()
def cli():
    """A simple calculator."""
    pass

# Subcommand for addition
@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    """Add two numbers."""
    result = a + b
    click.echo(f"The result of {a} + {b} is {result}")

# Subcommand for subtraction
@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def subtract(a, b):
    """Subtract two numbers."""
    result = a - b
    click.echo(f"The result of {a} - {b} is {result}")

# Subcommand for multiplication
@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    click.echo(f"The result of {a} * {b} is {result}")

# Subcommand for division
@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        click.echo("Error: Division by zero is not allowed.")
    else:
        result = a / b
        click.echo(f"The result of {a} / {b} is {result}")

# This ensures the script runs only if it's executed directly
if __name__ == '__main__':
    cli()

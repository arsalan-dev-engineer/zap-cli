import click

@click.group(help="A group of greeting commands.")
def greetings():
    """A group of greeting commands."""
    pass

@greetings.command(help="Greet a person a specified number of times.")
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

# Ensure that the command group is properly registered
if __name__ == '__main__':
    greetings()

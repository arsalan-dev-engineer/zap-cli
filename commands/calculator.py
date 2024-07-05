import click

# define click command
@click.command()
@click.option("--first", prompt="First number", type=float, help="The first number.")
@click.option("--second", prompt="Second number", type=float, help="The second number.")
@click.option("--operation", prompt="add", type=click.Choice(["add", "subtract"], case_sensitive=False), help="The operation to perform (add or subtract).")
def calcualator(first, second, operation):
    if operation == "add":
        result = first + second
        click.echo(f"{first} + {second} = {result}")
    
    elif operation == "subtract":
        result = first - second
        click.echo(f"{first} - {second} = {result}")


if __name__ == "__main__":
    calcualator()
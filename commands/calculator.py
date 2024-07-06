import click

@click.command(help="A simple calculator.\n\n*Example:*\n`calculator --num1 10 --num2 5 --operation +`")
@click.option("--num1", prompt="Prompt first number", type=int, help="The first number.")
@click.option("--num2", prompt="Prompt second number", type=int, help="The second number.")
@click.option("--operation", prompt="Input operator", type=click.Choice(["+", "-", "*", "/"], case_sensitive=False), help="Promopt operation: + - * /")
def calculator(num1, num2, operation):
    """Perform a simple arithmetic operation."""
    if operation == "+":
        result = num1 + num2    
    elif operation == "-":
        result = num1 - num2    
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # check for vidion by zero
        if num2 == 0:
            click.echo("Error: division by zero is not allowed.")
            return
        result = num1 / num2

    click.echo(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
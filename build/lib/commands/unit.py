import click

# define a click command group called unit
@click.group(help="A group of commands for unit conversions.")
def unit():
    """
    A group of commands for unit conversions.
    This function serves as the entry point for the click group.
    """
    # function is a placeholder for the command group
    pass


# define click command for converting grams to kilograms
# name the command explicitly as "convert"
@click.command("convert")
@click.option("-a", "--amount", type=float, required=True, help="Amount to convert.")
@click.option("-f", "--from-unit", type=click.Choice(["grams", "kilograms", "ounces", "pounds"], case_sensitive=False), required=True, help="Unit to convert from.")
@click.option("-t", "--to-unit", type=click.Choice(["grams", "kilograms", "ounces", "pounds"], case_sensitive=False), required=True, help="Unit to convert to.")
def convert(amount, from_unit, to_unit):
    """
    this function performs the unit conversion based on the provided options.
    it converts the amount from one unit to another and prints the results.
    """
    # conversion from grams
    if from_unit == "grams":
        if to_unit == "kilograms":
            result = amount * 0.001
            click.echo(f"{amount} grams = {result:.4f} kilograms.")
        if to_unit == "ounces":
            result = amount * 0.03527396
            click.echo(f"{amount} grams = {result:.4f} ounces.")
        if to_unit == "pounds":
            result = amount * 0.00220462
            click.echo(f"{amount} grams = {result:.4f} pounds.")
    
    # conversion from kilograms
    elif from_unit == "kilograms":
        if to_unit == "grams":
            result = amount * 1000
            click.echo(f"{amount} kilograms = {result:.4f} grams.")
        if to_unit == "ounces":
            result = amount * 35.27396
            click.echo(f"{amount} kilograms = {result:.4f} ounces.")
        if to_unit == "pounds":
            result = amount * 2.20462262
            click.echo(f"{amount} kilograms = {result:.4f} pounds.")
    
    # conversion from ounces
    elif from_unit == "ounces":
        if to_unit == "kilograms":
            result = amount * 0.0283495
            click.echo(f"{amount} ounces = {result:.4f} kilograms.")
        if to_unit == "grams":
            result = amount * 28.3495231
            click.echo(f"{amount} ounces = {result:.4f} grams.")
        if to_unit == "pounds":
            result = amount * 0.0625
            click.echo(f"{amount} ounces = {result:.4f} pounds.")

    # conversion from pounds
    elif from_unit == "pounds":
        if to_unit == "kilograms":
            result = amount * 0.45359237
            click.echo(f"{amount} pounds = {result:.4f} kilograms.")
        if to_unit == "ounces":
            result = amount * 16
            click.echo(f"{amount} pounds = {result:.4f} ounces.")
        if to_unit == "grams":
            result = amount * 453.59237
            click.echo(f"{amount} pounds = {result:.4f} grams.")
    # handle unsupported unit types
    else:
        click.echo("Error: Unsupported unit type.")


# add the sub-commands to the unit group
unit.add_command(convert)

# if this script is run directly, invoke the "unit" group
if __name__ == "__main__":
    unit()

import click


"""
SCRIPT NOT YET COMPLETE
"""

@click.group(help="A group of commands for accessing and storing credentials in a cache.")
def cache():
    """"""
    pass


@click.command(name="view", help="view credential")
def view_credential():
    """"""
    click.echo("viewing credentials.")
    pass


@click.command(name="add", help="add credential")
def add_credential():
    """"""
    click.echo("adding credentials.")
    pass


@click.command(name="update", help="update credential")
def update_credential():
    """"""
    click.echo("updating credentials.")
    pass


@click.command(name="delete", help="delete credential")
def delete_credential():
    """"""
    click.echo("deleting credentials.")
    pass


cache.add_command(view_credential)
cache.add_command(add_credential)
cache.add_command(update_credential)
cache.add_command(delete_credential)

if __name__ == "__main__":
    cache()
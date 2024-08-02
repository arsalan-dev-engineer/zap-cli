import click
import keyring
import os
import json

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


def load_cache():
    pass


@click.command()
@click.option("--username", prompt="username", help="username for your account.")
@click.option("--password", prompt="password", confirmation_prompt=True, help="password for your account.")
def store_credential(username, password):
    """stores the provided username and password securely."""
    keyring.set_password("my_service", username, password)
    click.echo(f"Credentials for {username} has been stored securely.")
    pass


@click.command()
@click.option("--username", prompt="username", help="username for your account.")
def view_credential(username):
    """Retrieves the stored password for the given username."""
    password = keyring.get_password("my_service", username)
    if password:
        click.echo(f'The password for {username} is {password}')
    else:
        click.echo(f'No credentials found for {username}')



cache.add_command(store_credential)
cache.add_command(view_credential)


if __name__ == "__main__":
    cache()
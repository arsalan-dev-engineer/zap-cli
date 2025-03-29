import click
from commands import logger

@click.group(help="A group of commands for managing credentials and tokens.")
def cache():
    """
    A group of commands for managing credentials and tokens.
    """
    pass

@click.command(help="Add credentials to the cache.")
def add_credential():
    pass

@click.command(help="Update an existing credential.")
def reset_credential():
    pass

@click.command(help="Delete an existing credential.")
def delete_credential():
    pass

@click.command(help="Add a token.")
def add_token():
    pass

@click.command(help="Delete a token.")
def delete_token():
    pass

@click.command(help="View all existing credentials.")
def view_credentials():
    pass

@click.command(help="View all existing tokens.")
def view_tokens():
    pass

@click.command(help="Delete a specific credential.")
def clear_credentials():
    pass

@click.command(help="Delete a speficic token.")
def clear_tokens():
    pass

# ===== COMMANDS ===============

# Add commands to cache group
cache.add_command(add_credential)
cache.add_command(reset_credential)
cache.add_command(delete_credential)
cache.add_command(add_token)
cache.add_command(delete_token)
cache.add_command(view_credentials)
cache.add_command(view_tokens)
cache.add_command(clear_credentials)
cache.add_command(clear_tokens)

if __name__ == "__main__":
    cache()

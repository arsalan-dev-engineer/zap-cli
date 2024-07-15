import click

@click.group(help="A group of password generators")
def pass_gen():
    """A group of password generators"""
    pass

@click.command(name="p", help="generate password")
def password():
    pass


pass_gen.add_command(password)

if (__name__) == ("__main__"):
    pass_gen()
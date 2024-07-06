import click

@click.group()
def test():
    """Test command group"""
    pass

@test.command()
def hello():
    """Prints Hello World"""
    print("Hello World")


if __name__ == "__main__":
    test()

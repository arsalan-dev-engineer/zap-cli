import click

# Define the main click group
@click.group()
def cli():
    """A simple file management tool."""
    pass

# Command to read a file
@cli.command()
@click.argument('file_path', type=click.Path(exists=True, readable=True))
def read(file_path):
    """Read the contents of a file."""
    with open(file_path, 'r') as f:
        content = f.read()
    click.echo(content)

# Command to write to a file
@cli.command()
@click.argument('file_path', type=click.Path(writable=True))
@click.argument('content')
def write(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)
    click.echo(f"Content written to {file_path}")

# Command to append to a file
@cli.command()
@click.argument('file_path', type=click.Path(writable=True))
@click.argument('content')
def append(file_path, content):
    """Append content to a file."""
    with open(file_path, 'a') as f:
        f.write(content + '\n')
    click.echo(f"Content appended to {file_path}")

# Command to delete a file
@cli.command()
@click.argument('file_path', type=click.Path(exists=True, writable=True))
def delete(file_path):
    """Delete a file."""
    try:
        os.remove(file_path)
        click.echo(f"File {file_path} deleted.")
    except OSError as e:
        click.echo(f"Error: {e.strerror}")

# This ensures the script runs only if it's executed directly
if __name__ == '__main__':
    cli()

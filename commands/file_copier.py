import click

# Define a click command
@click.command()
# Define an option for the source file path
@click.option("--src", prompt="Source file", type=click.Path(exists=True, readable=True), help="Path to the source file.")
# Define an option for the destination file path
@click.option("--dst", prompt="Destination file", type=click.Path(writable=True), help="Path to the destination file.")
def copy_file(src, dst):
    """
    Copies the contents of one file to another.
    
    Args:
        src (str): Path to the source file.
        dst (str): Path to the destination file.
    """
    # Open the source file for reading
    with open(src, 'r') as f_src:
        # Read the content of the source file
        content = f_src.read()
    
    # Open the destination file for writing
    with open(dst, 'w') as f_dst:
        # Write the content to the destination file
        f_dst.write(content)
    
    click.echo(f"Contents copied from {src} to {dst}.")

# This ensures the script runs only if it's executed directly
if __name__ == '__main__':
    copy_file()

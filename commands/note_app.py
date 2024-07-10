import os
import sys
import inspect
import click


# system path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# --------------------

# define the main command group for note taking application
@click.group(help="A group of commands for a note-taking application")
def note_app():
    """A group of commands for note-taking application"""
    pass

# --------------------

# Define the 'add' command to add a note
@click.command(name="add", help="add a note")
def add_note():
    # notes path
    file_path = os.path.join(parentdir, "misc/notes/")

    # select an editor
    note_content = click.edit()
    
    # condition for, if no notes prompted
    if not note_content:
        click.echo("No content added.\nNote not saved")
        return
    
    # prompt for the filename after the note content is written
    note_name = click.prompt("Enter note name: ", type=str)
    note_path = os.path.join(file_path, f"{note_name}.txt")

    # check if the note already exists
    if os.path.exists(note_path):
        if not click.confirm("note with this name already exists.\nDo you want to overwrite it?"):
            click.echo("Note not saved.")
            return
    
    # save the content to the specified file
    with open(note_path, "w") as f:
        f.write(note_content)
    click.echo("Note saved successfully.")

# --------------------

# Define the 'list' command to list all notes
@click.command(name="list", help="list all notes")
def list_notes():
    # notes path
    file_path = os.path.join(parentdir, "misc/notes/")
    notes = os.listdir(file_path)
    click.echo("\nListing all notes:")

    # check if notes exist
    if not notes:
        click.echo("No notes found.")
        return
    
    # display all notes
    for n in notes:
        click.echo(n)

# --------------------

# Define the 'search' command to search notes by a keyword
@click.command(name="search", help="search notes")
@click.argument("search")
def search_notes(search):
    # notes path
    file_path = os.path.join(parentdir, "misc/notes/")
    
    try:
        # list all files in the notes directory
        notes = os.listdir(file_path)
    except:
        # return echo message if file directory does not exist
        click.echo(f"Directory '{file_path}' does not exist.")


    # filter files that contain the search keyword in their names
    matching_notes = [note for note in notes if search in note]
    
    # if no matching files found, return echo message
    if not matching_notes:
        click.echo("File does not exist.")
        return
    
    # if matching files found, return file names
    if matching_notes:
        click.echo(f"\nNotes matching '{search}':\n" + "-" * 30)
    for note in matching_notes:
        click.echo(f"- {note}")
    click.echo("-" * 30)

# --------------------

# Define the 'delete' command to delete a note
@click.command(name="del", help="delete a note")
@click.argument("delete")
def delete_note(delete):
    file_path = os.path.join(parentdir, "misc/notes/")
    try:
        # list all files in the notes directory
        notes = os.listdir(file_path)
    except:
        # return echo message if file directory does not exist
        click.echo(f"Directory '{file_path}' does not exist.")

    matching_notes = [note for note in notes if delete in note]
    if not matching_notes:
        click.echo("File does not exist.")
        return

    click.echo(f"Deleting notes matching '{delete}':")
    click.echo("-" * 30)

    # if matching files found, delete notes and notify user
    for note in matching_notes:
        # construct full path for each note
        note_path = os.path.join(file_path, note)
        # delete note
        os.remove(note_path)
        click.echo(f"Deleted: {note}")
    click.echo("-" * 30)

# --------------------

# Register the subcommands with the main command group
note_app.add_command(add_note)
note_app.add_command(list_notes)
note_app.add_command(search_notes)
note_app.add_command(delete_note)

# --------------------

# Entry point for the CLI application
if __name__ == "__main__":
    note_app()
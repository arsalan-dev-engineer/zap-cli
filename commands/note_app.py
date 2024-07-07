import click

# define the main command group for note taking application
@click.group(help="A group of commands for a note-taking application")
def note_app():
    """A group of commands for note-taking application"""
    pass


# Define the 'add' command to add a note
@click.command(name="add", help="add a note")
@click.argument("note")
def add_note(note):
    click.echo(f"adding note: {note}")
    pass


# Define the 'list' command to list all notes
@click.command(name="list", help="list all notes")
def list_notes():
    click.echo(f"All notes: ")
    pass


# Define the 'search' command to search notes by a keyword
@click.command(name="search", help="search notes")
@click.argument("query")
def search_notes(query):
    click.echo(f"searching for note: {query}")
    pass


# Define the 'delete' command to delete a note
@click.command(name="del", help="delete a note")
@click.argument("note")
def delete_note(note):
    click.echo(f"deleting note: {note}")
    pass



# Register the subcommands with the main command group
note_app.add_command(add_note)
note_app.add_command(list_notes)
note_app.add_command(search_notes)
note_app.add_command(delete_note)


# Entry point for the CLI application
if __name__ == "__main__":
    note_app()



"""
3. Note-Taking Application
	• Features:
		○ Add notes
		○ List notes
		○ Search notes
		○ Delete notes
	• Commands:
		○ add: Create a new note
		○ list: Show all notes
		○ search: Find notes by keyword
delete: Remove a note
"""
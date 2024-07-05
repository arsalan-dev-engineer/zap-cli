import click  # Import the Click library to help with creating command-line interfaces.

# Define a group of commands related to to-do list management.
# Think of this as the main menu for the to-do list commands.
@click.group()
def todo():
    """
    A simple to-do list manager.
    
    This is the main command group for managing your to-do list.
    You can use this group to add, list, remove, and clear tasks from your to-do list.
    """
    pass  # This function doesn’t do anything by itself but groups the commands together.

# Define the command to add a new task to the to-do list.
# You will use this command to create new tasks.
@todo.command()
@click.argument('task')  # Get the task description from the command line.
def add(task):
    """
    Add a new task to the to-do list.

    Args:
        task (str): The description of the task you want to add.
    
    How to use:
        $ python azzy-cli.py todo add "Buy groceries"
        This will add "Buy groceries" to the to-do list.
    """
    # Open the `todo.txt` file in append mode.
    # If the file doesn't exist, it will be created.
    with open('todo.txt', 'a') as f:
        # Write the new task to the file with a newline.
        f.write(f"{task}\n")
    # Print a message to confirm that the task was added.
    click.echo(f"Task '{task}' added to the to-do list.")

# Define the command to list all tasks currently in the to-do list.
# You will use this command to see what tasks are in your list.
@todo.command(name='list')
def list_tasks():
    """
    List all tasks in the to-do list.
    
    How to use:
        $ python azzy-cli.py todo list
        This will display all tasks in the to-do list.
    """
    try:
        # Open the `todo.txt` file in read mode.
        # If the file doesn't exist, it will raise a FileNotFoundError.
        with open('todo.txt', 'r') as f:
            # Read all lines from the file.
            tasks = f.readlines()
        # Check if there are any tasks.
        if tasks:
            # Print a header for the to-do list.
            click.echo("To-Do List:")
            # Loop through each task and display it with a number.
            for i, task in enumerate(tasks, 1):
                click.echo(f"{i}. {task.strip()}")  # Remove any extra spaces and print the task.
        else:
            # If there are no tasks, print this message.
            click.echo("The to-do list is empty.")
    except FileNotFoundError:
        # If the file does not exist, print this message.
        click.echo("The to-do list is empty.")

# Define the command to remove a specific task from the to-do list.
# You will use this command to delete a task based on its number.
@todo.command()
@click.argument('task_number', type=int)  # Get the task number from the command line.
def remove(task_number):
    """
    Remove a task from the to-do list by its number.

    Args:
        task_number (int): The number of the task you want to remove.
    
    How to use:
        $ python azzy-cli.py todo remove 1
        This will remove the task numbered 1 from the to-do list.
    """
    try:
        # Open the `todo.txt` file in read mode.
        with open('todo.txt', 'r') as f:
            # Read all lines from the file.
            tasks = f.readlines()
        # Check if the task number is valid.
        if 0 < task_number <= len(tasks):
            # Remove the specified task from the list.
            removed_task = tasks.pop(task_number - 1).strip()
            # Open the `todo.txt` file in write mode.
            with open('todo.txt', 'w') as f:
                # Write the remaining tasks back to the file.
                f.writelines(tasks)
            # Print a message to confirm that the task was removed.
            click.echo(f"Task '{removed_task}' removed from the to-do list.")
        else:
            # If the task number is not valid, print this message.
            click.echo(f"Invalid task number: {task_number}.")
    except FileNotFoundError:
        # If the file does not exist, print this message.
        click.echo("The to-do list is empty.")

# Define the command to clear all tasks from the to-do list.
# You will use this command to delete everything in your to-do list.
@todo.command()
def clear():
    """
    Clear all tasks from the to-do list.
    
    How to use:
        $ python azzy-cli.py todo clear
        This will remove all tasks from the to-do list.
    """
    # Open the `todo.txt` file in write mode.
    # This will clear the file's contents.
    with open('todo.txt', 'w'):
        pass
    # Print a message to confirm that all tasks were removed.
    click.echo("All tasks have been cleared from the to-do list.")

# This part ensures the `todo.py` file runs correctly if it is executed directly.
# It allows you to use `python commands/todo.py` to run the `todo` command group.
if __name__ == '__main__':
    todo()

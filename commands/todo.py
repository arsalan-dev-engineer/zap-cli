import click

# Define the main click group, which serves as the entry point for the CLI application.
@click.group()
def cli():
    """A simple to-do list manager."""
    pass

# Define a command to add a task to the to-do list.
@cli.command()
@click.argument('task')
def add(task):
    """
    Add a new task to the to-do list.

    Args:
        task (str): The task to be added.
    """
    with open('todo.txt', 'a') as f:
        f.write(f"{task}\n")
    click.echo(f"Task '{task}' added to the to-do list.")

# Define a command to list all tasks in the to-do list.
@cli.command(name='list')
def list_tasks():
    """
    List all tasks in the to-do list.
    """
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
        if tasks:
            click.echo("To-Do List:")
            for i, task in enumerate(tasks, 1):
                click.echo(f"{i}. {task.strip()}")
        else:
            click.echo("The to-do list is empty.")
    except FileNotFoundError:
        click.echo("The to-do list is empty.")

# Define a command to remove a task from the to-do list by its number.
@cli.command()
@click.argument('task_number', type=int)
def remove(task_number):
    """
    Remove a task from the to-do list by its number.

    Args:
        task_number (int): The number of the task to be removed.
    """
    try:
        with open('todo.txt', 'r') as f:
            tasks = f.readlines()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1).strip()
            with open('todo.txt', 'w') as f:
                f.writelines(tasks)
            click.echo(f"Task '{removed_task}' removed from the to-do list.")
        else:
            click.echo(f"Invalid task number: {task_number}.")
    except FileNotFoundError:
        click.echo("The to-do list is empty.")

# Define a command to clear all tasks from the to-do list.
@cli.command()
def clear():
    """
    Clear all tasks from the to-do list.
    """
    with open('todo.txt', 'w'):
        pass
    click.echo("All tasks have been cleared from the to-do list.")

# This ensures the script runs only if it's executed directly, not when imported as a module.
if __name__ == '__main__':
    cli()

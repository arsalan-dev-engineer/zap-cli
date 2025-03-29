import time
from rich.console import Console
from rich.progress import Progress

"""
This module provides a set of utility functions for logging messages to 
the console using the Rich library for enhanced formatting.
This module also includes functions for showing progress during long-running operations.
Purpose of this script is to improve user experience and provide clear feedback 
during script executiions.
"""

console = Console()

def error(message: str):
    """Display critical errors that need immediate attention."""
    console.print(message, style="bold red")


def success(message: str):
    """Indicate successful operations or completed tasks."""
    console.print(message, style="bold green")


def warning(message: str):
    """Notify users of potential issues or cautions."""
    console.print(message, style="bold yellow")


def info(message: str):
    """Provide general information or updates about processes."""
    console.print(message, style="bold blue")


def debug(message: str):
    """Log debug information for troubleshooting purposes."""
    console.print(message, style="bold white")


def prompt_user(prompt_message: str) -> str:
    """Ask for user input or confirmations."""
    return console.input(prompt_message)


def show_progress(total: int):
    """Show the status of long-running operations."""
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...", total=total)
        while not progress.finished:
            time.sleep(0.1)  # Simulate work being done
            progress.update(task, advance=1)


def completion(message: str):
    """Indicate the end of a process with a summary of results."""
    console.print(message, style="bold green")


def critical_alert(message: str):
    """Highlight urgent alerts or critical issues requiring immediate action."""
    console.print(message, style="bold magenta")


def network_status(message: str):
    """Indicate the status of network connections or related operations."""
    console.print(message, style="bold bright_blue")


def config_loaded(message: str):
    """Confirm that a configuration file has been successfully loaded."""
    console.print(message, style="bold blue")


def resource_status(message: str):
    """Report on the status of system resources (e.g., CPU, memory)."""
    console.print(message, style="bold yellow")


def execution_time(duration: float):
    """Display the time taken to complete a task."""
    console.print(f"Execution time: {duration:.2f} seconds", style="bold white")

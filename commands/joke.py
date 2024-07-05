# commands/joke.py
import click  # Import the Click library for creating command-line interfaces
import requests  # Import the requests library for making HTTP requests

# Define a command group named 'joke'
# This serves as the entry point for the 'joke' commands
@click.group()
def joke():
    """Get a random joke."""
    pass  # The 'joke' command group does not perform any actions by itself

# Define a command named 'random' under the 'joke' command group
# This command fetches a random joke from an API
@joke.command(name="random")
def random():
    """\tFetch a random joke."""
    # Send a GET request to the Official Joke API to fetch a random joke
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    
    # Convert the JSON response into a Python dictionary
    data = response.json()
    
    # Check if the HTTP request was successful (status code 200)
    if response.status_code == 200:
        # Extract the setup and punchline from the response data
        setup = data['setup']
        punchline = data['punchline']
        # Print the joke in the format "Setup - Punchline"
        click.echo(f'Joke: {setup} - {punchline}')
    else:
        # If the request was not successful, print an error message
        click.echo('Failed to fetch a joke. Please try again later.')

# This section ensures that the script runs only if it is executed directly
# and not if it is imported as a module in another script
if __name__ == '__main__':
    joke()

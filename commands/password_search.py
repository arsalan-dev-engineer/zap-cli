import json
from rich.console import Console
from rich.table import Table

# create an object called console from Console class
console = Console()

# create an object called table from Table class
table = Table(title="Password Info Database")

# ------------------------------

def load_json_files(url):
    try:
        # Load address mapping from JSON file
        with open("commands/JSON/address_mapping.json") as file1:
            address_mapping = json.load(file1)

        # Load password mapping from JSON file
        with open("commands/JSON/password_mapping.json") as file2:
            password_mapping = json.load(file2)

        print("Files loaded successfully.")
        # Call the function to check address mapping
        check_address_mapping(address_mapping, password_mapping, url)
    except ValueError:
        print("File could not be loaded.")

# ------------------------------

def check_address_mapping(address_mapping, password_mapping, url):
    # Create and return results in table format
    table.add_column("Title", style="cyan", justify="center", no_wrap=False, width=30)
    # width will change width of table column
    table.add_column("Description", style="magenta", justify="center", no_wrap=False, width=30)
    # no_wrap = False will allow table to display multi lines of text
    table.add_column("Guide", style="yellow", justify="center", no_wrap=False, width=50)

    website_link = url.lower()

    # Iterate over each link in the address mapping
    for link in address_mapping.values():
        # Check if the website link is present in the given link (case insensitive)
        if link.lower() in website_link:
            print("Address:", link)
            # Check if the link exists in the password mapping
            if link in password_mapping:
                password_info = password_mapping[link]
                # Print password information
                print("Password Info:")
                # Convert title to lowercase
                table.add_row(password_info["title"].lower(),
                              # Convert description to lowercase
                              password_info["description"].lower(),  
                              # Convert guide to lowercase
                              password_info["guide"].lower())

    # If the link doesn't exist in the address mapping
    if len(table.rows) == 0:
        print("Link does not exist.")
        return
    else:
        # Print the table
        console.print("\n", table, "\n")

# ------------------------------

if __name__ == "__main__":
    load_json_files(input("Enter url: "))

import click
import requests

"""
SCRIPT REQUIRES expense_api.py to run with univorn.
"""

# base url for your fastapi server
BASE_URL = "http://127.0.0.1:8000"

@click.group(help="A group of commands for the expense tracker app.")
def expense():
    """
    command group for managing expenses.
    """
    pass

# ==========

@click.command()
@click.option("-a", "--amount", type=float, required=True, help="Amount of the expense.")
@click.option("-c", "--category", type=str, required=True, help="Category of the expense.")
@click.option("-d", "--date", type=click.DateTime(formats=["%d-%m-%y"]), required=True, help="Date of the expense (format: DD-MM-YY).")
@click.option("-n", "--note", type=str, help="Optional notes for the expense.")
def add_expense(amount, category, date, note):
    """
    add a new expense.
    """
    # send a POST request to the server to add a new expense
    response = requests.post(f"{BASE_URL}/expenses/", json={
        "amount": amount,
        "category": category,
        "date": date.date().isoformat(),
        "note": note or ""
    })

    # check if the response status code indicates success (201 Created)
    if response.status_code == 201:
        result = response.json()
        # output the added expense details in a formatted manner
        click.echo("\nExpense Added Successfully:")
        click.echo("=" * 30)
        click.echo(f"ID      : {result['id']}")
        click.echo(f"Amount  : ${amount:.2f}")
        click.echo(f"Category: {category}")
        click.echo(f"Date    : {date.date()}")
        click.echo(f"Note    : {note or 'No notes provided'}")
        click.echo("=" * 30)
    # handle bad request errors (400 Bad Request)
    elif response.status_code == 400:
        click.echo(f"Bad request: {response.json().get('detail', 'Invalid data provided')}")
    else:
        # handle other errors
        click.echo(f"Error adding expense: {response.status_code} - {response.text}")

# ==========

@click.command()
@click.option("-s", "--start-date", type=click.DateTime(formats=["%d-%m-%y"]), help="Start date for viewing expenses (format: DD-MM-YY).")
@click.option("-e", "--end-date", type=click.DateTime(formats=["%d-%m-%y"]), help="End date for viewing expenses (format: DD-MM-YY).")
def view_expenses(start_date, end_date):
    """
    view expenses within a date range.
    """
    # prepare query parameters for the GET request
    params = {
        "start_date": start_date.date().isoformat() if start_date else None,
        "end_date": end_date.date().isoformat() if end_date else None
    }

    # remove any parameters that are None to avoid sending unnecessary parameters
    params = {k: v for k, v in params.items() if v is not None}

    # send a GET request to the server to retrieve expenses
    response = requests.get(f"{BASE_URL}/expenses/", params=params)

    # check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        expenses = response.json()
        if not expenses:
            click.echo("No expenses found for the given dates.")
        else:
            # output the retrieved expenses in a formatted manner
            click.echo("\nExpenses Found:")
            click.echo("=" * 30)
            for exp in expenses:
                click.echo(f"ID      : {exp['id']}")
                click.echo(f"Amount  : ${exp['amount']:.2f}")
                click.echo(f"Category: {exp['category']}")
                click.echo(f"Date    : {exp['date']}")
                click.echo(f"Note    : {exp['note'] or 'No notes provided'}")
                click.echo("-" * 30)
    
    # handle bad request errors (400 Bad Request)
    elif response.status_code == 400:
        click.echo(f"Bad request: {response.json().get('detail', 'Invalid date format')}")
    else:
        # handle other errors
        click.echo(f"Error retrieving expenses: {response.status_code} - {response.text}")

# ==========

@click.command()
@click.option("--id", type=int, required=True, help="ID of the expense to delete.")
def delete_expense(id):
    """
    delete an expense by its id.
    """
    # send a DELETE request to the server to remove the expense with the given ID
    response = requests.delete(f"{BASE_URL}/expenses/{id}")

    # check if the response status code indicates success (204 No Content)
    if response.status_code == 204:
        click.echo(f"Deleted expense with ID: {id}")
    
    # handle not found errors (404 Not Found)
    elif response.status_code == 404:
        click.echo(f"Expense with ID {id} not found.")
    else:
        # handle other errors
        click.echo(f"Error deleting expense: {response.status_code} - {response.text}")

# ==========

@click.command()
@click.option("-s", "--start-date", type=click.DateTime(formats=["%d-%m-%y"]), help="Start date for the expense report (format: DD-MM-YY).")
@click.option("-e", "--end-date", type=click.DateTime(formats=["%d-%m-%y"]), help="End date for the expense report (format: DD-MM-YY).")
def generate_report(start_date, end_date):
    """
    generate an expense report within a date range.
    """
    # prepare query parameters for the GET request
    params = {
        "start_date": start_date.date().isoformat() if start_date else None,
        "end_date": end_date.date().isoformat() if end_date else None
    }

    # remove any parameters that are None to avoid sending unnecessary parameters
    params = {k: v for k, v in params.items() if v is not None}

    # send a GET request to the server to generate the expense report
    response = requests.get(f"{BASE_URL}/report/", params=params)

    # check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        report = response.json()
        total_amount = report.get("total_amount", 0)
        click.echo(f"Total expenses from {start_date.date() if start_date else 'start'} to {end_date.date() if end_date else 'end'}: ${total_amount:.2f}")
    
    # handle bad request errors (400 Bad Request)
    elif response.status_code == 400:
        click.echo(f"Bad request: {response.json().get('detail', 'Invalid date format')}")
    else:
        # handle other errors
        click.echo(f"Error generating report: {response.status_code} - {response.text}")

# ==========

# add the sub-commands to the "expense" group
expense.add_command(add_expense)
expense.add_command(view_expenses)
expense.add_command(delete_expense)
expense.add_command(generate_report)

# if this script runs directly, invoke the "expense" group
if __name__ == "__main__":
    expense()

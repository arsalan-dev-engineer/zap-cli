from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# create an instance of the FastAPI class
app = FastAPI()

# in-memory storage for expenses
# key: expense ID, value: expense details
expenses = {}
# a counter to generate unique IDs for new expenses
expense_id_counter = 1

# ==========

class Expense(BaseModel):
    amount: float
    category: str
    date: date
    note: Optional[str] = None

# ==========

@app.post("/expenses/", response_model=dict)
def create_expense(expense: Expense):
    """
    create a new expense and return its id.
    """
    global expense_id_counter
    # use the current counter value as the new expense ID
    expense_id = expense_id_counter
    # store the expense using the ID as the key
    expenses[expense_id] = expense.dict()
    # increment the counter for the next expense
    expense_id_counter += 1
    # return the ID and details of the newly created expense
    return {"id": expense_id, "expense": expenses[expense_id]}

# ==========

@app.get("/expenses/", response_model=List[dict])
def get_expenses(start_date: Optional[date] = None, end_date: Optional[date] = None):
    """
    retrieve all expenses within a date range.
    """
    # filter expenses based on the provided date range
    filtered_expenses = [
        {"id": eid, **exp} for eid, exp in expenses.items()
        if (start_date is None or exp["date"] >= start_date) and
           (end_date is None or exp["date"] <= end_date)
    ]
    # return the filtered list of expenses
    return filtered_expenses

# ==========

@app.get("/expenses/{expense_id}", response_model=dict)
def get_expense(expense_id: int):
    """
    retrieve an expense by its id.
    """
    if expense_id in expenses:
        # return the expense details if the ID exists
        return {"id": expense_id, **expenses[expense_id]}
    else:
        # raise a 404 error if the expense ID is not found
        raise HTTPException(status_code=404, detail="Expense not found")

# ==========

@app.delete("/expenses/{expense_id}", response_model=dict)
def delete_expense(expense_id: int):
    """
    delete an expense by its id.
    """
    if expense_id in expenses:
        # remove the expense from storage and return its details
        deleted_expense = expenses.pop(expense_id)
        return {"id": expense_id, "deleted_expense": deleted_expense}
    else:
        # raise a 404 error if the expense ID is not found
        raise HTTPException(status_code=404, detail="Expense not found")

# ==========

@app.get("/report/", response_model=dict)
def generate_report(start_date: Optional[date] = None, end_date: Optional[date] = None):
    """
    generate an expense report within a date range.
    """
    # filter expenses based on the provided date range
    filtered_expenses = [
        exp for exp in expenses.values()
        if (start_date is None or exp["date"] >= start_date) and
           (end_date is None or exp["date"] <= end_date)
    ]
    # calculate the total amount of the filtered expenses
    total_amount = sum(exp["amount"] for exp in filtered_expenses)
    # return the total amount and the list of filtered expenses
    return {
        "total_amount": total_amount,
        "expenses": filtered_expenses
    }

# ==========

# run the FastAPI application with Uvicorn when this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

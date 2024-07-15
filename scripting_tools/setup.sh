#!/bin/bash

# This script sets up a Python virtual environment for the project
# It creates the virtual environment, activates it, and installs the required packages from requirements.txt

# Stop the script if any command fails
set -e

# Define the virtual environment directory
VENV_DIR="../venv"

# Define the path to the `requirements.txt` file
REQUIREMENTS_FILE="../requirements.txt"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating it at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"  # Adjust this path to where the venv is located

# Upgrade `pip` to the latest version
pip install --upgrade pip

# Check if the `requirements.txt` file exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing packages from $REQUIREMENTS_FILE"
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "$REQUIREMENTS_FILE file not found!"
    exit 1
fi

# Notify the user that the setup process is complete
echo "Setup complete."

#!/bin/bash

# Exit on any error
set -e

# Define the project directory
PROJECT_DIR="$(pwd)"

# 1. Check if Python and venv are installed
echo "Checking Python and venv installation..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python 3."
    exit 1
fi

if ! command -v python3 -m venv &> /dev/null
then
    echo "venv module is not available. Installing..."
    python3 -m pip install --user virtualenv
fi

# 2. Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Install the packages from requirements.txt or setup.py
echo "Installing dependencies..."
if [[ -f "$PROJECT_DIR/requirements.txt" ]]; then
    pip install -r "$PROJECT_DIR/requirements.txt"
else
    echo "requirements.txt not found. Installing from setup.py..."
    pip install .
fi

# 5. Install zap-cli globally (editable mode)
echo "Installing zap-cli globally in editable mode..."
pip install -e .

# 6. Check if the installation was successful by running zap-cli
echo "Checking zap-cli installation..."
zap-cli --version

# 7. Deactivate the virtual environment
deactivate

echo "Setup complete! You can now use zap-cli globally."

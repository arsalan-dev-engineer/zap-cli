#!/bin/bash

# ------------------------------------------------------------------------
# This is the setup.sh script for the zap-cli project.
# It is used to set up the environment and install dependencies for the zap-cli
# command-line tool. The script performs the following tasks:
# - Checks if Python 3 and the venv module are installed.
# - Creates a virtual environment (venv) to isolate the project's dependencies.
# - Installs all required dependencies from requirements.txt or setup.py.
# - Installs the zap-cli package globally in editable mode.
# - Ensures that the zap-cli tool is available for use in any directory.
# ------------------------------------------------------------------------

# Exit the script if any command fails
set -e

# Get the current project directory
PROJECT_DIR="$(pwd)"

# 1. Check if Python and venv are installed
echo "Checking for Python and venv..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python 3."
    exit 1
fi

if ! command -v python3 -m venv &> /dev/null
then
    echo "venv module is not available. Installing virtualenv..."
    python3 -m pip install --user virtualenv
fi

# 2. Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# 3. Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# 4. Install dependencies from requirements.txt (or setup.py if no requirements.txt)
echo "Installing dependencies..."
if [[ -f "$PROJECT_DIR/requirements.txt" ]]; then
    # If requirements.txt exists, install the packages
    pip install -r "$PROJECT_DIR/requirements.txt"
else
    # If no requirements.txt, install from setup.py
    echo "No requirements.txt found, installing from setup.py..."
    pip install .
fi

# 5. Install the zap-cli package globally in editable mode
echo "Installing zap-cli globally in editable mode..."
pip install -e .

# 6. Deactivate the virtual environment after setup is complete
echo "Deactivating the virtual environment..."
deactivate

# Final message
echo "Setup complete! You can now use zap-cli globally."

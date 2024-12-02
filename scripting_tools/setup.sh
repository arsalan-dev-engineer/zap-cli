#!/bin/bash

# Enhanced Python virtual environment setup script
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Define the virtual environment directory and requirements file path
VENV_DIR="../venv"
REQUIREMENTS_FILE="../requirements.txt"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python3 is not installed. Please install Python3 and try again.${NC}"
    exit 1
fi

# Check if the python3-venv package is installed, and install it if missing
if ! python3 -m venv --help &> /dev/null; then
    echo -e "${RED}Error: python3-venv is not installed.${NC}"
    echo -e "${YELLOW}Installing python3-venv...${NC}"
    sudo apt update
    sudo apt install -y python3.10-venv  # Adjust version if necessary
fi

# Create or recreate the virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating it at $VENV_DIR...${NC}"
    python3 -m venv "$VENV_DIR"
else
    if [ ! -f "$VENV_DIR/bin/activate" ]; then
        echo -e "${RED}Error: Virtual environment exists but is corrupted. Recreating it...${NC}"
        rm -rf "$VENV_DIR"
        python3 -m venv "$VENV_DIR"
    else
        echo -e "${GREEN}Virtual environment already exists at $VENV_DIR.${NC}"
    fi
fi

# Activate the virtual environment
if [ -f "$VENV_DIR/bin/activate" ]; then
    echo -e "${YELLOW}Activating the virtual environment...${NC}"
    source "$VENV_DIR/bin/activate"
else
    echo -e "${RED}Error: Failed to activate virtual environment. Check the directory structure.${NC}"
    exit 1
fi

# Upgrade pip to the latest version
echo -e "${YELLOW}Upgrading pip to the latest version...${NC}"
pip install --upgrade pip

# Check if the requirements.txt file exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo -e "${YELLOW}Installing packages from $REQUIREMENTS_FILE...${NC}"
    pip install -r "$REQUIREMENTS_FILE"
else
    echo -e "${RED}Error: $REQUIREMENTS_FILE file not found! Please make sure it exists.${NC}"
    deactivate
    exit 1
fi

# Notify the user that the setup process is complete
echo -e "${GREEN}Setup complete. Virtual environment is ready to use.${NC}"
echo -e "${GREEN}To activate the virtual environment manually, run:${NC}"
echo -e "${GREEN}source $VENV_DIR/bin/activate${NC}"

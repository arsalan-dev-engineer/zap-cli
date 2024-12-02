#!/bin/bash

# Enhanced Python virtual environment setup script
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Automatically detect the script's root directory dynamically
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
ROOT_DIR="$(realpath "$SCRIPT_DIR/..")"  # Parent directory of the script

# Define the virtual environment directory and requirements file path, based on the current directory
VENV_DIR="${ROOT_DIR}/venv"
REQUIREMENTS_FILE="${ROOT_DIR}/requirements.txt"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python3 is not installed. Please install Python3 and try again.${NC}"
    exit 1
fi

# Check if the python3-venv package is installed, and install it if missing
if ! dpkg -s python3-venv &> /dev/null; then
    echo -e "${YELLOW}Installing python3-venv...${NC}"
    sudo apt update
    sudo apt install -y python3-venv
fi

# Function to find the requirements file dynamically if it's not in the root folder
find_requirements_file() {
    if [ -f "$1/requirements.txt" ]; then
        echo "$1/requirements.txt"
    elif [ -d "$1" ]; then
        for dir in "$1"/*; do
            if [ -d "$dir" ]; then
                find_requirements_file "$dir" # Recurse into subdirectories
            fi
        done
    fi
}

# If the requirements file is not found in the current directory, try searching for it in the parent directory
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo -e "${YELLOW}Requirements file not found in $ROOT_DIR. Searching in subdirectories...${NC}"
    REQUIREMENTS_FILE=$(find_requirements_file "$ROOT_DIR")
    
    if [ -z "$REQUIREMENTS_FILE" ]; then
        echo -e "${RED}Error: requirements.txt not found in the directory structure.${NC}"
        exit 1
    else
        echo -e "${YELLOW}Found requirements.txt at $REQUIREMENTS_FILE.${NC}"
    fi
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

# Check if Python executable exists in the virtual environment
if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo -e "${RED}Error: Python executable missing in the virtual environment. Exiting...${NC}"
    exit 1
fi

# Activate the virtual environment
echo -e "${YELLOW}Activating the virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

# Upgrade pip to the latest version
echo -e "${YELLOW}Upgrading pip to the latest version...${NC}"
pip install --upgrade pip

# Install the packages from requirements.txt if it exists
echo -e "${YELLOW}Installing packages from $REQUIREMENTS_FILE...${NC}"
pip install -r "$REQUIREMENTS_FILE"

# Create a symlink for the zap-cli command globally
ZAP_CLI_PATH="${ROOT_DIR}/zap_cli.py"

# Check if zap-cli.py exists before creating the symlink
if [ -f "$ZAP_CLI_PATH" ]; then
    echo -e "${YELLOW}Creating global symlink for zap-cli...${NC}"
    sudo ln -sf "$ZAP_CLI_PATH" /usr/local/bin/zap-cli
else
    echo -e "${RED}Error: zap-cli.py not found in $ROOT_DIR/${NC}"
    deactivate
    exit 1
fi

# Notify the user that the setup process is complete
echo -e "${GREEN}Setup complete. Virtual environment is ready to use.${NC}"
echo -e "${GREEN}To activate the virtual environment manually, run:${NC}"
echo -e "${GREEN}source $VENV_DIR/bin/activate${NC}"

# Instruction to run the main zap-cli.py script
echo -e "${GREEN}You can now run the CLI with:${NC}"
echo -e "${GREEN}zap-cli --help${NC}"

# Deactivate the virtual environment
deactivate

#!/bin/bash

# Enhanced Python virtual environment setup script without Zsh installation and setup
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Automatically detect the script's root directory dynamically
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
ROOT_DIR="$HOME"  # Set root directory to user's home directory

# Define the virtual environment directory and requirements file path
VENV_DIR="${ROOT_DIR}/venv"
REQUIREMENTS_FILE="${ROOT_DIR}/requirements.txt"
ZAP_CLI_PATH="${ROOT_DIR}/zap_cli.py"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python3 is not installed. Please install Python3 and try again.${NC}"
    exit 1
fi

# Check if the python3-venv package is installed, and install it if missing
if ! dpkg -s python3-venv &> /dev/null; then
    echo -e "${YELLOW}Installing python3-venv...${NC}"
    sudo apt update && sudo apt install -y python3-venv
fi

# If the requirements file is not found, search for it in the parent directory
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo -e "${YELLOW}Requirements file not found in $ROOT_DIR. Searching in subdirectories...${NC}"
    REQUIREMENTS_FILE=$(find "$ROOT_DIR" -name "requirements.txt" -print -quit)

    if [ -z "$REQUIREMENTS_FILE" ]; then
        echo -e "${RED}Error: requirements.txt not found.${NC}"
        exit 1
    else
        echo -e "${YELLOW}Found requirements.txt at $REQUIREMENTS_FILE.${NC}"
    fi
fi

# Create or recreate the virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Creating virtual environment at $VENV_DIR...${NC}"
    python3 -m venv "$VENV_DIR"
else
    echo -e "${GREEN}Virtual environment already exists at $VENV_DIR.${NC}"
fi

# Activate the virtual environment
echo -e "${YELLOW}Activating the virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

# Upgrade pip and install dependencies from requirements.txt
echo -e "${YELLOW}Upgrading pip and installing packages...${NC}"
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Create a symlink for the zap-cli command globally
if [ -f "$ZAP_CLI_PATH" ]; then
    echo -e "${YELLOW}Creating global symlink for zap-cli...${NC}"
    sudo ln -sf "$ZAP_CLI_PATH" /usr/local/bin/zap-cli
else
    echo -e "${RED}Error: zap-cli.py not found at $ZAP_CLI_PATH.${NC}"
    deactivate
    exit 1
fi

# Final messages
echo -e "${GREEN}Setup complete. Virtual environment is ready to use.${NC}"
echo -e "${GREEN}To activate the virtual environment manually, run:${NC}"
echo -e "${GREEN}source ${VENV_DIR}/bin/activate${NC}"

echo -e "${GREEN}You can now run the CLI with:${NC}"
echo -e "${GREEN}zap-cli --help${NC}"

# Deactivate the virtual environment
deactivate

#!/bin/bash

# Python virtual environment setup script for zap-cli
set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Directories
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
ROOT_DIR="$(realpath "$SCRIPT_DIR/..")"
VENV_DIR="${ROOT_DIR}/venv"

echo -e "${YELLOW}Creating virtual environment at ${VENV_DIR}...${NC}"
python3 -m venv "$VENV_DIR"

# Activate venv
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip

# Install dependencies
if [ -f "${ROOT_DIR}/setup.py" ]; then
    echo -e "${YELLOW}Installing zap-cli in editable mode...${NC}"
    pip install -e "$ROOT_DIR"
elif [ -f "${ROOT_DIR}/requirements.txt" ]; then
    echo -e "${YELLOW}Installing dependencies from requirements.txt...${NC}"
    pip install -r "${ROOT_DIR}/requirements.txt"
else
    echo -e "${RED}No setup.py or requirements.txt found. Exiting...${NC}"
    deactivate
    exit 1
fi

# Deactivate
deactivate

echo -e "${GREEN}✅ Setup complete.${NC}"
echo -e "${GREEN}To use zap-cli globally, make sure ~/.local/bin is in your PATH.${NC}"
echo -e "${GREEN}You can now run:${NC}"
echo -e "${GREEN}zap-cli --help${NC}"

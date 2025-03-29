#!/bin/bash

# Python virtual environment setup script with zap-cli global symlink

set -euo pipefail

ROOT_DIR="$HOME"
VENV_DIR="${ROOT_DIR}/venv"
REQUIREMENTS_FILE="${ROOT_DIR}/requirements.txt"
ZAP_CLI_PATH="${ROOT_DIR}/zap_cli.py"

error_exit() {
    echo "Error: $1"
    exit 1
}

info() {
    echo "[INFO] $1"
}

command -v python3 >/dev/null || error_exit "Python3 is not installed."

if command -v dpkg &> /dev/null && ! dpkg -s python3-venv &> /dev/null; then
    info "Installing python3-venv..."
    sudo apt update && sudo apt install -y python3-venv
fi

if [ ! -f "$REQUIREMENTS_FILE" ]; then
    info "requirements.txt not found. Searching..."
    REQUIREMENTS_FILE=$(find "$ROOT_DIR" -name "requirements.txt" -print -quit)
    [ -z "$REQUIREMENTS_FILE" ] && error_exit "requirements.txt not found."
    info "Found requirements.txt at $REQUIREMENTS_FILE."
fi

if [ ! -d "$VENV_DIR" ]; then
    info "Creating virtual environment at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    info "Virtual environment already exists at $VENV_DIR."
fi

source "$VENV_DIR/bin/activate"

info "Upgrading pip and installing packages..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Create symlink
if [ -f "$ZAP_CLI_PATH" ]; then
    if [ ! -L /usr/local/bin/zap-cli ]; then
        sudo ln -s "$ZAP_CLI_PATH" /usr/local/bin/zap-cli
        echo "[INFO] zap-cli command created."
    else
        echo "[INFO] zap-cli command already exists."
    fi
else
    deactivate
    error_exit "zap_cli.py not found at $ZAP_CLI_PATH."
fi

info "Setup complete."
info "To activate the virtual environment manually, run:"
echo "source ${VENV_DIR}/bin/activate"
info "You can now run:"
echo "zap-cli --help"

deactivate

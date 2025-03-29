#!/bin/bash

set -euo pipefail

# Ensure python3-venv is installed
command -v python3 >/dev/null || { echo "Python3 is not installed."; exit 1; }

if ! dpkg -s python3-venv &>/dev/null; then
    echo "Installing python3-venv..."
    sudo apt update && sudo apt install -y python3-venv
fi

# Get the script's directory dynamically, so we can resolve paths relative to the script location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."  # The root directory is the parent of the 'scripting_tools' folder

# Define the paths for the environment setup
VENV_DIR="${ROOT_DIR}/venv"
REQUIREMENTS_FILE="${ROOT_DIR}/requirements.txt"
ZAP_CLI_PATH="${ROOT_DIR}/zap_cli.py"   # Path to zap_cli.py in the root directory

# Debugging: Check if zap_cli.py exists in the expected location
echo "DEBUG: Checking if $ZAP_CLI_PATH exists..."
if [ ! -f "$ZAP_CLI_PATH" ]; then
    echo "ERROR: zap_cli.py not found at $ZAP_CLI_PATH"
    exit 1
else
    echo "zap_cli.py found at $ZAP_CLI_PATH"
fi

# Find requirements.txt
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "requirements.txt not found. Searching..."
    REQUIREMENTS_FILE=$(find "$ROOT_DIR" -name "requirements.txt" -print -quit)
    [ -z "$REQUIREMENTS_FILE" ] && { echo "requirements.txt not found."; exit 1; }
    echo "Found requirements.txt at $REQUIREMENTS_FILE."
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install dependencies inside the virtual environment
echo "Upgrading pip and installing requirements inside the virtual environment..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Ensure missing dependencies (like psutil) are installed
echo "Installing missing dependencies like psutil..."
pip install psutil

# Create a wrapper script for zap-cli command to always run inside the virtual environment
WRAPPER_SCRIPT="/usr/local/bin/zap-cli"

if [ ! -f "$WRAPPER_SCRIPT" ]; then
    echo "Creating zap-cli wrapper script at $WRAPPER_SCRIPT..."
    cat << EOF | sudo tee "$WRAPPER_SCRIPT" > /dev/null
#!/bin/bash
# Ensure virtual environment is activated
source $VENV_DIR/bin/activate
# Run zap-cli within the virtual environment
$VENV_DIR/bin/python $ZAP_CLI_PATH "\$@"
# Deactivate the environment once done
deactivate
EOF

    sudo chmod +x "$WRAPPER_SCRIPT"
    echo "zap-cli wrapper script created successfully."
else
    echo "zap-cli wrapper script already exists."
fi

# Final message
echo "Setup complete."
echo "To activate the virtual environment manually, run:"
echo "source ${VENV_DIR}/bin/activate"
echo "You can now run zap-cli --help"

deactivate

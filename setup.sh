#!/bin/bash

# Define the name of the virtual environment
VENV_DIR="scrapy-env"

# Create virtual environment
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv $VENV_DIR
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install required dependencies
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "requirements.txt not found!"
fi

echo "Setup complete. To activate the environment later, run: source $VENV_DIR/bin/activate"

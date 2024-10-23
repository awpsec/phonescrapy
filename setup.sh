#!/bin/bash

VENV_DIR="scrapy-env"

if [ ! -d "$VENV_DIR" ]; then
  echo "creating virtual environment..."
  python3 -m venv $VENV_DIR
else
  echo "virtual environment already exists."
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

if [ -f "requirements.txt" ]; then
  echo "installing dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "requirements.txt not found!"
fi

echo "setup complete. to activate the environment later, run: source $VENV_DIR/bin/activate"

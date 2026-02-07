#!/bin/bash

# Setup script for Food Safety Ontology Demo
# This creates a virtual environment and installs required packages

echo "========================================================================"
echo "Setting up Food Safety Ontology Demo Environment"
echo "========================================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    echo "Please install Python3 first."
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Virtual environment directory
VENV_DIR="venv"

# Create virtual environment if it doesn't exist
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists."
    echo "To recreate, delete the 'venv' directory first."
    echo ""
else
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created!"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install required packages
echo "Installing required packages..."
echo ""

pip install --upgrade pip
pip install rdflib owlrl

echo ""
echo "========================================================================"
echo "Setup Complete!"
echo "========================================================================"
echo ""
echo "Required packages installed:"
echo "  ✓ rdflib  - RDF library for Python"
echo "  ✓ owlrl   - OWL-RL reasoning engine"
echo ""
echo "To run the demo:"
echo "  ./run.sh"
echo ""
echo "Or manually:"
echo "  source venv/bin/activate"
echo "  python3 reason.py"
echo "  deactivate"
echo ""

# Deactivate virtual environment
deactivate

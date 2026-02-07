#!/bin/bash

# Food Safety Ontology - Runner Script
# This script sets up the environment and runs the reasoning demo

echo "========================================================================"
echo "Food Safety Ontology - OWL Reasoning Demonstration"
echo "========================================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    exit 1
fi

echo "Current directory: $SCRIPT_DIR"
echo ""

# Virtual environment directory
VENV_DIR="venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created!"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Check if required packages are installed in venv
echo "Checking required packages..."

PACKAGES_NEEDED=false

if ! python3 -c "import rdflib" 2>/dev/null; then
    echo "  - rdflib is not installed"
    PACKAGES_NEEDED=true
fi

if ! python3 -c "import owlrl" 2>/dev/null; then
    echo "  - owlrl is not installed"
    PACKAGES_NEEDED=true
fi

if [ "$PACKAGES_NEEDED" = true ]; then
    echo ""
    echo "Installing required packages in virtual environment..."
    pip install rdflib owlrl
    echo ""
fi

echo "All packages are ready!"
echo ""

# Run the reasoning script
echo "Running the reasoning demonstration..."
echo ""

python3 reason.py

# Deactivate virtual environment
deactivate

echo ""
echo "========================================================================"
echo "Demo completed!"
echo "========================================================================"
echo ""
echo "Files created:"
echo "  - food_safety.ttl    : Ontology in Turtle format"
echo "  - food_safety.rdf    : Ontology in RDF/XML format"
echo "  - reason.py          : Python reasoning script"
echo "  - run.sh             : This runner script"
echo "  - venv/              : Virtual environment (auto-created)"
echo ""
echo "To run again: ./run.sh"
echo ""

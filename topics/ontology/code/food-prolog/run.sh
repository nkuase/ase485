#!/bin/bash

# Food Safety Prolog Demo - Runner Script
# This script runs the Prolog demonstration

echo "========================================================================"
echo "Food Safety Knowledge Base - Prolog Reasoning Demonstration"
echo "========================================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if SWI-Prolog is installed
if ! command -v swipl &> /dev/null; then
    echo "Error: SWI-Prolog is not installed"
    echo ""
    echo "Please run the setup script first:"
    echo "  ./setup.sh"
    echo ""
    exit 1
fi

echo "SWI-Prolog version:"
swipl --version
echo ""

# Check if food_safety.pl exists
if [ ! -f "food_safety.pl" ]; then
    echo "Error: food_safety.pl not found"
    echo "Make sure you're in the correct directory"
    exit 1
fi

echo "Running Prolog demonstration..."
echo ""

# Run the Prolog file and execute the demonstrate predicate
swipl -q -s food_safety.pl -g "demonstrate,halt" -t "halt(1)"

RESULT=$?

if [ $RESULT -eq 0 ]; then
    echo ""
    echo "========================================================================"
    echo "Demo completed successfully!"
    echo "========================================================================"
    echo ""
    echo "Files in this directory:"
    echo "  - food_safety.pl : Prolog knowledge base"
    echo "  - run.sh        : This runner script"
    echo "  - setup.sh      : Installation script"
    echo ""
    echo "To explore interactively:"
    echo "  swipl -s food_safety.pl"
    echo ""
    echo "Try these queries in interactive mode:"
    echo "  ?- demonstrate."
    echo "  ?- unsafe(mushroom1)."
    echo "  ?- safe(apple1)."
    echo "  ?- find_all_unsafe(X)."
    echo "  ?- find_all_safe(X)."
    echo "  ?- explain_unsafe(mushroom1)."
    echo "  ?- is_food(X)."
    echo ""
else
    echo ""
    echo "========================================================================"
    echo "Demo encountered an error"
    echo "========================================================================"
    echo ""
    echo "Please check the Prolog code for syntax errors."
    echo ""
    echo "To debug, run interactively:"
    echo "  swipl -s food_safety.pl"
    echo ""
    exit 1
fi

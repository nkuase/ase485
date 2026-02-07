#!/bin/bash

# Setup script for Food Safety Prolog Demo
# Installs SWI-Prolog on Ubuntu or macOS

echo "========================================================================"
echo "Setting up Food Safety Prolog Demo Environment"
echo "========================================================================"
echo ""

# Detect operating system
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    # Check if it's Ubuntu/Debian
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        if [[ "$ID" == "ubuntu" ]] || [[ "$ID" == "debian" ]]; then
            OS="ubuntu"
        fi
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="mac"
fi

echo "Detected OS: $OS"
echo ""

# Check if SWI-Prolog is already installed
if command -v swipl &> /dev/null; then
    echo "✓ SWI-Prolog is already installed!"
    swipl --version
    echo ""
    echo "Setup complete! You can run the demo with: ./run.sh"
    echo ""
    exit 0
fi

echo "SWI-Prolog is not installed. Installing..."
echo ""

# Install based on OS
case $OS in
    ubuntu)
        echo "Installing SWI-Prolog on Ubuntu/Debian..."
        echo ""
        
        # Check if running with sudo
        if [ "$EUID" -ne 0 ]; then
            echo "This script needs sudo privileges to install packages."
            echo "Please run: sudo ./setup.sh"
            echo ""
            echo "Or manually install SWI-Prolog:"
            echo "  sudo apt-get update"
            echo "  sudo apt-get install -y swi-prolog"
            exit 1
        fi
        
        apt-get update
        apt-get install -y swi-prolog
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "✓ SWI-Prolog installed successfully!"
            swipl --version
        else
            echo ""
            echo "✗ Failed to install SWI-Prolog"
            exit 1
        fi
        ;;
        
    mac)
        echo "Installing SWI-Prolog on macOS..."
        echo ""
        
        # Check if Homebrew is installed
        if ! command -v brew &> /dev/null; then
            echo "Homebrew is not installed."
            echo "Please install Homebrew first:"
            echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            echo ""
            echo "Or manually install SWI-Prolog:"
            echo "  1. Download from: https://www.swi-prolog.org/Download.html"
            echo "  2. Install the .dmg package"
            exit 1
        fi
        
        echo "Using Homebrew to install SWI-Prolog..."
        brew install swi-prolog
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "✓ SWI-Prolog installed successfully!"
            swipl --version
        else
            echo ""
            echo "✗ Failed to install SWI-Prolog"
            echo ""
            echo "Alternative installation method:"
            echo "  1. Download from: https://www.swi-prolog.org/Download.html"
            echo "  2. Install the .dmg package"
            exit 1
        fi
        ;;
        
    *)
        echo "Unsupported operating system: $OSTYPE"
        echo ""
        echo "Please install SWI-Prolog manually:"
        echo "  - Ubuntu/Debian: sudo apt-get install swi-prolog"
        echo "  - macOS: brew install swi-prolog"
        echo "  - Other: https://www.swi-prolog.org/Download.html"
        exit 1
        ;;
esac

echo ""
echo "========================================================================"
echo "Setup Complete!"
echo "========================================================================"
echo ""
echo "SWI-Prolog has been installed successfully."
echo ""
echo "To run the demo:"
echo "  ./run.sh"
echo ""
echo "To run Prolog interactively:"
echo "  swipl"
echo "  ?- [food_safety]."
echo "  ?- demonstrate."
echo ""

#!/bin/bash

# Install required libraries
echo "Installing required libraries..."
pip install -q rdflib owlrl

echo ""
echo "Running ontology reasoning demo..."
echo ""

python3 run.py

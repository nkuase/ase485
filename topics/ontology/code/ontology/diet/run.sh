#!/bin/bash

# Install required library
echo "Installing rdflib if needed..."
pip install -q rdflib

echo ""
echo "Running diet restrictions ontology demo..."
echo ""

python3 run.py

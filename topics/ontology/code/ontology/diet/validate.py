#!/usr/bin/env python3
"""
SHACL Validation Demo for Diet Ontology

Shows how to validate data quality using SHACL shapes.
"""

from rdflib import Graph
from pyshacl import validate

def main():
    print("\n" + "="*70)
    print("SHACL Validation Demo")
    print("="*70)
    print("\nValidating diet ontology data against SHACL shapes...")
    
    # Load data and shapes
    data_graph = Graph()
    data_graph.parse("diet.ttl", format="turtle")
    
    shapes_graph = Graph()
    shapes_graph.parse("shacl_shapes.ttl", format="turtle")
    
    print(f"✓ Loaded {len(data_graph)} data triples")
    print(f"✓ Loaded {len(shapes_graph)} shape triples")
    
    # Validate
    print("\nRunning validation...")
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference='rdfs',
        abort_on_first=False
    )
    
    # Display results
    print("\n" + "="*70)
    print("Validation Results")
    print("="*70)
    
    if conforms:
        print("\n✓ All data is VALID!")
        print("  All persons have names and restrictions")
        print("  All foods have names and ingredients")
        print("  All restrictions define incompatibilities")
    else:
        print("\n✗ Validation FAILED!")
        print("\nDetails:")
        print(results_text)
    
    print()

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("\nERROR: pyshacl library not installed")
        print("Install it with: pip install pyshacl")
        print()

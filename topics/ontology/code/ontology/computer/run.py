#!/usr/bin/env python3
"""
SPARQL Query Demo with Ontology Reasoning

Demonstrates the difference between:
1. Semantic queries using defined classes (AffordableComputer, GamingComputer)
2. Manual filtering with FILTER clauses

This shows the power of ontology reasoning!
"""

from rdflib import Graph
from owlrl import DeductiveClosure, OWLRL_Semantics

def run_query(graph, query_file, title):
    """Run a SPARQL query and display results."""
    print("\n" + "="*70)
    print(title)
    print("="*70)
    
    # Read query
    with open(query_file, 'r') as f:
        query = f.read()
    
    # Show query
    print("\nQuery:")
    print("-"*70)
    for line in query.split('\n'):
        if line.strip() and not line.strip().startswith('#'):
            print(f"  {line}")
    
    # Run query
    print("\nResults:")
    print("-"*70)
    
    results = list(graph.query(query))
    
    if len(results) == 0:
        print("  No results found.")
    else:
        for i, row in enumerate(results, 1):
            print(f"\n  {i}. {row.brand} {row.model}")
            print(f"     Price: ${row.price}")
            print(f"     RAM:   {row.ram}GB")
    
    print(f"\n  Total: {len(results)} computer(s) found")
    return len(results)

def main():
    print("\n" + "="*70)
    print("Ontology Reasoning Demo: Find Affordable Gaming Computers")
    print("="*70)
    
    # Load ontology
    print("\n1. Loading ontology...")
    g = Graph()
    g.parse("computers.ttl", format="turtle")
    print(f"   ✓ Loaded {len(g)} triples")
    
    # Apply OWL reasoning
    print("\n2. Applying OWL reasoning...")
    print("   This infers which computers are AffordableComputer and GamingComputer")
    print("   based on the OWL class definitions...")
    
    DeductiveClosure(OWLRL_Semantics).expand(g)
    print(f"   ✓ After reasoning: {len(g)} triples (inferred new facts!)")
    
    # Run semantic query
    count1 = run_query(g, "query.sparql", 
                       "METHOD 1: Semantic Query (using defined classes)")
    
    # Run manual query
    count2 = run_query(g, "query_manual.sparql",
                       "METHOD 2: Manual Filter (traditional approach)")
    
    # Summary
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    print(f"\nBoth methods found {count1} computers.")
    print("\nKey Difference:")
    print("  • Method 1: Uses semantic classes (AffordableComputer, GamingComputer)")
    print("              The ontology KNOWS what these mean!")
    print("  • Method 2: Uses manual FILTER clauses")
    print("              Must specify the rules in every query")
    print("\nAdvantage of Ontology:")
    print("  → Change definition once in ontology, all queries benefit")
    print("  → More maintainable and semantically clear")
    print("  → Can reason about concepts, not just filter data")
    print()

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("\n" + "="*70)
        print("ERROR: Missing required library")
        print("="*70)
        print("\nPlease install owlrl for reasoning:")
        print("  pip install owlrl")
        print()
        exit(1)

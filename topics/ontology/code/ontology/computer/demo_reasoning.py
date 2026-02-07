#!/usr/bin/env python3
"""
Visual demonstration of OWL reasoning step-by-step

Shows how the reasoner infers AffordableComputer and GamingComputer
"""

from rdflib import Graph, Namespace
from rdflib.namespace import RDF
from owlrl import DeductiveClosure, OWLRL_Semantics

def main():
    print("\n" + "="*80)
    print("Step-by-Step Ontology Reasoning Demo")
    print("="*80)
    
    # Load ontology
    print("\nStep 1: Load the ontology")
    print("-"*80)
    g = Graph()
    g.parse("computers.ttl", format="turtle")
    
    ex = Namespace("http://example.org/computers#")
    
    print(f"Loaded {len(g)} triples")
    print("\nThe ontology defines:")
    print("  • AffordableComputer = Computer with price < 1000")
    print("  • GamingComputer = Computer with RAM ≥ 16 AND DedicatedGPU")
    
    # Show computers BEFORE reasoning
    print("\nStep 2: Check computers BEFORE reasoning")
    print("-"*80)
    
    query_affordable = """
    PREFIX : <http://example.org/computers#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?computer WHERE {
        ?computer rdf:type :AffordableComputer .
    }
    """
    
    query_gaming = """
    PREFIX : <http://example.org/computers#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?computer WHERE {
        ?computer rdf:type :GamingComputer .
    }
    """
    
    affordable_before = list(g.query(query_affordable))
    gaming_before = list(g.query(query_gaming))
    
    print(f"AffordableComputers found: {len(affordable_before)}")
    print(f"GamingComputers found: {len(gaming_before)}")
    print("\n❌ No computers classified yet! The data exists but reasoning hasn't happened.")
    
    # Show what we DO have
    print("\nWhat we DO have (explicit data):")
    print("-"*80)
    
    query_computers = """
    PREFIX : <http://example.org/computers#>
    SELECT ?computer ?brand ?model ?price ?ram ?gpu WHERE {
        ?computer a :Laptop .
        ?computer :hasBrand ?brand .
        ?computer :hasModel ?model .
        ?computer :hasPrice ?price .
        ?computer :hasRAM ?ram .
        ?computer :hasGPU ?gpu .
    }
    ORDER BY ?price
    """
    
    computers = list(g.query(query_computers))
    for i, row in enumerate(computers, 1):
        print(f"\n{i}. {row.brand} {row.model}")
        print(f"   Price: ${row.price}, RAM: {row.ram}GB")
        print(f"   GPU: {str(row.gpu).split('#')[1]}")
    
    # Apply reasoning
    print("\n" + "="*80)
    print("Step 3: Apply OWL Reasoning")
    print("="*80)
    print("\nThe reasoner will:")
    print("  1. Read the OWL class definitions")
    print("  2. Check each computer's properties")
    print("  3. Infer which computers match the definitions")
    print("  4. Add new type assertions (triples)")
    
    input("\nPress Enter to apply reasoning...")
    
    DeductiveClosure(OWLRL_Semantics).expand(g)
    
    print(f"\n✓ Reasoning complete! Graph now has {len(g)} triples")
    print(f"  Added {len(g) - len(computers)*5 - 89} inferred triples")
    
    # Show computers AFTER reasoning
    print("\n" + "="*80)
    print("Step 4: Check computers AFTER reasoning")
    print("="*80)
    
    affordable_after = list(g.query(query_affordable))
    gaming_after = list(g.query(query_gaming))
    
    print(f"\nAffordableComputers found: {len(affordable_after)}")
    for row in affordable_after:
        comp_name = str(row.computer).split('#')[1]
        print(f"  • {comp_name}")
    
    print(f"\nGamingComputers found: {len(gaming_after)}")
    for row in gaming_after:
        comp_name = str(row.computer).split('#')[1]
        print(f"  • {comp_name}")
    
    # Show the final answer
    print("\n" + "="*80)
    print("Step 5: Query for Affordable Gaming Computers")
    print("="*80)
    
    final_query = """
    PREFIX : <http://example.org/computers#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?brand ?model ?price ?ram WHERE {
        ?computer rdf:type :AffordableComputer .
        ?computer rdf:type :GamingComputer .
        ?computer :hasBrand ?brand .
        ?computer :hasModel ?model .
        ?computer :hasPrice ?price .
        ?computer :hasRAM ?ram .
    }
    ORDER BY ?price
    """
    
    final_results = list(g.query(final_query))
    
    print(f"\nFinal Results: {len(final_results)} computer(s)")
    print("-"*80)
    
    for i, row in enumerate(final_results, 1):
        print(f"\n{i}. {row.brand} {row.model}")
        print(f"   Price: ${row.price}")
        print(f"   RAM: {row.ram}GB")
        print(f"   ✓ Affordable (< $1000) AND Gaming (≥16GB + Dedicated GPU)")
    
    print("\n" + "="*80)
    print("Summary: The Power of Ontology Reasoning")
    print("="*80)
    print("\nWithout reasoning:")
    print("  ❌ Computers are just data points")
    print("  ❌ Must manually filter in every query")
    print("\nWith reasoning:")
    print("  ✓ Computers are automatically classified")
    print("  ✓ Query using semantic concepts")
    print("  ✓ Change definition once, all queries benefit")
    print()

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("\nERROR: Please install required libraries:")
        print("  pip install rdflib owlrl")
        exit(1)

#!/usr/bin/env python3
"""
Diet Restrictions Ontology Demo

Demonstrates how ontologies can solve the problem of matching
foods with people's dietary restrictions.
"""

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS

def load_ontology():
    """Load the diet ontology."""
    g = Graph()
    g.parse("diet.ttl", format="turtle")
    return g

def run_query(graph, query_file, title):
    """Run a SPARQL query and display results."""
    print("\n" + "="*70)
    print(title)
    print("="*70)
    
    # Read query
    with open(query_file, 'r') as f:
        query = f.read()
    
    # Run query
    results = list(graph.query(query))
    
    if len(results) == 0:
        print("  No results found.")
    else:
        for i, row in enumerate(results, 1):
            if hasattr(row, 'foodName'):
                print(f"  {i}. {row.foodName}")
            else:
                # Print all columns
                parts = []
                for var in results.bindings[0].keys():
                    parts.append(f"{var}: {row[var]}")
                print(f"  {i}. {', '.join(parts)}")
    
    print(f"\n  Total: {len(results)} result(s)")
    return len(results)

def show_menu(graph):
    """Display all foods in the menu."""
    print("\n" + "="*70)
    print("Restaurant Menu")
    print("="*70)
    
    query = """
    PREFIX diet: <http://example.org/diet#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?foodName ?ingredient
    WHERE {
        ?food rdf:type diet:Food ;
              diet:foodName ?foodName ;
              diet:containsIngredient ?i .
        ?i rdfs:label ?ingredient .
    }
    ORDER BY ?foodName ?ingredient
    """
    
    results = list(graph.query(query))
    
    current_food = None
    for row in results:
        if row.foodName != current_food:
            if current_food:
                print()
            current_food = row.foodName
            print(f"\n  {current_food}")
            print(f"    Ingredients:")
        print(f"      - {row.ingredient}")

def show_people(graph):
    """Display all people and their restrictions."""
    print("\n" + "="*70)
    print("People and Their Restrictions")
    print("="*70)
    
    query = """
    PREFIX diet: <http://example.org/diet#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?name ?restrictionLabel
    WHERE {
        ?person diet:hasName ?name ;
                diet:hasRestriction ?restriction .
        ?restriction rdfs:label ?restrictionLabel .
    }
    ORDER BY ?name
    """
    
    results = list(graph.query(query))
    
    for row in results:
        print(f"  • {row.name}: {row.restrictionLabel}")

def main():
    """Main demo function."""
    print("\n" + "="*70)
    print("Diet Restrictions Ontology Demo")
    print("="*70)
    print("\nProblem: Match foods with people's dietary restrictions")
    print("Solution: Use ontology reasoning with SPARQL queries")
    
    # Load ontology
    print("\n" + "-"*70)
    print("Loading ontology...")
    g = load_ontology()
    print(f"✓ Loaded {len(g)} triples")
    
    # Show the data
    show_people(g)
    show_menu(g)
    
    # Run queries
    print("\n" + "="*70)
    print("QUERIES")
    print("="*70)
    
    run_query(g, "query_alice.sparql", 
              "Query 1: What can Alice (Vegetarian) eat?")
    
    run_query(g, "query_bob.sparql",
              "Query 2: What can Bob (Peanut Allergy) eat?")
    
    run_query(g, "query_safe_for_all.sparql",
              "Query 3: What can EVERYONE eat? (Safe for all restrictions)")
    
    run_query(g, "query_why_not.sparql",
              "Query 4: Why can't Alice eat Beef Burger? (Explainability)")
    
    run_query(g, "query_compatibility_matrix.sparql",
              "Query 5: Complete Compatibility Matrix")
    
    # Summary
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    print("\nBenefits of Ontology Approach:")
    print("  ✓ Explicit domain knowledge (what restrictions mean)")
    print("  ✓ Flexible queries (can ask any question)")
    print("  ✓ Explainable results (can show why)")
    print("  ✓ Easy to extend (add new foods, restrictions)")
    print("  ✓ No hard-coded if-statements!")
    print()

if __name__ == "__main__":
    main()

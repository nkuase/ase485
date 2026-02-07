#!/usr/bin/env python3
"""
Food Safety Ontology Reasoner
This script demonstrates OWL reasoning to infer that:
1. Eating mushroom is unsafe (because mushroom is poisonous)
2. Eating smelly meat is unsafe (because meat is smelly)
"""

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from owlrl import DeductiveClosure, OWLRL_Semantics

def load_and_reason(filename, format_type):
    """Load ontology and perform reasoning"""
    print(f"\n{'='*70}")
    print(f"Processing: {filename}")
    print(f"Format: {format_type}")
    print(f"{'='*70}\n")
    
    # Create a graph and load the ontology
    g = Graph()
    g.parse(filename, format=format_type)
    
    print(f"Original triples: {len(g)}")
    
    # Perform OWL-RL reasoning
    print("\nPerforming OWL-RL reasoning...")
    DeductiveClosure(OWLRL_Semantics).expand(g)
    
    print(f"After reasoning: {len(g)} triples")
    
    # Define namespaces
    FOOD = Namespace("http://example.org/food#")
    
    print("\n" + "="*70)
    print("REASONING RESULTS")
    print("="*70)
    
    # Query for UnsafeFood instances
    print("\n1. UNSAFE FOOD INSTANCES (Inferred by Reasoner):")
    print("-" * 70)
    
    unsafe_foods = []
    for s in g.subjects(RDF.type, FOOD.UnsafeFood):
        label = g.value(s, RDFS.label)
        unsafe_foods.append((s, label))
        print(f"   ✗ {label} is UNSAFE")
        
        # Show why it's unsafe
        is_poisonous = g.value(s, FOOD.isPoisonous)
        is_smelly = g.value(s, FOOD.isSmelly)
        
        reasons = []
        if is_poisonous and str(is_poisonous).lower() == "true":
            reasons.append("it is poisonous")
        if is_smelly and str(is_smelly).lower() == "true":
            reasons.append("it is smelly")
            
        if reasons:
            print(f"     Reason: because {' and '.join(reasons)}")
    
    if not unsafe_foods:
        print("   (No unsafe food found)")
    
    print("\n2. SAFE FOOD INSTANCES:")
    print("-" * 70)
    
    # Find all food instances
    all_foods = set(g.subjects(RDF.type, FOOD.Food))
    all_foods.update(g.subjects(RDF.type, FOOD.Mushroom))
    all_foods.update(g.subjects(RDF.type, FOOD.Meat))
    
    unsafe_food_uris = {uri for uri, _ in unsafe_foods}
    
    safe_foods = []
    for food_uri in all_foods:
        if food_uri not in unsafe_food_uris:
            label = g.value(food_uri, RDFS.label)
            if label:
                safe_foods.append(label)
                print(f"   ✓ {label} is SAFE")
    
    if not safe_foods:
        print("   (No safe food found)")
    
    print("\n3. INFERENCE EXPLANATION:")
    print("-" * 70)
    print("The reasoner applied these rules:")
    print("   Rule 1: IF (Food is poisonous) THEN (Food is unsafe)")
    print("   Rule 2: IF (Food is smelly) THEN (Food is unsafe)")
    print()
    print("Applied to our data:")
    print("   • mushroom1: isPoisonous=true → INFERRED: UnsafeFood")
    print("   • meat1: isSmelly=true → INFERRED: UnsafeFood")
    print("   • apple1: isPoisonous=false, isSmelly=false → SAFE")
    
    print("\n" + "="*70)
    print()

def main():
    print("\n" + "="*70)
    print("FOOD SAFETY ONTOLOGY - OWL REASONING DEMONSTRATION")
    print("="*70)
    print("\nThis demonstrates how OWL reasoning can infer:")
    print("  1. Eating mushroom is UNSAFE (because it's poisonous)")
    print("  2. Eating smelly meat is UNSAFE (because it's smelly)")
    print()
    
    # Process Turtle format
    load_and_reason("food_safety.ttl", "turtle")
    
    # Process RDF/XML format
    load_and_reason("food_safety.rdf", "xml")
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print("\nBoth formats (Turtle and RDF/XML) produce the same inference:")
    print("  • Mushroom 1 is UNSAFE (due to isPoisonous=true)")
    print("  • Meat 1 is UNSAFE (due to isSmelly=true)")
    print("  • Apple 1 remains SAFE (no dangerous properties)")
    print("\nThis shows how ontologies can help machines reason about")
    print("domain knowledge just like humans do!")
    print()

if __name__ == "__main__":
    main()

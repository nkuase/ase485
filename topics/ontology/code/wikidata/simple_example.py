"""
Simple Wikidata Example - Understanding the Basics

This is a simplified introduction to Wikidata concepts.
Start here before moving to douglas_adams_example.py

Concept: "Douglas Adams was an English writer, born in 1952"
"""

from SPARQLWrapper import SPARQLWrapper, JSON


def simple_query():
    """
    The simplest possible Wikidata query
    
    Query Structure:
    - PREFIX: Define shortcuts for long URIs
    - SELECT: What data to retrieve
    - WHERE: The pattern to match
    - SERVICE: Get human-readable labels
    """
    
    # Step 1: Create connection to Wikidata
    endpoint = "https://query.wikidata.org/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.addCustomHttpHeader("User-Agent", "Educational Example/1.0")
    
    # Step 2: Write SPARQL query
    query = """
    SELECT ?name ?birthDate ?occupation
    WHERE {
        # wd:Q42 is the unique identifier for Douglas Adams
        wd:Q42 rdfs:label ?name .
        wd:Q42 wdt:P569 ?birthDate .
        wd:Q42 wdt:P106 ?occupationEntity .
        ?occupationEntity rdfs:label ?occupation .
        
        # Get labels in English
        FILTER(LANG(?name) = "en")
        FILTER(LANG(?occupation) = "en")
    }
    LIMIT 5
    """
    
    # Step 3: Execute query
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    # Step 4: Display results
    print("=== Simple Query Results ===\n")
    for result in results["results"]["bindings"]:
        name = result["name"]["value"]
        birth = result["birthDate"]["value"][:10]  # Just the date part
        occupation = result["occupation"]["value"]
        print(f"Name: {name}")
        print(f"Birth Date: {birth}")
        print(f"Occupation: {occupation}")
        print()


def understand_uris():
    """
    Understanding Wikidata URIs
    
    URIs (Uniform Resource Identifiers) uniquely identify everything in Wikidata
    """
    print("=== Understanding Wikidata URIs ===\n")
    
    print("Full URI format:")
    print("  http://www.wikidata.org/entity/Q42")
    print("  └─ This is the full web address for Douglas Adams")
    print()
    
    print("Shorthand in SPARQL:")
    print("  wd:Q42")
    print("  └─ Much easier to type and read!")
    print()
    
    print("Common prefixes:")
    print("  wd:     Entities (people, places, things)")
    print("  wdt:    Properties (relationships)")
    print("  rdfs:   RDF Schema (labels, descriptions)")
    print()
    
    print("Examples:")
    print("  wd:Q42       = Douglas Adams (entity)")
    print("  wdt:P569     = date of birth (property)")
    print("  wdt:P106     = occupation (property)")
    print("  wd:Q36180    = writer (entity)")
    print()


def understand_triples():
    """
    Understanding RDF Triples
    
    Everything in Wikidata is stored as triples:
    Subject - Predicate - Object
    """
    print("=== Understanding RDF Triples ===\n")
    
    print("Triple Structure:")
    print("  Subject   - Who/what we're talking about")
    print("  Predicate - The relationship or property")
    print("  Object    - The value or another entity")
    print()
    
    print("Sentence: 'Douglas Adams was an English writer, born in 1952'")
    print()
    print("Broken into triples:")
    print()
    
    triples = [
        {
            "subject": "Douglas Adams",
            "predicate": "is a",
            "object": "human",
            "wikidata": "wd:Q42 → wdt:P31 → wd:Q5"
        },
        {
            "subject": "Douglas Adams",
            "predicate": "has occupation",
            "object": "writer",
            "wikidata": "wd:Q42 → wdt:P106 → wd:Q36180"
        },
        {
            "subject": "Douglas Adams",
            "predicate": "date of birth",
            "object": "1952-03-11",
            "wikidata": "wd:Q42 → wdt:P569 → '1952-03-11'"
        },
        {
            "subject": "Douglas Adams",
            "predicate": "country",
            "object": "United Kingdom",
            "wikidata": "wd:Q42 → wdt:P27 → wd:Q145"
        }
    ]
    
    for i, triple in enumerate(triples, 1):
        print(f"Triple {i}:")
        print(f"  Subject:   {triple['subject']}")
        print(f"  Predicate: {triple['predicate']}")
        print(f"  Object:    {triple['object']}")
        print(f"  Wikidata:  {triple['wikidata']}")
        print()


def main():
    print("=" * 70)
    print("SIMPLE WIKIDATA TUTORIAL")
    print("Learning semantic web concepts with Douglas Adams")
    print("=" * 70)
    print()
    
    # Lesson 1: What are URIs?
    understand_uris()
    
    # Lesson 2: What are RDF triples?
    understand_triples()
    
    # Lesson 3: Run a simple query
    try:
        simple_query()
    except Exception as e:
        print(f"Query Error: {e}")
        print("\nMake sure to install: pip install SPARQLWrapper")
    
    print("=" * 70)
    print("Next Steps:")
    print("1. Try running: python douglas_adams_example.py")
    print("2. Visit: https://www.wikidata.org/wiki/Q42")
    print("3. Explore: https://query.wikidata.org/")
    print("=" * 70)


if __name__ == "__main__":
    main()

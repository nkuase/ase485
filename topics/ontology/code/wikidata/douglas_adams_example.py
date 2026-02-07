"""
Wikidata Example: Modeling "Douglas Adams was an English writer, born in 1952"

This example demonstrates:
1. Querying Wikidata using SPARQL
2. Understanding Wikidata's entity-property-value structure
3. Working with RDF triples
4. Exploring semantic relationships

Wikidata Concepts:
- Entity: Douglas Adams (Q42)
- Properties: instance of (P31), occupation (P106), date of birth (P569), country of citizenship (P27)
- Values: human, writer, 1952-03-11, United Kingdom
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import json


def query_wikidata(sparql_query):
    """
    Execute a SPARQL query against Wikidata endpoint
    
    Args:
        sparql_query: SPARQL query string
    
    Returns:
        JSON results from the query
    """
    endpoint = "https://query.wikidata.org/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    
    # Add user agent (required by Wikidata)
    sparql.addCustomHttpHeader("User-Agent", "Educational Example/1.0")
    
    return sparql.query().convert()


def get_douglas_adams_basic_info():
    """
    Query basic information about Douglas Adams
    
    Models: "Douglas Adams was an English writer, born in 1952"
    
    Wikidata structure:
    - Q42 = Douglas Adams (entity)
    - P31 = instance of (property)
    - P106 = occupation (property)
    - P569 = date of birth (property)
    - P27 = country of citizenship (property)
    """
    query = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?property ?propertyLabel ?value ?valueLabel
    WHERE {
        # Douglas Adams is Q42
        wd:Q42 ?property ?value .
        
        # Filter for relevant properties
        FILTER(?property IN (wdt:P31, wdt:P106, wdt:P569, wdt:P27))
        
        # Get human-readable labels
        SERVICE wikibase:label { 
            bd:serviceParam wikibase:language "en" .
        }
    }
    """
    
    print("=== Douglas Adams Basic Information ===\n")
    results = query_wikidata(query)
    
    for result in results["results"]["bindings"]:
        prop = result["propertyLabel"]["value"]
        val = result.get("valueLabel", result.get("value", {})).get("value", "N/A")
        print(f"{prop}: {val}")
    
    return results


def get_douglas_adams_occupations():
    """
    Query all occupations of Douglas Adams
    
    Demonstrates: One entity can have multiple values for a property
    """
    query = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?occupation ?occupationLabel
    WHERE {
        # Douglas Adams (Q42) has occupation (P106)
        wd:Q42 wdt:P106 ?occupation .
        
        # Get labels in English
        SERVICE wikibase:label { 
            bd:serviceParam wikibase:language "en" .
        }
    }
    ORDER BY ?occupationLabel
    """
    
    print("\n=== Douglas Adams Occupations ===\n")
    results = query_wikidata(query)
    
    for result in results["results"]["bindings"]:
        occupation = result["occupationLabel"]["value"]
        print(f"- {occupation}")
    
    return results


def get_birth_details():
    """
    Query detailed birth information
    
    Demonstrates: Different data types in Wikidata (date, place)
    """
    query = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?birthDate ?birthPlace ?birthPlaceLabel
    WHERE {
        # Birth date
        wd:Q42 wdt:P569 ?birthDate .
        
        # Birth place (optional)
        OPTIONAL { 
            wd:Q42 wdt:P19 ?birthPlace .
        }
        
        SERVICE wikibase:label { 
            bd:serviceParam wikibase:language "en" .
        }
    }
    """
    
    print("\n=== Birth Details ===\n")
    results = query_wikidata(query)
    
    for result in results["results"]["bindings"]:
        birth_date = result["birthDate"]["value"]
        birth_place = result.get("birthPlaceLabel", {}).get("value", "N/A")
        print(f"Born: {birth_date}")
        print(f"Place: {birth_place}")
    
    return results


def get_notable_works():
    """
    Query notable works by Douglas Adams
    
    Demonstrates: Relationships between entities
    """
    query = """
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?work ?workLabel ?publicationDate
    WHERE {
        # Works where Douglas Adams is the author
        ?work wdt:P50 wd:Q42 .
        
        # Get publication date if available
        OPTIONAL { ?work wdt:P577 ?publicationDate . }
        
        SERVICE wikibase:label { 
            bd:serviceParam wikibase:language "en" .
        }
    }
    ORDER BY ?publicationDate
    LIMIT 10
    """
    
    print("\n=== Notable Works ===\n")
    results = query_wikidata(query)
    
    for result in results["results"]["bindings"]:
        work = result["workLabel"]["value"]
        pub_date = result.get("publicationDate", {}).get("value", "N/A")
        if pub_date != "N/A":
            pub_date = pub_date[:4]  # Extract year
        print(f"- {work} ({pub_date})")
    
    return results


def demonstrate_rdf_triples():
    """
    Demonstrate RDF triple structure
    
    Shows how "Douglas Adams was an English writer, born in 1952" 
    is represented as multiple RDF triples
    """
    print("\n=== RDF Triple Representation ===\n")
    print("The sentence 'Douglas Adams was an English writer, born in 1952'")
    print("is represented as multiple subject-predicate-object triples:\n")
    
    triples = [
        ("wd:Q42", "rdfs:label", '"Douglas Adams"@en'),
        ("wd:Q42", "wdt:P31", "wd:Q5"),  # instance of human
        ("wd:Q42", "wdt:P106", "wd:Q36180"),  # occupation: writer
        ("wd:Q42", "wdt:P27", "wd:Q145"),  # country: United Kingdom
        ("wd:Q42", "wdt:P569", '"1952-03-11"^^xsd:date'),  # birth date
    ]
    
    print(f"{'Subject':<15} {'Predicate':<15} {'Object':<30}")
    print("-" * 60)
    for subject, predicate, obj in triples:
        print(f"{subject:<15} {predicate:<15} {obj:<30}")
    
    print("\nWhere:")
    print("  wd:Q42 = Douglas Adams")
    print("  wdt:P31 = instance of")
    print("  wdt:P106 = occupation")
    print("  wdt:P27 = country of citizenship")
    print("  wdt:P569 = date of birth")
    print("  wd:Q5 = human")
    print("  wd:Q36180 = writer")
    print("  wd:Q145 = United Kingdom")


def main():
    """
    Main demonstration function
    """
    print("=" * 70)
    print("WIKIDATA EXAMPLE: Douglas Adams")
    print("Modeling: 'Douglas Adams was an English writer, born in 1952'")
    print("=" * 70)
    
    try:
        # 1. Basic information
        get_douglas_adams_basic_info()
        
        # 2. All occupations (writer is one of them)
        get_douglas_adams_occupations()
        
        # 3. Birth details
        get_birth_details()
        
        # 4. Notable works
        get_notable_works()
        
        # 5. RDF triple structure
        demonstrate_rdf_triples()
        
        print("\n" + "=" * 70)
        print("Key Takeaways:")
        print("1. Wikidata uses URIs to identify entities (Q42 for Douglas Adams)")
        print("2. Properties connect entities to values (P106 for occupation)")
        print("3. Everything is represented as RDF triples (subject-predicate-object)")
        print("4. SPARQL queries allow flexible data retrieval")
        print("5. Entities can have multiple values for the same property")
        print("=" * 70)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nNote: Make sure you have installed the required package:")
        print("  pip install SPARQLWrapper")


if __name__ == "__main__":
    main()

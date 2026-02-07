# Wikidata Example: Douglas Adams

This directory contains Python examples demonstrating Wikidata concepts using semantic web standards (RDF, URIs, and SPARQL).

## Sentence to Model

**"Douglas Adams was an English writer, born in 1952."**

## Learning Objectives

1. How Wikidata represents knowledge using RDF triples
2. How to use SPARQL to query semantic data
3. Understanding URIs as unique identifiers
4. Working with the Wikidata ontology
5. Connecting entities through properties

## Prerequisites

Install the required Python package:

```bash
pip install SPARQLWrapper
```

## Files

### 1. `simple_example.py` - Start Here!

A beginner-friendly introduction covering:

- What are URIs and how they work
- Understanding RDF triple structure (Subject-Predicate-Object)
- A simple SPARQL query example
- Visual explanation of how the sentence breaks down into triples

**Run it:**

```bash
python simple_example.py
```

### 2. `douglas_adams_example.py` - Complete Example

A comprehensive demonstration showing:

- Multiple SPARQL query patterns
- Querying basic information (occupation, birth date, citizenship)
- Handling multiple values for properties
- Working with dates and places
- Finding related entities (notable works)
- Understanding the complete RDF triple representation

**Run it:**

```bash
python douglas_adams_example.py
```

## Key Concepts Demonstrated

### 1. Entities and URIs

Every "thing" in Wikidata has a unique identifier (URI):

- **Douglas Adams**: `Q42`
- **Writer**: `Q36180`
- **United Kingdom**: `Q145`
- **Human**: `Q5`

Full URI format: `http://www.wikidata.org/entity/Q42`  
Shorthand: `wd:Q42`

### 2. Properties

Properties define relationships between entities:

- **P31**: instance of (what type of thing is it?)
- **P106**: occupation (what does this person do?)
- **P569**: date of birth (when were they born?)
- **P27**: country of citizenship (which country?)

Full URI format: `http://www.wikidata.org/prop/direct/P569`  
Shorthand: `wdt:P569`

### 3. RDF Triples

Knowledge is stored as triples: **Subject - Predicate - Object**

Our sentence breaks down into:

| Subject       | Predicate     | Object         |
| ------------- | ------------- | -------------- |
| Douglas Adams | instance of   | human          |
| Douglas Adams | occupation    | writer         |
| Douglas Adams | date of birth | 1952-03-11     |
| Douglas Adams | country       | United Kingdom |

In Wikidata notation:

```
wd:Q42 wdt:P31 wd:Q5 .          # Douglas Adams is a human
wd:Q42 wdt:P106 wd:Q36180 .     # Douglas Adams has occupation writer
wd:Q42 wdt:P569 "1952-03-11" .  # Douglas Adams born on 1952-03-11
wd:Q42 wdt:P27 wd:Q145 .        # Douglas Adams from United Kingdom
```

### 4. SPARQL Queries

SPARQL is the query language for RDF data:

```sparql
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?occupation ?occupationLabel
WHERE {
    wd:Q42 wdt:P106 ?occupation .

    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
    }
}
```

This query finds all occupations of Douglas Adams.

## Example Output

```
=== Douglas Adams Basic Information ===

instance of: human
occupation: science fiction writer
date of birth: 1952-03-11T00:00:00Z
country of citizenship: United Kingdom

=== Douglas Adams Occupations ===

- children's writer
- novelist
- science fiction writer
- screenwriter
- writer

=== Notable Works ===

- The Hitchhiker's Guide to the Galaxy (1979)
- The Restaurant at the End of the Universe (1980)
- Life, the Universe and Everything (1982)
```

## Educational Value

These examples demonstrate:

1. **Semantic Web Standards**: Using RDF, URIs, and SPARQL as defined by W3C
2. **Ontology Usage**: Working with Wikidata's ontology (entities, properties, values)
3. **Real-world Data**: Querying actual data from Wikidata's knowledge base
4. **Linked Data**: Understanding how entities connect to form a knowledge graph
5. **Practical Skills**: Writing SPARQL queries to extract information

## Further Exploration

### Online Resources

- **Wikidata Entry for Douglas Adams**: <https://www.wikidata.org/wiki/Q42>
- **Wikidata Query Service**: <https://query.wikidata.org/>
- **SPARQL Tutorial**: <https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial>

### Try These Queries

1. Find all British writers born in the 1950s
2. List all books in "The Hitchhiker's Guide" series
3. Find people who share Douglas Adams' birthdate
4. Discover other science fiction writers

### Experiment

Modify the code to explore:

- Different entities (try Q1299 for The Beatles)
- Different properties (try P800 for notable works)
- More complex query patterns (combining multiple conditions)

## Common Issues

**Import Error**: Make sure SPARQLWrapper is installed:

```bash
pip install SPARQLWrapper
```

**Timeout Error**: Wikidata query service may be slow. Try:

- Reducing the LIMIT in queries
- Running queries at different times
- Simplifying complex WHERE clauses

**No Results**: Check:

- Entity IDs are correct (Q42 for Douglas Adams)
- Property IDs are correct (P569 for birth date)
- SPARQL syntax is valid

## Assignment Ideas

1. **Basic**: Modify the code to query a different person (e.g., your favorite author)
2. **Intermediate**: Add a function to find all people with the same occupation
3. **Advanced**: Create a visualization of the relationship graph
4. **Challenge**: Build a mini knowledge base from multiple Wikidata queries

## License

Educational use for ASE485 course at Northern Kentucky University.

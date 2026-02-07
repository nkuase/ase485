# Ontology & SPARQL Example with Semantic Reasoning

This example demonstrates **ontology reasoning** - the key difference between traditional databases and semantic web.

## The Question

**"Find affordable gaming computers"**

## Two Approaches

### Approach 1: Semantic Classes (Ontology Way) ✨

```sparql
SELECT ?computer WHERE {
  ?computer rdf:type :AffordableComputer .
  ?computer rdf:type :GamingComputer .
}
```

The ontology **defines** what these classes mean:

- `AffordableComputer` = Computer with price < $1000
- `GamingComputer` = Computer with RAM ≥ 16GB + Dedicated GPU

### Approach 2: Manual Filtering (Traditional Way)

```sparql
SELECT ?computer WHERE {
  ?computer rdf:type :Computer .
  ?computer :hasPrice ?price .
  ?computer :hasRAM ?ram .
  ?computer :hasGPU ?gpu .
  ?gpu rdf:type :DedicatedGPU .
  FILTER(?price < 1000 && ?ram >= 16)
}
```

Must repeat these rules in **every query**!

## Files

- `computers.ttl` - Ontology with OWL class definitions
- `query.sparql` - Semantic query using defined classes
- `query_manual.sparql` - Manual filtering for comparison
- `run.py` - Python script with OWL reasoning
- `run.sh` - One-command setup and run

## Quick Start

```bash
chmod +x run.sh
./run.sh
```

Or manually:

```bash
pip install rdflib owlrl
python3 run.py
```

## What is OWL Reasoning?

The script uses **OWL reasoning** to automatically infer that:

- Computer1 IS AN `AffordableComputer` (price 899 < 1000)
- Computer1 IS A `GamingComputer` (RAM 16 ≥ 16 AND has DedicatedGPU)

This happens **before** the query runs!

## Expected Output

```
Ontology Reasoning Demo: Find Affordable Gaming Computers
======================================================================

1. Loading ontology...
   ✓ Loaded 89 triples

2. Applying OWL reasoning...
   ✓ After reasoning: 147 triples (inferred new facts!)

======================================================================
METHOD 1: Semantic Query (using defined classes)
======================================================================

Results:
----------------------------------------------------------------------

  1. ASUS TUF Gaming A15
     Price: $899
     RAM:   16GB

  2. CyberPowerPC Gamer Xtreme
     Price: $949
     RAM:   16GB

  Total: 2 computer(s) found

======================================================================
METHOD 2: Manual Filter (traditional approach)
======================================================================

Results:
----------------------------------------------------------------------

  1. ASUS TUF Gaming A15
     Price: $899
     RAM:   16GB

  2. CyberPowerPC Gamer Xtreme
     Price: $949
     RAM:   16GB

  Total: 2 computer(s) found
```

## The Data

| Computer                  | Price | RAM  | GPU       | Affordable? | Gaming? |
| ------------------------- | ----- | ---- | --------- | ----------- | ------- |
| ASUS TUF Gaming A15       | $899  | 16GB | RTX4060   | ✓           | ✓       |
| CyberPowerPC Gamer Xtreme | $949  | 16GB | GTX1660   | ✓           | ✓       |
| Alienware M15 R7          | $1499 | 32GB | RTX4060   | ✗           | ✓       |
| HP Pavilion 15            | $599  | 16GB | Intel UHD | ✓           | ✗       |
| Dell Inspiron 15          | $449  | 8GB  | Intel UHD | ✓           | ✗       |

## Key Concepts

### 1. Defined Classes (OWL)

```turtle
:AffordableComputer a owl:Class ;
    owl:equivalentClass [
        owl:intersectionOf (
            :Computer
            [
                owl:onProperty :hasPrice ;
                owl:someValuesFrom [
                    owl:onDatatype xsd:integer ;
                    owl:withRestrictions (
                        [ xsd:maxExclusive 1000 ]
                    )
                ]
            ]
        )
    ] .
```

This says: **"AffordableComputer IS ANY Computer with price < 1000"**

### 2. Reasoning Engine

The `owlrl` library applies these definitions:

- Reads the class definitions
- Checks each computer's properties
- **Automatically adds** `rdf:type :AffordableComputer` to matching computers
- Does the same for `GamingComputer`

### 3. Semantic Query

After reasoning, we can query directly:

```sparql
?computer rdf:type :AffordableComputer .
?computer rdf:type :GamingComputer .
```

No manual filtering needed!

## Why This Matters

### Traditional Approach (SQL/Manual SPARQL)

```sql
-- Must know the rules
WHERE price < 1000 AND ram >= 16 AND gpu_type = 'dedicated'

-- If definition changes, update EVERY query
-- If you have 100 queries, change 100 places!
```

### Ontology Approach

```sparql
-- Just query the concept
WHERE ?computer rdf:type :AffordableComputer .
      ?computer rdf:type :GamingComputer .

-- Definition in ONE place (ontology)
-- Change once, all queries benefit!
```

## Benefits

1. **Semantic Clarity** - "AffordableComputer" is more meaningful than filters
2. **Maintainability** - Change definition once, not in every query
3. **Reasoning** - Automatic inference based on rules
4. **Interoperability** - Share domain knowledge across systems
5. **Extensibility** - Add new defined classes easily

## Exercise

Try modifying the ontology to define:

1. **BudgetComputer** (price < $500)
2. **HighEndComputer** (RAM ≥ 32GB)
3. **WorkLaptop** (RAM ≥ 16GB, any GPU)

Then write queries to find them!

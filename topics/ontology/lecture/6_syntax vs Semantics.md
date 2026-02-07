---
marp: true
paginate: true
---

# (Optional) Syntax vs Semantics

Turtle and RDF/XML vs OWL — Correct Mental Model

---

## Two Major Ways to Describe Syntax

There are two major ways to describe syntax in the Semantic Web:

- Turtle
- RDF/XML

It is comparable to:

- JSON (for data)
- XML (for data)
- YAML (for data)

---

It is serialization syntax, like a programming language syntax.

- It only defines how things are written in the form of RDF triple.
- Turtle does NOT define meaning or logic.

“A file format with grammar rules”: not a full programming language.

- How to format prefixes
- How to serialize RDF graphs as text

---

### Syntax Example: Turtle vs RDF/XML

```turtle
:GeorgeWashington rdf:type :President .
```

```xml
<rdf:Description rdf:about="GeorgeWashington">
  <rdf:type rdf:resource="President"/>
</rdf:Description>
```

Both represent the same RDF triple (SPO):

- Subject: :GeorgeWashington
- Predicate: rdf:type
- Object: :President

---

## Semantics to Define Meaning (OWL)

We use turtle or rdf/xml to write RDF data (triplet), but we need semantics to define meaning.

- It takes too much time to define all the meanings all by ourselves, so we use vocabularies (already defined terms).
- We need base data model; for example rdf:type to express the meaning of "is a".
- We need another model, such as OWL that defines higher-level semantic logic using RDF as its foundation.

---

### OWL: Web Ontology Language

OWL = Semantic Vocabulary + Logic Layer (Like a Library + Type System)

OWL is more like:

- A semantic framework
- A logic specification
- A vocabulary with formal meaning

---

### The OWL Vocabulary

OWL provides a vocabulary that defines semantic concepts and relationships.

It defines concepts such as:

- owl:Class
- owl:Restriction
- owl:equivalentClass
- owl:disjointWith

---

### OWL Semantics Example

Example:

```owl
:President rdf:type owl:Class ;
           rdfs:subClassOf :Person .
```

OWL tells the machine:

- What is a class (owl:Class)
- What subclass means (rdfs:subClassOf)
- What logical inference is allowed

So OWL behaves like:

- A domain-specific semantic library + reasoning rules

---

#### Line 1: :President rdf:type owl:Class

"President is a class" ✓
This declares that President is a type/category of things (class definition).

#### Line 2: rdfs:subClassOf :Person

"President is a subclass of Person" ✓
This means: All presidents are persons (inheritance/hierarchy)

---

#### Visualizing OWL Semantics

```txt
Person (superclass)
  └─ President (subclass)
```

#### Logical Implication

```txt
If X is a President
Then X is also a Person
```

---

## The Programming Analogy

RDF is like:

- Basic data structures (triples)
- In-memory object model
  OWL is like:

- Library that has existing classes and properties
- Type system that defines how to use them logically

---

### RDF as Basic Data Model

Think of **RDF** as the **syntax and storage layer** — a bit like Java’s ability to declare objects and relationships in memory, but without enforcing logic or constraints.

- **Purpose:** Represent data as triples (subject–predicate–object).
- **Analogy:** Like having plain objects, strings, or lists — flexible but not semantically rich.
- **Example:**

```java
// You can say anything; there’s no schema enforcement.
Triple t = new Triple("Alice", "likes", "Pizza");
Triple t2 = new Triple("Alice", "is_a", "Person");
```

- RDF just records relationships. It doesn’t know or care what "Person" or "likes" _mean_ — it only ensures a consistent structure.

---

### OWL as the Semantic Library and Logical Type System

**OWL (Web Ontology Language)** adds _vocabulary, constraints,_ and _reasoning_ on top of RDF — much like a **type system** or **framework** that defines how objects can relate and what rules apply.

- **Purpose:** Define **classes**, **properties**, **restrictions**, and enable **reasoning** (e.g., inferring new facts).
- **Analogy:** Like creating class hierarchies, interfaces, and type-safe relationships using Java Generics or frameworks like Spring.
- **Example:**

  ```java
  class Person extends LivingThing { }
  interface Vegetarian extends Person {
      List<Food> eats(); // Must eat only Food
  }
  ```

---

- **OWL defines semantic rules** — what classes mean, which properties they can use, and how they relate logically.
- **OWL enforces logical consistency** — it can detect contradictions and automatically infer classifications based on those rules.

Notice that OWL uses RDF as its underlying representation format, not as a coincidence but as an architectural choice.

- RDF provides the graph structure (triples: subject–predicate–object)
- OWL provides the semantics and logic (what those triples mean)

---

## Another Analogy

Semantic Web Programming Analogy

- Turtle Source code syntax (JSON / Python text)
- RDF Memory object model
- OWL Type system + logic library
- Ontology Application domain model

---

### Concrete Example

When we write:

```turtle
:President rdfs:subClassOf :Person .
```

A Turtle parser (not Turtle itself) does:

- Read text
- Apply grammar rules
- Convert it into RDF triples

Results in memory representation - triple (S, P, O):

```txt
( President , rdfs:subClassOf , Person )
```

---

An OWL reasoner (e.g., Pellet, HermiT, Fact++, or ELK) does:

- Understands subClassOf logically
- Enables inference:

If this additional fact is given:

```txt
GeorgeWashington rdf:type President
```

It infers:

```turtle
GeorgeWashington rdf:type Person
```

---

### Important Nuance

OWL is not executable code like Python.

Instead:

- OWL defines formal logic semantics
- A reasoner engine executes the logic

Like:

Component Role
OWL Rule specification
Reasoner Execution engine
Turtle Input syntax

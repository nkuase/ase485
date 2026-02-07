---
marp: true
paginate: true
---

# Ontology and Semantic Web

---

## How Are They Related?

Ontology and the Semantic Web are tightly connected.

In simple terms:

> **Ontology provides meaning**  
> **Semantic Web provides the infrastructure to use that meaning on the Web**

---

## Ontology

Ontology is a **formal model of knowledge**.

It defines:

- Concepts (Classes)
- Relationships (Properties)
- Rules (Constraints)
- Meaning (Semantics)

---

Example:

Student ⊆ Person
Person ⊆ Mammal

Ontology answers:

> What exists?  
> How are things related?  
> What rules apply?

---

## What Is the Semantic Web?

Semantic Web is a **web of machine-understandable data**.

Goal:

> Make web data understandable by machines, not just humans.

It uses standards:

- RDF → Data model
- RDFS → Basic schema
- OWL → Ontology language
- SPARQL → Query language

---

## How Ontology Fits Into the Semantic Web

Ontology is the **semantic layer** of the Semantic Web.

Relationship:

Semantic Web = Data + Meaning + Reasoning
Ontology = Meaning + Logic

Ontology supplies the meaning that Semantic Web systems use.

---

## Semantic Web Stack View

SPARQL ← Query knowledge
OWL ← Ontology (semantics + logic)
RDFS ← Basic schema
RDF ← Data representation
Web Data ← Raw information

Ontology (OWL) sits at the **core logic layer**.

---

## Without Ontology

Semantic Web becomes:

- Connected data only
- No logical rules
- No inference
- No semantic consistency

---

Example:

Alice eats Pizza

System does NOT know:

- Who Alice is
- What Pizza represents
- Whether this relationship is valid

---

## With Ontology

Ontology adds meaning:

Alice → Person
Pizza → Food
eats → Person → Food

Now the system can:

- Validate data
- Infer new facts
- Detect errors
- Enable reasoning

---

## Ontology Makes Semantic Web "Semantic"

Important idea:

> RDF creates links  
> Ontology creates understanding

Ontology transforms:

Data Web → Knowledge Web

---

## Real-World Usage

Ontology in Semantic Web enables:

- Knowledge Graphs
- AI reasoning systems
- Intelligent search
- Data integration
- Scientific databases
- Enterprise knowledge platforms

---

## Simple Analogy

| Component    | Analogy                      |
| ------------ | ---------------------------- |
| Semantic Web | Internet of data             |
| Ontology     | Dictionary + grammar + rules |

Data flows through the web.  
Ontology teaches machines how to understand it.

---

# Key Takeaway

- Ontology defines meaning
- Semantic Web uses that meaning at scale
- Ontology is the intelligence layer
- Semantic Web is the distribution platform

Together they create **machine-understandable knowledge on the web**.

---

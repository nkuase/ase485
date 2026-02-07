---
marp: true
paginate: true
---

# Avoiding Poisonous Food (Example of Ontology/OWL Reasoning)

(Domain → Language → Data)

---

## Domain Level (Human knowledge)

We have experiences about food domain.
These are **natural-language ideas in the food domain** from experience:

- "Poisonous mushrooms are dangerous to eat."
- "Meat with a weird smell is dangerous."
- "People should avoid dangerous food."

---

1. This is highest-level knowledge about food.
2. We use **natural language** to express it.
3. This is **human understanding**, not machine-readable yet.
4. In this level (domain level) description, we have **vague ideas** that are impossible for machines to understand.

---

### Domain Knowledge: "People should avoid dangerous food"

- This is informal knowledge in natural language.
- Machines cannot understand this directly.
  - What is "people" exactly?
  - What is "poisonous" exactly?
  - How to relate "dangerous" to "avoid"?

We need another level of description to make it precise for machines to understand and reason.

---

## Language Level (Adding Formal Meaning)

In the real world, when we need to specify meaning precisely,
(1) we define the meaning of the vocabulary, and (2) we set the logical relationships.

### Define Vocabulary

Think about the talk between a kid and mom:

- Kid: What is "food"? - Mom: It's something a person can eat.
- Kid:What is "poisonous"? - Mom: It contains poison that harms people.
- Kid: What is "smelly"? - Mom: It has a bad smell.

---

### Define Logical Relationships

Think about the instructions from mom:

- If a food is poisonous, then it is unsafe.
- If a food is smelly, then it is unsafe.

---

Likewise, we need to define concepts and rules for machines to understand the food domain.

### Concepts (Vocabulary)

- **Food** = something a person can eat
- **Poisonous** = contains poison
- **Smelly** = has bad smell
- **Safe** = OK to eat
- **Unsafe** = NOT OK to eat

---

### Rules (Logic)

- **Poisonous Food → Unsafe**
- **Smelly Food → Unsafe**
- **Unsafe Food → DoNotEat**

---

- When we define concepts and rules, we give formal meaning to natural language.
- This means we translate vague human ideas into precise machine-understandable definitions.
- In other words, we use the language form to represent knowledge formally.

Now the machine knows _what the words mean_ and _how they relate_.

---

## Data Level (Actual facts)

In the real world, we need to write down these knowledge so that others can use them to avoid dangerous food.

### Writing Actual Facts

"Mushroom is a food and it is poisonous."

We can use another language to express the same idea:

"Der Pilz ist ein Nahrungsmittel, und er ist giftig."
"キノコは食べ物ですが、毒があります。

At this level, we focus on writing down using the language we defined before; we don't care about the meaning itself.

---

To make machine understand this data level: we need to store the data **formally** using the vocabulary and rules defined in the language level.

### Example Data

(Mushroom, type, Food)
(Mushroom, Poisonous, Yes)

(Meat, type, Food)
(Meat, Smelly, Yes)

---

## Using the Domain Knowledge to Avoid Dangerous Food

Think about the kid who understands the domain knowledge about the food (domain level) from the talk with mom (language level) and the actual facts written down (data level).

---

### The Kid's Understanding Process

The kid sees the mushroom, and infers from the facts:

- This mushroom is Mushroom
- Mushroom is a Food.
- Mushroom is Poisonous.
- Possinous Food → Unsafe
- Therefore, this mushroom is Unsafe.

Likewise, the kid sees the meat that is smelly, and infers: "This Meat is Unsafe."

---

### Instances & Classes

From a concrete example "mushroom", the kid can infer that it is unsafe to eat this "mushroom".

- This is possible because the kid knows that "mushroom" is an instance of the class "Mushroom".
- The kid also knows that "Mushroom" is a subclass of "Food".
- Therefore, the kid can apply the rules defined for "Food" to the instance "mushroom".

### Properites & Relations

- Also, the Mushroom class has the property "poisonous".
- The poisonous property is related to the rule "Poisonous Food → Unsafe".
- Therefore, the kid can apply the property "poisonous" of the instance "mushroom" to the rule to infer that the mushroom is unsafe.

---

## Machine Result (Derived from rules)

Using the vocabulary and rules, we can make the machine derive conclusions automatically.:

Mushroom → Unsafe → DoNotEat
Meat & Smelly → Unsafe → DoNotEat

---

## Summary

<style scoped>
table {
  font-size: 18pt !important;
}
table thead tr {
  background-color: #aad8e6;
}
</style>

| Level    | Purpose                | Example                    |
| -------- | ---------------------- | -------------------------- |
| Domain   | Human knowledge        | "Smelly meat is dangerous" |
| Language | Formal meaning + rules | Smelly → Unsafe            |
| Data     | Concrete facts         | (Meat1, Smelly, Yes)       |
| Result   | Machine conclusion     | DoNotEat(Meat1)            |

---

## Implementation Examples: OWL vs Prolog

1. **Ontology/OWL Reasoning Example**: 1p1_avoiding_poisonous_food.md

- Using OWL ontology to define concepts, properties, and rules.
- Performing reasoning to derive conclusions about food safety.

2. **Prolog Example**: 1p2_avoiding_poisonous_food_prolog.md

- Using Prolog logic programming to define facts and rules.
- Performing reasoning to derive conclusions about food safety.

3. **Comparison of OWL vs Prolog**: 1p3_OWL_vs_PROLOG.md

- Comparing the two approaches in terms of structure, educational value, and performance.

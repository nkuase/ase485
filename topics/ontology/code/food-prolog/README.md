# Food Safety Knowledge Base - Prolog Example

This directory contains a Prolog implementation of the food safety reasoning system, demonstrating the same Domain → Language → Data approach as the OWL ontology example.

## Overview

This example shows how Prolog logic programming can reason about food safety:
- **Inference 1**: Eating mushroom is UNSAFE (because mushrooms are poisonous)
- **Inference 2**: Eating smelly meat is UNSAFE (because smelly meat is dangerous)

## Quick Start

```bash
# First time setup (installs SWI-Prolog)
chmod +x setup.sh run.sh
./setup.sh

# Run the demonstration
./run.sh
```

## Important: Understanding Prolog Naming

**In Prolog, capitalization has semantic meaning!**

- **Capital letters** (`Food`, `X`, `Type`) = **VARIABLES** (can be anything)
- **Lowercase letters** (`mushroom`, `meat1`) = **ATOMS/CONSTANTS** (specific values)

See [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md) for detailed explanation.

## Files

- **setup.sh** - Installation script for SWI-Prolog (Ubuntu & macOS)
- **run.sh** - Main runner script
- **food_safety.pl** - Prolog knowledge base (extensively commented)
- **README.md** - This file
- **QUICKSTART.md** - Quick start guide
- **NAMING_CONVENTIONS.md** - Detailed explanation of Prolog naming rules

## How It Works

### 1. Domain Level (Human Knowledge)

From experience, we know:
- "Poisonous mushrooms are dangerous to eat"
- "Meat with a weird smell is dangerous"

### 2. Language Level (Formal Meaning)

In Prolog, we define concepts and rules:

**Concepts (Facts and Rules)**:
```prolog
% Define what things are food
% X is a VARIABLE (capital)
is_food(X) :- mushroom(X).
is_food(X) :- meat(X).
is_food(X) :- fruit(X).
```

**Rules (Logic)**:
```prolog
% Rule 1: If a food is poisonous, then it is unsafe
% Food is a VARIABLE (capital)
unsafe(Food) :- 
    is_food(Food), 
    is_poisonous(Food).

% Rule 2: If a food is smelly, then it is unsafe
unsafe(Food) :- 
    is_food(Food), 
    is_smelly(Food).

% If not unsafe, then it's safe
safe(Food) :- 
    is_food(Food), 
    \+ unsafe(Food).
```

### 3. Data Level (Actual Facts)

We have specific instances (these are ATOMS - lowercase):
```prolog
% Instance 1: A specific mushroom
mushroom(mushroom1).
is_poisonous(mushroom1).

% Instance 2: A specific meat
meat(meat1).
is_smelly(meat1).

% Instance 3: A safe apple
fruit(apple1).
```

### 4. Reasoning Result

Prolog automatically infers:
- ✗ `mushroom1` is **UNSAFE** (because is_poisonous)
- ✗ `meat1` is **UNSAFE** (because is_smelly)
- ✓ `apple1` is **SAFE** (no dangerous properties)

## Example Output

```
======================================================================
FOOD SAFETY KNOWLEDGE BASE - PROLOG REASONING DEMONSTRATION
======================================================================

Note: In Prolog, capital letters (Food, X) are VARIABLES,
      lowercase letters (mushroom, meat1) are ATOMS/CONSTANTS.

----------------------------------------------------------------------
1. UNSAFE FOOD INSTANCES (Inferred by Prolog)
----------------------------------------------------------------------
   ✗ mushroom1 is UNSAFE
     Reason: because it is poisonous
   ✗ meat1 is UNSAFE
     Reason: because it is smelly

----------------------------------------------------------------------
2. SAFE FOOD INSTANCES
----------------------------------------------------------------------
   ✓ mushroom2 is SAFE
   ✓ meat2 is SAFE
   ✓ apple1 is SAFE
   ✓ banana1 is SAFE
```

## Interactive Mode

You can also run Prolog interactively to explore:

```bash
swipl -s food_safety.pl
```

Then try these queries:

```prolog
?- demonstrate.              % Run full demonstration

?- unsafe(mushroom1).        % Check if mushroom1 is unsafe
true.                        % mushroom1 is an ATOM (specific value)

?- unsafe(X).                % Find what X could be that makes it unsafe
X = mushroom1 ;              % X is a VARIABLE (finds all values)
X = meat1.

?- safe(apple1).             % Check if apple1 is safe
true.

?- find_all_unsafe(X).       % Find all unsafe foods
X = [mushroom1, meat1].

?- is_food(X).               % List all food items
X = mushroom1 ;
X = mushroom2 ;
X = meat1 ;
...
```

## Prolog vs OWL Comparison

### Key Difference: Capitalization

| Concept | OWL/RDF | Prolog |
|---------|---------|--------|
| Class name | `:Food` (capital) | N/A |
| Variable | N/A | `Food` (capital) |
| Instance | `:mushroom1` | `mushroom1` (lowercase) |
| Predicate | N/A | `unsafe` (lowercase) |

**In OWL**: `Food` is a class name (capitalization is style)
**In Prolog**: `Food` is a variable (capitalization has meaning)

### Similarities:
- Both use the Domain → Language → Data approach
- Both perform automatic reasoning
- Both infer new facts from rules
- Both handle the same use case

### Differences:

| Aspect | Prolog | OWL |
|--------|--------|-----|
| Paradigm | Logic Programming | Description Logic |
| Syntax | Horn clauses | RDF/XML or Turtle |
| Reasoning | Backward chaining | Forward/Backward |
| Queries | Interactive predicates | SPARQL queries |
| Use Case | AI, Expert Systems | Semantic Web |
| Naming | Semantic (caps=var) | Convention (caps=class) |

## Learning Points for Students

1. **Logic Programming Paradigm**:
   - Facts: ground truths (`mushroom(mushroom1)`)
   - Rules: logical implications (`unsafe(X) :- ...`)
   - Queries: questions to prove (`?- unsafe(mushroom1)`)

2. **Prolog Naming Convention**:
   - **Capital = Variable** (can be anything)
   - **Lowercase = Atom** (specific value)
   - This is NOT just style—it has semantic meaning!

3. **Declarative vs Procedural**:
   - Prolog: "What is true" (declarative)
   - Python/Java: "How to compute" (procedural)

4. **Automatic Reasoning**:
   - No explicit algorithms needed
   - Prolog engine handles inference
   - Rules automatically applied

5. **Pattern Matching**:
   - Variables (`X`, `Food`) match patterns
   - Unification finds solutions
   - Backtracking explores alternatives

## Installation Notes

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install swi-prolog
```

### macOS (with Homebrew)
```bash
brew install swi-prolog
```

### macOS (without Homebrew)
Download from: https://www.swi-prolog.org/Download.html

## Requirements

- SWI-Prolog 8.0+ (tested with 8.4+)
- Bash shell (for running scripts)
- Unix-like environment (Linux, macOS, WSL on Windows)

## Extending the Example

Try adding:

1. **New food types**:
```prolog
vegetable(carrot1).
is_food(X) :- vegetable(X).
```

2. **New properties**:
```prolog
is_expired(milk1).
```

3. **New rules**:
```prolog
% Expired food is unsafe
unsafe(Food) :- 
    is_food(Food), 
    is_expired(Food).
```

## Common Student Questions

### Q: Why is `Food` capitalized but `mushroom` is not?
**A**: In Prolog, capital letters indicate VARIABLES, lowercase indicates ATOMS (constants). See [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md) for full explanation.

### Q: Can I use `food` as a variable?
**A**: No! `food` (lowercase) is an atom, not a variable. Use `Food` (capital) for variables.

### Q: What's the difference between `unsafe(mushroom1)` and `unsafe(X)`?
**A**: 
- `unsafe(mushroom1)`: Check if specific atom `mushroom1` is unsafe
- `unsafe(X)`: Find all values `X` can be where `X` is unsafe

## Troubleshooting

### SWI-Prolog not found
```bash
which swipl
# If not found, run setup
./setup.sh
```

### Permission denied
```bash
chmod +x setup.sh run.sh
```

### Syntax errors
Run interactively to see detailed error messages:
```bash
swipl -s food_safety.pl
```

## Educational Use

This example is designed for teaching:
- Logic programming fundamentals
- Knowledge representation
- Automated reasoning
- Comparison with OWL/RDF
- Practical AI applications
- **Semantic significance of naming conventions**

The code includes extensive comments and demonstrates the same three-level model (Domain → Language → Data) from the lecture materials, making it easy to compare with the OWL example.

## References

- [SWI-Prolog Documentation](https://www.swi-prolog.org/pldoc/doc_for?object=manual)
- [Learn Prolog Now!](http://www.learnprolognow.org/)
- [Logic Programming Tutorial](https://www.metalevel.at/prolog)
- [Prolog Variables Explained](https://www.swi-prolog.org/pldoc/man?section=quickstart)

# Prolog Naming Conventions Explained

## The Capital Letter Question

**Student Question**: "Why is `Food` capitalized but `mushroom(X)` uses lowercase?"

**Answer**: In Prolog, capitalization has **semantic meaning** (not just style)!

## The Rule

| Starting Character | Meaning | Example | Usage |
|-------------------|---------|---------|-------|
| **Capital letter** | Variable | `Food`, `X`, `Type` | Represents unknown values |
| **Lowercase letter** | Atom/Constant | `mushroom`, `meat1` | Represents specific values |

## Visual Examples

### Example 1: Rule Definition

```prolog
% "Food is unsafe IF Food is a food AND Food is poisonous"
unsafe(Food) :- 
    is_food(Food), 
    is_poisonous(Food).
```

- `Food` = Variable (capital F)
  - Could be `mushroom1`
  - Could be `meat1`
  - Could be `apple1`
  - Could be ANY food

- `unsafe`, `is_food`, `is_poisonous` = Predicate names (lowercase)
  - These are fixed names, not variables

### Example 2: Querying

```prolog
% Specific check (using an atom)
?- unsafe(mushroom1).
true.

% General query (using a variable)
?- unsafe(X).
X = mushroom1 ;
X = meat1.
```

In the second query:
- `X` is a **variable** (capital)
- Prolog finds all values that make `unsafe(X)` true
- `X` gets "bound" to `mushroom1`, then `meat1`

### Example 3: Pattern Matching

```prolog
% Define facts with atoms (lowercase)
mushroom(mushroom1).
mushroom(mushroom2).

% Query with variable (uppercase)
?- mushroom(X).
X = mushroom1 ;    % First, X matches mushroom1
X = mushroom2.     % Then, X matches mushroom2
```

## Comparison with OWL

### OWL/RDF (Turtle):
```turtle
# In OWL, capitalization is just a naming convention
:Food rdf:type owl:Class .
:Mushroom rdfs:subClassOf :Food .
:mushroom1 rdf:type :Mushroom .

# Both Food and Mushroom are class names (not variables)
# mushroom1 is an instance
```

### Prolog:
```prolog
% In Prolog, capitalization has meaning!
is_food(X) :- mushroom(X).    % X is a VARIABLE
mushroom(mushroom1).           % mushroom1 is an ATOM

% You CANNOT write:
is_food(food) :- mushroom(food).  % WRONG! food is not a variable
```

## Common Mistakes Students Make

### ❌ Mistake 1: Using lowercase for variables
```prolog
% WRONG - 'x' is treated as an atom, not a variable
unsafe(x) :- is_food(x), is_poisonous(x).
```

This means: "x is unsafe if x is food and x is poisonous"
- But `x` is NOT a variable, it's the specific atom 'x'
- This rule only applies to something literally called 'x'

### ✅ Correct:
```prolog
% RIGHT - 'X' is a variable
unsafe(X) :- is_food(X), is_poisonous(X).
```

This means: "X (anything) is unsafe if X is food and X is poisonous"
- `X` can be `mushroom1`, `meat1`, etc.

### ❌ Mistake 2: Using capital letters for atoms
```prolog
% WRONG - Prolog thinks Food is a variable
mushroom(Food).
```

If you query `?- mushroom(Food).` you get:
```prolog
Food = Food.    % Prolog thinks you're asking if variable Food matches variable Food
```

### ✅ Correct:
```prolog
% RIGHT - mushroom1 is an atom
mushroom(mushroom1).
```

## Why This Design?

Historical reasons from the 1970s:

1. **Visual Distinction**: Easy to see what's variable vs constant
2. **No Type Declarations**: Variables don't need to be declared
3. **Pattern Matching**: Makes unification clearer

```prolog
% It's immediately clear that:
likes(Person, Food) :- ...    % Person and Food are variables
likes(john, pizza).           % john and pizza are constants
```

## Analogy for Students

Think of it like algebra:

### Math:
```
f(x) = x² + 3x + 2    % x is a variable
f(5) = 5² + 3(5) + 2  % 5 is a constant
```

### Prolog:
```prolog
unsafe(Food) :- ...     % Food is a variable
unsafe(mushroom1).      % mushroom1 is a constant (result)
```

## Special Cases

### Underscore `_` = Anonymous Variable
```prolog
% I don't care about the value, just that something exists
has_property(_, poisonous).    % "something has property poisonous"
```

### Numbers
Numbers are always constants (atoms):
```prolog
age(john, 25).    % 25 is a number (constant)
age(Person, 25).  % Person is a variable, 25 is constant
```

### Strings
Strings in quotes are constants:
```prolog
name(john, 'John Smith').    % 'John Smith' is a constant
```

## Practice Questions for Students

### Question 1:
```prolog
food_type(X, mushroom) :- mushroom(X).
```
What are the variables? What are the atoms?

**Answer**: 
- Variables: `X` (capital)
- Atoms: `food_type`, `mushroom` (lowercase)

### Question 2:
```prolog
?- unsafe(Food).
```
What does this query do?

**Answer**: Finds all values that `Food` can be such that `unsafe(Food)` is true.

### Question 3:
```prolog
?- unsafe(apple1).
```
What does this query do?

**Answer**: Checks if the specific item `apple1` is unsafe. Returns `true` or `false`.

### Question 4:
What's wrong with this code?
```prolog
is_food(food) :- mushroom(food).
mushroom(mushroom1).
?- is_food(mushroom1).
```

**Answer**: `food` should be `Food` (capital). The rule `is_food(food)` only matches the literal atom `food`, not variables. The query `?- is_food(mushroom1)` will fail because `mushroom1` doesn't match `food`.

**Corrected**:
```prolog
is_food(Food) :- mushroom(Food).
mushroom(mushroom1).
?- is_food(mushroom1).
true.  % Success!
```

## Summary for Students

| Code Element | Example | Meaning |
|--------------|---------|---------|
| Capital start | `Food`, `X`, `Type` | Variable (can be anything) |
| Lowercase start | `mushroom`, `meat1` | Atom/Constant (specific value) |
| Underscore | `_` | Anonymous variable (don't care) |
| Numbers | `1`, `25`, `3.14` | Constants |
| Predicate names | `unsafe/1`, `is_food/1` | Always lowercase |

**Golden Rule**: If it can change or be different values → Capital. If it's a fixed name or value → Lowercase.

## Comparison Table: OWL vs Prolog

| Aspect | OWL/RDF | Prolog |
|--------|---------|--------|
| `Food` | Class name | Variable |
| `food` | Could be instance | Atom/Constant |
| `mushroom` | Could be instance | Atom/Constant |
| `Mushroom` | Class name | Variable |
| Capitalization | Style convention | Semantic meaning |

## Teaching Tip

When explaining to students, use this mnemonic:

**"Capital letters are Containers (variables) that hold values"**
**"Lowercase letters are Locked values (constants)"**

Or simply:

**"Big = Blank to fill in"**
**"Small = Specific value"**

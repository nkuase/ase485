# Quick Start Guide - Prolog Version

## First Time Setup

1. Navigate to the Prolog directory:
   ```bash
   cd /Users/chos5/github/nkuase/course/c_ase485/ase485/topics/ontology/code/food-prolog
   ```

2. Make scripts executable:
   ```bash
   chmod +x setup.sh run.sh
   ```

3. Run the setup script (installs SWI-Prolog):
   ```bash
   ./setup.sh
   ```
   
   **Note**: On Ubuntu, you may need to run with sudo:
   ```bash
   sudo ./setup.sh
   ```

## Running the Demo

After setup, simply run:
```bash
./run.sh
```

## What to Expect

The demonstration will show:
1. **Mushroom is UNSAFE** (because it's poisonous)
2. **Smelly meat is UNSAFE** (because it's smelly)
3. **Apple, banana, and other foods are SAFE** (no dangerous properties)

## Interactive Mode

For hands-on exploration:

```bash
# Start Prolog with the knowledge base
swipl -s food_safety.pl
```

Then try these queries:
```prolog
?- demonstrate.              % Full demo
?- unsafe(mushroom1).        % true
?- safe(apple1).             % true
?- find_all_unsafe(X).       % List all unsafe foods
?- is_food(X).               % List all foods
?- halt.                     % Exit Prolog
```

## Installation Methods

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install swi-prolog
```

### macOS with Homebrew
```bash
brew install swi-prolog
```

### macOS without Homebrew
Download from: https://www.swi-prolog.org/Download.html

### Manual Check
```bash
swipl --version
```

## Troubleshooting

### SWI-Prolog not installed
```bash
# Check installation
which swipl

# If not found, run setup
./setup.sh
```

### Permission issues
```bash
chmod +x setup.sh run.sh
```

### Setup requires sudo (Ubuntu)
```bash
sudo ./setup.sh
```

### Interactive debugging
```bash
swipl -s food_safety.pl
?- demonstrate.
```

## Comparison with OWL Example

Both examples solve the same problem but use different approaches:

| Feature | OWL (Python) | Prolog |
|---------|--------------|--------|
| Setup | Virtual env + pip | SWI-Prolog install |
| Language | RDF/Turtle/XML | Prolog clauses |
| Reasoning | OWL-RL engine | Logic programming |
| Execution | Batch script | Interactive queries |

Try both to understand different knowledge representation paradigms!

## Files

- **setup.sh**: Installs SWI-Prolog
- **run.sh**: Runs the demonstration
- **food_safety.pl**: Prolog knowledge base
- **README.md**: Comprehensive documentation
- **QUICKSTART.md**: This file

## Next Steps

After running the demo:
1. Try the interactive queries above
2. Read the full README.md
3. Compare with the OWL example
4. Modify the knowledge base to add new rules
5. Experiment with your own queries

## Common Student Queries to Try

```prolog
% Is mushroom1 unsafe?
?- unsafe(mushroom1).

% What makes mushroom1 unsafe?
?- explain_unsafe(mushroom1).

% List all food items
?- is_food(X).

% Find all unsafe foods
?- find_all_unsafe(X).

% Find all safe foods
?- find_all_safe(X).

% What type is mushroom1?
?- food_type(mushroom1, Type).

% What properties does meat1 have?
?- food_properties(meat1, Props).
```

Happy learning! 🎓

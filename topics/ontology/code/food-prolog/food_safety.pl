% ============================================
% Food Safety Knowledge Base in Prolog
% ============================================
% This demonstrates the same Domain -> Language -> Data approach
% as the OWL ontology example, but using Prolog logic programming.

% ============================================
% PROLOG NAMING CONVENTIONS
% ============================================
% In Prolog:
%   - Capital letters (Food, X, Type) = VARIABLES (can be anything)
%   - Lowercase letters (mushroom, meat1) = ATOMS/CONSTANTS (specific values)
%
% Compare to OWL where Food and Mushroom are both class names.
% In Prolog, we use:
%   - Variables (Food, X) to represent "any food item"
%   - Atoms (mushroom, meat) to represent specific types or instances

% ============================================
% LANGUAGE LEVEL: Define Concepts (Classes)
% ============================================

% Define what types of things are food
% Read as: "X is food IF X is a mushroom"
% X is a VARIABLE (can be mushroom1, mushroom2, etc.)
is_food(X) :- mushroom(X).
is_food(X) :- meat(X).
is_food(X) :- fruit(X).

% ============================================
% LANGUAGE LEVEL: Define Rules (Logic)
% ============================================

% Rule 1: If a food is poisonous, then it is unsafe
% Read as: "Food is unsafe IF Food is a food AND Food is poisonous"
% Food is a VARIABLE (represents any food item)
unsafe(Food) :- 
    is_food(Food), 
    is_poisonous(Food),
    !.  % Cut to avoid backtracking once we found it's unsafe

% Rule 2: If a food is smelly, then it is unsafe
% Read as: "Food is unsafe IF Food is a food AND Food is smelly"
unsafe(Food) :- 
    is_food(Food), 
    is_smelly(Food),
    !.

% Inverse: If not unsafe, then it's safe
% Read as: "Food is safe IF Food is a food AND Food is NOT unsafe"
safe(Food) :- 
    is_food(Food), 
    \+ unsafe(Food).

% ============================================
% DATA LEVEL: Actual Facts (Instances)
% ============================================

% Mushroom instances
% These are ATOMS (constants) - specific mushroom objects
mushroom(mushroom1).
mushroom(mushroom2).  % Safe mushroom (not poisonous)

% Meat instances
% These are ATOMS (constants) - specific meat objects
meat(meat1).
meat(meat2).         % Fresh meat (not smelly)

% Fruit instances
% These are ATOMS (constants) - specific fruit objects
fruit(apple1).
fruit(banana1).

% Properties of specific food items
% These declare which specific items have dangerous properties
is_poisonous(mushroom1).  % mushroom1 is poisonous
is_smelly(meat1).         % meat1 is smelly
% Note: mushroom2, meat2, apple1, banana1 have no dangerous properties

% ============================================
% HELPER PREDICATES FOR QUERIES
% ============================================

% Get the type/class of a food item
% Food is a VARIABLE, the output Type is also a VARIABLE
food_type(Food, mushroom) :- mushroom(Food).
food_type(Food, meat) :- meat(Food).
food_type(Food, fruit) :- fruit(Food).

% Get all properties of a food item
% Food and Properties are VARIABLES
food_properties(Food, Properties) :-
    is_food(Food),
    findall(Prop, food_property(Food, Prop), Properties).

% Helper to collect individual properties
food_property(Food, poisonous) :- is_poisonous(Food).
food_property(Food, smelly) :- is_smelly(Food).

% Explain why a food is unsafe
% Food is a VARIABLE
explain_unsafe(Food) :-
    is_food(Food),
    format('~nAnalyzing: ~w~n', [Food]),
    format('  Type: '), 
    (food_type(Food, Type) -> format('~w~n', [Type]) ; format('unknown~n')),
    format('  Properties: '),
    (food_properties(Food, Props) -> 
        (Props = [] -> format('none~n') ; format('~w~n', [Props]))
    ; 
        format('none~n')),
    format('  Status: '),
    (unsafe(Food) -> 
        format('UNSAFE~n'),
        format('  Reason: '),
        (is_poisonous(Food) -> format('it is poisonous~n') ; 
         is_smelly(Food) -> format('it is smelly~n') ;
         format('unknown~n'))
    ;
        format('SAFE~n')
    ).

% Find all unsafe foods
% UnsafeFoods is a VARIABLE that will contain the list of results
find_all_unsafe(UnsafeFoods) :-
    findall(Food, (is_food(Food), unsafe(Food)), UnsafeFoods).

% Find all safe foods
% SafeFoods is a VARIABLE that will contain the list of results
find_all_safe(SafeFoods) :-
    findall(Food, (is_food(Food), safe(Food)), SafeFoods).

% ============================================
% DEMONSTRATION QUERIES
% ============================================

% Main demonstration predicate
demonstrate :-
    write('======================================================================'), nl,
    write('FOOD SAFETY KNOWLEDGE BASE - PROLOG REASONING DEMONSTRATION'), nl,
    write('======================================================================'), nl,
    nl,
    write('This demonstrates how Prolog can reason about food safety'), nl,
    write('using the same Domain -> Language -> Data approach as OWL.'), nl,
    nl,
    write('Note: In Prolog, capital letters (Food, X) are VARIABLES,'), nl,
    write('      lowercase letters (mushroom, meat1) are ATOMS/CONSTANTS.'), nl,
    nl,
    
    write('----------------------------------------------------------------------'), nl,
    write('1. UNSAFE FOOD INSTANCES (Inferred by Prolog)'), nl,
    write('----------------------------------------------------------------------'), nl,
    find_all_unsafe(UnsafeFoods),
    (UnsafeFoods = [] -> 
        write('   (No unsafe food found)'), nl
    ; 
        forall(member(Food, UnsafeFoods), (
            format('   ✗ ~w is UNSAFE~n', [Food]),
            format('     Reason: '),
            (is_poisonous(Food) -> write('because it is poisonous') ; 
             is_smelly(Food) -> write('because it is smelly') ;
             write('unknown')),
            nl
        ))
    ),
    nl,
    
    write('----------------------------------------------------------------------'), nl,
    write('2. SAFE FOOD INSTANCES'), nl,
    write('----------------------------------------------------------------------'), nl,
    find_all_safe(SafeFoods),
    (SafeFoods = [] -> 
        write('   (No safe food found)'), nl
    ; 
        forall(member(Food, SafeFoods), 
            format('   ✓ ~w is SAFE~n', [Food])
        )
    ),
    nl,
    
    write('----------------------------------------------------------------------'), nl,
    write('3. DETAILED ANALYSIS'), nl,
    write('----------------------------------------------------------------------'), nl,
    findall(Food, is_food(Food), AllFoods),
    forall(member(Food, AllFoods), explain_unsafe(Food)),
    nl,
    
    write('----------------------------------------------------------------------'), nl,
    write('4. INFERENCE EXPLANATION'), nl,
    write('----------------------------------------------------------------------'), nl,
    write('Prolog applied these rules:'), nl,
    write('   Rule 1: IF (Food is poisonous) THEN (Food is unsafe)'), nl,
    write('   Rule 2: IF (Food is smelly) THEN (Food is unsafe)'), nl,
    nl,
    write('Applied to our data:'), nl,
    write('   • mushroom1: isPoisonous=true → INFERRED: UNSAFE'), nl,
    write('   • meat1: isSmelly=true → INFERRED: UNSAFE'), nl,
    write('   • apple1: no dangerous properties → SAFE'), nl,
    write('   • mushroom2: no dangerous properties → SAFE'), nl,
    write('   • meat2: no dangerous properties → SAFE'), nl,
    write('   • banana1: no dangerous properties → SAFE'), nl,
    nl,
    
    write('======================================================================'), nl,
    write('SUMMARY'), nl,
    write('======================================================================'), nl,
    nl,
    write('Prolog inference results:'), nl,
    format('  • Unsafe foods: ~w~n', [UnsafeFoods]),
    format('  • Safe foods: ~w~n', [SafeFoods]),
    nl,
    write('This shows how logic programming can reason about domain knowledge!'), nl,
    nl.

% ============================================
% INTERACTIVE QUERIES (for teaching)
% ============================================

% Query examples that students can try:
%
% ?- demonstrate.
%     Run the full demonstration
%
% ?- unsafe(mushroom1).
%     Check if mushroom1 is unsafe (returns: true)
%     Here mushroom1 is an ATOM (specific value)
%
% ?- unsafe(X).
%     Find what X could be that makes it unsafe
%     Here X is a VARIABLE (finds all values: mushroom1, meat1)
%
% ?- safe(apple1).
%     Check if apple1 is safe (returns: true)
%
% ?- find_all_unsafe(X).
%     Find all unsafe foods, store in X
%     X will be bound to [mushroom1, meat1]
%
% ?- find_all_safe(X).
%     Find all safe foods, store in X
%
% ?- explain_unsafe(mushroom1).
%     Get detailed explanation about mushroom1
%
% ?- is_food(X).
%     List all food items by finding all values for X
%
% ?- food_type(mushroom1, Type).
%     Find the type of mushroom1, store in Type
%     Type will be bound to 'mushroom'
%
% ?- food_properties(mushroom1, Props).
%     Find properties of mushroom1, store in Props
%     Props will be bound to [poisonous]

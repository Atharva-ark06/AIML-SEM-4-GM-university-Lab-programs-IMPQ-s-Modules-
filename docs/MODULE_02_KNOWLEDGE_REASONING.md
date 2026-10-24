# Module 2 — Knowledge representation and reasoning

## Knowledge representation
Knowledge representation encodes facts, relationships, rules, or constraints in a form a program can process.

Common forms include:
- **Propositional logic:** statements that are true or false.
- **Predicate logic:** predicates and quantified relationships.
- **Production rules:** IF condition THEN conclusion/action.
- **Semantic networks / graphs:** nodes represent concepts and edges represent relationships.

## Reasoning
Reasoning applies rules or inference procedures to known facts to derive conclusions. The quality of a conclusion depends on the representation, rule validity, and assumptions.

## AND-OR graphs
- An **OR** node can be solved by selecting one suitable alternative.
- An **AND** choice requires all listed child subproblems to be solved.
- Costs should be defined consistently; an AND branch commonly adds the cost of all required children, while an OR branch selects the least-cost alternative.

## Good practice
State the assumptions of the representation. Distinguish facts from inferred conclusions, and define how contradictory or missing information is handled.

## Revision prompts
1. Compare facts, rules, and inference.
2. Explain AND and OR alternatives with a small graph.
3. Why is a knowledge representation useful for explainable reasoning?

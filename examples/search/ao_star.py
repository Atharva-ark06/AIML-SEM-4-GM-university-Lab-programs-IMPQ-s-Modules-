"""Small acyclic AND-OR cost evaluator for classroom demonstration.

Each node maps to alternatives of (arc_cost, children, kind). An AND
alternative requires all children; an OR alternative chooses the cheapest.
This is a compact cost evaluator, not a full heuristic-revision AO* engine.
"""
from math import inf


def ao_cost(graph, node, goal, memo=None, active=None):
    """Return (minimum_cost, chosen_children) for an acyclic AND-OR graph."""
    memo = {} if memo is None else memo
    active = set() if active is None else active
    if node == goal:
        return 0, []
    if node in memo:
        return memo[node]
    if node in active:
        raise ValueError("Cycle detected; this teaching evaluator expects a DAG")
    active.add(node)
    alternatives = graph.get(node, [])
    if not alternatives:
        result = (inf, [])
    else:
        candidates = []
        for arc_cost, children, kind in alternatives:
            if kind not in {"AND", "OR"}:
                raise ValueError(f"Unknown alternative type: {kind}")
            child_results = [ao_cost(graph, child, goal, memo, active) for child in children]
            child_costs = [item[0] for item in child_results]
            if any(cost == inf for cost in child_costs):
                total = inf
            elif kind == "AND":
                total = arc_cost + sum(child_costs)
            else:
                total = arc_cost + min(child_costs, default=0)
            candidates.append((total, children))
        result = min(candidates, key=lambda item: item[0])
    active.remove(node)
    memo[node] = result
    return result


def main():
    graph = {
        "A": [(1, ["B", "C"], "AND"), (5, ["D"], "OR")],
        "B": [(2, ["G"], "OR")],
        "C": [(3, ["G"], "OR")],
        "D": [(1, ["G"], "OR")],
        "G": [],
    }
    print("Minimum estimated cost A -> G:", ao_cost(graph, "A", "G"))


if __name__ == "__main__":
    main()

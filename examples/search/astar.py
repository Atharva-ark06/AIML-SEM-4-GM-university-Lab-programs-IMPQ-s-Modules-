"""A* search on a weighted adjacency-list graph.

Graph format: node -> [(neighbor, edge_cost), ...].
The heuristic should estimate remaining cost to the goal. For guaranteed
optimality, it should be admissible; consistency is a useful stronger property.
"""
from heapq import heappop, heappush
from math import inf


def astar_path(graph, start, goal, heuristic):
    """Return (path, cost) for the least-cost path, or (None, inf)."""
    if start not in graph or goal not in graph:
        return None, inf
    frontier = [(heuristic.get(start, 0), 0, start, [start])]
    best_cost = {start: 0}
    while frontier:
        _, cost, node, path = heappop(frontier)
        if cost != best_cost.get(node):
            continue
        if node == goal:
            return path, cost
        for neighbor, edge_cost in graph.get(node, []):
            if edge_cost < 0:
                raise ValueError("A* example requires non-negative edge costs")
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, inf):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic.get(neighbor, 0)
                heappush(frontier, (priority, new_cost, neighbor, path + [neighbor]))
    return None, inf


def main():
    graph = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}
    heuristic = {"A": 3, "B": 2, "C": 1, "D": 0}
    print(astar_path(graph, "A", "D", heuristic))


if __name__ == "__main__":
    main()

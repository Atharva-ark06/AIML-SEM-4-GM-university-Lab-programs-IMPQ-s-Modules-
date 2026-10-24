"""Breadth-first search for an unweighted graph.

Run: python examples/search/bfs.py
"""
from collections import deque


def bfs_path(graph, start, goal):
    """Return a shortest path by edge count, or None if unreachable."""
    if start not in graph or goal not in graph:
        return None
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def main():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": [], "F": []}
    print("BFS path A -> F:", bfs_path(graph, "A", "F"))


if __name__ == "__main__":
    main()

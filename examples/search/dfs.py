"""Depth-first search for a graph.

Run: python examples/search/dfs.py
"""


def dfs_path(graph, start, goal):
    """Return one depth-first path, or None if the goal is unreachable."""
    if start not in graph or goal not in graph:
        return None
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None


def main():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    print("DFS path A -> E:", dfs_path(graph, "A", "E"))


if __name__ == "__main__":
    main()

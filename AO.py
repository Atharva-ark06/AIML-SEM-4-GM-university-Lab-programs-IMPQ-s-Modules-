# ============================================================
# AO* Algorithm with Graph Visualization
# ============================================================

import networkx as nx
import matplotlib.pyplot as plt

# AND-OR Graph
GRAPH = {
    'A': [(1, ['B'], 'OR'),
          (4, ['C'], 'OR')],

    'B': [(2, ['D', 'E'], 'AND')],

    'C': [(3, ['F'], 'OR')],

    'D': [(2, ['G'], 'OR')],
    'E': [(1, ['G'], 'OR')],
    'F': [(5, ['G'], 'OR')],

    'G': []
}

# Heuristic values
HEURISTIC = {
    'A': 10,
    'B': 6,
    'C': 7,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}


# ============================================================
# AO* Function
# ============================================================

def ao_star(node, cost, best, visited=None):

    if visited is None:
        visited = set()

    if node in visited:
        return cost[node]

    visited.add(node)

    # Goal node
    if node == 'G':
        cost[node] = 0
        return 0

    min_cost = float('inf')
    best_child = None

    for arc_cost, children, node_type in GRAPH[node]:

        for child in children:
            ao_star(child, cost, best, visited)

        # AND node
        if node_type == 'AND':
            total = arc_cost + sum(cost[c] for c in children)

        # OR node
        else:
            total = arc_cost + min(cost[c] for c in children)

        if total < min_cost:
            min_cost = total
            best_child = children

    cost[node] = min_cost
    best[node] = best_child

    return min_cost


# ============================================================
# Run AO*
# ============================================================

cost = {n: HEURISTIC[n] for n in HEURISTIC}
best = {}

ao_star('A', cost, best)

# Find optimal path
path = []
node = 'A'

while node != 'G':
    path.append(node)
    node = best[node][0]

path.append('G')

# ============================================================
# Output
# ============================================================

print("=" * 40)
print("AO* Algorithm")
print("=" * 40)

print("Optimal Path :", " -> ".join(path))
print("Optimal Cost :", cost['A'])

print("\nNode Costs:")
for n, c in cost.items():
    print(f"{n} : {c}")


# ============================================================
# Graph Visualization
# ============================================================

G = nx.DiGraph()

# Add edges
for parent, edges in GRAPH.items():
    for cost_val, children, node_type in edges:
        for child in children:
            G.add_edge(parent, child, label=f"{cost_val} ({node_type})")

# Layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)

# Draw edges
nx.draw_networkx_edges(G, pos, arrows=True)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight optimal path
optimal_edges = list(zip(path[:-1], path[1:]))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=optimal_edges,
    edge_color='red',
    width=3
)

plt.title("AO* Algorithm Graph")
plt.axis('off')
plt.show()
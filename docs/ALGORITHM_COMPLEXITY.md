# Algorithm complexity quick reference

Let V be the number of vertices and E the number of edges in a graph.

| Algorithm | Typical time | Notes |
|---|---:|---|
| BFS | O(V + E) | With adjacency lists; shortest path in an unweighted graph |
| DFS | O(V + E) | With adjacency lists; does not guarantee a shortest path |
| Binary heap Dijkstra | O((V + E) log V) | Non-negative edge weights |
| A* | Depends on heuristic and graph | Worst-case exponential in search depth for tree search; heuristic quality matters |
| KNN prediction | Often O(n d) per query | Brute force with n examples and d features |
| Linear regression fit | Depends on solver and dimensions | Avoid treating one complexity expression as universal |
| Decision tree inference | O(tree depth) per example | Training cost depends on data, features, and implementation |
| K-means | O(n k d i) | n points, k clusters, d dimensions, i iterations |

Complexity depends on representation, data structures, implementation, and assumptions. State those assumptions when answering an exam question.

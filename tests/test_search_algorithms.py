from examples.search.bfs import bfs_path
from examples.search.dfs import dfs_path
from examples.search.astar import astar_path
from examples.search.ao_star import ao_cost


def test_bfs_finds_shortest_unweighted_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert bfs_path(graph, "A", "D") in (["A", "B", "D"], ["A", "C", "D"])


def test_bfs_returns_none_for_missing_or_unreachable_goal():
    assert bfs_path({"A": ["B"], "B": []}, "A", "Z") is None
    assert bfs_path({"A": []}, "X", "A") is None


def test_dfs_finds_a_path():
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert dfs_path(graph, "A", "D") == ["A", "B", "D"]


def test_astar_returns_low_cost_path():
    graph = {"A": [("B", 1), ("C", 5)], "B": [("C", 1), ("D", 4)], "C": [("D", 1)], "D": []}
    path, cost = astar_path(graph, "A", "D", {"A": 3, "B": 2, "C": 1, "D": 0})
    assert path == ["A", "B", "C", "D"]
    assert cost == 3


def test_astar_rejects_negative_edge_cost():
    graph = {"A": [("B", -1)], "B": []}
    try:
        astar_path(graph, "A", "B", {})
    except ValueError as error:
        assert "non-negative" in str(error)
    else:
        raise AssertionError("Expected negative edge to be rejected")


def test_ao_cost_selects_cheapest_alternative():
    graph = {"A": [(1, ["B", "C"], "AND"), (4, ["D"], "OR")],
             "B": [(1, ["G"], "OR")], "C": [(1, ["G"], "OR")],
             "D": [(1, ["G"], "OR")], "G": []}
    cost, children = ao_cost(graph, "A", "G")
    assert cost == 3
    assert children == ["B", "C"]

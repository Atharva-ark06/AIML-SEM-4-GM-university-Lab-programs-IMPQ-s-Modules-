import pytest
from examples.ml.minmax_scaling import scale_features
from examples.ml.standardization import standardize


@pytest.mark.parametrize("function", [scale_features, standardize])
def test_scalers_reject_one_dimensional_input(function):
    with pytest.raises(ValueError):
        function([1, 2, 3])


def test_empty_graph_search_returns_none():
    from examples.search.bfs import bfs_path
    assert bfs_path({}, "A", "B") is None

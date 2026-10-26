from examples.ml.phase3.12_euclidean_distance import euclidean_distance
from examples.ml.phase3.13_manhattan_distance import manhattan_distance
from examples.ml.phase3.15_entropy import entropy
import pytest

def test_distances():
    assert euclidean_distance([1, 2], [4, 6]) == 5.0
    assert manhattan_distance([1, 2], [4, 6]) == 7

def test_entropy():
    assert entropy(["yes", "yes", "no", "no"]) == 1.0
    assert entropy([]) == 0.0

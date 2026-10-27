from importlib import import_module
import pytest
cosine=import_module("examples.ml.phase4.19_cosine_similarity").cosine_similarity
entropy=import_module("examples.ml.phase4.20_entropy").entropy
def test_cosine_orthogonal(): assert cosine([1,0],[0,1])==pytest.approx(0.0)
def test_entropy_balanced(): assert entropy(["A","A","B","B"])==pytest.approx(1.0)
import unittest
from examples.ml.advanced.euclidean_distance import euclidean
from examples.ml.advanced.cosine_similarity import cosine_similarity
from examples.ml.advanced.pearson_correlation import pearson

class DistanceTests(unittest.TestCase):
    def test_euclidean_distance(self):
        self.assertAlmostEqual(euclidean([1, 2], [4, 6]), 5.0)
    def test_cosine_orthogonal_vectors(self):
        self.assertAlmostEqual(cosine_similarity([1, 0], [0, 1]), 0.0)
    def test_perfect_correlation(self):
        self.assertAlmostEqual(pearson([1, 2, 3], [2, 4, 6]), 1.0)

if __name__ == "__main__":
    unittest.main()

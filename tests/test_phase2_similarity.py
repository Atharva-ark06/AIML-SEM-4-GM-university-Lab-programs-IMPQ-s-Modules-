import unittest
from examples.ml.advanced.euclidean_distance import euclidean
from examples.ml.advanced.cosine_similarity import cosine_similarity

class SimilarityTests(unittest.TestCase):
    def test_distance_non_negative(self):
        self.assertGreaterEqual(euclidean([1, 2], [3, 4]), 0)
    def test_cosine_identical_vectors(self):
        self.assertAlmostEqual(cosine_similarity([2, 3], [2, 3]), 1.0)
    def test_zero_vector_rejected(self):
        with self.assertRaises(ValueError):
            cosine_similarity([0, 0], [1, 1])

if __name__ == "__main__":
    unittest.main()

import unittest
from examples.ml.advanced.accuracy import accuracy
from examples.ml.advanced.precision_recall import score
from examples.ml.advanced.threshold_predictions import threshold_predictions

class ClassificationTests(unittest.TestCase):
    def test_accuracy(self):
        self.assertAlmostEqual(accuracy([1, 0, 1], [1, 1, 1]), 2 / 3)
    def test_precision_recall_keys(self):
        result = score([1, 0, 1], [1, 1, 0])
        self.assertEqual(set(result), {"precision", "recall", "f1"})
    def test_threshold_boundary_is_positive(self):
        self.assertEqual(threshold_predictions([0.49, 0.5]), [0, 1])

if __name__ == "__main__":
    unittest.main()

import unittest
from examples.ml.advanced.metrics_from_confusion import metrics_from_counts
from examples.ml.advanced.mae_rmse import regression_errors

class MetricsTests(unittest.TestCase):
    def test_confusion_metrics(self):
        result = metrics_from_counts(3, 1, 1, 5)
        self.assertAlmostEqual(result["accuracy"], 0.8)
        self.assertAlmostEqual(result["precision"], 0.75)
        self.assertAlmostEqual(result["recall"], 0.75)
    def test_empty_confusion_matrix_rejected(self):
        with self.assertRaises(ValueError):
            metrics_from_counts(0, 0, 0, 0)
    def test_regression_errors(self):
        result = regression_errors([1, 3], [2, 2])
        self.assertAlmostEqual(result["mae"], 1.0)
        self.assertAlmostEqual(result["rmse"], 1.0)

if __name__ == "__main__":
    unittest.main()

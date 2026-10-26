import unittest
from examples.ml.advanced.missing_values import missing_count, mean_impute
from examples.ml.advanced.percent_missing import missing_report

class DataQualityTests(unittest.TestCase):
    def test_missing_count_handles_none_and_nan(self):
        self.assertEqual(missing_count([1.0, None, float("nan")]), 2)
    def test_mean_imputation(self):
        self.assertEqual(mean_impute([2.0, None, 6.0]), [2.0, 4.0, 6.0])
    def test_missing_report_percent(self):
        result = missing_report({"a": [1, None, 3]})
        self.assertAlmostEqual(result["a"]["missing_percent"], 100 / 3)

if __name__ == "__main__":
    unittest.main()

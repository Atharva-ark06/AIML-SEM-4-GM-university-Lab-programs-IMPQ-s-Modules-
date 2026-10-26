import unittest
from examples.ml.advanced.minmax_scale import minmax
from examples.ml.advanced.standardize import fit_standardizer, transform

class ScalingTests(unittest.TestCase):
    def test_minmax_range(self):
        self.assertEqual(minmax([2, 4, 6]), [0.0, 0.5, 1.0])
    def test_constant_column(self):
        self.assertEqual(minmax([5, 5]), [0.0, 0.0])
    def test_standardized_mean(self):
        values = [1.0, 2.0, 3.0]
        mean, scale = fit_standardizer(values)
        result = transform(values, mean, scale)
        self.assertAlmostEqual(sum(result) / len(result), 0.0)

if __name__ == "__main__":
    unittest.main()

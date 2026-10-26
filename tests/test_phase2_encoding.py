import unittest
from examples.ml.advanced.one_hot_encode import one_hot
from examples.ml.advanced.target_split import split_target

class EncodingTests(unittest.TestCase):
    def test_one_hot_categories_are_deterministic(self):
        columns, matrix = one_hot(["blue", "red", "blue"])
        self.assertEqual(columns, ["blue", "red"])
        self.assertEqual(matrix, [[1, 0], [0, 1], [1, 0]])
    def test_unknown_category_rejected(self):
        with self.assertRaises(ValueError):
            one_hot(["green"], ["red", "blue"])
    def test_target_is_removed_from_features(self):
        x, y = split_target([{"hours": 2, "passed": 0}], "passed")
        self.assertEqual(x, [{"hours": 2}])
        self.assertEqual(y, [0])

if __name__ == "__main__":
    unittest.main()

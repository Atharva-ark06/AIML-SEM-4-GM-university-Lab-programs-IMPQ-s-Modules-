import unittest
from examples.ml.advanced.train_test_split import split

class SplitTests(unittest.TestCase):
    def test_split_is_reproducible(self):
        items = list(range(20))
        self.assertEqual(split(items, seed=7), split(items, seed=7))
    def test_split_keeps_all_items_once(self):
        items = list(range(10))
        train, test = split(items, test_fraction=0.3)
        self.assertEqual(sorted(train + test), items)
        self.assertEqual(set(train).intersection(test), set())
    def test_invalid_fraction_rejected(self):
        with self.assertRaises(ValueError):
            split([1, 2, 3], test_fraction=1.0)

if __name__ == "__main__":
    unittest.main()

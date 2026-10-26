import unittest
from examples.ml.advanced.entropy import entropy
from examples.ml.advanced.majority_baseline import fit_majority
from examples.ml.advanced.majority_vote import majority_vote

class EntropyAndBaselineTests(unittest.TestCase):
    def test_balanced_binary_entropy(self):
        self.assertAlmostEqual(entropy([0, 0, 1, 1]), 1.0)
    def test_pure_labels_have_zero_entropy(self):
        self.assertAlmostEqual(entropy(["yes", "yes"]), 0.0)
    def test_majority_baseline(self):
        self.assertEqual(fit_majority(["a", "b", "a"]), "a")
    def test_vote_tie_is_deterministic(self):
        self.assertEqual(majority_vote(["b", "a"]), "a")

if __name__ == "__main__":
    unittest.main()

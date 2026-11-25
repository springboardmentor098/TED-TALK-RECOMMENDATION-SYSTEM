"""Task 12 smoke and input validation checks for the recommender."""
from pathlib import Path
import unittest

from src.recommender import TEDRecommender, precision_recall_at_k


ROOT = Path(__file__).resolve().parents[1]


class RecommenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = TEDRecommender.from_csv(
            ROOT / "dataset" / "ted_talks_cleaned.csv",
            ROOT / "dataset" / "user_interactions.csv",
        )
        cls.user_id = str(cls.model.user_item.index[0])

    def test_content_recommendations_return_talks(self):
        results = self.model.content_recommendations(self.user_id, top_n=5)
        self.assertFalse(results.empty)
        self.assertTrue(results["talk_id"].is_unique)

    def test_collaborative_recommendations_return_talks(self):
        results = self.model.collaborative_recommendations(self.user_id, top_n=5)
        self.assertFalse(results.empty)
        self.assertTrue(results["talk_id"].is_unique)

    def test_hybrid_recommendations_are_unique_and_ranked(self):
        results = self.model.hybrid_recommendations(
            self.user_id, top_n=5, content_weight=0.25
        )
        self.assertFalse(results.empty)
        self.assertTrue(results["talk_id"].is_unique)
        self.assertTrue(results["score"].is_monotonic_decreasing)

    def test_unknown_user_returns_no_collaborative_results(self):
        results = self.model.collaborative_recommendations("UNKNOWN_USER")
        self.assertTrue(results.empty)

    def test_empty_content_seeds_return_no_results(self):
        results = self.model.content_recommendations(seed_talk_ids=[])
        self.assertTrue(results.empty)

    def test_invalid_hybrid_weight_is_rejected(self):
        with self.assertRaises(ValueError):
            self.model.hybrid_recommendations(self.user_id, content_weight=1.5)

    def test_precision_recall(self):
        precision, recall = precision_recall_at_k(
            ["talk_a", "talk_b", "talk_c"], ["talk_b"], k=3
        )
        self.assertAlmostEqual(precision, 1 / 3)
        self.assertEqual(recall, 1.0)


if __name__ == "__main__":
    unittest.main()

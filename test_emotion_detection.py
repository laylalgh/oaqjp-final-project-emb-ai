"""Verify the dominant emotion returned by Watson NLP."""
import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the five expected emotion categories."""

    def test_dominant_emotions(self):
        """Check the dominant emotion for each example."""
        examples = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for statement, expected in examples:
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()

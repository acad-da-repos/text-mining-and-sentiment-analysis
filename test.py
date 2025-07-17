import unittest
import os
import sys

from assignment import tokenize_text, analyze_sentiment

class TestTextMiningAndSentimentAnalysis(unittest.TestCase):
    def test_tokenize_text(self):
        text = "Hello, world! This is a test."
        tokens = tokenize_text(text)
        self.assertIsInstance(tokens, list)
        self.assertIn('Hello', tokens)
        self.assertIn('world', tokens)

    def test_analyze_sentiment(self):
        positive_text = "This is a great movie!"
        negative_text = "This is a terrible movie!"
        neutral_text = "This is a movie."

        self.assertGreater(analyze_sentiment(positive_text), 0)
        self.assertLess(analyze_sentiment(negative_text), 0)
        self.assertEqual(analyze_sentiment(neutral_text), 0)

if __name__ == '__main__':
    unittest.main()

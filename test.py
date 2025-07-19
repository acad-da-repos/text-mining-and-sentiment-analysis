import unittest
import os
import sys

from assignment import tokenize_text, analyze_sentiment

class TestTextMiningAndSentimentAnalysis(unittest.TestCase):
    def test_tokenize_text(self):
        text = "Hello, world! This is a test."
        tokens = tokenize_text(text)
        self.assertIsInstance(tokens, list)
        # Check that words are properly tokenized (case may vary)
        token_text = " ".join(tokens).lower()
        self.assertIn('hello', token_text)
        self.assertIn('world', token_text)
        self.assertIn('this', token_text)
        self.assertIn('is', token_text)
        self.assertIn('a', token_text)
        self.assertIn('test', token_text)

    def test_analyze_sentiment(self):
        positive_text = "This is a great movie!"
        negative_text = "This is a terrible movie!"
        neutral_text = "This is a movie."

        # Test that sentiment analysis returns numeric values
        positive_score = analyze_sentiment(positive_text)
        negative_score = analyze_sentiment(negative_text)
        neutral_score = analyze_sentiment(neutral_text)
        
        self.assertIsInstance(positive_score, (int, float))
        self.assertIsInstance(negative_score, (int, float))
        self.assertIsInstance(neutral_score, (int, float))
        
        # Test that positive text has higher score than negative text
        self.assertGreater(positive_score, negative_score)

if __name__ == '__main__':
    unittest.main()

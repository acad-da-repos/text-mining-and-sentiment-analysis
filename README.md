
# Text Mining and Sentiment Analysis Assignment

## Problem Description

In this assignment, you will perform basic text mining and sentiment analysis using built-in Python libraries. This is a crucial skill for extracting insights from unstructured text data without relying on external NLP libraries.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find two function definitions: `tokenize_text(text)` and `analyze_sentiment(text)`.
3.  Your task is to implement these functions:
    *   `tokenize_text`: Tokenize the input `text` into words. You can use string splitting, regular expressions, or other built-in Python methods to separate words and remove punctuation.
    *   `analyze_sentiment`: Analyze the sentiment of the input `text` and return a sentiment score. You can implement a simple approach using predefined lists of positive and negative words, or use other techniques like counting sentiment words.

## Requirements

- Use only built-in Python libraries (no external packages like NLTK, spaCy, etc.)
- The `tokenize_text` function should return a list of words
- The `analyze_sentiment` function should return a numeric score (positive for positive sentiment, negative for negative sentiment, zero for neutral)

## Further Exploration (Optional)

*   Explore other text preprocessing techniques, such as stemming, lemmatization, and stop-word removal using built-in methods.
*   Investigate more sophisticated sentiment analysis approaches like TF-IDF or word embeddings.
*   How can you visualize the sentiment distribution in a corpus of text?
*   Consider implementing case-insensitive matching and handling contractions.

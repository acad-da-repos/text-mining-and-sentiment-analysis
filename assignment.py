
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

def _download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('sentiment/vader_lexicon')
    except LookupError:
        nltk.download('vader_lexicon', quiet=True)

_download_nltk_data()

def tokenize_text(text):
  """
  Tokenizes the input text into words.

  Args:
    text: A string of text.

  Returns:
    A list of words.
  """

  return word_tokenize(text)

def analyze_sentiment(text):
  """
  Analyzes the sentiment of the input text.

  Args:
    text: A string of text.

  Returns:
    The compound sentiment score.
  """

  analyzer = SentimentIntensityAnalyzer()
  vs = analyzer.polarity_scores(text)
  return vs['compound']

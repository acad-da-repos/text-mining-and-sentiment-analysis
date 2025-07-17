
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')
try:
    nltk.data.find('sentiment/vader_lexicon')
except nltk.downloader.DownloadError:
    nltk.download('vader_lexicon')

def tokenize_text(text):
  """
  Tokenizes the input text into words.

  Args:
    text: A string of text.

  Returns:
    A list of words.
  """

  # Your code here
  return None

def analyze_sentiment(text):
  """
  Analyzes the sentiment of the input text.

  Args:
    text: A string of text.

  Returns:
    The compound sentiment score.
  """

  # Your code here
  return None

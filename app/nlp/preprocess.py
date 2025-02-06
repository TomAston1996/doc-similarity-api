"""
Text Preprocessor
Author: Tom Aston
"""

import re
import string
from functools import reduce

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")


class TextPreprocessor:
    """
    class to preprocess text for NLP

    Preproccessing includes:
        - lower casing
        - removing punctuation
        - removing digits and words containing digits
        - remove stopwords
        - stemming i.e. walking -> walk
        - lemmatization i.e. running -> run, ate -> eat
        - remove whitespace
    """

    def __init__(self):
        """
        constructor for TextPreprocessor
        """
        self.stemmer = PorterStemmer()

    def get_cleaned_text(self, text: str) -> str:
        """
        public facing method for cleaning text strings for NLP models
        """
        preprocess_steps = [
            self._lowercase_text,
            self._remove_punctuation,
            self._remove_digits,
            self._remove_stop_words,
            self._remove_whitespace,
            self._lemmatize_text,
        ]
        return reduce(lambda t, step: step(t), preprocess_steps, text)

    def _lowercase_text(self, text: str) -> str:
        """
        return text in all lower case
        """
        return text.lower()

    def _remove_punctuation(self, text: str) -> str:
        """
        remove punctuation from text
        """
        table = str.maketrans({key: None for key in string.punctuation})
        return text.translate(table)

    def _remove_digits(self, text: str) -> str:
        """
        remove digits and words containing digits
        """
        return re.sub(r"\w*\d\w*", "", text).strip()

    def _remove_stop_words(self, text: str) -> str:
        """
        remove stopwords from text inc. like 'the', 'and', 'or'
        """
        stop_words = set(stopwords.words("english"))
        return " ".join([word for word in str(text).split() if word not in stop_words])

    def _remove_whitespace(self, text: str) -> str:
        """
        remove whitespace from text
        """
        return " ".join(text.split())

    def _lemmatize_text(self, text: str) -> str:
        """
        lemmatize text
        i.e. running -> run, ate -> eat
        """
        return " ".join([self.stemmer.stem(word) for word in text.split()])


if __name__ == "__main__":
    text_preprocessor = TextPreprocessor()
    test_string = "Hello my name is John"
    print(text_preprocessor.get_cleaned_text(test_string))
    test_string = "hello, how are you?"
    print(text_preprocessor.get_cleaned_text(test_string))
    test_string = "hello i am 20 years old and my name is nine9"
    print(text_preprocessor.get_cleaned_text(test_string))
    test_string = "i am at the meeting call"
    print(text_preprocessor.get_cleaned_text(test_string))
    test_string = "  hello  how  are  you  "
    print(text_preprocessor.get_cleaned_text(test_string))
    test_string = "running eating"
    print(text_preprocessor.get_cleaned_text(test_string))

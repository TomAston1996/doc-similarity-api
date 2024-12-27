'''
Text Preprocessor
Author: Tom Aston
'''
#inbuild dependencies
import string
import re

#external dependencies
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

class TextPreprocessor:
    '''
    class to preprocess text for NLP

    Preproccessing includes:
        - lower casing
        - removing punctuation
        - removing digits and words containing digits
        - remove stopwords
        - stemming i.e. walking -> walk
        - lemmatization i.e. running -> run, ate -> eat
        - remove whitespace
    '''

    def get_cleaned_text(self, text: str) -> str:
        '''
        public facing method for cleaning text strings for NLP models
        '''
        text = self._lowercase_text(text)
        text = self._remove_punctuation(text)
        text = self._remove_digits(text)
        text = self._remove_stop_words(text)
        return text
        

    def _lowercase_text(self, text: str) -> str:
        '''
        return text in all lower case
        '''
        return text.lower()


    def _remove_punctuation(self, text: str) -> str:
        '''
        remove punctuation from text
        '''
        table = str.maketrans({key: None for key in string.punctuation})
        return text.translate(table)
    

    def _remove_digits(self, text: str) -> str:
        '''
        remove digits and words containing digits
        '''
        return re.sub(r'\w*\d\w*', '', text).strip()

        
    def _remove_stop_words(self, text: str) -> str:
        '''
        remove stopwords from text inc. like 'the', 'and', 'or'
        '''
        stop_words = set(stopwords.words('english'))
        return ' '.join([word for word in str(text).split() if word not in stop_words])


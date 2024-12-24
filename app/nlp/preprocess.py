'''
Text Preprocessor
Author: Tom Aston
'''
import string

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
        
        text = self.__lowercase_text(text)
        text = self.__remove_punctuation(text)
        return text
        

    def __lowercase_text(self, text: str) -> str:
        '''
        return text in all lower case
        '''
        return text.lower()
    
    def __remove_punctuation(self, text: str) -> str:
        '''
        remove punctuation from text
        '''
        return text
        
    def __remove_stop_words():
        '''
        remove stopwords from text inc. like 'the', 'and', 'or'
        '''
        pass


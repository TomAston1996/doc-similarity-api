'''
Similarity Calculator
Author: Tom Aston
'''

#local dependencies
from preprocess import TextPreprocessor

#external dependencies
import spacy


class SimilarityCalculator:
    '''
    class to calculate similarity between two text strings
    '''
    def __init__(self, preprocessor: TextPreprocessor) -> None:
        '''
        constructor for SimilarityCalculator
        '''
        self.preprocessor = preprocessor
        self.nlp = spacy.load('en_core_web_md')

    def calculate_similarity(self, text1: str, text2: str) -> float:
        '''
        calculate the similarity between two text strings
        '''
        cleaned_text1 = self.preprocessor.get_cleaned_text(text1)
        cleaned_text2 = self.preprocessor.get_cleaned_text(text2)

        return self._calculate_cosine_similarity(cleaned_text1, cleaned_text2)
    
    def _calculate_cosine_similarity(self, text1: str, text2: str) -> float:
        '''
        calculate the cosine similarity between two text strings
        '''
        vector1 = self.nlp(text1)
        vector2 = self.nlp(text2)

        return vector1.similarity(vector2)
    

if __name__ == '__main__':
    text1 = 'I am a cat'
    text2 = 'I am a dog'

    preprocessor = TextPreprocessor()
    similarity_calculator = SimilarityCalculator(preprocessor)
    
    
    similarity1 = similarity_calculator.calculate_similarity(text1, text2)
    
    text3 = 'There was a fire in one of the electrical cupboards'
    text4 = 'Electrical cabinet found smoking'

    similarity2 = similarity_calculator.calculate_similarity(text3, text4)

    print(similarity1)
    print(similarity2)
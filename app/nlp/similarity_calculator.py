'''
Similarity Calculator
Author: Tom Aston
'''


#local dependencies
from app.nlp.preprocess import TextPreprocessor

#external dependencies
from nltk.tokenize import word_tokenize 


class SimilarityCalculator:
    '''
    class to calculate similarity between two text strings
    '''

    def __init__(self, preprocessor: TextPreprocessor) -> None:
        '''
        constructor for SimilarityCalculator
        '''
        self.preprocessor = preprocessor

    def calculate_similarity(self, text1: str, text2: str) -> float:
        '''
        calculate the similarity between two text strings
        '''
        cleaned_text1 = self.preprocessor.get_cleaned_text(text1)
        cleaned_text2 = self.preprocessor.get_cleaned_text(text2)

        return self._calculate_jaccard_similarity(cleaned_text1, cleaned_text2)
    

if __name__ == '__main__':
    text1 = 'I am a cat'
    text2 = 'I am a dog'

    preprocessor = TextPreprocessor()
    similarity_calculator = SimilarityCalculator(preprocessor)
    similarity = similarity_calculator.calculate_similarity(text1, text2)
    print(similarity)
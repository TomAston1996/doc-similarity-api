
from app.nlp.preprocess import TextPreprocessor

class TestPreprocessorSuite:
    '''
    test suite for text preprocessor
    '''
    def test_text_is_converted_to_lower_case(self) -> None:
        '''
        ensure text is converted to lower case       
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'Hello my name is John'
        actual_cleaned_text = text_preprocessor.get_cleaned_text(test_string)
        expected_cleaned_text = 'hello my name is john'
        assert actual_cleaned_text == expected_cleaned_text


    def test_punctuation_is_removed(self) -> None:
        '''
        ensure all punctuation removed from text
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'hello, how are you?'
        actual_cleaned_text = text_preprocessor.get_cleaned_text(test_string)
        expected_cleaned_text = 'hello how are you'
        assert actual_cleaned_text == expected_cleaned_text


    def test_digits_are_removed(self) -> None:
        '''
        ensure all digits and words containign digits are removed
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'hello i am 20 years old and my name is nine9'
        actual_cleaned_text = text_preprocessor.get_cleaned_text(test_string)
        expected_cleaned_text = 'hello i am  years old and my name is'
        assert actual_cleaned_text == expected_cleaned_text

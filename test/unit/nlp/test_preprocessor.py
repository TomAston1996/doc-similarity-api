
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
        actual_cleaned_text = text_preprocessor._lowercase_text(test_string)
        expected_cleaned_text = 'hello my name is john'
        assert actual_cleaned_text == expected_cleaned_text


    def test_punctuation_is_removed(self) -> None:
        '''
        ensure all punctuation removed from text
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'hello, how are you?'
        actual_cleaned_text = text_preprocessor._remove_punctuation(test_string)
        expected_cleaned_text = 'hello how are you'
        assert actual_cleaned_text == expected_cleaned_text


    def test_digits_are_removed(self) -> None:
        '''
        ensure all digits and words containign digits are removed
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'hello i am 20 years old and my name is nine9'
        actual_cleaned_text = text_preprocessor._remove_digits(test_string)
        expected_cleaned_text = 'hello i am  years old and my name is'
        assert actual_cleaned_text == expected_cleaned_text


    def test_stop_words_are_removed(self) -> None:
        '''
        ensure all stopwords are removed
        '''
        text_preprocessor = TextPreprocessor()
        test_string = 'i am at the meeting call'
        actual_cleaned_text = text_preprocessor._remove_stop_words(test_string)
        expected_cleaned_text = 'meeting call'
        assert actual_cleaned_text == expected_cleaned_text


    def test_remove_whitespace(self) -> None:
        '''
        ensure all whitespace is removed
        '''
        text_preprocessor = TextPreprocessor()
        test_string = '  hello  how  are  you  '
        actual_cleaned_text = text_preprocessor._remove_whitespace(test_string)
        expected_cleaned_text = 'hello how are you'
        assert actual_cleaned_text == expected_cleaned_text

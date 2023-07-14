'''
This a file to translate to english to french and vice versa
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
     Translate english to french
    """
    translator = MyMemoryTranslator(source='en-GB', target='fr-CA')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
     Translate french to english
    """
    translator = MyMemoryTranslator(source='fr-CA', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text

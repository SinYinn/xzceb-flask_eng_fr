import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        expected_translation = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_translation)
        self.assertNotEqual(translated_text, "Ni Hao")

    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_translation = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_translation)
        self.assertNotEqual(translated_text, "Hey")

if __name__ == '__main__':
    unittest.main()
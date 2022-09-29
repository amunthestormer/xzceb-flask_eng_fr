import unittest
import translator

class testEngToFr(unittest.TestCase):
    def test_input(self):
        self.assertEqual(translator.english_to_french('Hello'), "Bonjour")
        self.assertEqual(translator.english_to_french(None), None)

class testFrToEng(unittest.TestCase):
    def test_input(self):
        self.assertEqual(translator.french_to_english('Bonjour'), "Hello")
        self.assertEqual(translator.french_to_english(None), None)

unittest.main()
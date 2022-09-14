import unittest
import translator

class testEngToFr(unittest.TestCase):
    def test_input(self):
        self.assertEqual(translator.englishToFrench(None), None)
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")

class testFrToEng(unittest.TestCase):
    def test_input(self):
        self.assertEqual(translator.frenchToEnglish(None), None)
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")

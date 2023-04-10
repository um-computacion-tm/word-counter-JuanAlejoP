import unittest
from wordcounter import wordcounter

class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = wordcounter('Hola mundo.')
        self.assertEqual(result, {'hola': 1})
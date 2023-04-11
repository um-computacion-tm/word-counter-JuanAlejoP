import unittest
from wordcounter import wordcounter

class TestWordCounter(unittest.TestCase):
    
    def test_empty(self):
        result = wordcounter('')
        self.assertEqual(result, 0)
        
    def test_1word(self):
        result = wordcounter('Hola')
        self.assertEqual(result, 1)
        
    def test_2words(self):
        result = wordcounter('Hola mundo')
        self.assertEqual(result, 2)
        
    def test_wordsAndPunctuation(self):
        result = wordcounter('¡Hola, mundo!')
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
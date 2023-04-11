import unittest
from WordCount import count_words

class TestCountLetters(unittest.TestCase):

    def test_uno(self):
        result = count_words('hola como')
        self.assertEqual(result, {'hola': 1, 'como' : 1})

    def test_dos(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})

    def test_tres(self):
        result = count_words('hola como estas Hola')
        self.assertEqual(result, {'hola': 2, 'como' : 1, 'estas' : 1})
    def test_cuatro(self):
        result = count_words('hola Hola holA HOLA')
        self.assertEqual(result, {'hola': 4})

if __name__ == '__main__':
    unittest.main()
import unittest
from WordCount import count_words

class TestCountLetters(unittest.TestCase):

    def test_uno(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})


if __name__ == '__main__':
    unittest.main()
# coding: utf-8
import unittest
from s_aes.key_expansion_function import complex_function


class TestComplexFunction(unittest.TestCase):

    def test_complex_function(self):
        round_constant = "10000000"
        word = "01010101"
        output = int("10010001", 2)
        self.assertEqual(complex_function(word, round_constant), output)


if __name__ == '__main__':
    unittest.main()
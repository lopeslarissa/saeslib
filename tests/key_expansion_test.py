# coding: utf-8
import unittest
from s_aes.key_expansion_function import key_expansion, key_format


class TestKeyExpansion(unittest.TestCase):

    def test_key_expansion(self):
        enter_key = 11605
        output = ["00101101",
                  "01010101",
                  "10111100",
                  "11101001",
                  "10100011",
                  "01001010"]
        self.assertEqual(key_expansion(key_format(enter_key)), output)


if __name__ == '__main__':
    unittest.main()

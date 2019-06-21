# coding: utf-8
import unittest
from s_aes.cipher import cipher, cipher_rounds, decipher_rounds
from s_aes.constants import ROUNDS_RANGE_CIPHER, ROUNDS_RANGE_DECIPHER


class TestCipher(unittest.TestCase):

    def setUp(self):
        self.key = 19189

    def test_cipher_16bits(self):
        plain_text = 55080
        output = 9452
        self.assertEqual(cipher(plain_text, self.key, ROUNDS_RANGE_CIPHER, cipher_rounds), output)

    def test_cipher_more_16bits(self):
        plain_text = 28201390
        output = 2429632728
        self.assertEqual(cipher(plain_text, self.key, ROUNDS_RANGE_CIPHER, cipher_rounds), output)

    def test_cipher_16bits_inverse(self):
        plain_text = cipher(9452, self.key, ROUNDS_RANGE_CIPHER, cipher_rounds)
        output = 9452
        self.assertEqual(cipher(plain_text, self.key, ROUNDS_RANGE_DECIPHER, decipher_rounds), output)

    def test_cipher_more_16bits_inverse(self):
        plain_text = cipher(2429632728, self.key, ROUNDS_RANGE_CIPHER, cipher_rounds)
        output = 2429632728
        self.assertEqual(cipher(plain_text, self.key, ROUNDS_RANGE_DECIPHER, decipher_rounds), output)


if __name__ == '__main__':
    unittest.main()
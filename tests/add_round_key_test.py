# coding: utf-8
import unittest
from s_aes.add_key_round_function import add_round_key
from s_aes.key_expansion_function import key_format, key_expansion


class TestAddRoundKey(unittest.TestCase):

    def setUp(self):
        self.round = 0
        self.word_vector = key_expansion(key_format(11605))

    def test_add_round_key(self):
        input_state = ['0001', '0100', '0111', '1001']
        output_state = ['0011', '0001', '1010', '1100']
        self.assertEqual(add_round_key(self.round, input_state, self.word_vector), output_state)

    def test_add_round_key_inverse(self):
        output_state = ['0001', '0100', '0111', '1001']
        input_state = ['0011', '0001', '1010', '1100']
        self.assertEqual(add_round_key(self.round, input_state, self.word_vector), output_state)


if __name__ == '__main__':
    unittest.main()

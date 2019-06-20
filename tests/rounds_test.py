# coding: utf-8
import unittest
from s_aes.add_key_round_function import add_round_key
from s_aes.cipher_function import cipher_rounds, decipher_rounds
from s_aes.constants import TRANSFORMATION_MATRIX, S_BOX, TRANSFORMATION_MATRIX_INVERSE, S_BOX_I
from s_aes.key_expansion_function import key_expansion, key_format
from s_aes.mix_column_function import mix_column
from s_aes.shift_row_function import shift_row
from s_aes.substitute_sbox_function import substitute_sbox


class TestRounds(unittest.TestCase):

    def setUp(self):
        self.key_array = key_expansion(key_format(19189))
        self.input = ['0001', '0100', '0111', '1001']

    def test_cipher_round_0(self):
        state = add_round_key(0, self.input, self.key_array)
        self.assertEqual(cipher_rounds(0, self.key_array, self.input), state)

    def test_cipher_round_1(self):
        substitution = substitute_sbox(self.input, S_BOX)
        shift = shift_row(substitution)
        mix = mix_column(shift, TRANSFORMATION_MATRIX)
        add_key = add_round_key(1, mix, self.key_array)
        state = add_key
        self.assertEqual(cipher_rounds(1, self.key_array, self.input), state)

    def test_cipher_round_2(self):
        substitution = substitute_sbox(self.input, S_BOX)
        shift = shift_row(substitution)
        add_key = add_round_key(2, shift, self.key_array)
        state = add_key
        self.assertEqual(cipher_rounds(2, self.key_array, self.input), state)

    def test_decipher_round_0(self):
        state = add_round_key(2, self.input, self.key_array)
        self.assertEqual(decipher_rounds(2, self.key_array, self.input), state)

    def test_decipher_round_1(self):
        shift = shift_row(self.input)
        substitution = substitute_sbox(shift, S_BOX_I)
        add_key = add_round_key(1, substitution, self.key_array)
        mix = mix_column(add_key, TRANSFORMATION_MATRIX_INVERSE)
        state = mix
        self.assertEqual(decipher_rounds(1, self.key_array, self.input), state)

    def test_decipher_round_2(self):
        shift = shift_row(self.input)
        substitution = substitute_sbox(shift, S_BOX_I)
        add_key = add_round_key(0, substitution, self.key_array)
        state = add_key
        self.assertEqual(decipher_rounds(0, self.key_array, self.input), state)


if __name__ == '__main__':
    unittest.main()
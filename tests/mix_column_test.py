# coding: utf-8
import unittest
from s_aes.mix_column_function import mix_column
from s_aes.constants import TRANSFORMATION_MATRIX, TRANSFORMATION_MATRIX_INVERSE


class TestMixColumn(unittest.TestCase):

    def test_mix_column_case1(self):
        input_state = ['0110', '0100', '1100', '0000']
        output_state = ['0011', '0100', '0111', '0011']
        self.assertEqual(mix_column(input_state, TRANSFORMATION_MATRIX), output_state)

    def test_mix_column_case2(self):
        input_state = ['0010', '1110', '1110', '1110']
        output_state = ['1111', '0011', '0110', '0011']
        self.assertEqual(mix_column(input_state, TRANSFORMATION_MATRIX), output_state)

    def test_mix_column_case1_inverse(self):
        output_state = ['0110', '0100', '1100', '0000']
        input_state = ['0011', '0100', '0111', '0011']
        self.assertEqual(mix_column(input_state, TRANSFORMATION_MATRIX_INVERSE), output_state)

    def test_mix_column_case2_inverse(self):
        output_state = ['0010', '1110', '1110', '1110']
        input_state = ['1111', '0011', '0110', '0011']
        self.assertEqual(mix_column(input_state, TRANSFORMATION_MATRIX_INVERSE), output_state)


if __name__ == '__main__':
    unittest.main()

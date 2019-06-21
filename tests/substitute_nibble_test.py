# coding: utf-8
import unittest
from s_aes.substitute_sbox import substitute_sbox
from s_aes.constants import S_BOX, S_BOX_I


class TestSubstituteNibble(unittest.TestCase):

    def test_substitute_nibble_case1(self):
        input_state = ["1000", "0001", "1010", "1100"]
        output_state = ["0110", "0100", "0000", "1100"]
        self.assertEqual(substitute_sbox(input_state, S_BOX), output_state)

    def test_substitute_nibble_case2(self):
        input_state = ["0011", "1100", "0101", "1010"]
        output_state = ["1011", "1100", "0001", "0000"]
        self.assertEqual(substitute_sbox(input_state, S_BOX), output_state)

    def test_substitute_nibble_case1_inverse(self):
        output_state = ["1000", "0001", "1010", "1100"]
        input_state = ["0110", "0100", "0000", "1100"]
        self.assertEqual(substitute_sbox(input_state, S_BOX_I), output_state)

    def test_substitute_nibble_case2_inverse(self):
        output_state = ["0011", "1100", "0101", "1010"]
        input_state = ["1011", "1100", "0001", "0000"]
        self.assertEqual(substitute_sbox(input_state, S_BOX_I), output_state)


if __name__ == '__main__':
    unittest.main()
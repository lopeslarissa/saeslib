# coding: utf-8
import unittest
from s_aes.shift_row_function import shift_row


class TestShiftRow(unittest.TestCase):

    def test_shift_row(self):
        input_state = ["0110", "0100", "0000", "1100"]
        output_state = ["0110", "0100", "1100", "0000"]
        self.assertEqual(shift_row(input_state), output_state)

    def test_shift_row_inverse(self):
        output_state = ["0110", "0100", "0000", "1100"]
        input_state = ["0110", "0100", "1100", "0000"]
        self.assertEqual(shift_row(input_state), output_state)


if __name__ == '__main__':
    unittest.main()
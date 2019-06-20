# coding: utf-8
import unittest
from s_aes.cipher_function import state_to_text


class TestStateToText(unittest.TestCase):

    def test_state_text(self):
        state = ["0111", "1010", "0100", "0110"]
        output = "0111010010100110"
        self.assertEqual(state_to_text(state), output)


if __name__ == '__main__':
    unittest.main()
# coding: utf-8
import unittest
from s_aes.cipher import text_to_state


class TestTextToState(unittest.TestCase):

    def test_state_vector(self):
        text = 123456789
        output = [['0000', '0101', '0111', '1011'], ['1100', '0001', '1101', '0101']]
        self.assertEqual(text_to_state(text), output)


if __name__ == '__main__':
    unittest.main()

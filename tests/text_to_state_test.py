# coding: utf-8
import unittest
from s_aes.cipher_function import text_to_state


class TestTextToState(unittest.TestCase):

    def test_state_vector(self):
        text = 123456789
        output = [['0000', '0101', '0111', '1011'], ['1100', '0001', '1101', '0101']]
        self.assertEqual(text_to_state(text), output)

    # def test_state_vector_string(self):
    #     text = "lara"
    #     output = [['0110', '0110', '1100', '0001'], ['0111', '0110', '0010', '0001']]
    #     self.assertEqual(text_to_state(text), output)


if __name__ == '__main__':
    unittest.main()
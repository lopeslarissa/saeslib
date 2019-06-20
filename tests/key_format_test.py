# coding: utf-8
import unittest
from s_aes.key_expansion_function import key_format


class TestKeyFormat(unittest.TestCase):

    def test_key_format_sucess(self):
        key = 19189
        output = bin(key)[2:].zfill(16)
        self.assertEqual(key_format(key), output)

    def test_key_format_fail(self):
        key = 116055
        self.assertRaises(Exception, key_format, key)


if __name__ == '__main__':
    unittest.main()

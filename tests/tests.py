# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from tests.add_round_key_test import TestAddRoundKey
from tests.cipher_test import TestCipher
from tests.complex_function_test import TestComplexFunction
from tests.key_expansion_test import TestKeyExpansion
from tests.key_format_test import TestKeyFormat
from tests.mix_column_test import TestMixColumn
from tests.rounds_test import TestRounds
from tests.shift_row_test import TestShiftRow
from tests.state_to_text_test import TestStateToText
from tests.substitute_nibble_test import TestSubstituteNibble
from tests.text_to_state_test import TestTextToState


def main():
    suite_add_key = unittest.TestLoader().loadTestsFromTestCase(TestAddRoundKey)
    suite_cipher = unittest.TestLoader().loadTestsFromTestCase(TestCipher)
    suite_complex_function = unittest.TestLoader().loadTestsFromTestCase(TestComplexFunction)
    suite_key_expansion = unittest.TestLoader().loadTestsFromTestCase(TestKeyExpansion)
    suite_key_format = unittest.TestLoader().loadTestsFromTestCase(TestKeyFormat)
    suite_mix_column = unittest.TestLoader().loadTestsFromTestCase(TestMixColumn)
    suite_rounds = unittest.TestLoader().loadTestsFromTestCase(TestRounds)
    suite_shift_row = unittest.TestLoader().loadTestsFromTestCase(TestShiftRow)
    suite_state_to_text = unittest.TestLoader().loadTestsFromTestCase(TestStateToText)
    suite_substitute_nibble = unittest.TestLoader().loadTestsFromTestCase(TestSubstituteNibble)
    suite_text_to_state = unittest.TestLoader().loadTestsFromTestCase(TestTextToState)
    suite_tests = unittest.TestSuite(
        [suite_add_key,
         suite_cipher,
         suite_complex_function,
         suite_key_expansion,
         suite_key_format,
         suite_mix_column,
         suite_rounds,
         suite_shift_row,
         suite_state_to_text,
         suite_substitute_nibble,
         suite_text_to_state])
    unittest.TextTestRunner(verbosity=2).run(suite_tests)


if __name__ == '__main__': 
    main()   

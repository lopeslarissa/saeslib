# coding: utf-8
import numpy as np
from s_aes.constants import WORD_SIZE, NIBBLE_SIZE, S_BOX, ROUND_CONSTANT_ARRAY, KEY_SIZE
from s_aes.substitute_sbox_function import substitute_sbox


def key_expansion(key):
    word_0 = key[:WORD_SIZE]
    word_1 = key[WORD_SIZE:WORD_SIZE * 2]
    word_array = [word_0, word_1]
    other_words = range(2, 6)
    for i in other_words:
        previous_word = word_array[i - 1]
        if i % 2 == 0:
            previous_word = set_previous_word(i, previous_word)
        set_word_array(i, previous_word, word_array)
    return word_array


def complex_function(word, round_constant):
    nibble_0 = word[:NIBBLE_SIZE]
    nibble_1 = word[NIBBLE_SIZE:]
    shift_nibble = [nibble_1, nibble_0]
    substitute_nibble_array = substitute_sbox(shift_nibble, S_BOX)
    word = "".join(substitute_nibble_array)
    return np.bitwise_xor(int(word, 2), int(round_constant, 2))


def set_previous_word(i, previous_word):
    round_constant = ROUND_CONSTANT_ARRAY[(i // 2) - 1]
    previous_word = complex_function(previous_word, round_constant)
    previous_word = np.binary_repr(previous_word)
    return previous_word


def set_word_array(i, temp, word_array):
    previous = int(word_array[i - 2], 2)
    temp_word = int(temp, 2)
    word = np.bitwise_xor(previous, temp_word)
    bynary_word = np.binary_repr(word, WORD_SIZE)
    word_array.append(bynary_word)
    return word_array


def key_format(key):
    if isinstance(key, int):
        key = np.binary_repr(key, KEY_SIZE)
        if len(key) > KEY_SIZE:
            raise Exception("A chave precisa ter 16 bits")
        return key
    else:
        raise Exception("A chave deve conter apenas números")


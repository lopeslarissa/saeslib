# coding: utf-8
import numpy as np
from s_aes.add_key_round_function import add_round_key
from s_aes.constants import TRANSFORMATION_MATRIX_INVERSE, S_BOX_I, N_ROUNDS, TRANSFORMATION_MATRIX, S_BOX, BLOCK_SIZE
from s_aes.key_expansion_function import key_expansion, key_format
from s_aes.mix_column_function import mix_column
from s_aes.shift_row_function import shift_row
from s_aes.substitute_sbox_function import substitute_sbox
from s_aes.utils import distribute_array


def cipher(input_text, input_key, rounds_range, rounds_function):
    key_array = key_expansion(key_format(input_key))
    state_array = text_to_state(input_text)
    cipher_text = []
    for state in state_array:
        for i in rounds_range:
            state = rounds_function(i, key_array, state)
        cipher_text.insert(0, state_to_text(state))
    return int("".join(cipher_text), 2)


def cipher_rounds(r, key_array, state):
    if r > 0:
        state = substitute_sbox(state, S_BOX)
        state = shift_row(state)
    if 0 < r < (N_ROUNDS - 1):
        state = mix_column(state, TRANSFORMATION_MATRIX)
    state = add_round_key(r, state, key_array)
    return state


def decipher_rounds(r, key_array, state):
    if r < (N_ROUNDS - 1):
        state = shift_row(state)
        state = substitute_sbox(state, S_BOX_I)
    state = add_round_key(r, state, key_array)
    if 0 < r < (N_ROUNDS - 1):
        state = mix_column(state, TRANSFORMATION_MATRIX_INVERSE)
    return state


def text_to_state(plain_text):
    if isinstance(plain_text, int):
        state_array = []
        binary_text = np.binary_repr(plain_text)
        size = len(binary_text)
        while size > 0:
            text = extract_block(binary_text, size)
            state_array.insert(0, distribute_array(text))
            size -= BLOCK_SIZE
        return state_array
    else:
        raise Exception("O texto deve conter apenas números")


def extract_block(binary_text, part):
    if part - BLOCK_SIZE < 0:
        text = binary_text[:part].zfill(BLOCK_SIZE)
    else:
        text = binary_text[part - BLOCK_SIZE:part]
    return text


def state_to_text(state):
    temp_nibble = state[2]
    state[2] = state[1]
    state[1] = temp_nibble
    return "".join(state)
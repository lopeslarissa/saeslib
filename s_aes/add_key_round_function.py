# coding: utf-8
import numpy as np
from s_aes.utils import distribute_array, elements_to_int, elements_to_binary


def add_round_key(round, state, key_array):
    key = key_array[2 * round] + key_array[2 * round + 1]
    round_key = distribute_array(key)
    state = np.bitwise_xor(elements_to_int(state), elements_to_int(round_key))
    return elements_to_binary(state)

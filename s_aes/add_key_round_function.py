# coding: utf-8
import numpy as np
from s_aes.utils import distribute_array, elements_to_int, elements_to_binary


def add_round_key(round, state, word_array):
    """
    XOR bit a bit entre a matriz estado e a chave da rodada

    :param round: número da rodada
    :param state: matriz estado
    :param word_array: array contendo todas as palavras que geram as chaves
    :return: matriz estado com elementos em representação binária
    """
    key = word_array[2 * round] + word_array[2 * round + 1]
    round_key = distribute_array(key)
    state = np.bitwise_xor(elements_to_int(state), elements_to_int(round_key))
    return elements_to_binary(state)

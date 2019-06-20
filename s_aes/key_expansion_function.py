# coding: utf-8
import numpy as np
from s_aes.constants import WORD_SIZE, NIBBLE_SIZE, S_BOX, ROUND_CONSTANT_ARRAY, KEY_SIZE
from s_aes.substitute_sbox_function import substitute_sbox


def key_expansion(key):
    """
    Expande a chave de entrada em uma lista de palavras, Para isso faz um
    XOR bit a bit entre a palavra e a palavra anterior. Porém, se o índice
    da palavra for um múltiplo de 2 são realizadas funções adicionais.

    :param key: chave de entrada
    :return: lista de palavras
    """
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
    """
    1. Efetua um deslocamento de linha na palavra
    2. Faz substituição na palavra usando a caixa-S
    3. Com o resultado das operações anteriores, faz um XOR bit a bit com a constante da rodada

    :param word: palavra
    :param round_constant: constante da rodada
    :return: retorna um número inteiro
    """
    nibble_0 = word[:NIBBLE_SIZE]
    nibble_1 = word[NIBBLE_SIZE:]
    shift_nibble = [nibble_1, nibble_0]
    substitute_nibble_array = substitute_sbox(shift_nibble, S_BOX)
    word = "".join(substitute_nibble_array)
    return np.bitwise_xor(int(word, 2), int(round_constant, 2))


def set_previous_word(i, word):
    """
    define a palavra anterior no caso de índice múltiplo de 2

    :param i: índice
    :param word: palavra
    :return: palavra
    """
    round_constant = ROUND_CONSTANT_ARRAY[(i // 2) - 1]
    word = complex_function(word, round_constant)
    word = np.binary_repr(word)
    return word


def set_word_array(i, word, word_array):
    """
    Adiciona as novas palavras na lista

    :param i: índice
    :param word: palavra
    :param word_array: lista de palavras
    :return: lista de palavras
    """
    previous = int(word_array[i - 2], 2)
    int_word = int(word, 2)
    new_word = np.bitwise_xor(previous, int_word)
    bin_new_word = np.binary_repr(new_word, WORD_SIZE)
    word_array.append(bin_new_word)
    return word_array


def key_format(key):
    """
    Verifica inconsistências na chave inserida

    :param key: chave de entrada
    :return: chave
    """
    if isinstance(key, int):
        key = np.binary_repr(key, KEY_SIZE)
        if len(key) > KEY_SIZE:
            raise Exception("A chave precisa ter 16 bits")
        return key
    else:
        raise Exception("A chave deve conter apenas números")


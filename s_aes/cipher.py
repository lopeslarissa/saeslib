# coding: utf-8
import numpy as np
from s_aes.add_round_key import add_round_key
from s_aes.constants import TRANSFORMATION_MATRIX_INVERSE, S_BOX_I, N_ROUNDS, TRANSFORMATION_MATRIX, S_BOX, BLOCK_SIZE
from s_aes.key_expansion import key_expansion, key_format
from s_aes.mix_column import mix_column
from s_aes.shift_row import shift_row
from s_aes.substitute_sbox import substitute_sbox
from s_aes.utils import string_to_array


def cipher(input_text, input_key, rounds_range, rounds_function):
    """
    Criptografa ou descriptografa o texto inserido de acordo com os parametros

    :param input_text: texto a ser criptografado ou descriptografado
    :param input_key: chave usada para criptografar ou descriptografar
    :param rounds_range: define o número de rodadas.
        Use ROUNDS_RANGE_CIPHER para criptografar e ROUNDS_RANGE_DECIPHER para desciptografar
    :param rounds_function: define se a função será de criptografia ou descriptografia.
        Use cipher_rounds para criptografar e decipher_rounds para desciptografar
    :return: texto criptografado ou descriptografado respectivamente
    """
    key_array = key_expansion(key_format(input_key))
    state_array = text_to_state(input_text)
    cipher_text = []
    for state in state_array:
        for i in rounds_range:
            state = rounds_function(i, key_array, state)
        cipher_text.insert(0, state_to_text(state))
    return int("".join(cipher_text), 2)


def cipher_rounds(r, word_array, state):
    """
    Executa as rodadas de criptografia

    :param r: número da rodada
    :param word_array: array contendo todas as palavras que geram as chaves
    :param state: vetor estado
    :return: vetor estado criptografada
    """
    if r > 0:
        state = substitute_sbox(state, S_BOX)
        state = shift_row(state)
    if 0 < r < (N_ROUNDS - 1):
        state = mix_column(state, TRANSFORMATION_MATRIX)
    state = add_round_key(r, state, word_array)
    return state


def decipher_rounds(r, word_array, state):
    """
    Executa as rodadas de descriptografia

    :param r: número da rodada
    :param word_array: array contendo todas as palavras que geram as chaves
    :param state: vetor estado
    :return: vetor estado descriptografada
    """
    if r < (N_ROUNDS - 1):
        state = shift_row(state)
        state = substitute_sbox(state, S_BOX_I)
    state = add_round_key(r, state, word_array)
    if 0 < r < (N_ROUNDS - 1):
        state = mix_column(state, TRANSFORMATION_MATRIX_INVERSE)
    return state


def text_to_state(plain_text):
    """
    Formata o texto de entrada em uma lista de matrizes estado

    :param plain_text: texto de entrada
    :return: lista de matrizes estado
    """
    if isinstance(plain_text, int):
        state_array = []
        binary_text = np.binary_repr(plain_text)
        size = len(binary_text)
        while size > 0:
            text = extract_block(binary_text, size)
            state_array.insert(0, string_to_array(text))
            size -= BLOCK_SIZE
        return state_array
    else:
        raise Exception("O texto deve conter apenas números")


def extract_block(text, part):
    """
    Extrai blocos do texto

    :param text: texto de entrada
    :param part: tamanho do bloco a ser extraído
    :return: texto estraído
    """
    if part - BLOCK_SIZE < 0:
        text = text[:part].zfill(BLOCK_SIZE)
    else:
        text = text[part - BLOCK_SIZE:part]
    return text


def state_to_text(state):
    """
    Converte o vetor estado em texto plano

    :param state: vetor estado
    :return: texto plano
    """
    temp_nibble = state[2]
    state[2] = state[1]
    state[1] = temp_nibble
    return "".join(state)
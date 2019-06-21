# coding: utf-8
import numpy as np


def elements_to_binary(state):
    """
    Formata os elementos do vetor estado para repesentação binária

    :param state: vetor estado
    :return: vetor estado
    """
    return [np.binary_repr(nibble, 4) for nibble in state]


def elements_to_int(state):
    """
    Formata os elementos do vetor estado para números inteiros

    :param state: vetor estado
    :return: vetor estado
    """
    return [int(nibble, 2) for nibble in state]


def string_to_array(text, part=4):
    """
    Transforma um texto em vetor estado

    :param text: texto
    :param part: tamanho do nibble
    :return: vetor estado
    """
    return [text[:part], text[part * 2:part * 3], text[part:part * 2], text[part * 3:]]







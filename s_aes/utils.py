# coding: utf-8
import numpy as np


def elements_to_binary(state):
    return [np.binary_repr(nibble, 4) for nibble in state]


def elements_to_int(state):
    return [int(nibble, 2) for nibble in state]


def distribute_array(matrix, part=4):
    return [matrix[:part], matrix[part * 2:part * 3], matrix[part:part * 2], matrix[part * 3:]]







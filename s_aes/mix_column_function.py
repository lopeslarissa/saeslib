# coding: utf-8
import numpy as np
from pyfinite import ffield
from s_aes.utils import elements_to_int, elements_to_binary


def mix_column(state, transformation_matrix):
    state_int = elements_to_int(state)
    state_matrix = transform_state_to_matrix(state_int)
    state_multiplied = multiply_matrix(state_matrix, transformation_matrix)
    state = transform_matrix_to_state(state_multiplied)
    return elements_to_binary(state)


def transform_matrix_to_state(matrix):
    return [matrix[0][0], matrix[1][0], matrix[0][1], matrix[1][1]]


def transform_state_to_matrix(state):
    return [[state[0], state[2]], [state[1], state[3]]]


def multiply_matrix(state, matrix):
    size = 2
    finite_field = ffield.FField(4)
    state_result = [[0, 0], [0, 0]]
    for i in range(size):
        for j in range(size):
            xor_add = 0
            for k in range(size):
                multiplication = finite_field.Multiply(state[i][k], matrix[k][j])
                xor_add = np.bitwise_xor(xor_add, multiplication)
                state_result[i][j] = xor_add
    return state_result
# coding: utf-8
import numpy as np


def shift_row(state):
    """
    Rotação circular à esquerda de uma posição na segunda linha da matriz

    :param state: vetor estado
    :return: vetor estado
    """
    state_matrix = [[state[0], state[1]], [state[2], state[3]]]
    second_row = state_matrix[1]
    state_matrix[1] = np.roll(second_row, 1)
    state_array = [state_matrix[0][0], state_matrix[0][1], state_matrix[1][0], state_matrix[1][1]]
    return state_array

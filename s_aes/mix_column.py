# coding: utf-8
import numpy as np
from pyfinite import ffield
from s_aes.utils import elements_to_int, elements_to_binary


def mix_column(state, transformation_matrix):
    """
    Multiplicação entre o vetor estado e a matriz da transformação. Para isso, converte o vetror estado em matriz e
    pós a multiplicação converte em vetor novamente

    :param state: vetor estado
    :param transformation_matrix: matriz da transformação
    :return: vetor estado com elementos em representação binária
    """
    state_int = elements_to_int(state)
    state_matrix = array_to_matrix(state_int)
    state_multiplied = multiply_matrix(state_matrix, transformation_matrix)
    state = matrix_to_array(state_multiplied)
    return elements_to_binary(state)


def matrix_to_array(matrix):
    """
    Converte uma matriz de tamanho 2x2 em um vetor linear, ordenando por coluna
    :param matrix: matriz
    :return: vetor
    """
    return [matrix[0][0], matrix[1][0], matrix[0][1], matrix[1][1]]


def array_to_matrix(state):
    """
    Converte um vetor linear em uma matriz de tamanho 2x2, ordenando por coluna

    :param state: vetor
    :return: matriz
    """
    return [[state[0], state[2]], [state[1], state[3]]]


def multiply_matrix(matrixA, matrixB):
    """
    Multiplica duas matrizes 2x2 com as operações internas sobre o corpo finito GF(2⁴)

    :param matrixA: primeira matriz
    :param matrixB: segunda matriz
    :return: matriz resultado
    """
    size = 2
    finite_field = ffield.FField(4)
    matrix_result = [[0, 0], [0, 0]]
    for i in range(size):
        for j in range(size):
            xor_add = 0
            for k in range(size):
                multiplication = finite_field.Multiply(matrixA[i][k], matrixB[k][j])
                xor_add = np.bitwise_xor(xor_add, multiplication)
                matrix_result[i][j] = xor_add
    return matrix_result

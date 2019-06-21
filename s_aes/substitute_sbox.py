# coding: utf-8
def substitute_sbox(state, sbox):
    """
    Substituição dos nibbles de acordo com a caixa-S

    :param state: vetor estado
    :param sbox: caixa-S. Use S_BOX para caixa-S e S_BOX_I para caixa-S inversa
    :return: vetor estado
    """
    return [sbox[int(nibble, 2)] for nibble in state]

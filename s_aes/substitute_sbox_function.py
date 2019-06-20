# coding: utf-8
def substitute_sbox(state, sbox):
    return [sbox[int(nibble, 2)] for nibble in state]

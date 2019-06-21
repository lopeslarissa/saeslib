# coding: utf-8
from s_aes.add_round_key import add_round_key
from s_aes.cipher import text_to_state, cipher, cipher_rounds, decipher_rounds
from s_aes.constants import S_BOX, TRANSFORMATION_MATRIX, ROUNDS_RANGE_CIPHER, S_BOX_I, TRANSFORMATION_MATRIX_INVERSE, \
    ROUNDS_RANGE_DECIPHER
from s_aes.key_expansion import key_expansion, key_format
from s_aes.mix_column import mix_column
from s_aes.shift_row import shift_row
from s_aes.substitute_sbox import substitute_sbox


def set_context_encrypt(text, key):
    context = {}
    context['plain_text'] = text
    context['key'] = key
    context['word_array'] = key_expansion(key_format(key))
    context['state_array'] = text_to_state(text)
    context['round_0'] = round_0_encrypt(context['state_array'], context['word_array'])
    context['round_1'] = round_1_encrypt(context['round_0']['add_round_key']['after'], context['word_array'])
    context['round_2'] = round_2_encrypt(context['round_1']['add_round_key']['after'], context['word_array'])
    context['cipher_text'] = cipher(text, key, ROUNDS_RANGE_CIPHER, cipher_rounds)
    return context


def set_context_decrypt(text, key):
    context = {}
    context['cipher_text'] = text
    context['key'] = key
    context['word_array'] = key_expansion(key_format(key))
    context['state_array'] = text_to_state(text)
    context['round_0'] = round_0_encrypt(context['state_array'], context['word_array'])
    context['round_1'] = round_1_encrypt(context['round_0']['add_round_key']['after'], context['word_array'])
    context['round_2'] = round_2_encrypt(context['round_1']['mix_column']['after'], context['word_array'])
    context['plain_text'] = cipher(text, key, ROUNDS_RANGE_DECIPHER, decipher_rounds)
    return context


def loop_substitute_nibble(state_array, sbox=S_BOX):
    return [substitute_sbox(state, sbox) for state in state_array]


def loop_add_key(round, state_array, key_array):
    return [add_round_key(round, state, key_array) for state in state_array]


def loop_mix_column(state_array, matrix=TRANSFORMATION_MATRIX):
    return [mix_column(state, matrix) for state in state_array]


def loop_shift_row(state_array):
    return [shift_row(state) for state in state_array]


def round_0_encrypt(state_array, key_array):
    return {'add_round_key': {'before': state_array, 'after': loop_add_key(0, state_array, key_array)}}


def round_0_decrypt(state_array, key_array):
    return {'add_round_key': {'before': state_array, 'after': loop_add_key(2, state_array, key_array)}}


def round_1_encrypt(state_array, key_array):
    substitution = loop_substitute_nibble(state_array)
    shift = loop_shift_row(substitution)
    mix = loop_mix_column(shift)
    add_key = loop_add_key(1, mix, key_array)
    return {'substitute_nibble': {'before': state_array, 'after': substitution},
            'shift_row': {'before': substitution, 'after': shift},
            'mix_column': {'before': shift, 'after': mix},
            'add_round_key': {'before': mix, 'after': add_key}}


def round_1_decrypt(state_array, key_array):
    shift = loop_shift_row(state_array)
    substitution = loop_substitute_nibble(shift, S_BOX_I)
    add_key = loop_add_key(1, substitution, key_array)
    mix = loop_mix_column(add_key, TRANSFORMATION_MATRIX_INVERSE)
    return {'shift_row': {'before': state_array, 'after': shift},
            'substitute_nibble': {'before': shift, 'after': substitution},
            'add_round_key': {'before': substitution, 'after': add_key},
            'mix_column': {'before': add_key, 'after': mix}}


def round_2_encrypt(state_array, key_array):
    substitution = loop_substitute_nibble(state_array)
    shift = loop_shift_row(substitution)
    add_key = loop_add_key(2, shift, key_array)
    return {'substitute_nibble': {'before': state_array, 'after': substitution},
            'shift_row': {'before': substitution, 'after': shift},
            'add_round_key': {'before': shift, 'after': add_key}}


def round_2_decrypt(state_array, key_array):
    shift = loop_shift_row(state_array)
    substitution = loop_substitute_nibble(shift, S_BOX_I)
    add_key = loop_add_key(0, substitution, key_array)
    return {'shift_row': {'before': state_array, 'after': shift},
            'substitute_nibble': {'before': shift, 'after': substitution},
            'add_round_key': {'before': substitution, 'after': add_key}}


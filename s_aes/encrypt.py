# coding: utf-8
# !/usr/bin/env python
import json
import argparse
import os
from s_aes.report_generate import set_context_encrypt


def main():
    parser = argparse.ArgumentParser(description='Algoritmo de criptografia AES simplificado')
    parser.add_argument('-k', action='store', dest='key', required=True,
                        help='Chave de 16 bits', type=int)
    parser.add_argument('-t', action='store', dest='text', required=True,
                        help='Texto', type=int)
    parser.add_argument('-p', action='store', dest='path',
                        help='Local para salvar o relatório', type=dir_path)
    args = parser.parse_args()
    if args.path:
        args.path = str(args.path)
    else:
        args.path = ''
    with open(args.path + 'report.json', 'w') as outfile:
        json.dump(set_context_encrypt(args.text, args.key), outfile, indent=4)


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError("{}: não é um local valido".format(path))


if __name__ == '__main__':
    main()

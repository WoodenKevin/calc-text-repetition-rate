#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from util.handle_args import handle_args
from util.colourful_print import colourful_print


def main():
    if handle_args(sys.argv, 3):
        pass
    else:
        colourful_print(
            'primary',
            'EXAMPLE: python main.py origin.txt compared.txt result.txt')


if __name__ == "__main__":
    main()

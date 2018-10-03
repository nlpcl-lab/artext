import string
import random
import logging
import operator
import argparse

import inflect


log = logging.getLogger('artext')
fmt = '%(asctime)s %(levelname)s:%(message)s '
logging.basicConfig(format='', level=logging.INFO, datefmt='%Y:%m:%d %I:%M:%S')
fh = logging.FileHandler('log.txt')
log.addHandler(fh)
console = logging.StreamHandler()
log.addHandler(console)


def arg_parser():
    """
    CLI options for inject.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', '--source', type=str, required=True,
                        help='Path to source text file')
    parser.add_argument('-out', '--output', type=str, required=True,
                        help='Path to ouput text file')
    parser.add_argument('-n', '--samples', type=int, default=1,
                        help='Number of noise samples to generate per sentence')
    parser.add_argument('-sep', '--separator', type=str, default='\n',
                        help='String to separate noise samples of a sentence')
    parser.add_argument('-er', '--error_rate', type=float,
                        help='Error rate in decimal, eg. 0.3')
    parser.add_argument('-l', '--level', choices=['sent', 'doc'],
                        help='Level at which to generate noises', default='all')
    parser.add_argument('-c', '--config', type=str, default='config.ini',
                        help='Configuration file')

    return parser


def rand_index(word):
    """
    Returns a random index in a given text.
    """

    return random.randint(0, len(word)-1)
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__)) + os.path.sep


def open_file(filename, mode='r'):
    return open(BASEDIR + filename, mode=mode, encoding='utf8')


def read_roots(n):
    with open_file('roots_{}.txt'.format(n)) as f:
        return [x.split()[::-1] for x in f.read().strip().split('\n')]


def read_file(filename, mode='r'):
    with open(BASEDIR + filename, mode=mode, encoding='utf8') as f:
        return f.read()

import os

BASEDIR = os.path.dirname(os.path.abspath(__file__)) + os.path.sep


def open_file(filename, mode='r'):
    return open(BASEDIR + filename, mode=mode, encoding='utf8')


def read_roots(n):
    with open_file('roots_{}.txt'.format(n)) as f:
        print(f.name)
        return [x.split()[::-1] for x in f.read().strip().split('\n')]

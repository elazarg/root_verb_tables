import random
from root_verb_tables import heb_io

PRE = '_'


def instantiate(proto, root, templates):
    NON_PRE = '~'
    res = templates
    for p, c in zip(proto, root):
        res = res.replace(PRE + p, NON_PRE + c)

    # apply the only linguistic rule:
    # ננ -> נ
    res = res.replace('ננה\t', 'נה\t')

    return res.replace(NON_PRE, '')


def read_root(root, tag):
    with heb_io.open_file('{}/{}.tsv'.format(len(root), tag)) as f:
        proto = next(f).strip()
        templates = f.read()
    return proto, templates


def load_roots_map():
    roots_map = {}
    for n in [3, 4]:
        with heb_io.open_file('roots_{}_tagged.tsv'.format(n)) as f:
            for line in f.read().strip().split('\n'):
                w, *root, tag = line.split()
                roots_map[w] = (root, tag)
    return roots_map


roots_map = load_roots_map()

roots = list(roots_map)


def read_template(w):
    root, tag = roots_map[w]
    proto, templates = read_root(root, tag)
    return instantiate(proto, root, templates)


if __name__ == '__main__':
    print(read_template(random.choice(roots)))

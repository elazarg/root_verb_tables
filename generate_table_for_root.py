import random
from root_verb_tables import heb_io

PRE = '_'


def instantiate(proto, root, templates):
    NON_PRE = '~'
    res = templates
    for p, c in zip(proto, root):
        # ו -> וו
        if c in ['ו', 'י']:
            res = res + res.replace(PRE + p, PRE + p + PRE + p)
        res = res.replace(PRE + p, NON_PRE + c)

    # apply the only linguistic rule:
    # ננ -> נ
    res = res.replace('ננה\t', 'נה\t')
    res = res.replace(NON_PRE, '')
    res = res.replace('ווו', 'וו')
    res = res.replace('ווו', 'וו')
    res = res.replace('ייי', 'יי')
    return res


def read_root(root, tag):
    with heb_io.open_file('{}/{}.tsv'.format(len(root), tag)) as f:
        proto = next(f).strip()
        templates = f.read()
    return proto, templates


def load_roots_map(numbers):
    roots_map = {}
    for n in numbers:
        with heb_io.open_file('roots_{}_tagged.tsv'.format(n)) as f:
            for line in f.read().strip().split('\n'):
                w, *root, tag = line.split()
                roots_map[w] = (root, tag)
    return roots_map


roots_map_3 = load_roots_map([3])
roots_map_4 = load_roots_map([4])
roots_map_all = load_roots_map([3, 4])

roots_3 = list(roots_map_3)
roots_4 = list(roots_map_4)
roots_all = list(roots_map_all)


def read_template(w) -> str:
    root, tag = roots_map_all[w]
    proto, templates = read_root(root, tag)
    return instantiate(proto, root, templates)


if __name__ == '__main__':
    print(read_template(random.choice(roots_all)))

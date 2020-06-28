import random
from root_verb_tables import heb_io

PRE = '_'


def instantiate(proto, radicals, templates):
    NON_PRE = '~'
    res = templates
    for p, c in zip(proto, radicals):
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


def load_roots_map(arity: str):
    numbers = {
        '3': [3],
        '4': [4],
        'combined': [3, 4],
    }[arity]
    roots_map = {}
    for n in numbers:
        with heb_io.open_file('roots_{}_tagged.tsv'.format(n)) as f:
            for line in f.read().strip().split('\n'):
                w, *root, tag = line.split()
                roots_map[w] = (root, tag)
    return roots_map


def load_all_root_maps():
    r_3 = load_roots_map('3')
    r_4 = load_roots_map('4')
    r_combined = r_3.copy()
    r_combined.update(r_4)
    return {
        '3': r_3,
        '4': r_4,
        'combined': r_combined,
    }


def read_template(radicals, tag) -> str:
    proto, templates = read_root(radicals, tag)
    return instantiate(proto, radicals, templates)


if __name__ == '__main__':
    roots_map = load_roots_map('combined')
    roots = list(roots_map)
    root = random.choice(roots)
    tag = roots_map[root]
    print(read_template(root, tag))

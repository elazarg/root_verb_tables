import random

PRE = '_'


def instantiate(proto, root, templates):
    res = templates
    for p, c in zip(proto, root):
        res = res.replace(PRE + p, PRE + c)

    # apply the only linguistic rule:
    # ננ -> נ
    res = res.replace('ננה\t', 'נה\t')

    return res\
        .replace('כ\n', 'ך\n')\
        .replace('מ\n', 'ם\n')\
        .replace('נ\n', 'ן\n')\
        .replace('פ\n', 'ף\n')\
        .replace('צ\n', 'ץ\n')\
        .replace(PRE, '')


def read_root(root, tag):
    with open('{}/{}.tsv'.format(len(root), tag), encoding='utf8') as f:
        proto = next(f).strip()
        templates = f.read()
    return proto, templates


def load_roots_map():
    roots_map = {}
    for n in [3, 4]:
        with open('roots_{}_tagged.tsv'.format(n), encoding='utf8') as f:
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

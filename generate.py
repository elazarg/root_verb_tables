import random

PRE = '_'


def read_template(basedir):
    ROOTS = basedir + '/roots.txt'
    PROTO = basedir + '/proto.txt'
    TABLE = basedir + '/table.tsv'

    with open(PROTO, encoding='utf8') as f:
        proto = f.read().strip()

    with open(ROOTS, encoding='utf8') as f:
        roots = [line.split()[::-1] for line in f.read().split('\n')]

    with open(TABLE, encoding='utf8') as f:
        templates = f.read()

    return proto, roots, templates


def instantiate(proto, root, templates):
    res = templates
    for p, c in zip(proto, root):
        res = res.replace(PRE + p, c)

    return res\
        .replace(PRE + 'כ', 'ך')\
        .replace(PRE + 'מ', 'ם')\
        .replace(PRE + 'נ', 'ן')\
        .replace(PRE + 'פ', 'ף')\
        .replace(PRE + 'צ', 'ץ')\
        .replace(PRE, '')


def instantiate_random(basedir):
    proto, roots, templates = read_template(basedir)
    root = random.choice(roots)
    return instantiate(proto, root, templates)


if __name__ == '__main__':
    # print(instantiate_random('שלמים'))
    print()
    # print(instantiate_random('מרובעים'))
    print()
    print(instantiate_random('מרובעים_פדטת'))
    print()
    # print(instantiate_random('מרובעים_פשס'))

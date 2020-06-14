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


def read_random_template(n):
    with open('roots_{}_tagged.tsv'.format(n), encoding='utf8') as f:
        roots = [line.split()[::-1] for line in f.read().split('\n')]

    choice = random.choice(roots)
    print(choice)
    tag, *root = choice
    print(''.join(root))
    print(tag)

    with open('{}/{}.tsv'.format(n, tag), encoding='utf8') as f:
        proto = next(f).strip()
        templates = f.read()

    return instantiate(proto, root, templates)


if __name__ == '__main__':
    print(read_random_template(3))

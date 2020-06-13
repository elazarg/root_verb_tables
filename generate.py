import random

BASEDIR = 'שלמים'
ROOTS = BASEDIR + '/roots.txt'
TABLE = BASEDIR + '/table.tsv'

with open(ROOTS, encoding='utf8') as f:
    roots = [line.split() for line in f.read().split('\n')]

root = random.choice(roots)

with open(TABLE, encoding='utf8') as f:
    forms = f.read()

d = forms.replace('.ק', root[0]).replace('.ט', root[1]).replace('.ל', root[2])


def replace_sofiot(txt):
    return txt.replace('כ.', 'ך').replace('מ.', 'ם').replace('נ.', 'ן').replace('פ.', 'ף').replace('צ.', 'ץ').replace('.', '')


print(replace_sofiot(d))

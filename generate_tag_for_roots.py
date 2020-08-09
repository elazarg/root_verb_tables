from collections import Counter
from root_verb_tables import heb_io


def tag_root_3(root):
    a, b, c = root
    root = ''.join(root)
    if root in "אבי אפי אמר אבד אהב אהד אכל".split():
        return 'נפא'
    if root in 'יצב יצק יצע יצת יצג יצר יזע יזמ'.split():
        return 'חפיצ'
    tag = []
    h = "נבכ נבל נבע נבר נגה נגח " \
        "נגנ נגע נגפ נגר נגש נדח נדי נדפ נדר נזי נזל נזר נטי נטל " \
        "נטע נטפ נכי נכר נכש נסח נסי נסכ נסע נסק נסר נפח נפט נפל " \
        " נפע נצל נצר נשא נשב נשכ נשל נשק נשׂא נתב נתז נתנ נתק נתר ".split()
    if root in h:
        tag.append('חפנ')
    elif a in 'יו':
        tag.append('נפיו')
    elif a == 'צ':
        tag.append('פצ')
    elif a in ['ז', "ג'"]:
        tag.append('פז')
    elif a in ['ס', "ש", "שׂ"]:
        tag.append('פשס')
    elif a in ['ט', 'ת', 'ד']:
        tag.append('פדטת')

    if b in ['י', 'ו']:
        tag.append('נעו')

    if root in "קרא מצא סמא חבא נשא".split():
        tag.append('נלא')
    elif c in ['י', 'ה']:
        tag.append('נליה')

    if b == c and b != 'י':
        tag.append('כפולים')

    return '_'.join(tag) or 'שלמים'


def tag_root_4(root):
    a, b, c, d = root
    if a == 'צ':
        return 'פצ'
    elif a in ['ז', "ג'"]:
        return 'פז'
    elif a in ['ס', "ש", "שׂ"]:
        if d in ['י', 'ה']:
            return 'פשס_נליה'
        return 'פשס'
    elif a in ['ט', 'ד']:
        return 'פדט'
    elif a in ['ת']:
        return 'פת'
    return 'שלמים'


def tag(n):
    roots = heb_io.read_roots(n)
    tag = tag_root_3 if n == 3 else tag_root_4

    c = Counter()
    with heb_io.open_file('roots_{}_tagged.tsv'.format(n), 'w') as f:
        for root in roots:
            t = tag(root)
            c[t] += 1
            print(''.join(root), *root, t, sep='\t', file=f)

    total = 0
    for k, v in sorted(c.items(), key=lambda x: x[1]):
        with heb_io.open_file('{}/{}.tsv'.format(n, k)) as f:
            num_lines = len(f.read().strip().split('\n')) - 1
        print(k, v, num_lines)
        total += v * num_lines

    print(total)
    print()


if __name__ == '__main__':
    tag(3)
    tag(4)

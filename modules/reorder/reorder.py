# bracketPML / reorder — sort members of an E3D owner by name with the fewest REORDER moves. MIT licence.
# A port of PML Console's sort tool; the bracketPML build checks it against the original on random lists.
#
#   python reorder.py q_mem.txt [EQUI,CWBRAN] [nat|abc|nat-desc|abc-desc]
#
# Input: the output of Q MEM copied from the Commands window (or written with alpha log).
# Output: REORDER … BEFORE … lines, already proven on a model of the member list.
import functools
import re
import sys

# « 12 EQUI 12 /P-101» or «10 EQUI 10=12345678/1» — from the tenth line on the number eats the space before a reference;
# the type can be a user type like «:MyBox»
Q_MEM_LINE = re.compile(r'^\s*(\d+)\s+(:?[A-Za-z][\w:-]*)\s+(\d+)\s*(=\d+/\d+|/\S+)\s*$')


def parse_q_mem(text):
    """Rows of a Q MEM output: [{'n', 'type', 'addr', 'named'}]."""
    rows = []
    for line in str(text or '').splitlines():
        m = Q_MEM_LINE.match(line)
        if m:
            rows.append({'n': int(m.group(1)), 'type': m.group(2).upper(), 'addr': m.group(4),
                         'named': m.group(4).startswith('/')})
    return rows


def nat_cmp(a, b):
    """Numbers inside a name compare as numbers: P-2 before P-10."""
    ra, rb = re.findall(r'\d+|\D+', a or ''), re.findall(r'\d+|\D+', b or '')
    for x, y in zip(ra, rb):
        if x[0].isdigit() and y[0].isdigit():
            d = int(x) - int(y)
            if d:
                return d
        elif x != y:
            return -1 if x < y else 1
    return len(ra) - len(rb)


def _cmp(order):
    def nat(a, b):
        return nat_cmp(a.upper(), b.upper()) or nat_cmp(a, b)

    def abc(a, b):
        A, B = a.upper(), b.upper()
        if A != B:
            return -1 if A < B else 1
        return -1 if a < b else (1 if a > b else 0)
    f = abc if order in ('abc', 'abc-desc') else nat
    return (lambda a, b: f(b, a)) if order.endswith('desc') else f


def plan(text, types=None, order='nat'):
    """The REORDER chain for a Q MEM output. Raises ValueError with the reason instead of returning doubtful code."""
    rows = parse_q_mem(text)
    if not rows:
        raise ValueError('no Q MEM lines found: stand on the owner, run Q MEM and copy the whole output')
    # the Commands window keeps ~1000 lines and drops the BEGINNING silently; Q MEM numbers lines from 1 without gaps
    if rows[0]['n'] != 1:
        raise ValueError('the output starts at line %d, not 1 — the beginning was lost; export with alpha log' % rows[0]['n'])
    for a, b in zip(rows, rows[1:]):
        if b['n'] != a['n'] + 1:
            raise ValueError('line %d is followed by %d — part of the output was lost' % (a['n'], b['n']))
    types = [t.upper() for t in (types or [])]
    in_type = [r for r in rows if not types or r['type'] in types]
    if not in_type:
        raise ValueError('no members of type %s in the output' % ', '.join(types))
    sel = [r for r in in_type if r['named']]
    unnamed = [r for r in in_type if not r['named']]
    target = sorted((r['addr'] for r in sel), key=functools.cmp_to_key(_cmp(order)))
    if len(set(target)) != len(target):
        raise ValueError('a name appears twice — this is not the output of one Q MEM')

    lst = [r['addr'] for r in rows]                 # model of the member list, all rows in output order
    pos = [lst.index(a) for a in target]
    n = len(target)
    # the longest already ordered subsequence that ENDS on the last target element: BEFORE cannot move anything
    # to the very end of the list (AFTER is not verified), so the last one has to stay where it is
    length, prev = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if pos[j] < pos[i] and length[j] + 1 > length[i]:
                length[i], prev[i] = length[j] + 1, j
    keep, i = set(), n - 1
    while i >= 0:
        keep.add(i)
        i = prev[i]
    cmds = []
    for i in range(n - 2, -1, -1):                  # from the end: the element it goes before is already in place
        if i in keep:
            continue
        x, before = target[i], target[i + 1]
        lst.remove(x)
        lst.insert(lst.index(before), x)
        cmds.append('REORDER %s BEFORE %s' % (x, before))
    got = [a for a in lst if a in set(target)]
    if got != target:                               # the proof: the model must give exactly the target order
        raise ValueError('internal error: the REORDER chain does not give the target order — no code produced')
    return {'cmds': cmds, 'target': target, 'unnamed': [r['addr'] for r in unnamed], 'kept': len(keep)}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('usage: python reorder.py <q_mem.txt> [TYPE,TYPE] [nat|abc|nat-desc|abc-desc]')
    with open(sys.argv[1], encoding='utf-8-sig') as f:
        src = f.read()
    tps = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] else None
    try:
        p = plan(src, tps, sys.argv[3] if len(sys.argv) > 3 else 'nat')
    except ValueError as e:
        sys.exit('NO CODE: %s' % e)
    print('\n'.join(p['cmds']) if p['cmds'] else '-- already in order, nothing to move')
    print('-- %d moves, %d members, %d already in place%s' % (
        len(p['cmds']), len(p['target']), p['kept'],
        ', %d unnamed left where they are' % len(p['unnamed']) if p['unnamed'] else ''))

# bracketPML — repository check (CI and local): relative links resolve, every module is complete,
# no private data slipped in. MIT licence.  python tools/verify.py
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# traces of a working project or a personal PC must never reach the public repository
BANNED = re.compile(r'npg|ShchegolevIuA|67131235|Desktop\\+PML_console|job_PC', re.I)
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')
bad = []

for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('.git', 'node_modules')]
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, ROOT)
        if f.endswith(('.md', '.pmlmac', '.py', '.js', '.json', '.yml', '.txt', '.html')):
            text = open(p, encoding='utf-8').read()
            m = BANNED.search(text)
            if m and rel != os.path.join('tools', 'verify.py'):
                bad.append('%s: private trace «%s»' % (rel, m.group(0)))
            if f.endswith('.md'):
                for link in LINK.findall(text):
                    if re.match(r'[a-z]+:', link):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(dp, link))):
                        bad.append('%s: broken link %s' % (rel, link))

mods = os.path.join(ROOT, 'modules')
for m in sorted(os.listdir(mods)) if os.path.isdir(mods) else []:
    for need in ('README.md', 'probe.pmlmac'):
        if not os.path.isfile(os.path.join(mods, m, need)):
            bad.append('modules/%s: no %s' % (m, need))

# register.json: the contract from schema/register.schema.md — plain Python, no dependencies
reg_p = os.path.join(ROOT, 'register.json')
if os.path.isfile(reg_p):
    import collections
    import io
    import json as _json
    reg = _json.load(io.open(reg_p, encoding='utf-8'))
    ids = [r.get('id') for r in reg.get('rows', [])]
    dup = [k for k, v in collections.Counter(ids).items() if v > 1]
    if dup:
        bad.append('register.json: duplicate row ids %s' % dup[:5])
    gids = {g.get('id') for g in reg.get('groups', [])}
    for r in reg.get('rows', []):
        if r.get('g') not in gids:
            bad.append('register.json: row %s points to a missing group %s' % (r.get('id'), r.get('g')))
            break
    for g in reg.get('groups', []):
        real = sum(1 for r in reg['rows'] if r['g'] == g['id'])
        if g.get('n') != real:
            bad.append('register.json: group %s says n=%s, actually %d' % (g['id'], g.get('n'), real))
    for r in reg.get('rows', []):
        if r.get('st') not in reg.get('status', {}):
            bad.append('register.json: row %s has unknown status %s' % (r.get('id'), r.get('st')))
            break

if bad:
    print('\n'.join(bad))
    sys.exit(1)
print('ok')

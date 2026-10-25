# bracketPML / export-safe — read a file written by export-safe.pmlmac and refuse a broken one.
# MIT licence. Python 3.8+, no dependencies.
#
#   python read_export.py C:\Temp\bpml-export.txt
#
# A file is trusted only if it has the end line «#BPML END <n>» and exactly n «#ITEM» lines.
# Areas that were not found («#BPML NOAREA <name>») are reported; the rest of the file is still used.
import sys


class BrokenExport(Exception):
    pass


def read_export(path):
    """Return (items, missing_areas). items: list of (ref, name). Raises BrokenExport with the reason."""
    # alpha log writes UTF-8 with BOM: utf-8-sig drops the three BOM bytes
    with open(path, encoding='utf-8-sig') as f:
        lines = [ln.strip() for ln in f]
    items, missing, end = [], [], None
    for ln in lines:
        if ln.startswith('#ITEM '):
            parts = ln.split(None, 2)
            if len(parts) < 3:
                raise BrokenExport('a line without a reference or a name: %r' % ln)
            items.append((parts[1], parts[2]))
        elif ln.startswith('#BPML NOAREA'):
            missing.append(ln[len('#BPML NOAREA'):].strip())
        elif ln.startswith('#BPML END'):
            tail = ln[len('#BPML END'):].strip()
            if not tail.isdigit():
                raise BrokenExport('the end line has no count: %r' % ln)
            end = int(tail)
    if end is None:
        raise BrokenExport('no «#BPML END» line — the macro stopped before the end; do not use this file')
    if end != len(items):
        raise BrokenExport('the macro wrote %d items, the file holds %d — the file is damaged' % (end, len(items)))
    return items, missing


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: python read_export.py <file>')
    try:
        items, missing = read_export(sys.argv[1])
    except BrokenExport as e:
        sys.exit('NOT TRUSTED: %s' % e)
    for ref, name in items:
        print(ref, name)
    for area in missing:
        print('area not found in the model: %s (check the name: a hyphen and an underscore differ)' % area, file=sys.stderr)
    print('ok: %d items' % len(items), file=sys.stderr)

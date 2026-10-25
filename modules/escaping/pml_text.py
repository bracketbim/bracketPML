# bracketPML / escaping — write text and names into PML without losses. MIT licence. Python 3.8+.
#
# The rules, each verified in AVEVA E3D 2.1 (see README.md for the runs):
#   - text goes in vertical bars |...|; a text that contains a bar goes in single quotes '...';
#   - every $ is doubled: $ is a control character ($1 is a macro argument, $!x a variable);
#   - a line break cannot be written (one PML command is one line) — refused;
#   - a bar AND an apostrophe in one text cannot be wrapped — refused;
#   - a name is one word starting with /: no spaces, quotes, bars or $.
APO = "'"


def pml_text_why(value):
    """The reason a text cannot be written, or '' if it can."""
    s = '' if value is None else str(value)
    if '\n' in s or '\r' in s:
        return 'line break: a PML command is one line, the rest would run as a separate command'
    if '|' in s and APO in s:
        return 'both a vertical bar and an apostrophe: there is nothing left to wrap the text in'
    return ''


def pml_text(value):
    """Text attribute value, ready for a command: pml_text('price $5') -> '|price $$5|'."""
    s = ('' if value is None else str(value)).strip()
    why = pml_text_why(s)
    if why:
        raise ValueError('text %r cannot be written: %s' % (s[:40], why))
    d = s.replace('$', '$$')
    return '|' + d + '|' if '|' not in d else APO + d + APO


def pml_name(value, what='name'):
    """Element name, ready for NEW / NAME / navigation: pml_name('PMLC-CWAY-T1') -> '/PMLC-CWAY-T1'."""
    s = ('' if value is None else str(value)).strip()
    if not s:
        raise ValueError(what + ' is empty')
    if any(c.isspace() for c in s):
        raise ValueError('%s %r has a space: an E3D name is one word, the command would split in two' % (what, s))
    bad = [c for c in ('|', APO, '"', '$') if c in s]
    if bad:
        raise ValueError('%s %r: %s is not allowed in an E3D name' % (what, s, ' '.join(bad)))
    return s if s.startswith('/') else '/' + s


if __name__ == '__main__':
    for t in ('cable tray 600', 'price $5', '3/4" pipe', 'a|b'):
        print('%-16s -> DESC %s' % (t, pml_text(t)))
    print('%-16s -> %s' % ('PMLC-CWAY-T1', pml_name('PMLC-CWAY-T1')))

// bracketPML / escaping — write text and names into PML without losses. MIT licence.
// The same rules as pml_text.py (see README.md): bars, single quotes for a text with a bar,
// every $ doubled, a line break and «bar + apostrophe» refused, a name is one word starting with /.
const APO = "'";

export function pmlTextWhy(value) {
  const s = value == null ? '' : String(value);
  if (s.includes('\n') || s.includes('\r'))
    return 'line break: a PML command is one line, the rest would run as a separate command';
  if (s.includes('|') && s.includes(APO))
    return 'both a vertical bar and an apostrophe: there is nothing left to wrap the text in';
  return '';
}

export function pmlText(value) {
  const s = (value == null ? '' : String(value)).trim();
  const why = pmlTextWhy(s);
  if (why) throw new Error('text «' + s.slice(0, 40) + '» cannot be written: ' + why);
  const d = s.split('$').join('$$');
  return d.includes('|') ? APO + d + APO : '|' + d + '|';
}

export function pmlName(value, what = 'name') {
  const s = (value == null ? '' : String(value)).trim();
  if (!s) throw new Error(what + ' is empty');
  if (/\s/.test(s)) throw new Error(what + ' «' + s + '» has a space: an E3D name is one word, the command would split in two');
  const bad = ['|', APO, '"', '$'].filter(c => s.includes(c));
  if (bad.length) throw new Error(what + ' «' + s + '»: ' + bad.join(' ') + ' is not allowed in an E3D name');
  return s.startsWith('/') ? s : '/' + s;
}

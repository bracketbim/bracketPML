# Text in PML without losses

> How to write any text into an attribute — bars, quotes, the dollar sign — and the two cases that cannot be written at all.

**Commands:** `DESC` **Verified** · `CABLAY` **Verified** · `NAME` **Verified** · `$M` **Verified**

When you generate PML from Excel, Python or a web page, every text value has to be **wrapped** so E3D reads it as text. Get it wrong and E3D does one of two things: it stops with `CP: Syntax error` — which is the good case — or it **silently writes a different text**. That second case is why this module exists.

## The rules

| Your text | Write it as | E3D stores | Status |
|---|---|---|---|
| `cable tray 600` | `DESC \|cable tray 600\|` | `cable tray 600` | **Verified** |
| `cable tray 600` | `DESC 'cable tray 600'` | `cable tray 600` | **Verified** — single quotes are equal to bars |
| `price $5` | `DESC \|price $$5\|` | `price $5` | **Verified** — double every `$` |
| `price $5` in a **macro**, not doubled | `DESC \|a$1b\|` | `ab` — **`$1` is eaten** as a macro argument | **Verified** |
| `3/4" pipe` | `DESC \|3/4" pipe\|` | `3/4" pipe` | **Verified** — a double quote goes in as it is |
| `CEN` (a text attribute) | `CABLAY \|CEN\|` | `CEN` | **Verified** — `CABLAY CEN` without bars is a syntax error |
| `600` (a number attribute) | `VWIDTH 600` or `VWIDTH 600mm` | `600mm` | **Verified** — **no bars** on numbers: `VWIDTH \|600\|` is a syntax error |

### Two texts that cannot be written

- **A line break.** A PML command is one line; the rest of the text would run as a separate command. Replace line breaks before writing.
- **A vertical bar *and* an apostrophe in the same text.** Bars are the wrapper, so a text with a bar goes in single quotes — and then an apostrophe has nothing left to wrap it. Change one of the two characters.

Both the console and the helpers below **refuse** such a text instead of writing something else.

## Why the dollar sign matters

`$` is a control character in PML: `$1…$9` are macro arguments, `$!x` substitutes a variable. In a macro `DESC |a$1b|` writes `ab` — no error, the text is just shorter. Doubling helps both in a plain paste and in Paste as Macro: `$$` becomes one `$`.

## Names are stricter

A name is one word: a space splits the command in two, and quotes, bars and `$` are not allowed. A name must start with `/` — without it E3D does not navigate, **silently**, and the next `POS` lands on whatever element was current.

## Files

| File | What it is |
|---|---|
| [`pml_text.py`](pml_text.py) | `pml_text(value)` and `pml_name(value)` for Python — wrap, double `$`, refuse what cannot be written. |
| [`pml_text.js`](pml_text.js) | The same for JavaScript (browser or Node). |
| [`probe.pmlmac`](probe.pmlmac) | Check the rules in **your** E3D: writes test descriptions under a rollback mark and undoes them. |

```python
from pml_text import pml_text, pml_name
pml_text('price $5')        # -> |price $$5|
pml_text('a|b')             # -> 'a|b'
pml_name('PMLC-CWAY-T1')    # -> /PMLC-CWAY-T1
pml_text('line 1\nline 2')  # raises ValueError: line break
```

## Check it yourself

`probe.pmlmac` runs on **one element you stand on** (an EQUI, a SUBE, a branch — anything with a DESC). It sets a rollback mark, writes several descriptions, prints what E3D stored, and rolls everything back with `UNDODB`. Run it on a test project; nothing stays in the model as long as you do not `SAVEWORK` in between.

One line in the probe is marked **not yet verified by us** — a bar inside single quotes. Tell us what your E3D prints, and the register gets a new line: [test report](../../CONTRIBUTING.md).

## Verified

| Command | What it does | Status |
|---|---|---|
| `$M C:\Temp\file.pmlmac` | The same, as a command | Verified |
| `CABLAY \|CEN\|` | Cable layout | Verified |
| `CABLAY CEN` | This does NOT work | Fails |
| `DESC \|text with spaces\|` | Write a description | Verified |
| `NAME /NEW` | Rename the CURRENT element | Verified |
| `$M C:\Temp\t.mac arg1 arg2` | Run a macro from the Command Line | Verified |


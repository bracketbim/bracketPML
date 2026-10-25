# Part of your text disappears after a $

> In a macro $1 is an argument; DESC |a$1b| stores «ab» without a word. Double every dollar sign.

**E3D prints:** `(no error — the text is just shorter)`

**Commands:** `DESC` **Verified** — last run 15 Oct 2026 · `$M` **Verified**

## What you see

A macro writes descriptions from a table. One of them was `price $15`, and E3D stored `price 5`. No error, no warning.

## Why

`$` is a control character in PML. In a macro `$1…$9` are its arguments, and a missing argument is replaced by nothing. `DESC |a$1b|` run through Paste as Macro stores `ab`.

## The rule

Double every `$` in text you write: `$$` becomes one `$` both in a plain paste and in a macro. `DESC |price $$15|` stores `price $15`.

If you generate PML in code, do it in one function and never by hand — see [escaping](../modules/escaping/README.md).

## Check it yourself

Stand on a test element with a DESC and paste as macro. The mark and `UNDODB` take the change back.

```
MARKDB |dollar probe|
DESC |price $$15|
Q DESC
UNDODB
```

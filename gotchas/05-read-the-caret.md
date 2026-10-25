# The command is fine — the value is not

> Read the ^^ caret: it points at the word E3D did not accept. Text values need bars; number values must not have them.

**E3D prints:** `CP: Syntax error`

**Commands:** `CABLAY` **Verified** — last run 27 Aug 2026 · `VWIDTH` **Verified** — last run 22 Sep 2026 · `DESC` **Verified** — last run 15 Oct 2026

## What you see

```
CP: Syntax error
CABLAY ^^CEN
```

It looks like the command `CABLAY` does not exist, or does not work on this element.

## Why

Look where the caret `^^` stands — **on the value**, not on the command. `CABLAY` is a text attribute, and text goes in vertical bars: `CABLAY |CEN|` works. The opposite happens with numbers: `VWIDTH |400|` is a syntax error, `VWIDTH 400` and `VWIDTH 400mm` both work. Bars mean «this is text», not «this is a value».

## The rule

On every syntax error, read the caret first. Ask «how is the value written?», not «does the command work?».

- Text attribute → `|text|` or `'text'`.
- Number → as it is, with or without a unit, never in bars.

## Check it yourself

On a test cable tray branch, under a mark:

```
MARKDB |caret probe|
CABLAY |CEN|
Q ATT
UNDODB
```

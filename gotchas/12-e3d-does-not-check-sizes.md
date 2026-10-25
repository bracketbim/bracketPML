# E3D accepts a box of length -100

> Size attributes accept zero and negative values without a word. Validation is the generator's job.

**E3D prints:** `(no error — XLEN -100 is accepted)`

**Commands:** `XLEN` **Verified** — last run 24 Sep 2026 · `YLEN` **Verified** — last run 27 Aug 2026 · `ZLEN` **Verified** — last run 27 Aug 2026

## What you see

A table with a typo produces `XLEN -100`, and E3D takes it. `Q XLEN` prints `-100mm`. `XLEN 0` and `XLEN 250.5` pass too.

## Why

E3D stores what it is given. It checks syntax, not engineering sense.

## The rule

Validate sizes **before** you write code: positive, within a sane range, numbers and not text. PML Console refuses to produce code from a value it cannot defend; whatever generates your PML should do the same.

The same goes for names: an E3D name is one word starting with `/`. Without the slash navigation silently does not happen, and the next `POS` lands on whatever element was current — see [escaping](../modules/escaping/README.md).

# RENAME with two names does not work

> There is no RENAME /OLD /NEW. Stand on the element, then NAME /NEW. For bulk renames, go by =ref.

**E3D prints:** `(2,109) Undefined name`

**Commands:** `RENAME` **Verified** — last run 18 Sep 2026 · `NAME` **Verified** — last run 19 Sep 2026

## What you see

```
RENAME /PMLC-CWAY-T3 /PMLC-CWAY-T5
(2,109) Undefined name /PMLC-CWAY-T5
```

The caret is on the second name. Some command lists show this two-argument form — it is wrong.

## Why

`RENAME` (and `NAME`) renames the **current** element. The second word is read as something to navigate to, and there is no element with the new name yet.

## The rule

Two lines per element: go to it, then give the new name. For bulk renaming go by stable reference — numbers and names shift, `=ref` does not:

```
=12345678/6304
NAME /PMLC-CWAY-T5
```

A name that is already in use is rejected (`Name … already used`) and nothing changes. When you swap names between elements, rename through a temporary prefix first.

## Check it yourself

On a test element, under a mark:

```
MARKDB |rename probe|
NAME /BPML-RENAME-PROBE
Q NAME
UNDODB
Q NAME
```

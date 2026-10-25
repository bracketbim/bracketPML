# UNDODB says there is nothing to undo

> SAVEWORK erases the rollback mark. Check first, save second.

**E3D prints:** `No mark to UNDO to`

**Commands:** `UNDODB` **Verified** — last run 19 Sep 2026 · `MARKDB` **Verified** · `SAVEWORK` **Verified** — last run 17 Sep 2026

## What you see

You ran a bulk change, saved, noticed a mistake and typed `UNDODB`. E3D answers `(43,27) No mark to UNDO to`.

## Why

`MARKDB` marks live only until `SAVEWORK`. Saving erases them, and after that there is nothing to roll back to. It is not a bug — it is the boundary of the rollback.

## The rule

Mark → change → **check** → save. The time between the mark and `SAVEWORK` is your whole safety window; use it to look at `Q ATT`, `Q MEM` and the 3D view. If it is too late for `UNDODB`, `QUIT` still drops everything since the last save.

More in [guard](../modules/guard/README.md).

## Check it yourself

On a test element with a DESC: the first `UNDODB` works, the one after `SAVEWORK` would not — so this probe stops before saving. Do not add `SAVEWORK` on a real project.

```
MARKDB |undo probe|
DESC |temporary text|
UNDODB
Q DESC
```

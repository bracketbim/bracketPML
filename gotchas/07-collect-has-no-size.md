# A COLLECT result has no array methods

> VAR !x COLLECT … gives a list you can loop over, but not call .Size() on. Count inside the loop.

**E3D prints:** `Object does not have a member SIZE`

**Commands:** `VAR` **Verified** · `COLLECT` **Fails** · `DO` **Macro only**

## What you see

```
VAR !!x COLLECT ALL CWBRAN FOR CE
$P $!!x.Size()
Object does not have a member SIZE
```

Same in a macro — it is not about the way you paste.

## Why

`COLLECT` is not a command of its own (`COLLECT $Q` is a syntax error); it exists only as a tail of `VAR`. Its result is not an `ARRAY` object, so array methods are not there. But `do … values` walks over it fine, and navigation `$!e` inside the loop goes to each element.

## The rule

Loop over the result and count yourself:

```
VAR !items COLLECT ALL CWBRAN FOR CE
!n = 0
do !e values !items
  !n = !n + 1
enddo
$P branches: $!n
```

Two more things worth knowing:

- `FOR <element>` takes **everything** under it, nested elements included.
- A condition can test an attribute directly: `WITH (UNSET(DESC))` finds branches without a description — a wrong condition returns an empty list, not an error, so check the count against what you expect.

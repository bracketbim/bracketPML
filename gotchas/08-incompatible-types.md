# Reading an attribute into a variable fails

> !x = MAXLAY fails if !x already holds a string. VAR !x MAXLAY works whatever was in the variable.

**E3D prints:** `Cannot assign variable to result - incompatible types (STRING=REAL)`

**Commands:** `VAR` **Verified** — last run 23 Sep 2026

## What you see

A macro reads several attributes into the same variable. The first works, then:

```
Cannot assign variable to result - incompatible types (STRING=REAL)
```

## Why

Assignment `!x = MAXLAY` keeps the type of the variable. If `!x` already holds a string and the attribute is a number, the types clash. It works only in a fresh variable.

## The rule

Read attributes with `VAR`: it does not depend on what the variable held before, and it works in the Command Line too (with a global `!!` variable).

```
!x = 'some text'
VAR !x MAXLAY
q var !x
```

On a cable tray branch this prints its MaxLay value — no type clash.

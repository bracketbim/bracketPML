# Your if block fails in the Commands window

> A plain paste runs every line as a separate command — blocks never come together, and the paste stops at the first error.

**E3D prints:** `PML: Invalid syntax in the current context`

**Commands:** `IF` **Macro only** · `DO` **Macro only** · `HANDLE` **Macro only** · `PASTE` **Verified** — last run 27 Sep 2026

## What you see

You paste a macro with `if … endif` into the Commands window and get `PML: Invalid syntax` on the `if` line — and again on `endif`. Or a long paste stops halfway, and the lines after the error never run.

## Why

The Common Functionality guide says it word for word: a plain paste «executes each line of the copied text as a separate command as if they had been typed». An `if` line alone is not a complete statement, so it fails. And a paste behaves like a temporary macro: on the first error **the rest is not executed** — you have to enter the tail again.

## The rule

- One-line commands — paste as usual.
- Anything with `if`, `do`, `handle` — **right-click → Paste as Macro**. It writes the paste to a temporary file and runs it as a macro; blocks work there.
- After a stopped paste, check where it stopped before pasting again — the first part has already run.

## Check it yourself

Paste this both ways. A plain paste fails on `if`; Paste as Macro prints `big`.

```
!x = 7
if (!x GT 5) then
  $P big
endif
```

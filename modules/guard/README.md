# Guard — undo a bulk change in one command

> E3D has no UNDO command, but it has a rollback. Put a mark before a bulk change, check, and either save or roll everything back at once.

**Commands:** `MARKDB` **Verified** · `UNDODB` **Verified** · `SAVEWORK` **Verified** · `QUIT` **Seen in code** · `UNDO` **Fails**

A macro that renames 300 elements or writes 2000 attributes is one paste away from a very long evening. Before you run anything that **writes**, you want a way back. E3D has one — it is just not called `UNDO`.

## Five facts

| # | Fact | Status |
|---|---|---|
| 1 | There is no command named `UNDO` — `CP: Syntax error`. | **Fails** |
| 2 | `MARKDB \|label\|` sets a rollback mark. The label must be in bars or single quotes; without them it is a syntax error. | **Verified** |
| 3 | `UNDODB` rolls the database back to the last mark: changed attributes, renames, **and created elements** are undone. | **Verified** |
| 4 | One `UNDODB` undoes **everything under one mark** at once — not one edit. `UNDODB 2` goes back two **marks**. Do not count edits. | **Verified** |
| 5 | `SAVEWORK` **erases** the mark. After saving, `UNDODB` answers `No mark to UNDO to`. | **Verified** |

And the second line of defence: `QUIT` leaves without saving — everything since the last `SAVEWORK` is gone. **Seen in code**

## The pattern

```
MARKDB |before: rename tray branches|      $* 1. the mark goes FIRST
…  your bulk change  …                     $* 2. the change
Q MEM                                      $* 3. check: Q ATT / Q MEM / the 3D view
$* fine  → SAVEWORK                        $* 4a. only after checking
$* wrong → UNDODB                          $* 4b. everything under the mark is undone
```

Three rules make it work:

1. **The mark is the first line** of every code that writes. PML Console puts it there automatically.
2. **Check before you save.** The mark lives until `SAVEWORK` — that is your whole safety window.
3. **One mark per operation.** Then `UNDODB` means «undo the last operation», and `UNDODB 2` — the last two.

## Files

| File | What it is |
|---|---|
| [`guard-template.pmlmac`](guard-template.pmlmac) | The pattern above, ready to wrap your own change. |
| [`probe.pmlmac`](probe.pmlmac) | See it work in your E3D: writes a description, prints it, rolls back, prints again. |

## Check it yourself

Stand on one test element that has a DESC and paste `probe.pmlmac` (a plain paste is enough — there are no blocks in it). The first `Q DESC` shows the probe text, the second one — your original description. Nothing is saved.

## Good to know

- `REDODB`, `CLEARMARK` and `ENDMARKDB` exist in the grammar (`MARKDB $Q` lists them) but we have not run them yet. **Documented**
- A plain paste stops at the first error, and the lines after it do not run. If that happens after the mark, the lines that did run are under the mark — `UNDODB` is the way back (this exact case has not been run separately yet).

## Verified

| Command | What it does | Status |
|---|---|---|
| `UNDO` | There is no command with this name | Fails |
| `MARKDB \|before bulk edit\|` | Set a rollback mark BEFORE the operation | Verified |
| `UNDODB` | Roll the database back to the last mark | Verified |
| `SAVEWORK` | Save your work to the database | Verified |
| `QUIT` | Exit WITHOUT saving | Seen in code |


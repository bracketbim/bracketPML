# Safe export — a file you can trust

> Write data from E3D to a text file with alpha log so that a broken or half-written file can never pass for a good one.

**Commands:** `ALPHA LOG` **Verified** · `HANDLE` **Macro only** · `VAR` **Verified** · `$P` **Verified** · `DO` **Macro only**

Getting data **out** of E3D is the first step of almost every automation: a list of trays to measure, equipment to tag, a tree to sort. The usual way is `alpha log` — everything the Commands window prints goes to a file. It works, and it fails in three quiet ways. Each of them cost us a real test in E3D.

## Three silent failures

| # | What happens | Why it is dangerous |
|---|---|---|
| 1 | **The log is left open.** The macro stops on an error halfway; `alpha log END` never runs. The next macro cannot open its log — E3D is still writing to the old one. | You see an error that has nothing to do with your new macro. Until you type `alpha log END` by hand, nothing works. |
| 2 | **The file is half-written.** The macro stopped in the middle, but the file is there and looks fine. | A script reads it and processes 40 trays instead of 120 — and says nothing. |
| 3 | **An area does not exist.** One name in your list has a typo (`/env-2` instead of `/env_2`). Paste as Macro stops on it. | Everything after the bad area is lost, and failures 1 and 2 follow. |

## The pattern

Five ideas, all verified in E3D 2.1:

1. **Close a log left by someone else first.** `alpha log END` under `handle any`: if no log is open, the error is caught and the macro goes on.
2. **Count what you write.** A counter `!n` grows with every line of data.
3. **End with the count.** The last line is `#BPML END <n>`. A reader checks that it is there **and** that the number matches the lines it read. No end line — the file is broken. Wrong number — the file is broken.
4. **Guard each area.** Go to an area under `handle any`; if it does not exist, write `#BPML NOAREA <name>` and skip it — the rest is still exported.
5. **Close the log at the end** with `alpha log END`.

```
alpha log END                              $* close a log left open by a stopped macro
handle any                                 $* … no log open — the error is caught here
endhandle
!n = 0
alpha log /C:\Temp\bpml-export.txt OVERWRITE
$P #BPML BEGIN
…  $P #ITEM … ;  !n = !n + 1  for every item …
$P #BPML END $!n                           $* the reader checks this number
alpha log END
```

`handle any` goes **right after** the line it guards, not before it — that is how E3D attaches a handler.

## Files

| File | What it is |
|---|---|
| [`export-safe.pmlmac`](export-safe.pmlmac) | A complete export: every cable tray branch (CWBRAN) under the current element, one line each with its reference and name. Read-only. |
| [`read_export.py`](read_export.py) | A reader that refuses a broken file: no end line, wrong count, or an area that was not found. |
| [`output-example.txt`](output-example.txt) | What a good file looks like. |

## Run it

1. In E3D stand on a zone (or a site) with cable trays.
2. Open the macro, copy everything, right-click in the Commands window → **Paste as Macro**.
3. The last line in the window says where the file went and how many lines it holds.
4. `python read_export.py C:\Temp\bpml-export.txt` — prints the items, or tells you exactly why the file must not be trusted.

## Good to know

- The file is **UTF-8 with BOM**. Read it with `utf-8-sig` in Python, or the first line starts with three stray bytes.
- `alpha log` writes **answers and errors**, not the commands themselves.
- `COLLECT … FOR <element>` takes **everything** under the element, nested items included. If you need only direct members, check the owner of each item.
- A PML string is at most about 1000 characters; keep one written line well below that.

## Verified

| Command | What it does | Status |
|---|---|---|
| `alpha log /C:\Temp\log.txt OVERWRITE` | Write everything the window prints to a file | Verified |
| `alpha log END` | Stop writing to the file | Verified |
| `VAR !!x ACTTYPE` | Project element type (:EXTZONE) | Verified |
| `VAR !!x NAME` | Read an attribute of the current element into a variable | Verified |
| `$P $!!x` | Print the value | Verified |
| `VAR !!eq COLLECT ALL EQUI WITH ( TYPE EQ 'EQUI' ) FOR CE` | Collect elements with a filter | Verified |
| `do … enddo` | Loop | Macro only |
| `handle any … endhandle` | Catch an error | Macro only |
| `VAR !!x OWNER` | An element's owner into a variable — then $!!x goes to it | Verified |
| `VAR !x COLLECT ALL CWBRAN WITH (UNSET(DESC)) FOR /PMLC` | Collect with a condition on an attribute | Verified |
| `VAR !s COLLECT ALL SITE FOR WORLD` | Collect across the whole database | Verified |
| `do !i from 1 to 10` | Counting loop | Macro only |
| `do !i from 1 to 10 by 2` | Loop with a step | Verified |
| `do !elem values !array` | Loop over array values | Macro only |
| `do !i indices !array` | Loop over indices | Macro only |
| `do while ( !flag )` | Loop on a condition — does NOT work | Fails |
| `handle any … endhandle` | Catch any error | Macro only |
| `handle (41,64)` | Catch a specific error by number | Documented |


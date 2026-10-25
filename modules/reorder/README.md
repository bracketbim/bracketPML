# Reorder — sort the model tree with the fewest moves

> Sort members of a zone by name with REORDER, moving only the elements that are out of place, and prove the result before it reaches E3D.

**Commands:** `REORDER` **Verified** — last run 21 Oct 2026 · `Q` **Verified** — last run 28 Aug 2026 · `VAR` **Verified** — last run 23 Sep 2026 · `NEXT` **Verified** — last run 27 Sep 2026

A zone with 120 branches in the order they were created is hard to read. E3D can change the order of members with `REORDER` — it is not in the 2.1 manual, but it is in real PML code, and it works.

## What REORDER does

```
REORDER /PMLC-CWBRAN-LP2/02 BEFORE /PMLC-CWBRAN-LP2/01
```

- It changes the **order of members** inside the owner. Coordinates, connections and attributes stay as they were. **Verified** — last run 21 Oct 2026
- First what you move, then what it goes before.
- It works with names and with `=ref` of unnamed elements (through a variable: `REORDER $!!a BEFORE $!!b`).
- The form `AFTER` exists in the grammar but has **never been run** by us. So the chain below uses `BEFORE` only.

## The fewest moves

Sorting 120 members by moving each one is 120 commands and 120 chances for a typo. Most members are usually already in order. The trick:

1. Find the **longest subsequence that is already in the right order** — those elements stay where they are.
2. Move every other element **before the next one in the target order**, going from the end. When an element moves, the one it goes before is already in place.
3. The last element in the target order must be among those that stay: `BEFORE` cannot put anything at the very end, and `AFTER` is not verified. The subsequence is chosen to end on it.
4. **Prove it.** Apply every command to a model of the list, exactly as E3D would, and compare with the target. A mismatch means no code — never plausible code.

The number of moves is the number of sorted members minus the length of that subsequence. If the last name is already last, that is the least possible number of single moves.

## Files

| File | What it is |
|---|---|
| [`reorder.py`](reorder.py) | `parse_q_mem(text)` reads the output of `Q MEM`; `plan(text, types, order)` returns the `REORDER` chain and checks it on a model of the list. A port of PML Console's sort tool, checked against it on random lists at every build. |
| [`q-mem-example.txt`](q-mem-example.txt) | A `Q MEM` output to try it on. |
| [`probe.pmlmac`](probe.pmlmac) | See `REORDER` in your E3D: swaps two members by `=ref` under a rollback mark and undoes it. |

```
$ python reorder.py q-mem-example.txt
REORDER /PMLC-CWBRAN-T1/05 BEFORE /PMLC-CWBRAN-T1/10
REORDER /PMLC-CWBRAN-T1/03 BEFORE /PMLC-CWBRAN-T1/04
-- 2 moves, 6 members, 4 already in place, 1 unnamed left where they are
```

## Read Q MEM carefully

The Commands window keeps about the last thousand lines and **drops the beginning silently**. `Q MEM` numbers its lines from 1 without gaps, so `reorder.py` refuses an output that does not start at 1 or has a gap — part of the members never reached you. For big zones, export with [`export-safe`](../export-safe/README.md) instead of copying from the window.

Unnamed members are printed as `=ref`. `reorder.py` sorts named members only and leaves unnamed ones where they are.

## Check it yourself

Stand on the **first** member of any owner with at least two members, then paste `probe.pmlmac` (Paste as Macro). It reads the references of the first two members, swaps them, prints `Q MEM` of the owner, and rolls back with `UNDODB`.

## Verified

| Command | What it does | Status | Last run |
|---|---|---|---|
| `Q EVAR \|PMLLIB\|` | See the PML library path from inside E3D | Verified | 16 Sep 2026 |
| `Q POS WRT WORLD` | Current element's world coordinates | Verified | 28 Aug 2026 |
| `Q HCREF` | What the branch head connects to (Q TCREF — the tail) | Verified | 28 Sep 2026 |
| `Q SPREF` | Catalogue reference of an item (on an ELCONN — Q CATREF) | Verified | 27 Sep 2026 |
| `Q DESPARAM` | Design parameters from the catalogue | Verified | 27 Sep 2026 |
| `Q POS` | Current element's coordinates | Verified | 28 Aug 2026 |
| `Q ATT` | All attributes of the current element | Verified | 28 Aug 2026 |
| `Q NAME` | Name | Verified | 28 Aug 2026 |
| `Q TYPE` | Element type | Verified | 28 Aug 2026 |
| `Q OWNER` | Owner | Verified | 28 Aug 2026 |
| `Q REF` | Stable reference like =12345678/26685 | Verified | 28 Aug 2026 |
| `Q MEM` | Members: what is inside | Verified | 28 Aug 2026 |
| `Q DESC` | Description | Verified | 28 Aug 2026 |
| `Q DRAWLIST` | What is on screen now | Verified | 28 Aug 2026 |
| `Q NAME OF /PMLC-CWBRAN-T1/01` | Read an attribute WITHOUT moving to the element | Verified | 28 Aug 2026 |
| `Q NAME TYPE OWNER` | Several attributes in one line | Verified | 28 Aug 2026 |
| `Q VAR !!x` | Show a variable | Verified | 23 Sep 2026 |
| `Q MEM ATT` | Members and attributes | Verified | 27 Aug 2026 |
| `Q $Q` | What the Q command accepts at all | Verified | 28 Aug 2026 |
| `Q PURP` | Purpose mark (PURPOSE) | Verified | 9 Oct 2026 |
| `Q ORI` | Orientation | Verified | 24 Sep 2026 |
| `VAR !!x ACTTYPE` | Project element type (:EXTZONE) | Verified | 27 Sep 2026 |
| `NEXT` | To the next member of the same owner | Verified | 27 Sep 2026 |
| `REORDER /A BEFORE /B` | Move within the list of members | Verified | 23 Sep 2026 |
| `REORDER /A AFTER /B` | The same, but after the given element | Seen in code |  |
| `VAR !!x NAME` | Read an attribute of the current element into a variable | Verified | 23 Sep 2026 |
| `VAR !!eq COLLECT ALL EQUI WITH ( TYPE EQ 'EQUI' ) FOR CE` | Collect elements with a filter | Verified | 23 Sep 2026 |
| `VAR !!x OWNER` | An element's owner into a variable — then $!!x goes to it | Verified | 1 Oct 2026 |
| `VAR !x COLLECT ALL CWBRAN WITH (UNSET(DESC)) FOR /PMLC` | Collect with a condition on an attribute | Verified | 19 Sep 2026 |
| `VAR !s COLLECT ALL SITE FOR WORLD` | Collect across the whole database | Verified | 22 Sep 2026 |


# A file read from PML turns into mojibake

> WriteFile writes UTF-8 with BOM; ReadFile and macro files read a single-byte code page. Save files that PML reads in ANSI.

**E3D prints:** `(no error — «РЎРўРђР РћР•» instead of the text)`

**Commands:** `READFILE` **Verified** — last run 18 Sep 2026 · `WRITEFILE` **Verified** — last run 27 Sep 2026 · `$M` **Verified**

## What you see

A macro reads a file you prepared in Notepad with `!f.ReadFile()`. Latin text is fine, but every non-Latin letter becomes garbage like `РЎРўРђР РћР•`. Or a macro file with non-Latin comments breaks when run with `$M`.

## Why

The two directions are not symmetric:

- **Writing** (`WriteFile`, `alpha log`) produces **UTF-8 with BOM**. Notepad and Excel read it correctly.
- **Reading** (`ReadFile`) and **running a macro file** (`$M`) use a **single-byte code page** (ANSI). A UTF-8 file is read byte by byte, and every two-byte letter becomes two wrong characters.

## The rule

- Files that PML **reads** — data files and `.mac` files — save in **ANSI** (in Notepad: Save As → Encoding → ANSI).
- Files that PML **writes** — read them as UTF-8 with BOM (`utf-8-sig` in Python).
- Simplest of all: keep macro files in plain Latin.

## Check it yourself

```
!f = object FILE('C:\Temp\bpml-read-probe.txt')
!lines = !f.ReadFile()
q var !lines
```

Save `C:\Temp\bpml-read-probe.txt` with one non-Latin word, once as UTF-8 and once as ANSI, and compare.

# A long line cannot be built or written

> A PML string is limited to about 1000 characters, and WriteFile refuses one line somewhere between 800 and 1200 bytes. Keep each line of an export under 800 bytes.

**E3D prints:** `CALCULATOR ERROR: The concatenated text is too long`

**Commands:** `WRITEFILE` **Verified**

## What you see

A macro builds a CSV line by joining attributes and writes it with `WriteFile`. Most lines are fine; one fails with `CALCULATOR ERROR: The concatenated text is too long`. Or `WriteFile` fails and the file is left empty — only the three BOM bytes.

## Why

Two separate limits:

- **Building a string:** a line of 1000 characters was written; joining more to it failed. A PML string holds about 1000–1100 characters.
- **Writing a line:** 400 non-Latin letters (800 bytes in UTF-8) were written; 600 letters (1200 bytes) failed, though the string itself was built. The file write has its own limit, counted in **bytes**.

Non-Latin text takes two bytes per letter in UTF-8, so a «short» Cyrillic line hits the limit twice as fast.

## The rule

- Keep every exported line under **800 bytes**.
- Split wide records: one line per attribute group, or one attribute per line with the element's `=ref` in front.
- Prefer `alpha log` + `$P` for exports — see [export-safe](../modules/export-safe/README.md).

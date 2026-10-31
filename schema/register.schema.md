# Register data format

The `register.json` / `attributes.json` files and the page data blob share one contract. It is checked by
`tools/verify.py` at every CI run; the page and the two language editions are built from it.

## Rows (`register.json` → `rows[]`)

| Field | Type | Meaning |
|---|---|---|
| `id` | string, unique | Anchor slug of the row (from the command text; `-2`, `-3`… on collision). Stable across builds while the command text is unchanged — links like `register.md#undodb` point here. |
| `g` | number | Group id, one of `groups[].id`. |
| `cmd` | string | The command as typed in the Commands window (no language editions — commands are language-neutral). |
| `what` | string | One-line summary. |
| `note` | string | The fact: what E3D 2.1 printed, or where the documentation form comes from. Empty is allowed only for rows whose status explains itself. |
| `st` | enum | `ok` Verified · `bad` Fails · `mac` Macro only · `doc` Documented · `ref` Seen in code. A status changes only after a test in E3D. |
| `key` | string | Search key (may be non-Latin; empty on some rows). |

`dates` and `runs` exist inside the build pipeline (from the console's own registry) and are **stripped before anything
goes out** — run numbers and dates are internal since 27.10.

## Optional future field

| Field | Type | Meaning |
|---|---|---|
| `versions` | object | `{ "2.1": "ok", "3.1": "differs" }` — per-version outcome, filled from test reports. Not emitted yet: nothing to fill it from. |

## Top level (`register.json`)

`about`, `e3d` (target version), `updated` (date of the latest run), `status` (id → name + meaning per language),
`groups` (`id`, `title`, `desc`, computed `n`), `rows`.

## Invariants checked by CI

- every row's `g` points to an existing group; `groups[].n` equals the actual row count;
- row `id`s are unique; status counts match the README/stats line;
- no run dates or numbers in the public text (27.10 rule);
- no working-project traces (same check as everywhere else).

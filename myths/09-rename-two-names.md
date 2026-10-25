# «RENAME /OLD /NEW renames an element»

**We believed:** A command list said RENAME takes the old and the new name.

**In fact:** There is no two-argument form — «(2,109) Undefined name». Stand on the element and RENAME /NEW (or NAME /NEW).

**Commands:** `RENAME` **Verified** — last run 18 Sep 2026 · `NAME` **Verified** — last run 19 Sep 2026

**What we believed.** A reference list of commands described `RENAME /OLD /NEW`.

**What refuted it.** A run: `RENAME /PMLC-CWAY-T3 /PMLC-CWAY-T5` → `(2,109) Undefined name /PMLC-CWAY-T5`, caret on the second name.

**Why the mistake was possible.** A reference list is a source too, and it can be wrong. The same list had no `MARKDB` in it — which is part of why we believed there was no rollback.

**The lesson.** A list's silence is not evidence of absence, and its statements are not evidence of presence. Run it.

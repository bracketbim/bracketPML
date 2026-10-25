# «The manual says if works in the Command Line»

**We believed:** if, do and handle work when typed or pasted into the Commands window — the manual says input from the keyboard and from a macro is treated the same.

**In fact:** A plain paste runs each line alone, and if fails with «PML: Invalid syntax». Blocks work through Paste as Macro.

**Commands:** `IF` **Macro only** · `DO` **Macro only** · `HANDLE` **Macro only**

**What we believed.** First a guess that blocks fail in the Command Line. Then a quote from the PML guide — «The program does not discriminate between input from the GUI, the keyboard, or a macro file» — and we wrote that we had been wrong.

**What a run showed.** `if (!!t GT 1) then` → `PML: Invalid syntax in the current context`. The same for `do … enddo` and `endhandle`. The first guess was right; the «correction» from the manual was not.

**Why the mistake was possible.** The manual describes the PML language as a whole. The Command Line field does not accept all of it. A quote from a manual is a statement about the product, not about your installation.

**The lesson.** Trust in this order: a run > `$Q` on the real machine > documentation > real code from GitHub > reasoning.

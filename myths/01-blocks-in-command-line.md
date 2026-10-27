# «The manual says if works in the Command Line»

**We believed:** if, do and handle work when typed or pasted into the Commands window — the manual says input from the keyboard and from a macro is treated the same.

**In fact:** A plain paste runs each line alone, and if fails with «PML: Invalid syntax». Blocks work through Paste as Macro.

**Commands:** `IF` **Macro only** · `DO` **Macro only** · `HANDLE` **Macro only**

**What we believed.** First a guess that blocks fail in the Command Line. Then a quote from the PML guide (Software Customisation Guide 2.1, 8.08.2) — «The program does not discriminate between input from the GUI, the keyboard, or a macro file» — and we wrote that we had been wrong.

**What E3D 2.1 showed.** `if (!!t GT 1) then` → `PML: Invalid syntax in the current context`. The same for `do … enddo` and `endhandle`. The first guess was right; the «correction» from the manual was not.

**Why the mistake was possible.** The manual describes the PML language as a whole. The Command Line field does not accept all of it. A quote from a manual is a statement about the product, not about your installation.

**The lesson.** Trust in this order: a test in E3D > `$Q` on the real machine > documentation > real code from GitHub > reasoning.

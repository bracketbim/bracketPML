# «There is no GOTO command»

**We believed:** GOTO does not exist in PML — GOTO /NAME gives a syntax error.

**In fact:** GOTO exists, but it follows a reference attribute (GOTO OWNER, GOTO PARENT…), not a name.

**Commands:** `GOTO` **Fails** — last run 26 Oct 2026

**What we believed.** No such command: `GOTO /NAME` → `CP: Syntax error`.

**What refuted it.** `GOTO $Q` prints its continuations: `CFDPROPERTY`, `LFDPROPERTY`, `TFDPROPERTY`, `FRSTWORLD`, `PARENT`, `SPLPARENT`, `CLCONNECTIONS` and «any reference attribute». The command exists — it just does not take a name. Going by name is typing the name itself.

**Why the mistake was possible.** The same as with `UNDO`, and that should be alarming: a failed run of **one form** was spread over the whole command.

**The lesson.** Before writing «does not exist», ask `$Q`. It prints what your build actually accepts.

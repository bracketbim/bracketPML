# «E3D has no rollback»

**We believed:** There is no way to undo a change in E3D from PML; the only safety net is not saving and leaving with QUIT.

**In fact:** The rollback is MARKDB / UNDODB. One UNDODB takes back everything under a mark — until SAVEWORK.

**Commands:** `UNDO` **Fails** · `MARKDB` **Verified** · `UNDODB` **Verified**

**What we believed** for two months: `UNDO` gives `CP: Syntax error`, so there is no undo.

**What refuted it.** A search through real PML code found `UNDODB` — it had been in our own corpus all along. A test in E3D 2.1 confirmed `MARKDB` / `UNDODB`.

**Why the mistake was possible.** We searched for the **word** `UNDO`, not for the **mechanism** of rollback. The question «is there a command UNDO» has a different answer from «is there a way back».

**The lesson.** A failed test closes **one line**, not the topic. Write «there is no command named `UNDO`», not «there is no rollback». See [guard](../modules/guard/README.md).

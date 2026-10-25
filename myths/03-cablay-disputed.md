# «CABLAY does not work»

**We believed:** CABLAY is broken or a «disputed» attribute — setting it gives a syntax error.

**In fact:** The caret was on the value. CABLAY |CEN| works; text values need bars.

**Commands:** `CABLAY` **Verified** — last run 27 Aug 2026

**What we believed** for two days, in two versions: first «the command does not work», then «a disputed attribute».

**What refuted it.** Reading the same error more carefully:

```
CP: Syntax error
CABLAY ^^CEN
```

The caret stands on the **value**. `CABLAY |CEN|` — text in vertical bars, like `DESC` — works.

**Why the mistake was possible.** The error was read as «something is wrong with this line», while E3D pointed at one exact word. The right question was not «does the command work», but «how is the value written».

**The lesson.** Read the caret `^^`. It points at a word, not at a line.

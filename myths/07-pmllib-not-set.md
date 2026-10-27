# «PMLLIB is not set»

**We believed:** The PMLLIB variable is empty, so .pmlfnc functions and forms are out of reach.

**In fact:** Q EVAR |PMLLIB| inside E3D prints about ten paths. (They are not writable for a normal user — so the conclusion held, by accident.)

**Commands:** `Q` **Verified** · `EVAR` **Verified**

**What we believed.** `%PMLLIB%` is empty — checked with `echo %PMLLIB%` in a Windows command prompt.

**What refuted it.** `Q EVAR |PMLLIB|` in the Commands window printed about ten paths. E3D has its own environment variables, and the Windows prompt does not know about them.

**Why the mistake was possible.** The check was done in a different environment from the one the claim was about. A wrong check is worse than none: it looks like evidence.

**The twist.** Going through every path showed there is no write access to any of them — the original **conclusion** («your own functions are out of reach») was right, on a completely wrong basis. That happens too, and it does not make the method any better.

**The lesson.** Check in the environment you make the claim about.

# «Q MEM ATT prints the attributes of the members»

**We believed:** One Q MEM ATT on a route prints all its points with their positions and radii.

**In fact:** Q MEM ATT is Q MEM plus Q ATT of the CURRENT element. Members' attributes are not there.

**Commands:** `Q` **Verified** — last run 28 Aug 2026

**What we believed.** A run showed «members and attributes in one command». From it we built a convenient conclusion: «so it prints the members' attributes too» — it would solve the task in one line.

**What refuted it.** Two dumps we already had: after the list of members came the attributes of the current element itself.

**Why the mistake was possible.** A fact from a run and a conclusion from that fact are different things. Nobody had run the command on a route, and the two dumps that said otherwise were not re-read — because the conclusion was convenient.

**The lesson.** A conclusion from a fact needs its own run. Especially a convenient one. To read the points of a route, go to each `POINTR`.

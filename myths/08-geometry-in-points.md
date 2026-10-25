# «Tray geometry belongs in the route points»

**We believed:** Height and side offset of a tray rack go into the route points; the branch POS stays at zero.

**In fact:** The numbers matched — but the edit gizmo sits on the branch POS. With POS at zero, every gizmo landed on the first tray.

**Commands:** `POS` **Verified** — last run 29 Sep 2026

**What we believed.** After a run where every coordinate in the database came out right: all geometry goes into the route points, branch `POS` stays at zero.

**What refuted it.** A designer working with the model: when editing an upper tray, the gizmo sits on the axis of the **lowest** tray, not the one being edited.

**Why the mistake was possible.** The check compared numbers, and the numbers were right. The defect lived where nobody looked — in how the model is edited with the mouse. The gizmo attaches to the `POS` of the `CWBRAN` itself.

**The lesson.** Matching numbers are not enough. Ask **which element carries the value** — the interface hooks onto the element.

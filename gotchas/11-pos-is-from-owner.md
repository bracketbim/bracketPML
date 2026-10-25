# POS put the element in the wrong place

> POS without WRT is relative to the owner, not the world. For a primitive it is the centre. Q POS prints in the owner's system too.

**E3D prints:** `(no error — the element is just somewhere else)`

**Commands:** `POS` **Verified** — last run 29 Sep 2026 · `Q` **Verified** — last run 28 Aug 2026

## What you see

`POS E 0 N 0 U 0` on a tray in a zone that sits at `E 10000`, and the tray lands at world `E 10000`, not at zero. Or a box created with `POS E 0 N 0 U 0` sticks out half its size in every direction.

## Why

- `POS` **without `WRT`** is measured **from the owner**. In a zone shifted to `E 10000`, `POS E 0` is world `E 10000`. `Q POS` also prints in the owner's system; `Q POS WRT WORLD` prints world coordinates.
- Inside a `SUBE`, a primitive's `POS` is from the `SUBE`.
- For a primitive (`BOX`, `CYLINDER`), `POS` is its **centre**: a 1000 mm cube at zero spans −500…+500.
- No minus signs needed: `W`, `S`, `D` are the negative directions.

## The rule

Say which system you mean:

```
POS E 0 N 0 U 0 WRT WORLD
Q POS WRT WORLD
```

`WRT /element` measures from another element, and the name can come from a variable: `POS E 1000 N 0 U 0 WRT $!!x`. `POS $Q` does not list `WRT` at all — the grammar printout is incomplete, and its silence is no argument against a command.

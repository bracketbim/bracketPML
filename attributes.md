# Attributes

The standard attributes of AVEVA E3D 2.1 elements that we know: the list, owners and members follow the Data Model Reference Manual 2.1 (page reference for each type); the descriptions, statuses and notes are ours. «Accepts» is what `<ATTRIBUTE> $Q` printed in E3D 2.1 (run of 26 Oct 2026); empty — not asked yet. User-defined attributes of a project (`:NAME`) are not here.

| Status | Meaning |
|---|---|
| **Command verified** | The command that writes or reads it ran in E3D — on at least one element type; the register row says which. |
| **In a real model** | Printed by Q ATT on a real model; not written by us yet. |
| **Manual only** | In the Data Model Reference Manual 2.1; not in our model dumps. |

## Cable trays

### CWAY — Cable way

The container of a cable tray route. It holds branches (CWBRAN); the geometry lives in them, not here.

Owners: CONVEYOR, ZONE · Members: CWBRAN · DMRM 5.09.129

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Cablayout` | Cable arrangement setting; the value is text in \|bars\| | text in \|bars\| or 'quotes' | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `MaxCab` | Upper limit of cables | a number | Command verified |  |
| `MaxLay` | Upper limit of cable layers | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified | A code word, up to 4 characters by DMRM. |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Underground` | Flag: the route runs below ground | TRUE / FALSE (YES / NO, ON / OFF) | In a real model |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### CWBRAN — Cable way branch

One run of tray. Head and tail have no coordinates of their own: the first and last points of its RPATH set them. HPOS / TPOS on a CWBRAN give an error — verified by a run.

Owners: CWAY · Members: RBRAN, CTMTRL, HATTA, RPATH, RTFEAT, SEGSEQ, TATTA · DMRM 5.09.130

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Bangle` | Turn of the section about the branch axis (beta) | a number | Command verified |  |
| `BRadius` | Radius of the bends along the branch | a number | Command verified |  |
| `Cablayout` | Cable arrangement setting; the value is text in \|bars\| | text in \|bars\| or 'quotes' | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `CWJusLine` | Which line of the tray section the route follows | a word or text | Command verified |  |
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Desparam` | A list of numeric design values | a number | Command verified |  |
| `HCRef` | What the start of the branch is connected to | a reference: /NAME, =ref or NULREF | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `MatType` | Kind of tray material | text in \|bars\| or 'quotes' | Command verified |  |
| `MaxCab` | Upper limit of cables | a number | Command verified |  |
| `MaxLay` | Upper limit of cable layers | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `VHeight` | Height of the tray section | a number | Command verified | Written like VWidth. |
| `VWidth` | Width of the tray section | a number | Command verified | Units are allowed: VWIDTH 700mm (run of 22 Sep). A number in bars is a syntax error. |
| `Area` | The area number the element belongs to | a number | In a real model |  |
| `CExs` | Extra allowance, in percent, for cables passing through | a number | In a real model |  |
| `CloseFlag` | Flag: the branch forms a closed loop | TRUE / FALSE (YES / NO, ON / OFF) | In a real model |  |
| `Extvolume` | Space taken by the tray material | a number | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `IClass` | The class used when checking clashes | text in \|bars\| or 'quotes' | In a real model |  |
| `MaxFil` | The highest allowed fill, in percent | a number | In a real model |  |
| `Number` | A numeric label of the element | a number | In a real model |  |
| `Resvolume` | Space kept free around the tray | a number | In a real model |  |
| `Rllogical` | Logical values used by rules | a value or an expression | In a real model |  |
| `TCRef` | What the end of the branch is connected to | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Underground` | Flag: the route runs below ground | TRUE / FALSE (YES / NO, ON / OFF) | In a real model |  |
| `VShape` | Shape of the tray section | a number | In a real model |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`, `AHeight`, `UseMaterial`, `Fixedb`

### RPATH — Route path

NEW RPATH does not create the first point: Q MEM right after it is unset. Points are added one by one with NEW POINTR — verified by a run (26 Aug).

Owners: BPANEL, BPOPEN, CABLE, CTWALL, CWBRAN, HANDRA, PLOPEN, PLTFRM, RBRAN, RUTVOLUME, STRFLT, STRLNG, WLOPEN · Members: CURVE, EXTGEO, POINTR, RSECT · DMRM 5.09.143

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Drnend` | Direction of the cut plane at the end of the section | a direction; ORI as Y IS N AND Z IS U | In a real model |  |
| `Drnstart` | Direction of the cut plane at the start of the section | a direction; ORI as Y IS N AND Z IS U | In a real model |  |
| `Ydirection` | Which way the Y axis of the section should point | a direction; ORI as Y IS N AND Z IS U | In a real model |  |

### POINTR — Point on a path

A point of the route. Its POS is measured from the owner, like any POS without WRT.

Owners: RPATH · Members: — · DMRM 5.09.138

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Fradius` | Fillet radius at this point, measured on the tray axis | a number | Command verified | Measured on the tray AXIS, not on its edge (run of 29 Sep); Q FRADIUS prints a number (run of 28 Sep). |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `SIGREF` | Link to a significant point | a reference: /NAME, =ref or NULREF | In a real model |  |
| `PointType` | Kind of route point |  | Manual only |  |

### HATTA — Head attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.135

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |

### TATTA — Tail attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.146

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |

### CONSEQ — Connectivity sequence

A branch made by the standard tool has one; a branch created by hand does not get one. What it is needed for — not found out yet.

Owners: CWBRAN, RBRAN · Members: RATTA · DMRM 5.09.119

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |

### CTMTRL — Cable tray material

Owners: CWBRAN · Members: CTBEND, CTCOUP, CTCROS, CTREDU, CTRISE, CTSTRA, CTTEE · DMRM 5.09.792

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Desparam` | A list of numeric design values | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `CTSPE` | Link to the cable tray specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `FGap` | Gap: the first one | a number | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `IGap` | Gap: the ones in between | a number | In a real model |  |
| `LGap` | Gap: the last one | a number | In a real model |  |
| `TierHeight` | Height of each tray tier above the route | a number | In a real model |  |
| `TrayH` | How high the trays are | a number | In a real model |  |
| `TrayW` | How wide the trays are | a number | In a real model |  |


## Equipment

### EQUIPMENT — Equipment

Can own NOZZLEs besides the usual primitives — that is what sets it apart from other carriers of geometry.

Owners: CONVEYOR, ZONE · Members: AIDGROUP, BOX, BPANEL, CONE, CTORUS, CYLINDER, DDSE, DIMGROUP, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, SUBEQUIPMENT, TEXT, TMPLATE · DMRM 5.09.184

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified | EQUI and SUBE have it, BOX does not; 250 characters — «Too many values» (run of 1 Oct). |
| `Desparam` | A list of numeric design values | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified | ORI on an EQUI turns it together with its children (run of 24 Sep); with an angle: ORI Y IS N AND Z IS E 45 U (run of 29 Sep). |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified | Written and inherited by a copy made in E3D — verified by a run. |
| `Spref` | Link to the component specification | a reference: /NAME, =ref or NULREF | Command verified |  |
| `Area` | The area number the element belongs to | a number | In a real model |  |
| `Built` | Flag: built or not yet built | TRUE / FALSE (YES / NO, ON / OFF) | In a real model |  |
| `Dscode` | Code of the design standard | text in \|bars\| or 'quotes' | In a real model |  |
| `Fstatus` | Not explained in the manual | text in \|bars\| or 'quotes' | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Inprtref` | Paint on the inside (link) | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Inschedule` | Schedule of inspections | text in \|bars\| or 'quotes' | In a real model |  |
| `Ispec` | Link to the insulation specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Mdsysf` | Links to model and design elements | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Number` | A numeric label of the element | a number | In a real model |  |
| `Ouprtref` | Paint on the outside (link) | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Propst` | Links to property sets | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Ptspec` | Link to the paint specification | text in \|bars\| or 'quotes' | In a real model |  |
| `Skey` | Key of the drawing symbol | text in \|bars\| or 'quotes' | In a real model |  |
| `StlRef` | Link to a steel element | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Usrcogravity` | Centre of gravity typed in by hand | a value or an expression | In a real model |  |
| `Usrwcogravity` | Centre of gravity with contents, typed in by hand | a value or an expression | In a real model |  |
| `Usrweight` | Weight typed in by hand | a value or an expression | In a real model |  |
| `Usrwweight` | Weight with contents (wet), typed in by hand | a value or an expression | In a real model |  |
| `Uwmtxt` | Text kept for the weight manager | text in \|bars\| or 'quotes' | In a real model |  |
| `Invfarray` | List of inventory items |  | Manual only |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |
| `Stmf` | Pointer that picks the template |  | Manual only |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### SUBEQUIPMENT — Sub-equipment

The same as EQUIPMENT, but it lives inside one and cannot hold sub-equipment of its own.

Owners: EQUIPMENT · Members: BPANEL, BOX, CONE, CTORUS, CYLINDER, DDSE, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, TEXT, TMPLATE · DMRM 5.09.187

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Desparam` | A list of numeric design values | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Spref` | Link to the component specification | a reference: /NAME, =ref or NULREF | Command verified |  |
| `Area` | The area number the element belongs to | a number | In a real model |  |
| `Built` | Flag: built or not yet built | TRUE / FALSE (YES / NO, ON / OFF) | In a real model |  |
| `Dscode` | Code of the design standard | text in \|bars\| or 'quotes' | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Inschedule` | Schedule of inspections | text in \|bars\| or 'quotes' | In a real model |  |
| `Ispec` | Link to the insulation specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Mdsysf` | Links to model and design elements | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Number` | A numeric label of the element | a number | In a real model |  |
| `Propst` | Links to property sets | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Ptspec` | Link to the paint specification | text in \|bars\| or 'quotes' | In a real model |  |
| `Skey` | Key of the drawing symbol | text in \|bars\| or 'quotes' | In a real model |  |
| `StlRef` | Link to a steel element | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Usrcogravity` | Centre of gravity typed in by hand | a value or an expression | In a real model |  |
| `Usrwcogravity` | Centre of gravity with contents, typed in by hand | a value or an expression | In a real model |  |
| `Usrweight` | Weight typed in by hand | a value or an expression | In a real model |  |
| `Usrwweight` | Weight with contents (wet), typed in by hand | a value or an expression | In a real model |  |
| `Uwmtxt` | Text kept for the weight manager | text in \|bars\| or 'quotes' | In a real model |  |
| `Invfarray` | List of inventory items |  | Manual only |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |
| `Stmf` | Pointer that picks the template |  | Manual only |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

### NOZZLE — Nozzle

A connection point on equipment, built from a catalogue component (Catref).

Owners: EQUIPMENT, SUBEQUIPMENT, TMPLATE · Members: DDSE, DPSET, TMPLATE · DMRM 5.09.185

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Desparam` | A list of numeric design values | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `Bselector` | Text that picks which bolts the connection takes | text in \|bars\| or 'quotes' | In a real model |  |
| `Catref` | Points to the catalogue component this element is drawn from | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Cref` | Points to whatever is connected here, such as a pipe branch | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Duty` | Free text: what the connection carries | text in \|bars\| or 'quotes' | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Inprtref` | Paint on the inside (link) | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Ispec` | Link to the insulation specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Ouprtref` | Paint on the outside (link) | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Pressure` | Design pressure of the connection | a number | In a real model |  |
| `Radius` | A radius of the shape (for a dish, the knuckle) | a number | In a real model |  |
| `Temperature` | Design temperature of the connection | a number | In a real model |  |
| `TPressure` | Pressure used to test the connection | a number | In a real model |  |
| `Invfarray` | List of inventory items |  | Manual only |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |
| `SloDirection` | A list of directions the slope follows |  | Manual only |  |
| `Stmf` | Pointer that picks the template |  | Manual only |  |


## Primitives

### BOX — Box

A block of Xlength by Ylength by Zlength. POS is the centre of the box.

Owners: EQUIPMENT, ENVLOP, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.547

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Xlength` | Size along the local X axis | a number | Command verified |  |
| `Ylength` | Size along the local Y axis | a number | Command verified |  |
| `Zlength` | Size along the local Z axis | a number | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### CYLINDER — Cylinder

Diameter and Height; POS is the centre. Without ORI the axis is Z of the owner.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.550

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### CONE — Cone

Two diameters, Dtop and Dbottom, and a Height between them.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.548

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Dbottom` | Diameter at the base end | a number | In a real model |  |
| `Dtop` | Diameter at the far end | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### SNOUT — Snout

A cone whose top can be shifted off the axis (Xoffset, Yoffset).

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.570

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Dbottom` | Diameter at the base end | a number | In a real model |  |
| `Dtop` | Diameter at the far end | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xoffset` | How far the top is shifted from the base along local X | a number | In a real model |  |
| `Yoffset` | How far the top is shifted from the base along local Y | a number | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### DISH — Dish

A dished end: Diameter, Height and the knuckle Radius.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.551

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Radius` | A radius of the shape (for a dish, the knuckle) | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### PYRAMID — Pyramid

A rectangular base and top of their own sizes; the top can be shifted.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.566

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xbottom` | Size of the base along local X | a number | In a real model |  |
| `Xoffset` | How far the top is shifted from the base along local X | a number | In a real model |  |
| `Xtop` | Size of the top face along local X | a number | In a real model |  |
| `Ybottom` | Size of the base along local Y | a number | In a real model |  |
| `Yoffset` | How far the top is shifted from the base along local Y | a number | In a real model |  |
| `Ytop` | Size of the top face along local Y | a number | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### CTORUS — Circular torus

A bend of round section: inner and outer radius and the Angle it sweeps.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.549

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Rinside` | Distance from the torus centre to its inner edge | a number | In a real model |  |
| `Routside` | Distance from the torus centre to its outer edge | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### RTORUS — Rectangular torus

A bend of rectangular section; Height is the section height.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.568

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Rinside` | Distance from the torus centre to its inner edge | a number | In a real model |  |
| `Routside` | Distance from the torus centre to its outer edge | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### SLCYLINDER — Slope-bottomed cylinder

A cylinder whose end faces are tilted (the four shear angles).

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TRNPRI, TMPLATE, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.569

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xbshear` | Tilt of the base face, measured about local X | an angle, or as a direction | In a real model |  |
| `Xtshear` | Tilt of the top face, measured about local X | an angle, or as a direction | In a real model |  |
| `Ybshear` | Tilt of the base face, measured about local Y | an angle, or as a direction | In a real model |  |
| `Ytshear` | Tilt of the top face, measured about local Y | an angle, or as a direction | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### EXTRUSION — Extrusion

A profile drawn as a loop of vertices, pushed out by Height.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: LOOP, NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.553

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### REVOLUTION — Revolution

A profile loop turned about an axis by Angle.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: LOOP, NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION · DMRM 5.09.567

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### POLYHEDRON — Polyhedron

A solid described face by face.

Owners: EQUIPMENT, JNTBOX, PTRACK, PULLPIT, STRUCTURE, SUBEQUIPMENT, SUBSTRUCTURE, SVOLMODEL, TMPLATE, TRNPRI, VOLMODEL · Members: NBOX, NCONE, NCTORUS, NCYLINDER, NDISH, NPOLYHEDRON, NPYRAMID, NREVOLUTION, NRTORUS, NSLCYLINDER, NSNOUT, NXTRUSION, POLFACE, POLPTLIST · DMRM 5.09.565

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |


## Holes (negative primitives)

### NBOX — Negative box

Cut out of its owner primitive; sizes as BOX.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.573

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Xlength` | Size along the local X axis | a number | Command verified |  |
| `Ylength` | Size along the local Y axis | a number | Command verified |  |
| `Zlength` | Size along the local Z axis | a number | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NCYLINDER — Negative cylinder

A round hole in its owner; sizes as CYLINDER.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.576

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NCONE — Negative cone

Cut out of its owner; sizes as CONE.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.574

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Dbottom` | Diameter at the base end | a number | In a real model |  |
| `Dtop` | Diameter at the far end | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NSNOUT — Negative snout

Cut out of its owner; sizes as SNOUT.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.583

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Dbottom` | Diameter at the base end | a number | In a real model |  |
| `Dtop` | Diameter at the far end | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xoffset` | How far the top is shifted from the base along local X | a number | In a real model |  |
| `Yoffset` | How far the top is shifted from the base along local Y | a number | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NDISH — Negative dish

Cut out of its owner; sizes as DISH.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.577

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Radius` | A radius of the shape (for a dish, the knuckle) | a number | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NPYRAMID — Negative pyramid

Cut out of its owner; sizes as PYRAMID.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.579

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xbottom` | Size of the base along local X | a number | In a real model |  |
| `Xoffset` | How far the top is shifted from the base along local X | a number | In a real model |  |
| `Xtop` | Size of the top face along local X | a number | In a real model |  |
| `Ybottom` | Size of the base along local Y | a number | In a real model |  |
| `Yoffset` | How far the top is shifted from the base along local Y | a number | In a real model |  |
| `Ytop` | Size of the top face along local Y | a number | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NCTORUS — Negative circular torus

Cut out of its owner; sizes as CTORUS.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.575

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Rinside` | Distance from the torus centre to its inner edge | a number | In a real model |  |
| `Routside` | Distance from the torus centre to its outer edge | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NRTORUS — Negative rectangular torus

Cut out of its owner; sizes as RTORUS.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.581

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Angle` | How far the shape sweeps or turns, in degrees | an angle, or as a direction | In a real model |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Rinside` | Distance from the torus centre to its inner edge | a number | In a real model |  |
| `Routside` | Distance from the torus centre to its outer edge | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |

### NSLCYLINDER — Negative slope-bottomed cylinder

Cut out of its owner; sizes as SLCYLINDER.

Owners: BOX, BPANEL, CONE, CTORUS, CYLINDER, DISH, EXTRUSION, FLOOR, GWALL, PANEL, POLYHEDRON, PYRAMID, REVOLUTION, RTORUS, SCREED, SLCYLINDER, SNOUT, TMPLATE, TRNPRI · Members: — · DMRM 5.09.582

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Diameter` | Full width of the round section | a number | Command verified |  |
| `Height` | Length along the local Z axis | a number | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | a number | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | a number, or HARD / SOFT / NONE | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `RepCount` | Counter used when a template rule repeats the element | a number | In a real model |  |
| `Tmrref` | Points back to the template element that repeats this one | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Xbshear` | Tilt of the base face, measured about local X | an angle, or as a direction | In a real model |  |
| `Xtshear` | Tilt of the top face, measured about local X | an angle, or as a direction | In a real model |  |
| `Ybshear` | Tilt of the base face, measured about local Y | an angle, or as a direction | In a real model |  |
| `Ytshear` | Tilt of the top face, measured about local Y | an angle, or as a direction | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |


## Where everything lives

### ZONE — Zone

Owners: APPLDATA, SITE, ZONE · Members: AIDGROUP, BOUNDARY, CABLE, RBRAN, CWAY, CONVEYOR, DATUM, DDSE, DIMGROUP, DPSET, DRAWING, EQUIPMENT, HVAC, JNTBOX, PIPE, PTRACK, PULLPIT, PVOLUME, RBRAN, RESTRAINT, RPLANE, STRUCTURE, SUPPORT, TEXT, TRNMOD, UPANEL, VOLMODEL, XGEOMETRY, ZONE · DMRM 5.09.082

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Area` | The area number the element belongs to | a number | In a real model |  |
| `BendMacReference` | Link to the pipe bending machine | a reference: /NAME, =ref or NULREF | In a real model |  |
| `DUnion` | Flag used by DRAFT for joining element details | a number | In a real model |  |
| `Facode` | Not explained in the manual | text in \|bars\| or 'quotes' | In a real model |  |
| `Fstatus` | Not explained in the manual | text in \|bars\| or 'quotes' | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Ispec` | Link to the insulation specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Module` | The module the element belongs to | text in \|bars\| or 'quotes' | In a real model |  |
| `Number` | A numeric label of the element | a number | In a real model |  |
| `Offsrf` | Datum point of the model offset | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Pspec` | Link to the piping specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Rlstored` | Rules saved by ROUTER | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Tspec` | Link to the trace heating specification | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |
| `SpcRef` | Link to a space element |  | Manual only |  |
| `Stmf` | Pointer that picks the template |  | Manual only |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

In a real dump but not in the manual: `Type`, `ActType`, `Lock`, `Owner`

### SITE — Site

Owners: WORLD · Members: AIDGROUP, BOUNDARY, DDSE, DIMGROUP, DPSET, DRAWING, GRDMODEL, TEXT, TRNMOD, ZONE · DMRM 5.09.079

| Attribute | What it is | Accepts | Status | Note |
|---|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | text in \|bars\| or 'quotes' | Command verified |  |
| `Name` | The element’s name; it starts with a slash | a name: /NAME | Command verified |  |
| `Orientation` | Which way the element’s axes point | a direction; ORI as Y IS N AND Z IS U | Command verified |  |
| `Position` | Where the element sits, measured from its owner | a position: E … N … U … (WRT …) | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | a word or text | Command verified |  |
| `Area` | The area number the element belongs to | a number | In a real model |  |
| `Function` | Free text: what the element is for | text in \|bars\| or 'quotes' | In a real model |  |
| `Module` | The module the element belongs to | text in \|bars\| or 'quotes' | In a real model |  |
| `Number` | A numeric label of the element | a number | In a real model |  |
| `Rlstored` | Rules saved by ROUTER | a reference: /NAME, =ref or NULREF | In a real model |  |
| `Orrf` | Origin link used by templates |  | Manual only |  |
| `Stmf` | Pointer that picks the template |  | Manual only |  |
| `Uuidia` | Globally unique ID of the element |  | Manual only |  |

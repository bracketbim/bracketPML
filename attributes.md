# Attributes

The standard attributes of AVEVA E3D 2.1 elements that we know: the list, owners and members follow the Data Model Reference Manual 2.1 (page reference for each type); the descriptions, statuses and notes are ours. User-defined attributes of a project (`:NAME`) are not here.

| Status | Meaning |
|---|---|
| **Command verified** | The command that writes or reads it ran in E3D — on at least one element type; the register row says which. |
| **In a real model** | Printed by Q ATT on a real model; not written by us yet. |
| **Manual only** | In the Data Model Reference Manual 2.1; not in our model dumps. |

## Cable trays

### CWAY — Cable way

The container of a cable tray route. It holds branches (CWBRAN); the geometry lives in them, not here.

Owners: CONVEYOR, ZONE · Members: CWBRAN · DMRM 5.09.129

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Cablayout` | Cable arrangement setting; the value is text in \|bars\| | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `MaxCab` | Upper limit of cables | Command verified |  |
| `MaxLay` | Upper limit of cable layers | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified | A code word, up to 4 characters by DMRM. |
| `Function` | Free text: what the element is for | In a real model |  |
| `Underground` | Flag: the route runs below ground | In a real model |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### CWBRAN — Cable way branch

One run of tray. Head and tail have no coordinates of their own: the first and last points of its RPATH set them. HPOS / TPOS on a CWBRAN give an error — verified by a run.

Owners: CWAY · Members: RBRAN, CTMTRL, HATTA, RPATH, RTFEAT, SEGSEQ, TATTA · DMRM 5.09.130

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Bangle` | Turn of the section about the branch axis (beta) | Command verified |  |
| `BRadius` | Radius of the bends along the branch | Command verified |  |
| `Cablayout` | Cable arrangement setting; the value is text in \|bars\| | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `CWJusLine` | Which line of the tray section the route follows | Command verified |  |
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Desparam` | A list of numeric design values | Command verified |  |
| `HCRef` | What the start of the branch is connected to | Command verified |  |
| `Level` | The range of drawing levels at which the element is shown | Command verified |  |
| `MatType` | Kind of tray material | Command verified |  |
| `MaxCab` | Upper limit of cables | Command verified |  |
| `MaxLay` | Upper limit of cable layers | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Obstruction` | How solid the element counts in clash checks | Command verified |  |
| `Orientation` | Which way the element’s axes point | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified |  |
| `VHeight` | Height of the tray section | Command verified | Written like VWidth. |
| `VWidth` | Width of the tray section | Command verified | Units are allowed: VWIDTH 700mm (run of 22 Sep). A number in bars is a syntax error. |
| `Area` | The area number the element belongs to | In a real model |  |
| `CExs` | Extra allowance, in percent, for cables passing through | In a real model |  |
| `CloseFlag` | Flag: the branch forms a closed loop | In a real model |  |
| `Extvolume` | Space taken by the tray material | In a real model |  |
| `Function` | Free text: what the element is for | In a real model |  |
| `IClass` | The class used when checking clashes | In a real model |  |
| `MaxFil` | The highest allowed fill, in percent | In a real model |  |
| `Number` | A numeric label of the element | In a real model |  |
| `Resvolume` | Space kept free around the tray | In a real model |  |
| `Rllogical` | Logical values used by rules | In a real model |  |
| `TCRef` | What the end of the branch is connected to | In a real model |  |
| `Underground` | Flag: the route runs below ground | In a real model |  |
| `VShape` | Shape of the tray section | In a real model |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`, `AHeight`, `UseMaterial`, `Fixedb`

### RPATH — Route path

NEW RPATH does not create the first point: Q MEM right after it is unset. Points are added one by one with NEW POINTR — verified by a run (26 Aug).

Owners: BPANEL, BPOPEN, CABLE, CTWALL, CWBRAN, HANDRA, PLOPEN, PLTFRM, RBRAN, RUTVOLUME, STRFLT, STRLNG, WLOPEN · Members: CURVE, EXTGEO, POINTR, RSECT · DMRM 5.09.143

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Drnend` | Direction of the cut plane at the end of the section | Manual only |  |
| `Drnstart` | Direction of the cut plane at the start of the section | Manual only |  |
| `Ydirection` | Which way the Y axis of the section should point | Manual only |  |

### POINTR — Point on a path

A point of the route. Its POS is measured from the owner, like any POS without WRT.

Owners: RPATH · Members: — · DMRM 5.09.138

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Fradius` | Fillet radius at this point, measured on the tray axis | Command verified | Measured on the tray AXIS, not on its edge (run of 29 Sep); Q FRADIUS prints a number (run of 28 Sep). |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Function` | Free text: what the element is for | Manual only |  |
| `PointType` | Kind of route point | Manual only |  |
| `SIGREF` | Link to a significant point | Manual only |  |

### HATTA — Head attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.135

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Function` | Free text: what the element is for | Manual only |  |

### TATTA — Tail attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.146

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Function` | Free text: what the element is for | Manual only |  |

### CONSEQ — Connectivity sequence

A branch made by the standard tool has one; a branch created by hand does not get one. What it is needed for — not found out yet.

Owners: CWBRAN, RBRAN · Members: RATTA · DMRM 5.09.119

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Function` | Free text: what the element is for | Manual only |  |

### CTMTRL — Cable tray material

Owners: CWBRAN · Members: CTBEND, CTCOUP, CTCROS, CTREDU, CTRISE, CTSTRA, CTTEE · DMRM 5.09.792

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Desparam` | A list of numeric design values | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified |  |
| `CTSPE` | Link to the cable tray specification | Manual only |  |
| `FGap` | Gap: the first one | Manual only |  |
| `Function` | Free text: what the element is for | Manual only |  |
| `IGap` | Gap: the ones in between | Manual only |  |
| `LGap` | Gap: the last one | Manual only |  |
| `TierHeight` | Height of each tray tier above the route | Manual only |  |
| `TrayH` | How high the trays are | Manual only |  |
| `TrayW` | How wide the trays are | Manual only |  |


## Equipment

### EQUIPMENT — Equipment

Can own NOZZLEs besides the usual primitives — that is what sets it apart from other carriers of geometry.

Owners: CONVEYOR, ZONE · Members: AIDGROUP, BOX, BPANEL, CONE, CTORUS, CYLINDER, DDSE, DIMGROUP, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, SUBEQUIPMENT, TEXT, TMPLATE · DMRM 5.09.184

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified | EQUI and SUBE have it, BOX does not; 250 characters — «Too many values» (run of 1 Oct). |
| `Desparam` | A list of numeric design values | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Orientation` | Which way the element’s axes point | Command verified | ORI on an EQUI turns it together with its children (run of 24 Sep); with an angle: ORI Y IS N AND Z IS E 45 U (run of 29 Sep). |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified | Written and inherited by a copy made in E3D — verified by a run. |
| `Spref` | Link to the component specification | Command verified |  |
| `Area` | The area number the element belongs to | In a real model |  |
| `Built` | Flag: built or not yet built | In a real model |  |
| `Dscode` | Code of the design standard | In a real model |  |
| `Fstatus` | Not explained in the manual | In a real model |  |
| `Function` | Free text: what the element is for | In a real model |  |
| `Inprtref` | Paint on the inside (link) | In a real model |  |
| `Inschedule` | Schedule of inspections | In a real model |  |
| `Ispec` | Link to the insulation specification | In a real model |  |
| `Mdsysf` | Links to model and design elements | In a real model |  |
| `Number` | A numeric label of the element | In a real model |  |
| `Ouprtref` | Paint on the outside (link) | In a real model |  |
| `Propst` | Links to property sets | In a real model |  |
| `Ptspec` | Link to the paint specification | In a real model |  |
| `Skey` | Key of the drawing symbol | In a real model |  |
| `StlRef` | Link to a steel element | In a real model |  |
| `Usrcogravity` | Centre of gravity typed in by hand | In a real model |  |
| `Usrwcogravity` | Centre of gravity with contents, typed in by hand | In a real model |  |
| `Usrweight` | Weight typed in by hand | In a real model |  |
| `Usrwweight` | Weight with contents (wet), typed in by hand | In a real model |  |
| `Uwmtxt` | Text kept for the weight manager | In a real model |  |
| `Invfarray` | List of inventory items | Manual only |  |
| `Orrf` | Origin link used by templates | Manual only |  |
| `Stmf` | Pointer that picks the template | Manual only |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### SUBEQUIPMENT — Sub-equipment

The same as EQUIPMENT, but it lives inside one and cannot hold sub-equipment of its own.

Owners: EQUIPMENT · Members: BPANEL, BOX, CONE, CTORUS, CYLINDER, DDSE, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, TEXT, TMPLATE · DMRM 5.09.187

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Desparam` | A list of numeric design values | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Orientation` | Which way the element’s axes point | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified |  |
| `Spref` | Link to the component specification | Command verified |  |
| `Area` | The area number the element belongs to | Manual only |  |
| `Built` | Flag: built or not yet built | Manual only |  |
| `Dscode` | Code of the design standard | Manual only |  |
| `Function` | Free text: what the element is for | Manual only |  |
| `Inschedule` | Schedule of inspections | Manual only |  |
| `Invfarray` | List of inventory items | Manual only |  |
| `Ispec` | Link to the insulation specification | Manual only |  |
| `Mdsysf` | Links to model and design elements | Manual only |  |
| `Number` | A numeric label of the element | Manual only |  |
| `Orrf` | Origin link used by templates | Manual only |  |
| `Propst` | Links to property sets | Manual only |  |
| `Ptspec` | Link to the paint specification | Manual only |  |
| `Skey` | Key of the drawing symbol | Manual only |  |
| `StlRef` | Link to a steel element | Manual only |  |
| `Stmf` | Pointer that picks the template | Manual only |  |
| `Usrcogravity` | Centre of gravity typed in by hand | Manual only |  |
| `Usrwcogravity` | Centre of gravity with contents, typed in by hand | Manual only |  |
| `Usrweight` | Weight typed in by hand | Manual only |  |
| `Usrwweight` | Weight with contents (wet), typed in by hand | Manual only |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |
| `Uwmtxt` | Text kept for the weight manager | Manual only |  |


## Where everything lives

### ZONE — Zone

Owners: APPLDATA, SITE, ZONE · Members: AIDGROUP, BOUNDARY, CABLE, RBRAN, CWAY, CONVEYOR, DATUM, DDSE, DIMGROUP, DPSET, DRAWING, EQUIPMENT, HVAC, JNTBOX, PIPE, PTRACK, PULLPIT, PVOLUME, RBRAN, RESTRAINT, RPLANE, STRUCTURE, SUPPORT, TEXT, TRNMOD, UPANEL, VOLMODEL, XGEOMETRY, ZONE · DMRM 5.09.082

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Orientation` | Which way the element’s axes point | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified |  |
| `Area` | The area number the element belongs to | In a real model |  |
| `BendMacReference` | Link to the pipe bending machine | In a real model |  |
| `DUnion` | Flag used by DRAFT for joining element details | In a real model |  |
| `Facode` | Not explained in the manual | In a real model |  |
| `Fstatus` | Not explained in the manual | In a real model |  |
| `Function` | Free text: what the element is for | In a real model |  |
| `Ispec` | Link to the insulation specification | In a real model |  |
| `Module` | The module the element belongs to | In a real model |  |
| `Number` | A numeric label of the element | In a real model |  |
| `Offsrf` | Datum point of the model offset | In a real model |  |
| `Pspec` | Link to the piping specification | In a real model |  |
| `Rlstored` | Rules saved by ROUTER | In a real model |  |
| `Tspec` | Link to the trace heating specification | In a real model |  |
| `Orrf` | Origin link used by templates | Manual only |  |
| `SpcRef` | Link to a space element | Manual only |  |
| `Stmf` | Pointer that picks the template | Manual only |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |

In a real dump but not in the manual: `Type`, `ActType`, `Lock`, `Owner`

### SITE — Site

Owners: WORLD · Members: AIDGROUP, BOUNDARY, DDSE, DIMGROUP, DPSET, DRAWING, GRDMODEL, TEXT, TRNMOD, ZONE · DMRM 5.09.079

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Description` | Free text about the element; text with spaces goes in \|bars\| | Command verified |  |
| `Name` | The element’s name; it starts with a slash | Command verified |  |
| `Orientation` | Which way the element’s axes point | Command verified |  |
| `Position` | Where the element sits, measured from its owner | Command verified |  |
| `Purpose` | A short code word for marking and filtering elements | Command verified |  |
| `Area` | The area number the element belongs to | Manual only |  |
| `Function` | Free text: what the element is for | Manual only |  |
| `Module` | The module the element belongs to | Manual only |  |
| `Number` | A numeric label of the element | Manual only |  |
| `Orrf` | Origin link used by templates | Manual only |  |
| `Rlstored` | Rules saved by ROUTER | Manual only |  |
| `Stmf` | Pointer that picks the template | Manual only |  |
| `Uuidia` | Globally unique ID of the element | Manual only |  |

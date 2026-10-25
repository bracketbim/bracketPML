# Attributes

The standard attributes of AVEVA E3D 2.1 elements that we know: the list, owners and members follow the Data Model Reference Manual 2.1 (page reference for each type); the statuses and notes are ours. User-defined attributes of a project (`:NAME`) are not here.

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
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | In a real model |  |
| `Cablayout` | Cable layout | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `Purpose` | Description code word | Command verified | A code word, up to 4 characters by DMRM. |
| `Position` | Position | Command verified |  |
| `MaxLay` | Maximum Layers | Command verified |  |
| `MaxCab` | Maximum Number of cables | Command verified |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Underground` | Underground | In a real model |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### CWBRAN — Cable way branch

One run of tray. Head and tail have no coordinates of their own: the first and last points of its RPATH set them. HPOS / TPOS on a CWBRAN give an error — verified by a run.

Owners: CWAY · Members: RBRAN, CTMTRL, HATTA, RPATH, RTFEAT, SEGSEQ, TATTA · DMRM 5.09.130

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | In a real model |  |
| `Cablayout` | Cable layout | Command verified | A text attribute: CABLAY \|CEN\| — without bars it is a syntax error. |
| `Purpose` | Description code word | Command verified |  |
| `Number` | Number | In a real model |  |
| `Area` | Area | In a real model |  |
| `MaxLay` | Maximum Layers | Command verified |  |
| `MaxCab` | Maximum Number of cables | Command verified |  |
| `Position` | Position | Command verified |  |
| `Orientation` | Orientation | Command verified |  |
| `HCRef` | Head connections | Command verified |  |
| `TCRef` | Tail connections | In a real model |  |
| `Level` | Drawing level | Command verified |  |
| `Obstruction` | Obstruction level | Command verified |  |
| `Desparam` | Design parameters | Command verified |  |
| `Bangle` | Beta angle | Command verified |  |
| `CloseFlag` | True if branch is closed | In a real model |  |
| `CWJusLine` | Cable Way Justification Line | Command verified |  |
| `BRadius` | Bend radius | Command verified |  |
| `VHeight` | Volume height | Command verified | Written like VWidth. |
| `VWidth` | Volume width | Command verified | Units are allowed: VWIDTH 700mm (run of 22 Sep). A number in bars is a syntax error. |
| `VShape` | Volume shape | In a real model |  |
| `Rllogical` | Rule logical array | In a real model |  |
| `CExs` | Percentage excess for passing cables | In a real model |  |
| `MaxFil` | Maximum percentage fill level | In a real model |  |
| `IClass` | Interference class | In a real model |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Resvolume` | Reserved volume | In a real model |  |
| `Extvolume` | Volume for material | In a real model |  |
| `Underground` | Underground | In a real model |  |
| `MatType` | Material type | Command verified |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`, `AHeight`, `UseMaterial`, `Fixedb`

### RPATH — Route path

NEW RPATH does not create the first point: Q MEM right after it is unset. Points are added one by one with NEW POINTR — verified by a run (26 Aug).

Owners: BPANEL, BPOPEN, CABLE, CTWALL, CWBRAN, HANDRA, PLOPEN, PLTFRM, RBRAN, RUTVOLUME, STRFLT, STRLNG, WLOPEN · Members: CURVE, EXTGEO, POINTR, RSECT · DMRM 5.09.143

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Ydirection` | Preferred Y axis direction | Manual only |  |
| `Drnstart` | Plane normal at start of SCTN/GENSEC | Manual only |  |
| `Drnend` | Plane normal at end of SCTN/GENSEC | Manual only |  |

### POINTR — Point on a path

A point of the route. Its POS is measured from the owner, like any POS without WRT.

Owners: RPATH · Members: — · DMRM 5.09.138

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |
| `Position` | Position | Command verified |  |
| `SIGREF` | Significant point reference | Manual only |  |
| `PointType` | Point type | Manual only |  |
| `Fradius` | Fillet radius | Command verified | Measured on the tray AXIS, not on its edge (run of 29 Sep); Q FRADIUS prints a number (run of 28 Sep). |

### HATTA — Head attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.135

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |

### TATTA — Tail attachment point

No coordinates of its own — only name, description and function. Verified by a run.

Owners: CABLE, CTWALL, CWBRAN, HANDRA, RBRAN, RUTVOLUME · Members: — · DMRM 5.09.146

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |

### CONSEQ — Connectivity sequence

A branch made by the standard tool has one; a branch created by hand does not get one. What it is needed for — not found out yet.

Owners: CWBRAN, RBRAN · Members: RATTA · DMRM 5.09.119

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |

### CTMTRL — Cable tray material

Owners: CWBRAN · Members: CTBEND, CTCOUP, CTCROS, CTREDU, CTRISE, CTSTRA, CTTEE · DMRM 5.09.792

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |
| `Purpose` | Description code word | Command verified |  |
| `Desparam` | Design parameters | Command verified |  |
| `CTSPE` | Cable tray specification | Manual only |  |
| `TrayW` | Tray Width | Manual only |  |
| `TrayH` | Tray height | Manual only |  |
| `TierHeight` | Heights of trays measured from path | Manual only |  |
| `FGap` | First offset distance | Manual only |  |
| `IGap` | Intermediate offset distance | Manual only |  |
| `LGap` | Last offset distance | Manual only |  |


## Equipment

### EQUIPMENT — Equipment

Can own NOZZLEs besides the usual primitives — that is what sets it apart from other carriers of geometry.

Owners: CONVEYOR, ZONE · Members: AIDGROUP, BOX, BPANEL, CONE, CTORUS, CYLINDER, DDSE, DIMGROUP, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, SUBEQUIPMENT, TEXT, TMPLATE · DMRM 5.09.184

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified | EQUI and SUBE have it, BOX does not; 250 characters — «Too many values» (run of 1 Oct). |
| `Function` | Function | In a real model |  |
| `Purpose` | Description code word | Command verified | Written and inherited by a copy made in E3D — verified by a run. |
| `Number` | Number | In a real model |  |
| `Area` | Area | In a real model |  |
| `Usrweight` | User entered weight value | In a real model |  |
| `Usrwweight` | User entered wet weight value | In a real model |  |
| `Usrcogravity` | User centre of gravity position | In a real model |  |
| `Usrwcogravity` | User wet centre of gravity position | In a real model |  |
| `Position` | Position | Command verified |  |
| `Orientation` | Orientation | Command verified | ORI on an EQUI turns it together with its children (run of 24 Sep); with an angle: ORI Y IS N AND Z IS E 45 U (run of 29 Sep). |
| `Desparam` | Design parameters | Command verified |  |
| `Built` | Built/Unbuilt flag | In a real model |  |
| `Ispec` | Insulation spec reference | In a real model |  |
| `Uwmtxt` | User weight Manager text | In a real model |  |
| `Dscode` | Design code | In a real model |  |
| `Ptspec` | Paint specification | In a real model |  |
| `Inschedule` | Inspection schedule | In a real model |  |
| `Skey` | Symbol key | In a real model |  |
| `StlRef` | Steel Reference | In a real model |  |
| `Orrf` | Origin reference (for templates) | Manual only |  |
| `Stmf` | Template selection pointer | Manual only |  |
| `Invfarray` | Array of Inventory Items | Manual only |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Propst` | Property set reference array | In a real model |  |
| `Spref` | Component spec reference | Command verified |  |
| `Fstatus` | Fstatus | In a real model |  |
| `Mdsysf` | Reference Array of Model and Design Elements | In a real model |  |
| `Inprtref` | Inside paint reference | In a real model |  |
| `Ouprtref` | Outside paint reference | In a real model |  |

In a real dump but not in the manual: `Type`, `Lock`, `Owner`

### SUBEQUIPMENT — Sub-equipment

The same as EQUIPMENT, but it lives inside one and cannot hold sub-equipment of its own.

Owners: EQUIPMENT · Members: BPANEL, BOX, CONE, CTORUS, CYLINDER, DDSE, DISH, DPSET, DRAWING, ELCONN, EQUCOM, EXTRUSION, LOAPOINT, NOZZLE, PANEL, POHEDRON, POLYHEDRON, PVOLUME, PYRAMID, REVOLUTION, RPLANE, RTORUS, SLCYLINDER, SNOUT, TEXT, TMPLATE · DMRM 5.09.187

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |
| `Purpose` | Description code word | Command verified |  |
| `Number` | Number | Manual only |  |
| `Area` | Area | Manual only |  |
| `Usrweight` | User entered weight value | Manual only |  |
| `Usrwweight` | User entered wet weight value | Manual only |  |
| `Usrcogravity` | User centre of gravity position | Manual only |  |
| `Usrwcogravity` | User wet centre of gravity position | Manual only |  |
| `Uwmtxt` | User weight Manager text | Manual only |  |
| `Position` | Position | Command verified |  |
| `Orientation` | Orientation | Command verified |  |
| `Built` | Built/Unbuilt flag | Manual only |  |
| `Ispec` | Insulation spec reference | Manual only |  |
| `Dscode` | Design code | Manual only |  |
| `Ptspec` | Paint specification | Manual only |  |
| `Inschedule` | Inspection schedule | Manual only |  |
| `Skey` | Symbol key | Manual only |  |
| `StlRef` | Steel Reference | Manual only |  |
| `Desparam` | Design parameters | Command verified |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Propst` | Property set reference array | Manual only |  |
| `Orrf` | Origin reference (for templates) | Manual only |  |
| `Stmf` | Template selection pointer | Manual only |  |
| `Invfarray` | Array of Inventory Items | Manual only |  |
| `Spref` | Component spec reference | Command verified |  |
| `Mdsysf` | Reference Array of Model and Design Elements | Manual only |  |


## Where everything lives

### ZONE — Zone

Owners: APPLDATA, SITE, ZONE · Members: AIDGROUP, BOUNDARY, CABLE, RBRAN, CWAY, CONVEYOR, DATUM, DDSE, DIMGROUP, DPSET, DRAWING, EQUIPMENT, HVAC, JNTBOX, PIPE, PTRACK, PULLPIT, PVOLUME, RBRAN, RESTRAINT, RPLANE, STRUCTURE, SUPPORT, TEXT, TRNMOD, UPANEL, VOLMODEL, XGEOMETRY, ZONE · DMRM 5.09.082

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | In a real model |  |
| `Purpose` | Description code word | Command verified |  |
| `Number` | Number | In a real model |  |
| `Area` | Area | In a real model |  |
| `Position` | Position | Command verified |  |
| `Orientation` | Orientation | Command verified |  |
| `Pspec` | Pipe specification | In a real model |  |
| `Ispec` | Insulation spec reference | In a real model |  |
| `Tspec` | Tracing spec reference | In a real model |  |
| `BendMacReference` | Bending Machine reference | In a real model |  |
| `DUnion` | DRAFT element union detail flag | In a real model |  |
| `Module` | Module | In a real model |  |
| `Orrf` | Origin reference (for templates) | Manual only |  |
| `Stmf` | Template selection pointer | Manual only |  |
| `Offsrf` | Model offset datum | In a real model |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Rlstored` | Array of ROUTER saved rules | In a real model |  |
| `Fstatus` | Fstatus | In a real model |  |
| `Facode` | Facode | In a real model |  |
| `SpcRef` | Reference to a space element | Manual only |  |

In a real dump but not in the manual: `Type`, `ActType`, `Lock`, `Owner`

### SITE — Site

Owners: WORLD · Members: AIDGROUP, BOUNDARY, DDSE, DIMGROUP, DPSET, DRAWING, GRDMODEL, TEXT, TRNMOD, ZONE · DMRM 5.09.079

| Attribute | What it is | Status | Note |
|---|---|---|---|
| `Name` | Name of the element | Command verified |  |
| `Description` | Description of the element | Command verified |  |
| `Function` | Function | Manual only |  |
| `Purpose` | Description code word | Command verified |  |
| `Number` | Number | Manual only |  |
| `Area` | Area | Manual only |  |
| `Position` | Position | Command verified |  |
| `Orientation` | Orientation | Command verified |  |
| `Module` | Module | Manual only |  |
| `Orrf` | Origin reference (for templates) | Manual only |  |
| `Stmf` | Template selection pointer | Manual only |  |
| `Uuidia` | Universally unique identifier | Manual only |  |
| `Rlstored` | Array of ROUTER saved rules | Manual only |  |

# What is new

## 29 Oct 2026

- New: `NEW PIPE / NEW BRAN` — A pipe and its branch (Verified)
- New: `NEW STRU / FRMW / SBFR / SCTN / GENSEC / PANE` — Steel: structure, framework, subframework, section, generic section, panel (Verified)
- New: `MOVE …` — Move the current element (Documented)
- New: `COPY …` — Copy an element (Documented)
- New: `MIRROR PLANE …` — Mirror (Documented)
- New: `ROTATE …` — Rotate (Documented)
- New: `ALIGN …` — Align (Documented)
- New: `CONNECT …` — Connect a head or a tail (Documented)
- New: `DISCONNECT …` — Disconnect (Documented)
- New: `SPLIT …` — Split (Documented)
- New: `ORIENTATE …` — The full word for ORI (Documented)
- New: `POSITION …` — The full word for POS (Documented)
- `handle (41,64)`: the note was updated

## 28 Oct 2026

- `handle any … endhandle`: Seen in code → **Macro only**

## 28 Oct 2026

- `right-click → Paste`: Documented → **Verified**
- `right-click → Paste as Macro`: Documented → **Verified**
- `PML TRACE ON`: Documented → **Verified**
- `REM ALL`: Seen in code → **Verified**
- `AXES ON`: Seen in code → **Verified**
- `$H`: Documented → **Fails**
- `$* comment`: Seen in code → **Verified**
- `if ( !x gt 5 ) then … elseif … else … endif`: Seen in code → **Macro only**
- `if ( !x > 5 and !n.Matchwild('PIPE*') ) then`: Seen in code → **Fails**
- `do !i from 1 to 10`: Seen in code → **Macro only**
- `do !elem values !array`: Seen in code → **Macro only**
- `do !i indices !array`: Seen in code → **Macro only**
- `break`: Seen in code → **Macro only**
- `skip`: Seen in code → **Macro only**
- `break if ( … ) / skip if ( … )`: Documented → **Macro only**
- `handle any … endhandle`: the note was updated
- `elsehandle NONE / elsehandle ANY`: Seen in code → **Macro only**
- `$!!error.text`: Seen in code → **Macro only**
- `define function !!name`: Documented → **Verified**

## 28 Oct 2026

- `REDODB`: Documented → **Verified**
- `ADD ALL WITHIN VOL CE 1000 ALL`: Seen in code → **Verified**

## 27 Oct 2026

- `PML REHASH ALL`: the note was updated
- `OWNER`: the note was updated
- `GOTO OWNER`: the note was updated
- `NEW NBOX`: the note was updated
- `NEW NOZZLE`: the note was updated
- `NEW CONE`: the note was updated
- `NEW NCONE`: the note was updated
- `RADI 500`: the note was updated
- `ANGLE 90`: the note was updated
- `XOFF 100`: the note was updated
- `DTOP 300`: the note was updated
- `LOCK ALL`: the note was updated
- `UNLOCK ALL`: the note was updated
- `ADD CE`: the note was updated
- `UNMARK ALL`: the note was updated
- `COL CE GREEN`: the note was updated
- `AXES AT CE`: the note was updated
- `ALP REQ CLEAR`: the note was updated
- `ENHANCE CE COL RED`: the note was updated
- `console show`: the note was updated
- `ISO3`: the note was updated
- `do !i from 1 to 10 by 2`: the note was updated
- `do while ( !flag )`: the note was updated
- `return error 1 'Could not run'`: the note was updated
- `golabel /label`: the note was updated
- `return`: the note was updated

## 27 Oct 2026

- `OWNER`: Documented → **Verified**
- `RADI 500`: Seen in code → **Verified**
- `ANGLE 90`: Seen in code → **Verified**
- `XOFF 100`: Seen in code → **Verified**
- `DTOP 300`: Documented → **Verified**
- `ALP REQ CLEAR`: Seen in code → **Verified**
- `return error 1 'Could not run'`: Seen in code → **Verified**
- `golabel /label`: Documented → **Verified**
- `return`: Documented → **Verified**

## 26 Oct 2026

- `PML REHASH ALL`: Documented → **Verified**
- `GOTO OWNER`: Documented → **Verified**
- `NEW NBOX`: Documented → **Verified**
- `NEW NOZZLE`: Documented → **Verified**
- `NEW CONE`: Documented → **Verified**
- `NEW NCONE`: Documented → **Verified**
- `LOCK ALL`: Seen in code → **Verified**
- `UNLOCK ALL`: Seen in code → **Verified**
- `ADD CE`: Seen in code → **Verified**
- `UNMARK ALL`: Seen in code → **Verified**
- `COL CE GREEN`: Seen in code → **Verified**
- `AXES AT CE`: Seen in code → **Verified**
- `ENHANCE CE COL RED`: Seen in code → **Verified**
- `console show`: Seen in code → **Verified**
- `ISO3`: the note was updated
- `do !i from 1 to 10 by 2`: Documented → **Verified**
- `do while ( !flag )`: Documented → **Fails**

## 23 Oct 2026 — first release

**194 commands** in the register: **107 verified**, 7 documented failures, 6 macro-only, 38 from documentation and 36 from real code still waiting to be tested in E3D 2.1. Updated 23 Oct 2026.

- 4 modules, 12 gotchas, 9 myths.

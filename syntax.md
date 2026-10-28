# Command syntax

What each command tested in E3D 2.1 takes. The forms and their statuses come from the [register](register.md); the arguments are described only from what E3D 2.1 showed.

## `NAV` — Go to an element

| Argument | What it is |
|---|---|
| `/NAME` | The full name with the leading slash. Without the slash E3D does not navigate — silently. |
| `=REF` | A stable reference like =12345678/7844. It does not shift when elements move or are renamed — use it for bulk work. |
| `TYPE n` | The n-th member of that type inside the current element: RPATH 1, then POINTR 2. |
| `TYPE n OF owner` | n is counted among ALL members of the owner and shifts when they move. |

The element becomes current (CE).

**Forms**

- `/PMLC-CWAY-T1` — Verified · Go to an element by name
- `EQUIPMENT 2 of :EXTZONE /PMLC` — Verified · Go to an unnamed element by number
- `=12345678/7844` — Verified · Go by stable reference

## `NEW` — Create an element inside the current one

| Argument | What it is |
|---|---|
| `TYPE` | CWAY, CWBRAN, RPATH, POINTR, HATTA, TATTA, CTMTRL, EQUI, SUBE, NOZZLE, ELCONN, ZONE, every primitive (BOX, CYLINDER, CONE, SNOUT, DISH, PYRAMID, CTORUS, RTORUS, SLCYLINDER, EXTRUSION, REVOLUTION, POLYHEDRON) and every hole (NBOX, NCYLINDER…) — all created in E3D 2.1; PIPE, BRAN, STRU, FRMW, SBFR, SCTN, GENSEC, PANE — in E3D 2.1. The current element must be a legal owner: CWAY in a ZONE, CWBRAN in a CWAY, SUBE only in an EQUI, a hole inside a primitive, BRAN in a PIPE, SCTN in a FRMW. GPSET in a ZONE: «Cannot create a GPSET at this level». |
| `/NAME` | Optional: the name of the new element. |
| `$Q` | Instead of creating, prints the grammar of the command in your build: NEW EQUI $Q. |

The new element becomes current — except NEW POINTR: CE stays where it was. NEW RPATH creates no points.

**Forms**

- `NEW CWAY /PMLC-CWAY-T1` — Verified · Create a cable tray in a zone
- `NEW CWBRAN /PMLC-CWBRAN-T2/01` — Verified · Create a branch in a tray
- `NEW RPATH` — Verified · Create a route
- `NEW POINTR` — Verified · Add a route point
- `NEW NOZZLE` — Verified · Equipment nozzle
- `NEW DRWG /CWAY-ISO-001` — Documented · Create a drawing
- `NEW SHEET /SH1` — Documented · Create a sheet
- `NEW VIEW /V1` — Documented · Create a view

## `POS` — Set the position

| Argument | What it is |
|---|---|
| `E\|W x  N\|S y  U\|D z` | Coordinates in mm. No minus signs: W, S and D are the negative directions. |
| `WRT WORLD` | In world coordinates. Without WRT the position is measured from the owner. |
| `WRT /NAME` | From another element. |
| `WRT $!!x` | From an element whose name is in a variable. |

On a primitive POS is its centre; inside a SUBE — from the SUBE. On a cable tray branch the edit gizmo sits on POS.

**Forms**

- `POS E 0 N 0 U 0` — Verified · Set the position
- `POS E 0 N 0 U 0 WRT WORLD` — Verified · The same in world coordinates
- `POS E 0 N 0 U 500 WRT /PMLC-CWAY-T1` — Verified · Coordinates relative to another element
- `POS E 0 N 0 U 0 WRT $!!PMLCINS` — Verified · Relative to an element whose name is in a variable
- `POS E 8000 N 0 U 0` — Verified · Move an element

## `Q` — Ask — print without changing anything

| Argument | What it is |
|---|---|
| `ATTR [ATTR …]` | One or more attributes in one line: Q NAME TYPE OWNER. |
| `ATT · MEM · REF · POS` | All attributes · members with their =ref · the stable reference · the position (in the owner's system). |
| `ATTR OF /NAME \| =REF` | Read an attribute of another element without moving to it. |
| `POS WRT WORLD` | The position in world coordinates. |
| `VAR !!x` | The content and type of a variable. |
| `EVAR \|NAME\|` | An environment variable of E3D (not of Windows). |

Q MEM ATT is Q MEM plus Q ATT of the CURRENT element — not the attributes of the members.

**Forms**

- `Q EVAR |PMLLIB|` — Verified · See the PML library path from inside E3D
- `Q POS WRT WORLD` — Verified · Current element's world coordinates
- `Q HCREF` — Verified · What the branch head connects to (Q TCREF — the tail)
- `Q SPREF` — Verified · Catalogue reference of an item (on an ELCONN — Q CATREF)
- `Q DESPARAM` — Verified · Design parameters from the catalogue
- `Q POS` — Verified · Current element's coordinates
- `Q ATT` — Verified · All attributes of the current element
- `Q NAME` — Verified · Name
- `Q TYPE` — Verified · Element type
- `Q OWNER` — Verified · Owner
- `Q REF` — Verified · Stable reference like =12345678/26685
- `Q MEM` — Verified · Members: what is inside
- `Q DESC` — Verified · Description
- `Q DRAWLIST` — Verified · What is on screen now
- `Q NAME OF /PMLC-CWBRAN-T1/01` — Verified · Read an attribute WITHOUT moving to the element
- `Q NAME TYPE OWNER` — Verified · Several attributes in one line
- `Q VAR !!x` — Verified · Show a variable
- `Q MEM ATT` — Verified · Members and attributes
- `Q $Q` — Verified · What the Q command accepts at all
- `Q PURP` — Verified · Purpose mark (PURPOSE)
- `Q ORI` — Verified · Orientation

## `VAR` — Read into a variable

| Argument | What it is |
|---|---|
| `!x \| !!x` | Local or global. In the Command Line only a global !!x lives to the next line. |
| `ATTR` | Reads an attribute of any type, whatever the variable held before: VAR !x MAXLAY. |
| `COLLECT ALL TYPE [WITH (…)] FOR element \| WORLD` | Collects elements. WITH can test an attribute: WITH (UNSET(DESC)). The result can be looped over with do … values, but has no .Size(). |

FOR element takes everything under it, nested elements included.

**Forms**

- `VAR !!x ACTTYPE` — Verified · Project element type (:EXTZONE)
- `VAR !!x NAME` — Verified · Read an attribute of the current element into a variable
- `VAR !!eq COLLECT ALL EQUI WITH ( TYPE EQ 'EQUI' ) FOR CE` — Verified · Collect elements with a filter
- `VAR !!x OWNER` — Verified · An element's owner into a variable — then $!!x goes to it
- `VAR !x COLLECT ALL CWBRAN WITH (UNSET(DESC)) FOR /PMLC` — Verified · Collect with a condition on an attribute
- `VAR !s COLLECT ALL SITE FOR WORLD` — Verified · Collect across the whole database

## `DESC` — Write the description

| Argument | What it is |
|---|---|
| `\|text\| · 'text'` | Text in vertical bars or single quotes — they are equal. Double every $; a double quote goes in as it is; no line breaks. |

A primitive (BOX) has no DESC: «Current element does not have an attribute DESC». EQUI and SUBE have it.

**Forms**

- `DESC |text with spaces|` — Verified · Write a description

## `NAME` — Rename the current element

| Argument | What it is |
|---|---|
| `/NEW` | The new name, with the slash. A name in use is rejected — «Name … already used» — and nothing changes. |

For bulk renaming: =ref, then NAME — two lines per element. To swap names, go through a temporary prefix.

**Forms**

- `NAME /NEW` — Verified · Rename the CURRENT element

## `RENAME` — The same as NAME

| Argument | What it is |
|---|---|
| `/NEW` | Renames the current element, exactly like NAME. |

There is no two-name form: RENAME /OLD /NEW → «(2,109) Undefined name».

**Forms**

- `RENAME /NEW` — Verified · The same
- `RENAME /OLD /NEW` — Fails · This does NOT work

## `REORDER` — Change the order of members

| Argument | What it is |
|---|---|
| `WHAT BEFORE WHERE` | First what moves, then what it goes before. Full names with the slash, or $!!a / $!!b holding =ref of unnamed elements. |

Only the order in the owner changes; coordinates stay. WHAT AFTER WHERE ran without an error, but the element already stood there — its effect is not seen yet.

**Forms**

- `REORDER /A BEFORE /B` — Verified · Move within the list of members
- `REORDER /A AFTER /B` — Seen in code · The same, but after the given element

## `MARKDB` — Set a rollback mark

| Argument | What it is |
|---|---|
| `\|label\| · 'label'` | The label is required, in bars or single quotes. Without them — CP: Syntax error. |

The mark lives until SAVEWORK.

**Forms**

- `MARKDB |before bulk edit|` — Verified · Set a rollback mark BEFORE the operation

## `UNDODB` — Roll back to a mark

| Argument | What it is |
|---|---|
| `[n]` | How many MARKS to go back — not how many edits. Without n — one mark. |

Undoes changed attributes, renames and created elements. After SAVEWORK — «No mark to UNDO to».

**Forms**

- `UNDODB` — Verified · Roll the database back to the last mark

## `SAVEWORK` — Save the work

No arguments. Erases the rollback marks — save only after checking.

**Forms**

- `SAVEWORK` — Verified · Save your work to the database

## `ALPHA LOG` — Write the window's output to a file

| Argument | What it is |
|---|---|
| `/PATH OVERWRITE` | The path as one word with a slash in front: alpha log /C:\Temp\log.txt OVERWRITE. |
| `END` | Stop writing. |

Answers and errors go to the file, the commands themselves do not. UTF-8 with BOM.

**Forms**

- `alpha log /C:\Temp\log.txt OVERWRITE` — Verified · Write everything the window prints to a file
- `alpha log END` — Verified · Stop writing to the file

## `$P` — Print a line

| Argument | What it is |
|---|---|
| `text $!x` | Any text; $!x and $!!x are replaced by the value of the variable — numbers too. |

**Forms**

- `$P $!!x` — Verified · Print the value

## `$M` — Run a macro file

| Argument | What it is |
|---|---|
| `PATH` | The macro file: $M C:\Temp\file.pmlmac. |
| `arg1 … arg9` | Positional arguments, available in the file as $1…$9. |

Non-Latin text in the file is read correctly only if the file is saved in ANSI.

**Forms**

- `$M C:\Temp\file.pmlmac` — Verified · The same, as a command
- `$M C:\Temp\t.mac arg1 arg2` — Verified · Run a macro with arguments
- `$M C:\Temp\t.mac arg1 arg2` — Verified · Run a macro from the Command Line

## `CABLAY` — Cable layout

| Argument | What it is |
|---|---|
| `\|TEXT\|` | A text value — in bars: CABLAY \|CEN\|. Without bars — syntax error, the caret on the value. |

**Forms**

- `CABLAY |CEN|` — Verified · Cable layout
- `CABLAY CEN` — Fails · This does NOT work

## `VWIDTH` — Tray width (CWBRAN)

| Argument | What it is |
|---|---|
| `n \| n mm` | A number, with or without a unit: VWIDTH 700mm. Never in bars — VWIDTH \|400\| is a syntax error. |

On a CWBRAN it is VWIDTH, not WIDTH.

**Forms**

- `VWIDTH 600` — Verified · Tray width

## `VHEIGHT` — Tray height (CWBRAN)

| Argument | What it is |
|---|---|
| `n \| n mm` | Like VWIDTH. |

On a CWBRAN it is VHEIGHT, not HEIGHT.

**Forms**

- `VHEIGHT 100` — Verified · Tray height

## `CWJUSLINE` — Justification line of a branch

| Argument | What it is |
|---|---|
| `WORD` | CWJUSLINE CENT. The grammar ($Q) accepts a word or text — there is no fixed list of values. |

**Forms**

- `CWJUSLINE CENT` — Verified · Branch justification line

## `BRADIUS` — Bend radius of a branch

| Argument | What it is |
|---|---|
| `n` | In mm: Q ATT prints BRadius 300mm. |

**Forms**

- `BRADIUS 300` — Verified · Branch bend radius

## `BANGLE` — Angle of a branch

| Argument | What it is |
|---|---|
| `n` | In degrees: Q ATT prints Bangle 0degree. |

**Forms**

- `BANGLE 0` — Verified · Branch angle

## `MAXLAY` — Maximum cable layers

| Argument | What it is |
|---|---|
| `n` | A whole number. |

**Forms**

- `MAXLAY 1` — Verified · Maximum cable layers

## `MAXCAB` — Maximum number of cables

| Argument | What it is |
|---|---|
| `n` | A whole number. |

**Forms**

- `MAXCAB 0` — Verified · Maximum cables

## `MATTYPE` — Tray material type

| Argument | What it is |
|---|---|
| `unset \| Perforated \| Unperforated` | The values Q ATT shows for this attribute. |

Only the read was checked: MatType unset.

**Forms**

- `MATTYPE unset` — Verified · Tray material type

## `FRADIUS` — Fillet radius at a route point (POINTR)

| Argument | What it is |
|---|---|
| `n` | In mm, measured on the tray AXIS, not on its edge. |

**Forms**

- `FRADIUS 300` — Verified · Fillet radius at a point (on POINTR)

## `XLEN` — Box length along X (YLEN, ZLEN the same)

| Argument | What it is |
|---|---|
| `n` | In mm. E3D also accepts 0 and negative values without an error — check sizes before writing. |

**Forms**

- `XLEN 1000` — Verified · Length along X

## `DIAM` — Diameter (cylinder, dish, sloped cylinder)

| Argument | What it is |
|---|---|
| `n` | In mm. Written and read back on CYLINDER, DISH and SLCYLINDER. |

The axis of a new cylinder is the owner's Z (Orientation Y is N and Z is U).

**Forms**

- `DIAM 800` — Verified · Diameter

## `HEIG` — Height of a primitive

| Argument | What it is |
|---|---|
| `n` | In mm. Written and read back on CYLINDER, DISH, SNOUT, PYRAMID, SLCYLINDER. POS is the centre: a cylinder sticks out half its height both ways. |

**Forms**

- `HEIG 1000` — Verified · Height

## `ORI` — Orientation

| Argument | What it is |
|---|---|
| `Y IS dir AND Z IS dir` | Where the element's Y and Z axes point: ORI Y IS N AND Z IS E. |
| `… n dir` | With an angle: ORI Y IS N AND Z IS E 45 U. |

ORI on an EQUI turns it together with all its parts.

**Forms**

- `ORI Y IS N AND Z IS E` — Verified · Rotate: cylinder axis to the east
- `ORI Y IS N AND Z IS E 45 U` — Verified · Rotate by an angle (a tilted element)

## `LEVEL` — Drawing levels

| Argument | What it is |
|---|---|
| `from to` | Two numbers: LEVEL 1 3. |

**Forms**

- `LEVEL 1 3` — Verified · Drawing levels (e.g. hide a service zone from review models)

## `OBST` — Obstruction level

| Argument | What it is |
|---|---|
| `n` | OBST 1 → Q OBST prints Obstruction 1. |

**Forms**

- `OBST 1` — Verified · Obstruction level

## `DELETE` — Delete the current element

| Argument | What it is |
|---|---|
| `TYPE` | The type of the current element: DELETE EQUI deletes the current EQUI with all its children. |

Check where you stand with Q NAME first; put a MARKDB before — UNDODB brings it back.

**Forms**

- `DELETE EQUI` — Verified · Delete the current equipment

## `INCLUDE` — Move an element into the current one (INCL)

| Argument | What it is |
|---|---|
| `/NAME \| =REF` | The element to move — by name or by stable reference. |

CE does not change: stand in the receiving zone once, then include many.

**Forms**

- `INCLUDE =12345678/6393` — Verified · Move an element inside the current one

## `CLAIM` — Claim an element

| Argument | What it is |
|---|---|
| `/NAME HIER` | The element together with its hierarchy. |

**Forms**

- `CLAIM /PMLC-CWBRAN-T1/01 HIER` — Verified · Claim an element with its hierarchy

## `MARK` — Label elements in the 3D view

| Argument | What it is |
|---|---|
| `CE MEM` | The members of the current element — this is how route points get labels. |

**Forms**

- `MARK CE MEM` — Verified · Label the members of the current element

## `BY` — Move by a distance

| Argument | What it is |
|---|---|
| `dir n` | A direction and a distance in mm, written together: BY W2000. |

**Forms**

- `BY W2000` — Verified · Shift by 2000 towards W

## `SYSCOM` — Run a Windows command

| Argument | What it is |
|---|---|
| `'command' · \|command\|` | The command as text — single quotes or bars: SYSCOM \|$!cmd\|. |

Needs no administrator rights.

**Forms**

- `SYSCOM 'cmd /c mkdir C:\Temp\OUT'` — Verified · Run a Windows command from PML

## `PURPOSE` — Purpose code

| Argument | What it is |
|---|---|
| `WORD` | A word without bars: PURPOSE PMLC. |

A copy of the element made in E3D inherits it.

**Forms**

- `PURPOSE PMLC` — Verified · A purpose mark to find your own elements later
- `PURPOSE PMLC` — Verified · Mark an element as yours (works on equipment too)

## `NEXT` — Go to the next member

No arguments: to the next member of the same owner.

**Forms**

- `NEXT` — Verified · To the next member of the same owner

## `GOTO` — Follow a reference attribute

| Argument | What it is |
|---|---|
| `REFERENCE ATTRIBUTE` | OWNER, PARENT, FRSTWORLD, CLCONNECTIONS… or any reference attribute (from GOTO $Q). Not a name. GOTO OWNER is tested in E3D 2.1. |

GOTO /NAME is a syntax error: to go by name, type the name itself.

**Forms**

- `GOTO OWNER` — Verified · Follow a reference attribute
- `GOTO /NAME` — Fails · This does NOT work

## `DO` — Loop (macro only)

| Argument | What it is |
|---|---|
| `!i from a to b` | A counter: tested in E3D 2.1 with from 1 to 3. |
| `!i from a to b by s` | With a step: from 1 to 5 by 2 gives 1, 3, 5. |
| `!e values !list` | Over a list, including a COLLECT result; $!e goes to each element. |
| `!i indices !list` | The positions of a list: over two elements gives 1, 2. |
| `(nothing) … enddo` | A loop without a condition; leave it with break if ( … ). This is the way instead of do while. |

A plain paste gives «Invalid syntax» — use Paste as Macro. Inside: skip if ( … ) goes to the next turn, break if ( … ) leaves the loop. do while is a syntax error in E3D 2.1 and stops the macro. Plain break and skip work too.

**Forms**

- `do … enddo` — Macro only · Loop
- `do !i from 1 to 10` — Macro only · Counting loop
- `do !i from 1 to 10 by 2` — Verified · Loop with a step
- `do !elem values !array` — Macro only · Loop over array values
- `do !i indices !array` — Macro only · Loop over indices
- `do while ( !flag )` — Fails · Loop on a condition — does NOT work

## `IF` — Condition (macro only)

| Argument | What it is |
|---|---|
| `( condition ) then … endif` | A condition in brackets: if (!x GT 5) then. |
| `elseif ( … ) then / else` | More branches; the right one runs. |

A plain paste gives «Invalid syntax» — use Paste as Macro. Compare with words — GT, LT, EQ…: the sign > gives «Meaningless symbol(s)» and stops the macro.

**Forms**

- `if … then … endif` — Macro only · Condition
- `if ( !x gt 5 ) then … elseif … else … endif` — Macro only · Condition, PML1 form
- `if ( !x > 5 and !n.Matchwild('PIPE*') ) then` — Fails · Condition, PML2 form

## `HANDLE` — Catch an error (macro only)

| Argument | What it is |
|---|---|
| `any … endhandle` | Right AFTER the line it guards. handle any catches a move to an element that does not exist, and the syntax error of a single command line (TYPE $Q) — the macro goes on. |
| `(2,109) … endhandle` | Catches only that error number: here «Undefined name». |
| `… elsehandle any` | After a numbered handle: every other error. |
| `… elsehandle none` | Runs when the guarded line gave no error. |

A plain paste gives «Invalid syntax» — use Paste as Macro. A syntax error of the macro itself (do while) is not caught: the macro stops. The text of the error — $!!error.text; there is no member code.

**Forms**

- `handle any … endhandle` — Macro only · Catch an error
- `handle any … endhandle` — Seen in code · Catch any error
- `handle (41,64)` — Documented · Catch a specific error by number

## `!` — Variables and objects

| Argument | What it is |
|---|---|
| `!x = value · !!x = value` | Local (inside a macro) or global (the whole session). |
| `object FILE('path')` | A file object: then .ReadFile() → an array of lines, .WriteFile('OVERWRITE', !lines). |
| `object ARRAY()` | An array; .Append() adds to it. |
| `!x = ATTR` | An attribute into a FRESH variable only — otherwise «incompatible types»; VAR is safer. |

WriteFile writes UTF-8 with BOM; ReadFile reads a single-byte code page (save input files in ANSI). Keep a written line under 800 bytes.

**Forms**

- `!!CE.Attributes()` — Verified · Array of the names of all attributes of the current element
- `!f = object FILE('C:\Temp\out.csv')` — Verified · Open a file from PML
- `!lines = !f.ReadFile()` — Verified · Read a file into an array of lines
- `!f.WriteFile('OVERWRITE', !lines)` — Verified · Write an array of lines to a file
- `!!x = 3` — Verified · Global variable, lives for the whole session
- `!x = 3` — Verified · Local — only inside a macro
- `!!cmd = 'Q NAME'   then   $!!cmd` — Verified · Run a command built as a string
- `!nm = NAME` — Verified · An attribute of the current element into a variable (in a macro)
- `!!a = object ARRAY()` — Verified · An array; .Append() adds

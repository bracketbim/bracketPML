# Register

Every PML command we know about, with its status and the runs behind it. **Generated** from the source of truth at every build — please send changes as a [run report](CONTRIBUTING.md).

| Status | Meaning | Rows |
|---|---|---|
| **Verified** | Ran in E3D 2.1, the result was checked. | 122 |
| **Fails** | Ran and gave an error — do not use; the row says what to use instead. | 8 |
| **Macro only** | Works in a macro file or with Paste as Macro, not line by line. | 6 |
| **Documented** | In the AVEVA documentation or the $Q grammar; not run by us yet. | 30 |
| **Seen in code** | Appears in real PML code; not run by us yet. | 28 |

Last run: 26 Oct 2026 · E3D 2.1 · searchable at [bracketbim.com/pml](https://bracketbim.com/pml/)

## The Commands window — how it runs what you paste

Common Functionality User Guide 2.1, Command Window. The window opens from Home → Windows and is hidden by default. The key fact: a plain paste runs every line as a separate command, so a multi-line block never comes together. The right-click menu has a second item that solves it.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="right-click-paste"></a>`right-click → Paste` | Plain paste | Documented | 27 Sep 2026 | Word for word: «executes each line of the copied text as a separate command as if they had been typed». That is why an if line fails with «Invalid syntax» — it runs alone. And on the first error the remaining lines of the paste do NOT run — the tail has to be entered again. |
| <a id="right-click-paste-as-macro"></a>`right-click → Paste as Macro` | Paste as a macro | Documented |  | Word for word: «first creates a temporary file containing the copied macro commands and executes this as a macro». This is how if, do and handle work — and it is faster for many commands. |
| <a id="drag-a-mac-file-from-explorer"></a>`drag a .mac file from Explorer` | Run a macro file | Documented |  | «Macro files can also be dragged into the command window». |
| <a id="m-c-temp-file-pmlmac"></a>`$M C:\Temp\file.pmlmac` | The same, as a command | Verified | 26 Aug 2026 | Arguments $1…$9 work. |
| <a id="alpha-log-c-temp-log-txt-overwrite"></a>`alpha log /C:\Temp\log.txt OVERWRITE` | Write everything the window prints to a file | Verified | 25 Sep 2026 | Long Q MEM and Q ATT outputs land in full, without the window's truncation. The file is UTF-8 with BOM. Stop with alpha log END. |
| <a id="alpha-log-end"></a>`alpha log END` | Stop writing to the file | Verified | 25 Sep 2026 |  |
| <a id="double-click-a-history-line"></a>`double-click a history line` | Bring a command back into the input field | Documented |  | Up and Down arrows walk the history. |
| <a id="right-click-clear"></a>`right-click → Clear` | Clear the window | Documented |  | The window keeps roughly the last 1000 lines of output. |
| <a id="q-evar-pmllib"></a>`Q EVAR \|PMLLIB\|` | See the PML library path from inside E3D | Verified | 27 Aug 2026, 16 Sep 2026 | Printed about ten paths. This is an E3D variable, not a Windows one — echo %PMLLIB% in cmd does not see it. But those folders are not writable for a normal user: your own functions and forms through PMLLIB are out of reach. |
| <a id="pml-rehash-all"></a>`PML REHASH ALL` | Re-read the library after editing a .pmlfnc | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: ran inside a macro with no error. |
| <a id="pml-index"></a>`PML INDEX` | Library index | Documented |  |  |
| <a id="pml-trace-on"></a>`PML TRACE ON` | Trace PML execution | Documented |  |  |

## Where to stand — navigation

Almost every command works on the current element (CE). First stand on it, then act.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="pmlc-cway-t1"></a>`/PMLC-CWAY-T1` | Go to an element by name | Verified | 27 Aug 2026 | The main way: just the name on its own line. |
| <a id="rpath-1"></a>`RPATH 1` | Step into a member of the current element by type and number | Verified |  | Inside a branch: RPATH 1, then POINTR 2. |
| <a id="pointr-2"></a>`POINTR 2` | Second route point | Verified |  | Works after stepping into RPATH. |
| <a id="equipment-2-of-extzone-pmlc"></a>`EQUIPMENT 2 of :EXTZONE /PMLC` | Go to an unnamed element by number | Verified | 27 Aug 2026 | The number counts ALL members of the zone and shifts when elements move. |
| <a id="12345678-7844"></a>`=12345678/7844` | Go by stable reference | Verified | 27 Aug 2026 | Works; Q NAME afterwards prints the name. A reference does not shift when elements move or are renamed — bulk operations go by =ref only. |
| <a id="owner"></a>`OWNER` | Go up to the owner | Documented |  | Not run. Templates use the full name instead. |
| <a id="goto-owner"></a>`GOTO OWNER` | Follow a reference attribute | Verified | 18 Sep 2026, 26 Oct 2026, run 25 | GOTO $Q prints what may follow (run of 18 Sep): CFDPROPERTY, LFDPROPERTY, TFDPROPERTY, FRSTWORLD, PARENT, SPLPARENT, CLCONNECTIONS and «any reference attribute». So the command exists, but it follows a REFERENCE, not a name. Run of 26 Oct 2026: from a SUBE it moved to its EQUI. |
| <a id="goto-name"></a>`GOTO /NAME` | This does NOT work | Fails | 26 Aug 2026 | CP: Syntax error. A name is not among GOTO's continuations — that is why it fails. Going by name means typing the name itself: /PMLC-CWAY-T1. Jumping to a label in a macro is GOLABEL. |

## Create — cable trays

The order is exactly this: tray, branch, section, head and tail, route, point coordinates.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="new-cway-pmlc-cway-t1"></a>`NEW CWAY /PMLC-CWAY-T1` | Create a cable tray in a zone | Verified | 26 Oct 2026, run 25 | Owner — ZONE. NEW makes the new element current. |
| <a id="new-cwbran-pmlc-cwbran-t2-01"></a>`NEW CWBRAN /PMLC-CWBRAN-T2/01` | Create a branch in a tray | Verified | 26 Oct 2026, run 25 | Owner — CWAY. |
| <a id="pos-e-0-n-0-u-0"></a>`POS E 0 N 0 U 0` | Set the position | Verified | 18 Sep 2026, 24 Sep 2026, 25 Sep 2026, run 10 | Without WRT — FROM THE OWNER. For a tray branch this is where the tray is: the edit gizmo sits on the branch's POS. For a primitive POS is its centre, inside a SUBE — from the SUBE. No minus sign needed: use W / S / D. |
| <a id="pos-e-0-n-0-u-0-wrt-world"></a>`POS E 0 N 0 U 0 WRT WORLD` | The same in world coordinates | Verified | 18 Sep 2026 | The line ran and moved the tray. POS $Q does not list WRT — the $Q grammar is incomplete, and its silence is no argument against a command. |
| <a id="pos-e-0-n-0-u-500-wrt-pmlc-cway-t1"></a>`POS E 0 N 0 U 500 WRT /PMLC-CWAY-T1` | Coordinates relative to another element | Verified | 19 Sep 2026 |  |
| <a id="pos-e-0-n-0-u-0-wrt-pmlcins"></a>`POS E 0 N 0 U 0 WRT $!!PMLCINS` | Relative to an element whose name is in a variable | Verified | 23 Sep 2026 | VAR !!PMLCINS NAME on the picked element, then this line — the rack landed next to it. This is how «pick an object in E3D» works as an insertion point. |
| <a id="q-pos-wrt-world"></a>`Q POS WRT WORLD` | Current element's world coordinates | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | Q POS without WRT prints relative to the owner. |
| <a id="vwidth-600"></a>`VWIDTH 600` | Tray width | Verified | 22 Sep 2026 | On a CWBRAN it is VWidth, not WIDTH. |
| <a id="vheight-100"></a>`VHEIGHT 100` | Tray height | Verified |  | On a CWBRAN it is VHeight, not HEIGHT. |
| <a id="cwjusline-cent"></a>`CWJUSLINE CENT` | Branch justification line | Verified | 19 Sep 2026 | Q ATT showed CWJusLine CENT. |
| <a id="new-hatta"></a>`NEW HATTA` | Create the head attachment point | Verified |  | Has no coordinates of its own. NEW moves CE — go back to the branch. |
| <a id="new-tatta"></a>`NEW TATTA` | Create the tail attachment point | Verified | 26 Aug 2026 | The same. |
| <a id="new-rpath"></a>`NEW RPATH` | Create a route | Verified | 26 Oct 2026, run 25 | Creates NO points: Q MEM right after it is unset. |
| <a id="new-pointr"></a>`NEW POINTR` | Add a route point | Verified | 26 Oct 2026, run 25 | Needed twice for a straight branch. CE does NOT move to the new point — set coordinates in a second pass. |
| <a id="cablay-cen"></a>`CABLAY \|CEN\|` | Cable layout | Verified | 27 Aug 2026 | The value is text — in vertical bars. Q ATT showed Cablayout CEN. |
| <a id="cablay-cen-2"></a>`CABLAY CEN` | This does NOT work | Fails | 27 Aug 2026 | CP: Syntax error with the caret on the value — the bars are needed. |
| <a id="bradius-300"></a>`BRADIUS 300` | Branch bend radius | Verified | 27 Aug 2026 | Q ATT of the branch showed BRadius 300mm. |
| <a id="bangle-0"></a>`BANGLE 0` | Branch angle | Verified | 27 Aug 2026 | Q ATT of the branch showed Bangle 0degree. |
| <a id="maxlay-1"></a>`MAXLAY 1` | Maximum cable layers | Verified | 27 Aug 2026 | Q ATT of the branch showed MaxLay 1. |
| <a id="maxcab-0"></a>`MAXCAB 0` | Maximum cables | Verified | 27 Aug 2026 | Q ATT of the branch showed MaxCab 0. |
| <a id="mattype-unset"></a>`MATTYPE unset` | Tray material type | Verified | 27 Aug 2026 | Q ATT: MatType unset. Values: unset, Perforated, Unperforated. |
| <a id="fradius-300"></a>`FRADIUS 300` | Fillet radius at a point (on POINTR) | Verified | 27 Aug 2026, 29 Sep 2026 | The radius is measured on the tray AXIS, not on its edge. Q FRADIUS prints the number. |
| <a id="q-hcref"></a>`Q HCREF` | What the branch head connects to (Q TCREF — the tail) | Verified | 28 Sep 2026 | Unconnected trays print HCRef unset. Connected ones were not seen yet. |
| <a id="new-conseq"></a>`NEW CONSEQ` | Branch connection sequence | Verified | 17 Sep 2026 | Do NOT create it by hand: a tee connection creates it itself, and later branches go into the same one. |
| <a id="usematerial"></a>`USEMATERIAL` | Use Material in the branch creation form | Documented |  | Cable Design User Guide 2.1; not run as a command. |
| <a id="hpos"></a>`HPOS` | Branch head — this does NOT work (nor TPOS, HDIR, TDIR) | Fails |  | Current element does not have a head or a tail attribute: a branch's position is set by its RPATH points. |
| <a id="width-600"></a>`WIDTH 600` | Width — this does NOT work (nor HEIGHT) | Fails |  | On a CWBRAN it is VWIDTH / VHEIGHT. |

## Create — equipment

Equipment and its geometry: EQUI, SUBE, primitives and negative primitives.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="new-equi-test-equi-001"></a>`NEW EQUI /TEST-EQUI-001` | Create equipment in a zone | Verified | 26 Aug 2026 |  |
| <a id="new-sube-test-equi-001-sube-1"></a>`NEW SUBE /TEST-EQUI-001/SUBE-1` | Sub-equipment inside equipment | Verified | 27 Aug 2026 | Owner — EQUIPMENT only. A SUBE has DESC. |
| <a id="new-box-test-equi-001-box-1"></a>`NEW BOX /TEST-EQUI-001/BOX-1` | Box | Verified | 27 Aug 2026 | Owner — EQUI or SUBE. POS is the centre of the box. A BOX has no DESC. |
| <a id="xlen-1000"></a>`XLEN 1000` | Length along X | Verified | 24 Sep 2026 | Accepts 0 and negative values too — E3D does not check sizes; your generator must. |
| <a id="ylen-1000"></a>`YLEN 1000` | Length along Y | Verified | 27 Aug 2026 |  |
| <a id="zlen-1000"></a>`ZLEN 1000` | Height along Z | Verified | 27 Aug 2026 |  |
| <a id="new-cylinder-cyl-1"></a>`NEW CYLINDER /…/CYL-1` | Cylinder | Verified | 27 Aug 2026 | DIAM and HEIG. POS is the centre of the cylinder. |
| <a id="diam-800"></a>`DIAM 800` | Diameter | Verified | 27 Aug 2026 |  |
| <a id="heig-1000"></a>`HEIG 1000` | Height | Verified | 27 Aug 2026 |  |
| <a id="ori-y-is-n-and-z-is-e"></a>`ORI Y IS N AND Z IS E` | Rotate: cylinder axis to the east | Verified | 24 Sep 2026, 25 Sep 2026 | The cylinder lay perpendicular to face E (Z IS W — to the west). ORI on an EQUI rotates it with all its parts. |
| <a id="new-ncylinder"></a>`NEW NCYLINDER` | Round hole (negative primitive) | Verified | 18 Sep 2026 | The hole is visible in 3D. A negative lives INSIDE the primitive, not in the EQUI. |
| <a id="new-nbox"></a>`NEW NBOX` | Rectangular cut-out | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: created inside a BOX; XLEN / YLEN / ZLEN were written. |
| <a id="delete-equi"></a>`DELETE EQUI` | Delete the current equipment | Verified | 24 Sep 2026 | Deleted it with all children; UNDODB brought it back. Check Q NAME first — be sure where you stand. |
| <a id="new-nozzle"></a>`NEW NOZZLE` | Equipment nozzle | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: created in an EQUI even without a specification — Catref Nulref, Temperature −100000degC. Its look in 3D and connecting to it were not checked. |
| <a id="new-elconn"></a>`NEW ELCONN` | Electrical connection point | Verified | 27 Sep 2026 | Created directly in an EQUI, POS works; by default Y is N and Z is U, Catref empty. Like a nozzle on a pipe — a cable connects to it. On real catalogue boxes the link to the catalogue is CATREF, not SPREF. Look in 3D and cable connection not checked. |
| <a id="purpose-pmlc"></a>`PURPOSE PMLC` | A purpose mark to find your own elements later | Verified | 9 Oct 2026, run 17 | Written without bars, Q PURP prints Purpose PMLC, and a Ctrl+C / Ctrl+V copy of the EQUI inherits it — keep that in mind when you filter by it. |
| <a id="level-1-3"></a>`LEVEL 1 3` | Drawing levels (e.g. hide a service zone from review models) | Verified | 28 Sep 2026, 29 Sep 2026 | Q LEVEL prints Level 1 3; works right at creation. |
| <a id="obst-1"></a>`OBST 1` | Obstruction level | Verified | 28 Sep 2026 | Q OBST prints Obstruction 1. |
| <a id="ori-y-is-n-and-z-is-e-45-u"></a>`ORI Y IS N AND Z IS E 45 U` | Rotate by an angle (a tilted element) | Verified | 29 Sep 2026 | Q ORI prints the same form back. |
| <a id="q-spref"></a>`Q SPREF` | Catalogue reference of an item (on an ELCONN — Q CATREF) | Verified | 27 Sep 2026 | Prints the SPCO of a catalogue box. Writing SPREF / CATREF was not run. |
| <a id="q-desparam"></a>`Q DESPARAM` | Design parameters from the catalogue | Verified | 27 Sep 2026 | Printed 2 2 1 1 0.3 on a catalogue box; meaning not established. |
| <a id="new-cone"></a>`NEW CONE` | Cone (also NEW SNOUT, DISH, PYRAMID, CTORUS, RTORUS, SLCYLINDER, EXTRUSION, REVOLUTION, POLYHEDRON) | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: all ten were created in a SUBE with sizes; the Q ATT of each is in the bracketPML attribute reference. Before: DMRM 2.1, Primitive category; not run. |
| <a id="new-ncone"></a>`NEW NCONE` | Negative cone — a cut-out (also NSNOUT, NDISH, NPYRAMID, NCTORUS, NRTORUS, NSLCYLINDER) | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: all seven were created inside a BOX. |
| <a id="radi-500"></a>`RADI 500` | Primitive radius | Seen in code |  | DMRM 2.1: Radius; this form appears in real code. |
| <a id="angle-90"></a>`ANGLE 90` | Primitive angle | Seen in code |  | DMRM 2.1: Angle; this form appears in real code. |
| <a id="xoff-100"></a>`XOFF 100` | X offset (also XBOT, YBOT, XTOP, YTOP) | Seen in code |  | DMRM 2.1; these forms appear in real code. |
| <a id="dtop-300"></a>`DTOP 300` | Top diameter (also DBOT, YOFF, RINS, ROUT, XTSH, YTSH, XBSH, YBSH) | Documented |  | DMRM 2.1; these abbreviations were not seen in real code — check with $Q. |
| <a id="new-gpset"></a>`NEW GPSET` | A set (collection) of elements | Documented | 17 Sep 2026 | NEW GPSET $Q prints its grammar; the element itself was not created. |

## Find and look

Read-only. These commands change nothing — use them freely.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="q-pos"></a>`Q POS` | Current element's coordinates | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | Position E 10000mm N 0mm U 0mm |
| <a id="q-att"></a>`Q ATT` | All attributes of the current element | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | The fullest answer — and the way to check a result. |
| <a id="q-name"></a>`Q NAME` | Name | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 |  |
| <a id="q-type"></a>`Q TYPE` | Element type | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 |  |
| <a id="q-owner"></a>`Q OWNER` | Owner | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 |  |
| <a id="q-ref"></a>`Q REF` | Stable reference like =12345678/26685 | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | Does not depend on numbering — the best way to address an element. |
| <a id="q-mem"></a>`Q MEM` | Members: what is inside | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | Prints =ref references of all members at once. |
| <a id="q-desc"></a>`Q DESC` | Description | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 |  |
| <a id="q-drawlist"></a>`Q DRAWLIST` | What is on screen now | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | An element differs from its contents by owner. |
| <a id="q-name-of-pmlc-cwbran-t1-01"></a>`Q NAME OF /PMLC-CWBRAN-T1/01` | Read an attribute WITHOUT moving to the element | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | Cuts bulk queries to a third. |
| <a id="q-name-type-owner"></a>`Q NAME TYPE OWNER` | Several attributes in one line | Verified | 28 Aug 2026 |  |
| <a id="q-var-x"></a>`Q VAR !!x` | Show a variable | Verified | 23 Sep 2026 |  |
| <a id="q-mem-att"></a>`Q MEM ATT` | Members and attributes | Verified | 27 Aug 2026 | Prints Q MEM and Q ATT of the CURRENT element — not attributes of its members. |
| <a id="q-q"></a>`Q $Q` | What the Q command accepts at all | Verified | 26 Aug 2026, 27 Aug 2026, 28 Aug 2026 | $Q after any command prints its syntax for your build. Changes nothing. |
| <a id="q-wvol"></a>`Q WVOL` | Element's world box — 6 numbers | Verified | 9 Oct 2026, run 17 | «Wvolume x1 y1 z1 x2 y2 z2», in mm, without E/N/U, world coordinates. Works on GENSEC, EQUI, TEE. |
| <a id="q-purp"></a>`Q PURP` | Purpose mark (PURPOSE) | Verified | 9 Oct 2026, run 17 | Prints Purpose PMLC. |
| <a id="q-ori"></a>`Q ORI` | Orientation | Verified | 24 Sep 2026 | Prints Orientation Y is N and Z is U. |
| <a id="var-x-acttype"></a>`VAR !!x ACTTYPE` | Project element type (:EXTZONE) | Verified | 27 Sep 2026 | <STRING> ':EXTZONE', with the colon; TYPE of the same zone is ZONE. |
| <a id="next"></a>`NEXT` | To the next member of the same owner | Verified | 27 Sep 2026 | From ELCONN 1 to ELCONN 2 and 3. |
| <a id="new-equi-q"></a>`NEW EQUI $Q` | $Q after a command — its syntax in this build | Verified | 26 Aug 2026 | The main scouting tool (but the grammar is incomplete: WRT is missing from POS $Q, yet it works). |
| <a id="id"></a>`ID @` | Pick an element with a click in 3D | Verified | 28 Sep 2026 | ID @ + click — the element becomes current. Esc does not leave the mode. |
| <a id="syn"></a>`SYN` | This does NOT work | Fails |  | There is no such command: CP: Syntax error. |

## Change

These write to the database. There is no UNDO command, but rollback exists and is verified: MARKDB |label| before the operation, UNDODB back to it, UNDODB n — n marks back. Its one limit is verified too: SAVEWORK erases the mark, after saving UNDODB answers «No mark to UNDO to». Order of work: mark, change, check, and only then SAVEWORK.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="pos-e-8000-n-0-u-0"></a>`POS E 8000 N 0 U 0` | Move an element | Verified | 17 Sep 2026, 18 Sep 2026, 19 Sep 2026, 23 Sep 2026, 24 Sep 2026, 25 Sep 2026, 29 Sep 2026, run 14 |  |
| <a id="by-w2000"></a>`BY W2000` | Shift by 2000 towards W | Verified | 26 Aug 2026 | Checked on a route point: 10000 became 8000. |
| <a id="desc-text-with-spaces"></a>`DESC \|text with spaces\|` | Write a description | Verified | 22 Sep 2026, 24 Sep 2026, 11 Oct 2026, 15 Oct 2026, run 18, run 19 | Text with spaces — only in vertical bars (single quotes work too). A $ inside must be doubled: $$. |
| <a id="name-new"></a>`NAME /NEW` | Rename the CURRENT element | Verified | 27 Aug 2026, 18 Sep 2026 | Stand on the element, NAME /NEW — renamed. Together with going by =ref this is bulk tagging: two lines per element and no positional addressing. A name already in use is rejected and nothing changes. |
| <a id="rename-new"></a>`RENAME /NEW` | The same | Verified | 18 Sep 2026 | Works just like NAME. |
| <a id="rename-old-new"></a>`RENAME /OLD /NEW` | This does NOT work | Fails | 18 Sep 2026 | «(2,109) Undefined name», caret on the second name. There is no two-argument form: you rename by STANDING on the element. |
| <a id="reorder-a-before-b"></a>`REORDER /A BEFORE /B` | Move within the list of members | Verified | 23 Sep 2026 | Changes the order inside the owner, does not touch the elements: branches swapped places in Q MEM, coordinates unchanged. First what you move, then what it goes before; works with full names and with =ref of unnamed elements. Found in real public code; the 2.1 manual has no page for it. |
| <a id="reorder-a-after-b"></a>`REORDER /A AFTER /B` | The same, but after the given element | Seen in code |  | The AFTER form was never run — build chains from BEFORE only. |
| <a id="include-12345678-6393"></a>`INCLUDE =12345678/6393` | Move an element inside the current one | Verified | 26 Aug 2026 | Takes a name or a reference. Does not change CE — stand on the receiving zone once. |
| <a id="claim-pmlc-cwbran-t1-01-hier"></a>`CLAIM /PMLC-CWBRAN-T1/01 HIER` | Claim an element with its hierarchy | Verified | 26 Aug 2026 |  |
| <a id="unclaim-all"></a>`UNCLAIM ALL` | Release claims | Seen in code |  |  |
| <a id="lock-all"></a>`LOCK ALL` | Lock against changes | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: Q LOCK afterwards — Lock true. |
| <a id="undo"></a>`UNDO` | There is no command with this name | Fails | 16 Sep 2026 | CP: Syntax error. Rollback is called differently — see the next rows. |
| <a id="markdb-before-bulk-edit"></a>`MARKDB \|before bulk edit\|` | Set a rollback mark BEFORE the operation | Verified | 16 Sep 2026 | Both forms ran: MARKDB \|probe\| and MARKDB 'probe'. WITHOUT quotes — CP: Syntax error, as with DESC and CABLAY. PML Console puts a mark as the first line of every code it writes. |
| <a id="undodb"></a>`UNDODB` | Roll the database back to the last mark | Verified | 16 Sep 2026, 17 Sep 2026 | Restored a broken DESC, undid a rename and the creation of an element; UNDODB n goes back n MARKS (not n edits). After SAVEWORK there is no mark any more — No mark to UNDO to. |
| <a id="incl-12345678-6393"></a>`INCL =12345678/6393` | Same as INCLUDE | Verified |  | Abbreviation. |
| <a id="redodb"></a>`REDODB` | Redo what UNDODB undid | Documented | 16 Sep 2026 | In the $Q grammar; not run. |
| <a id="clearmark"></a>`CLEARMARK` | Clear rollback marks | Documented | 16 Sep 2026 | In the $Q grammar; not run. |
| <a id="endmarkdb"></a>`ENDMARKDB` | Close a mark's scope | Documented | 16 Sep 2026 | In the $Q grammar; not run. |
| <a id="unlock-all"></a>`UNLOCK ALL` | Unlock | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: Q LOCK afterwards — Lock false. |
| <a id="purpose-pmlc-2"></a>`PURPOSE PMLC` | Mark an element as yours (works on equipment too) | Verified | 9 Oct 2026 | Written, and a copy inherits it. |

## Show on screen

Working with the view. The model does not change.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="add-ce"></a>`ADD CE` | Add the current element to the view | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026. ADD /NAME and REMOVE /NAME too: the element appeared in the view and went away. |
| <a id="add-all-within-vol-ce-1000-all"></a>`ADD ALL WITHIN VOL CE 1000 ALL` | Add everything within a distance of the element | Seen in code |  |  |
| <a id="rem-all"></a>`REM ALL` | Clear the view | Seen in code |  |  |
| <a id="mark-ce-mem"></a>`MARK CE MEM` | Label the members of the current element | Verified | 26 Aug 2026 | This is how route points get labels. |
| <a id="unmark-all"></a>`UNMARK ALL` | Remove labels | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026. |
| <a id="col-ce-green"></a>`COL CE GREEN` | Change colour | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: no error; the colour on screen was not checked. |
| <a id="axes-at-ce"></a>`AXES AT CE` | Show axes at the element | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: the axes stay in the view even after the rollback — remove them with AXES OFF (not checked). |
| <a id="alp-req-clear"></a>`ALP REQ CLEAR` | Clear the command window | Seen in code |  |  |
| <a id="axes-on"></a>`AXES ON` | Axes on screen (AXES OFF — remove) | Seen in code |  |  |
| <a id="choo-all"></a>`CHOO ALL` | Choose all | Seen in code |  |  |
| <a id="dir-n-45-e"></a>`DIR N 45 E` | View direction | Seen in code |  |  |
| <a id="thro-ce"></a>`THRO CE` | View through the element | Seen in code |  |  |
| <a id="update-all"></a>`UPDATE ALL` | Refresh the view | Seen in code |  |  |
| <a id="enhance-ce-col-red"></a>`ENHANCE CE COL RED` | Highlight the element | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: no error; the highlight was not checked. |
| <a id="console-show"></a>`console show` | Show the console window | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026: no error. |

## Drawings and isometrics (DRAW module)

IsoADP is NOT in this build: the DRAW module has no Isometric Automatic Drawing Production item and ISOADP $Q gives CP: Syntax error. The 2.1 docs describe it, but the licence is different. An isometric is therefore an ordinary view with an isometric direction, built with the commands below. NEW DRWG $Q and ISODRAFT $Q print their syntax, so the commands exist; they were not run.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="new-drwg-cway-iso-001"></a>`NEW DRWG /CWAY-ISO-001` | Create a drawing | Documented |  | Hierarchy DEPT → REGI → DRWG → SHEE → VIEW. Missing DEPT and REGI are created automatically. |
| <a id="new-sheet-sh1"></a>`NEW SHEET /SH1` | Create a sheet | Documented |  | Can be skipped if the drawing has one sheet. |
| <a id="new-view-v1"></a>`NEW VIEW /V1` | Create a view | Documented |  | With NEW DRWG this is the minimum; the rest is optional. |
| <a id="desadd-cway-el-001"></a>`DESADD /CWAY-EL-001` | Put a model element into the view | Documented |  | Takes a zone, a tray, equipment. Several calls add several elements. |
| <a id="desremove-name"></a>`DESREMOVE /name` | Remove an element from the view | Documented |  | Abbreviation DESREM. |
| <a id="iso3"></a>`ISO3` | Isometric view direction | Documented | 26 Oct 2026, run 25 | There are ISO1…ISO4 — a route may run across the sheet, so the direction is chosen. These are DRAWING view commands: in Model (Run of 26 Oct 2026) ISO3, ELEVATION N and LOOK E gave CP: Syntax error, PLAN gave Incomplete command line; not tried in DRAW. |
| <a id="plan"></a>`PLAN` | Plan view | Documented |  |  |
| <a id="elevation-n"></a>`ELEVATION N` | Elevation from the north | Documented |  |  |
| <a id="look-e"></a>`LOOK E` | Look east | Documented |  | Also LOOK N45W and LOOK THROUGH / LOOK FROM with coordinates. |
| <a id="update-design"></a>`UPDATE DESIGN` | Redraw the view | Documented |  | Required after changing the direction or the contents of the view. |

## Beyond E3D — files and Windows

Found in real PML code, then verified by runs. Works from a macro file (Paste as Macro) and needs neither admin rights nor PMLLIB. Cyrillic and other non-Latin text passes on write but NOT on read — see the ReadFile row.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="syscom-cmd-c-mkdir-c-temp-out"></a>`SYSCOM 'cmd /c mkdir C:\Temp\OUT'` | Run a Windows command from PML | Verified | 16 Sep 2026 | The command ran and the file was created. The value goes in single quotes or vertical bars: SYSCOM \|$!cmd\|. No admin rights needed. |
| <a id="ce-attributes"></a>`!!CE.Attributes()` | Array of the names of all attributes of the current element | Verified | 25 Sep 2026 | Includes project UDAs. |
| <a id="f-object-file-c-temp-out-csv"></a>`!f = object FILE('C:\Temp\out.csv')` | Open a file from PML | Verified |  | Works in a macro file; PMLLIB not needed. |
| <a id="lines-f-readfile"></a>`!lines = !f.ReadFile()` | Read a file into an array of lines | Verified | 18 Sep 2026 | Returned an <ARRAY> of lines. ENCODING: a file saved by Notepad in UTF-8 came in as mojibake — ReadFile reads a single-byte code page, so save files for reading in ANSI. On write non-Latin text comes out right — the two directions are not symmetric. |
| <a id="f-writefile-overwrite-lines"></a>`!f.WriteFile('OVERWRITE', !lines)` | Write an array of lines to a file | Verified | 16 Sep 2026, 17 Sep 2026, run 11 | Writes UTF-8 with BOM, read correctly by Notepad and Excel — no PMLLIB, no admin rights. A PML string is at most ~1000 characters, and one written line must stay under ~800 bytes. |

## Save and exit

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="get-work"></a>`GET WORK` | Pull other users' changes from the database | Seen in code |  |  |
| <a id="savework"></a>`SAVEWORK` | Save your work to the database | Verified | 17 Sep 2026 | Erases the rollback mark — afterwards UNDODB answers No mark to UNDO to. Save only after checking. |
| <a id="quit"></a>`QUIT` | Exit WITHOUT saving | Seen in code |  | Rolls back the whole session. The second line of defence: UNDODB undoes one mark, QUIT — everything since the last SAVEWORK. |
| <a id="finish"></a>`FINISH` | Exit with saving | Seen in code |  |  |

## Variables and substitution

Works right in the Command Line. Anything beyond substitution lives in a macro file — see the next section.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="x-3"></a>`!!x = 3` | Global variable, lives for the whole session | Verified |  | Non-Latin text in the value works. |
| <a id="x-3-2"></a>`!x = 3` | Local — only inside a macro | Verified | 19 Sep 2026 | In the Command Line it does not survive to the next line — use !!x there. |
| <a id="var-x-name"></a>`VAR !!x NAME` | Read an attribute of the current element into a variable | Verified | 22 Sep 2026, 23 Sep 2026 | Works in the Command Line too. VAR reads an attribute of any type into a string; !x = NAME fails if the types do not match. |
| <a id="p-x"></a>`$P $!!x` | Print the value | Verified | 11 Oct 2026, run 18 |  |
| <a id="cmd-q-name-then-cmd"></a>`!!cmd = 'Q NAME'   then   $!!cmd` | Run a command built as a string | Verified |  | The only way found to be dynamic without a macro. |
| <a id="var-eq-collect-all-equi-with-type-eq-equi-for-ce"></a>`VAR !!eq COLLECT ALL EQUI WITH ( TYPE EQ 'EQUI' ) FOR CE` | Collect elements with a filter | Verified | 16 Sep 2026, 22 Sep 2026, 23 Sep 2026 | Collects, but the result has no array methods: !!eq.Size() is an error. do !e values !!eq works. |
| <a id="m-c-temp-t-mac-arg1-arg2"></a>`$M C:\Temp\t.mac arg1 arg2` | Run a macro with arguments | Verified | 27 Aug 2026 | $1…$9 are available in the file. Non-Latin text in the file body reads correctly only if the file is saved in ANSI; UTF-8 breaks. |
| <a id="if-then-endif"></a>`if … then … endif` | Condition | Macro only |  | Plain paste — PML: Invalid syntax. Through right-click → Paste as Macro it works. |
| <a id="do-enddo"></a>`do … enddo` | Loop | Macro only |  | The same. |
| <a id="handle-any-endhandle"></a>`handle any … endhandle` | Catch an error | Macro only |  | The same. |
| <a id="var-x-owner"></a>`VAR !!x OWNER` | An element's owner into a variable — then $!!x goes to it | Verified | 1 Oct 2026 | Returns '/name'. |
| <a id="var-x-collect-all-cwbran-with-unset-desc-for-pml"></a>`VAR !x COLLECT ALL CWBRAN WITH (UNSET(DESC)) FOR /PMLC` | Collect with a condition on an attribute | Verified | 19 Sep 2026 | Gave 2 of 6 — exactly the number without a description. Logical functions apply to attributes inside WITH. |
| <a id="var-s-collect-all-site-for-world"></a>`VAR !s COLLECT ALL SITE FOR WORLD` | Collect across the whole database | Verified | 22 Sep 2026 |  |
| <a id="nm-name"></a>`!nm = NAME` | An attribute of the current element into a variable (in a macro) | Verified | 19 Sep 2026 | !x = REF — the reference. If !x already holds a string and the attribute is a number — incompatible types. |
| <a id="a-object-array"></a>`!!a = object ARRAY()` | An array; .Append() adds | Verified | 16 Sep 2026 |  |
| <a id="h"></a>`$H` | Help | Documented |  |  |

## The PML language — works in a macro file, not in the Command Line

E3D 2.1 runs PML2 with full backward compatibility with PML1: one interpreter, both syntaxes work and mix in real macros. Anything longer than one line will not run from a plain paste — each line goes as a separate command (if and endif each fail on their own). The way out is in the docs: right-click → Paste as Macro writes the paste to a temporary file and runs it as a macro, and there blocks work. So logic can run straight from the Commands window — just from a different menu item.

| Command | What it does | Status | Runs | Note |
|---|---|---|---|---|
| <a id="comment"></a>`$* comment` | A comment in a macro | Seen in code |  | On a par with --; appears 103 times in the code corpus. |
| <a id="if-x-gt-5-then-elseif-else-endif"></a>`if ( !x gt 5 ) then … elseif … else … endif` | Condition, PML1 form | Seen in code |  | PML1: comparisons only in words eq ne gt lt ge le, variables !name, substitution $!name. |
| <a id="if-x-5-and-n-matchwild-pipe-then"></a>`if ( !x > 5 and !n.Matchwild('PIPE*') ) then` | Condition, PML2 form | Seen in code |  | PML2 added == != > < and the logical AND OR NOT. Matchwild appears 37 times in the corpus. |
| <a id="do-i-from-1-to-10"></a>`do !i from 1 to 10` | Counting loop | Seen in code |  | 88 times in the corpus. |
| <a id="do-i-from-1-to-10-by-2"></a>`do !i from 1 to 10 by 2` | Loop with a step | Verified | 26 Oct 2026, run 25 | Run of 26 Oct 2026, in a macro: do !i from 1 to 5 by 2 printed 1, 3, 5. |
| <a id="do-elem-values-array"></a>`do !elem values !array` | Loop over array values | Seen in code |  | The most common form, 117 times. |
| <a id="do-i-indices-array"></a>`do !i indices !array` | Loop over indices | Seen in code |  | 5 times in the corpus. |
| <a id="do-while-flag"></a>`do while ( !flag )` | Loop on a condition — does NOT work | Fails | 26 Oct 2026, run 25, run 26 | Run of 26 Oct 2026, in a macro: CP: Syntax error, pointing at while; the macro stops (handle does not catch it). Instead — do !i from 1 to N with break if ( … ); break if is not checked yet — a probe in the next run. |
| <a id="break"></a>`break` | Leave the loop | Seen in code |  |  |
| <a id="skip"></a>`skip` | Go to the next iteration | Seen in code |  |  |
| <a id="break-if-skip-if"></a>`break if ( … ) / skip if ( … )` | Leave or skip on a condition | Documented |  | skip if met once, break if — never. |
| <a id="handle-any-endhandle-2"></a>`handle any … endhandle` | Catch any error | Seen in code |  | 193 times in the corpus. It goes RIGHT AFTER the guarded line, not before it. |
| <a id="handle-41-64"></a>`handle (41,64)` | Catch a specific error by number | Documented |  | Not met in the corpus. |
| <a id="elsehandle-none-elsehandle-any"></a>`elsehandle NONE / elsehandle ANY` | Handler branches: no error / any | Seen in code |  | 47 times in the corpus. |
| <a id="error-text"></a>`$!!error.text` | Text of the caught error | Seen in code |  | In the corpus. The code and line fields — by the documentation. |
| <a id="return-error-1-could-not-run"></a>`return error 1 'Could not run'` | Raise your own error | Seen in code |  | 3 times in the corpus. |
| <a id="m-c-temp-t-mac-arg1-arg2-2"></a>`$M C:\Temp\t.mac arg1 arg2` | Run a macro from the Command Line | Verified | 26 Aug 2026 | The only bridge between the command line and the language: the call itself works. |
| <a id="define-function-name"></a>`define function !!name` | A function in name.pmlfnc | Documented | 16 Sep 2026 | The file must sit in a PMLLIB folder, and those are not writable for a normal user — the way is closed. |
| <a id="setup-form-name-exit"></a>`setup form !!name … exit` | A form with fields and buttons straight from a macro | Verified | 27 Sep 2026 | Via Paste as Macro the form appeared without PMLLIB, buttons work — a field, !!CE.Name, q var, $M file.mac. define method after exit — Method not found: keep the logic in .mac files. |
| <a id="endif"></a>`endif` | End of if (macro only) | Macro only | 27 Aug 2026 | Plain paste — Invalid syntax; through Paste as Macro — works. |
| <a id="enddo"></a>`enddo` | End of do (macro only) | Macro only |  | The same. |
| <a id="endhandle"></a>`endhandle` | End of handle (macro only) | Macro only |  | The same. |
| <a id="golabel-label"></a>`golabel /label` | Jump to a label (and label /label) | Documented |  | Only in a macro file (SOFTCG 6.06.11). |
| <a id="return"></a>`return` | Leave the PML file | Documented |  | SOFTCG 4.04.03. |
| <a id="view-v-volume-width-60-height-20"></a>`view .v VOLUME width 60 height 20` | A 3D window in a form from a macro | Verified | 28 Sep 2026, run 13 | Shows everything the main 3D view shows. |
| <a id="edgpacket"></a>`EDGPACKET` | Pick a point on an edge with a click (definePosition) | Verified | 28 Sep 2026, run 13 | q var prints the point WRT the owner; the packet lives until Esc. |

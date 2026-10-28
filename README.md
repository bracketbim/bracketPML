<p align="center"><img src="assets/bracketpml.svg" width="96" alt="bracketPML"></p>

<h1 align="center">bracketPML</h1>

<p align="center"><b>PML for AVEVA E3D 2.1 — tested, not guessed.</b><br>
Every command here is tested in AVEVA E3D 2.1. Nothing is written from memory.</p>

<p align="center">
<a href="https://bracketbim.com/pml/">Search the library</a> ·
<a href="register.md">Register</a> ·
<a href="#modules">Modules</a> ·
<a href="#gotchas">Gotchas</a> ·
<a href="#myths">Myths</a> ·
<a href="attributes.md">Attributes</a> ·
<a href="syntax.md">Syntax</a> ·
<a href="CONTRIBUTING.md">Send a test report</a>
</p>

---

There is almost no public material on PML — and next to none on cable trays and cable supports. What exists is mostly «this should work». bracketPML is the opposite: a register of PML commands for AVEVA E3D 2.1, each one **tested in a real E3D 2.1 model**, with the exact answer E3D printed, and the traps found on the way.

**194 commands** in the register: **140 verified**, 10 documented failures, 16 macro-only, 19 from documentation and 9 from real code still waiting to be tested in E3D 2.1. Updated 28 Oct 2026.

## How to read a status

| Status | Meaning |
|---|---|
| ![Verified](https://img.shields.io/badge/-Verified-2e9d5c) | Ran in E3D 2.1, the result was checked. |
| ![Fails](https://img.shields.io/badge/-Fails-c94a4a) | Ran and gave an error. Do not use — the row says what to use instead. |
| ![Macro only](https://img.shields.io/badge/-Macro%20only-c98a1e) | Works in a macro file or with Paste as Macro, not line by line. |
| ![Documented](https://img.shields.io/badge/-Documented-6b7280) | In the AVEVA documentation or in the `$Q` grammar; not tested in E3D yet. |
| ![Seen in code](https://img.shields.io/badge/-Seen%20in%20code-4f6fae) | Appears in real PML code; not tested in E3D yet. |

A status changes **only after a test in E3D 2.1**. The order of trust: a test in E3D > `$Q` on the real machine > documentation > real code > reasoning.

## Modules

<a id="modules"></a>
Small, complete patterns you can copy into your own macros. Each has a **probe** — a short macro that shows the behaviour in *your* E3D, under a rollback mark.

- [Safe export — a file you can trust](modules/export-safe/README.md) — Write data from E3D to a text file with alpha log so that a broken or half-written file can never pass for a good one.
- [Text in PML without losses](modules/escaping/README.md) — How to write any text into an attribute — bars, quotes, the dollar sign — and the two cases that cannot be written at all.
- [Guard — undo a bulk change in one command](modules/guard/README.md) — E3D has no UNDO command, but it has a rollback. Put a mark before a bulk change, check, and either save or roll everything back at once.
- [Reorder — sort the model tree with the fewest moves](modules/reorder/README.md) — Sort members of a zone by name with REORDER, moving only the elements that are out of place, and prove the result before it reaches E3D.

## Gotchas

<a id="gotchas"></a>
Short notes named after the exact message E3D prints — search for the error, find the reason.

- [Your if block fails in the Commands window](gotchas/01-paste-runs-line-by-line.md) — `PML: Invalid syntax in the current context`
- [Part of your text disappears after a $](gotchas/02-dollar-eats-text.md) — `(no error — the text is just shorter)`
- [UNDODB says there is nothing to undo](gotchas/03-no-mark-to-undo.md) — `No mark to UNDO to`
- [There is no UNDO command — but there is a rollback](gotchas/04-there-is-no-undo.md) — `CP: Syntax error`
- [The command is fine — the value is not](gotchas/05-read-the-caret.md) — `CP: Syntax error`
- [RENAME with two names does not work](gotchas/06-rename-two-names.md) — `(2,109) Undefined name`
- [A COLLECT result has no array methods](gotchas/07-collect-has-no-size.md) — `Object does not have a member SIZE`
- [Reading an attribute into a variable fails](gotchas/08-incompatible-types.md) — `Cannot assign variable to result - incompatible types (STRING=REAL)`
- [A long line cannot be built or written](gotchas/09-string-too-long.md) — `CALCULATOR ERROR: The concatenated text is too long`
- [A file read from PML turns into mojibake](gotchas/10-readfile-encoding.md) — `(no error — «РЎРўРђР РћР•» instead of the text)`
- [POS put the element in the wrong place](gotchas/11-pos-is-from-owner.md) — `(no error — the element is just somewhere else)`
- [E3D accepts a box of length -100](gotchas/12-e3d-does-not-check-sizes.md) — `(no error — XLEN -100 is accepted)`

## Myths

<a id="myths"></a>
Things we were sure about and got wrong — and **why** the mistake was possible. A wrong fact is fixed once; a way of being wrong repeats.

- [«The manual says if works in the Command Line»](myths/01-blocks-in-command-line.md) — A plain paste runs each line alone, and if fails with «PML: Invalid syntax». Blocks work through Paste as Macro.
- [«E3D has no rollback»](myths/02-no-rollback.md) — The rollback is MARKDB / UNDODB. One UNDODB takes back everything under a mark — until SAVEWORK.
- [«CABLAY does not work»](myths/03-cablay-disputed.md) — The caret was on the value. CABLAY |CEN| works; text values need bars.
- [«Q MEM ATT prints the attributes of the members»](myths/04-q-mem-att.md) — Q MEM ATT is Q MEM plus Q ATT of the CURRENT element. Members' attributes are not there.
- [«A branch is as long as the distance between its end points»](myths/05-branch-length.md) — It is the sum of the segments between neighbouring POINTR — for a bent route the chord is shorter.
- [«There is no GOTO command»](myths/06-no-goto.md) — GOTO exists, but it follows a reference attribute (GOTO OWNER, GOTO PARENT…), not a name.
- [«PMLLIB is not set»](myths/07-pmllib-not-set.md) — Q EVAR |PMLLIB| inside E3D prints about ten paths. (They are not writable for a normal user — so the conclusion held, by accident.)
- [«Tray geometry belongs in the route points»](myths/08-geometry-in-points.md) — The numbers matched — but the edit gizmo sits on the branch POS. With POS at zero, every gizmo landed on the first tray.
- [«RENAME /OLD /NEW renames an element»](myths/09-rename-two-names.md) — There is no two-argument form — «(2,109) Undefined name». Stand on the element and RENAME /NEW (or NAME /NEW).

## Use it

- **Search** the whole library at [bracketbim.com/pml](https://bracketbim.com/pml/): by command, by error text, by status.
- **Copy** a module into your macro folder. The `.pmlmac` files are plain text; paste them with right-click → *Paste as Macro*.
- **Check** anything on your own installation with its probe. If your E3D answers differently, [tell us](CONTRIBUTING.md) — your version goes into the register.

## The tools behind it

The register is built from the reference of **[PML Console](https://bracketbim.com/app/)** — a browser tool that writes PML for cable trays, cable supports and equipment. Try the free demo; a version set up for your catalogues and rules is available on request: [info@bracketbim.com](mailto:info@bracketbim.com).

## Licence

Code (`.pmlmac`, `.py`, `.js`) — [MIT](LICENSE). Text — [CC BY 4.0](LICENSE-DOC).
bracketPML is an independent project, not affiliated with or endorsed by AVEVA. AVEVA and E3D are trademarks of their owners. See [DISCLAIMER](DISCLAIMER.md).

[bracketbim.com](https://bracketbim.com) · [Telegram](https://t.me/bracketbim) · [YouTube](https://www.youtube.com/channel/UCHJ7CHzWSxiN43U371hUpzQ) · [LinkedIn](https://www.linkedin.com/in/iurii-shchegolev-a88b0bb8)

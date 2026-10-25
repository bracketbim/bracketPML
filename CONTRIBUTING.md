# Send a run report

The register grows from runs. If you ran a command or a probe in your E3D, your result is valuable — **especially** when it differs from ours, and especially on a version other than 2.1.

## What makes a good run report

1. **E3D version** — from Help → About (for example *AVEVA E3D Design 2.1.0.x*, *3.1*).
2. **What you ran** — the exact lines, as you pasted them.
3. **How you ran it** — typed, plain paste, or right-click → *Paste as Macro*.
4. **What E3D printed** — copy the answer word for word, including error numbers like `(2,109)` and the caret line `^^`.
5. **What you checked afterwards** — `Q ATT`, `Q MEM`, the 3D view.

Please remove project names, references and paths you do not want to share — the register only needs the command and the answer.

## How to send it

- **GitHub:** open an issue with the *Run report* template — it asks for exactly these five things.
- **Mail:** [info@bracketbim.com](mailto:info@bracketbim.com), subject «Run report».
- **Telegram:** [t.me/bracketbim](https://t.me/bracketbim).

## What happens next

The report is repeated on our side where possible and goes into the register with its version and date. A status changes only after a run — a report is the run, not an opinion about it. Reports that contradict the register are the most useful of all: they become [myths](README.md#myths) when we were wrong, or version notes when both answers are right.

## Pull requests

Text fixes and new probes are welcome. The register itself (`register.md`, `register.json`) is **generated** from the source of truth — please send changes to it as a run report rather than an edit.

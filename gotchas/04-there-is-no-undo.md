# There is no UNDO command — but there is a rollback

> UNDO gives a syntax error. The rollback is MARKDB / UNDODB, and one UNDODB takes back everything under a mark.

**E3D prints:** `CP: Syntax error`

**Commands:** `UNDO` **Fails** · `MARKDB` **Verified** · `UNDODB` **Verified**

## What you see

You type `UNDO` after a wrong change and get `CP: Syntax error`.

## Why

There is no command with that name. The rollback exists, but it is called `MARKDB` (set a mark before the change) and `UNDODB` (go back to it). It undoes changed attributes, renames and created elements. One `UNDODB` takes back **everything under one mark** at once; `UNDODB 2` goes back two marks.

We believed «E3D has no rollback» for two months because we searched for the word `UNDO`. A search for `UNDODB` in any PML code would have found it at once. A failed command closes **that line**, not the topic.

## The rule

Put `MARKDB |what you are about to do|` before every bulk change. If it goes wrong — `UNDODB`.

## Check it yourself

```
UNDO
```

…fails. And this works (on a test element with a DESC):

```
MARKDB |probe|
DESC |probe text|
UNDODB
Q DESC
```

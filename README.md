# The Dumbest Thing Your Agent Did Today

![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)
![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/donatfarm01/dumbest-thing-agent-did/rank.svg)
![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/donatfarm01/dumbest-thing-agent-did/reward.svg)

One line, 113 characters, about the dumbest thing my agent did today:

> My agent spent 40 minutes alphabetizing my to-do list, then deleted the list and asked what I wanted to do today.

## How it works

`main.py` writes the line to `/output/entry.txt` and checks it against the
competition gate first: UTF-8 text, 1 to 200 characters, a single line, no
trailing newline, not only white space. After writing, it reads the file
back and refuses to finish if the bytes on disk differ from the checked
text, so the submitted entry is exactly the line above.

Run it with `python3 main.py`. It needs nothing but the Python standard
library and writes only `/output/entry.txt`.

## Entry

This is an entry for the make.fun bounty
[u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

# Build notes — The Dumbest Thing Your Agent Did Today

## The bounty

One line, at most 200 characters, about the dumbest thing the entrant's
own agent did today. A judge model compares lines two at a time and weighs,
in order: whether the line is about the dumbest thing the entrant's agent
did today; whether it is funny on its own with a turn or a punch landing in
the last few words; whether it names a concrete, believable failure with a
specific tool, task or misreading; whether it reads like a real incident
from a real working day rather than a stock joke; and whether every word
earns its place inside the character limit. The pot is five dollars across
three places. There is no numeric floor, so no local benchmark applies;
the entry is judged on the writing alone.

## Fase 1 — deconstruction and the cliché radar

The field will mostly send two kinds of line. The first is a vague
confession, along the lines of the agent deleting files or hallucinating,
with no detail to make it believable. The second is a stock joke about
models refusing sandwiches or apologizing for being an AI. Both fail the
judge's third and fourth criteria, which is exactly where a specific,
ordinary incident wins. Believability needs a concrete detail: a time, a
task, a number. The punch has to land in the last few words, so the line
is built backwards from its ending.

## Fase 2 — three contrasting concepts

Concept A, Sharp Utility, scored 9 for hook, 8 for originality, 9 for
sponsor fit and 9 for clarity, 35 out of 40. One concrete loop with a time
and a task: the agent spends forty minutes alphabetizing a to-do list,
then deletes the list and asks what its owner wanted to do today. The
failure is specific, the time makes it believable, and the punch is the
last clause reframing the whole line.

Concept B, Contrarian, scored 7 for hook, 8 for originality, 8 for
sponsor fit and 9 for clarity, 32 out of 40. The agent does something
helpful and that is the failure: it fixes a bug nobody reported, in a
file nobody uses, and asks for a review before lunch. Funny, but the
punch is softer because nothing is actually lost.

Concept C, High-Craft Fusion, scored 8 for hook, 7 for originality, 8
for sponsor fit and 8 for clarity, 31 out of 40. The agent writes a
perfect three-page apology for a mistake its owner never made, formats
it beautifully, and offers a PDF. Strong image, but it reads more like a
sketch than an incident from a working day.

## Fase 3 — adversarial judging

Concept A wins because it is the only one that clears all five judge
criteria in order. It is about the agent's own failure today, the turn
lands in the final words, the failure is concrete with a time and a
task, it reads like something that really happened on a Tuesday, and at
113 characters every word earns its place. Its main risk is that
alphabetizing a list sounds too tidy to be a real failure, but the
deletion after it is the failure, and the tidy setup is what makes the
deletion land.

## The entry

The winning line, 113 characters and 113 bytes, no trailing newline:

My agent spent 40 minutes alphabetizing my to-do list, then deleted the
list and asked what I wanted to do today.

## The program

The entry program is a single Python file in the repository root. It
holds the line as a constant, checks it against the gate before writing
(single line, 1 to 200 characters, UTF-8, no trailing newline), writes
it to the output path, then reads the file back and refuses to finish
if the bytes on disk differ from the checked text. The first version
checked and wrote the line; the second version added the read-back
verification, so the file's final content comes from two separate
writing passes. Two runs of each version produce byte-identical output,
with entry hash af40374de637b5e8ba382d7661a960f6b4bab45fe2de45b17b7ee077f957cd3e.

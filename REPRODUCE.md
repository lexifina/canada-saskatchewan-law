# How this repository was made (Saskatchewan)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Legislative Assembly of Saskatchewan: Votes and Proceedings (Minutes) | <https://docs.legassembly.sk.ca/legdocs/Assembly/Minutes/> | 2026-10-30 | Facts only (bill number, title, Royal Assent date); no text of the Votes and Proceedings is reproduced |
| Legislative Assembly of Saskatchewan: Progress of Bills (per session) | <https://www.legassembly.sk.ca/legislative-business/bills/> | 2026-10-30 | Facts only (bill number, title, Royal Assent date); no text of the tables is reproduced |
| Wikidata | <https://www.wikidata.org/wiki/Q1989> | 2026-10-30 | CC0 1.0 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue` | Catalogue of Saskatchewan bills given Royal Assent (title, bill number and Royal Assent date only) | 67 | 2006-12-06 to 2026-05-14 |
| `legal-system` | Saskatchewan: legal system facts (Wikidata) | 1 | 2026-10-30 to 2026-10-30 |

The build made 68 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 66 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 68 laws in the record.
- 134 tags.

## Dates

Each commit is dated at noon (America/Regina) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Catalogue entries are dated by the day of Royal Assent recorded in the Assembly's Votes and Proceedings; they describe bills and are not law text. https://www.legassembly.sk.ca/legislative-business/minutes-votes/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `556eacb559df79cda0793b3054aa4541d1faeda0d8e87de0a7d65d7fa2ff1ba8` (322914 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- No law text is published: Publications Saskatchewan (King's Printer) forbids redistribution without a written copyright release, and the Copyright Act (Canada) gives no exemption for provincial statutes. Nothing was fetched from it.
- The catalogue holds facts only: bill number, English title, and the Royal Assent date recorded in the Assembly's Votes and Proceedings for each sitting day. Chapter numbers (S.S. year, c. N) are not in that source and are not given.
- Coverage: the 30th Legislature comes from the Votes and Proceedings. Earlier sessions, back to the 3rd session of the 25th Legislature (2006), come from the Assembly’s published Progress of Bills tables; the 24th and 23rd Legislatures’ tables were not machine-readable and are not used. For the 25th to 27th Legislatures (sessions 1 to 3) a Royal Assent date is used only when two or more bills share it, to screen out misread cells.
- Where the Progress of Bills table and a Votes and Proceedings Royal Assent list disagree (the 4 December 2025 Minutes list bills that the table, whose readings run to April 2026, shows as assented on 12 March and 14 May 2026), the Progress of Bills date is used.
- Wikidata facts (CC0) form the "legal-system" act in one version dated by the retrieval date 2026-10-30: Wikidata gives only the year (1905) for the province's inception, so no day-precision date exists.
- Not built: treaty actions (Saskatchewan is not a party to treaties).

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Sonnet 5.5 wrote Lexifina's code and chose the sources; it did not write or alter any legal text. The code is deterministic and runs no model.

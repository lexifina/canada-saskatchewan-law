# Saskatchewan: law history in git

The law of Saskatchewan as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

**Metadata only, no law text, because Saskatchewan's statutes are published by the King's Printer (Publications Saskatchewan), whose terms prohibit redistribution without a written copyright release, and Canada's Copyright Act gives provincial statutes no exemption.** This repository records which bills received Royal Assent and when, and a handful of open facts about the province's legal system. To read a statute, go to [Publications Saskatchewan](https://publications.saskatchewan.ca). Text will be added if the King's Printer grants a release.

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `catalogue/` | Catalogue of bills given Royal Assent: title, bill number and Royal Assent date only | 67 | 67 Royal Assent days from 6 December 2006 to 14 May 2026 (818 bills, 25th to 30th Legislatures) |
| `legal-system/` | Legal system facts from Wikidata (CC0) | 1 | The facts Wikidata held on 30 October 2026 (no day-precision date exists) |

## Source

The catalogue's bill numbers, English titles and Royal Assent dates are facts taken from the Legislative Assembly of Saskatchewan's [Votes and Proceedings](https://www.legassembly.sk.ca/legislative-business/minutes-votes/) for each sitting day from 26 November 2024 (30th Legislature) and, for earlier sessions back to 2006, from the Assembly's [Progress of Bills](https://www.legassembly.sk.ca/legislative-business/bills/) tables; no text of those documents is reproduced. Where the two disagree the Progress of Bills date is used. The Wikidata facts are from [Wikidata](https://www.wikidata.org/wiki/Q1989) (CC0).

## Dates

A catalogue entry is dated by the day of Royal Assent recorded in the Votes and Proceedings, not by commencement (many Saskatchewan Acts commence on proclamation) and is credited to a `catalogue-<date>` entry. The Wikidata facts are dated by the retrieval date (30 October 2026): Wikidata gives only the year (1905) for the province's inception.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law (or, for facts, the retrieval) that made the change, with an e-mail address that cannot exist (`<law key>@legassembly.sk.ca.invalid`). The committer is always Lexifina.

## Limits

Only bills assented from the 3rd session of the 25th Legislature (late 2006) onward are listed; earlier statutes are not, and for the 25th to 27th Legislatures a date shared by only one bill is left out. Chapter citations (S.S. year, c. N) are not in the source and are not given. Entries do not record later amendment or repeal. Nothing here is an official record of the statutes.

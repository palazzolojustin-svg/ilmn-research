# ILMN Research Workspace

A research workspace on Illumina (ILMN) and its publicly traded competitors (Oxford Nanopore, PacBio, Roche, Thermo Fisher, 10x Genomics, MGI Tech), built to be used with [Claude Code](https://claude.com/claude-code).

## Getting started

1. Clone the repo and open the folder in Claude Code (desktop app Code tab, or `claude` in a terminal from this folder).
2. Claude automatically loads `CLAUDE.md`, which holds the operating rules: it reads the Core Notes first, then sends agents into the Working Notes for each question.
3. To read the material yourself, start with `Core Notes/00_Start_Here.md`.

## Layout

- `Core Notes/`: the master briefing, synthesized from all sources. Start with `00_Start_Here.md`.
- `Working Notes/INDEX.md`: one entry per source document.
- `Working Notes/Extracts/`: a readable note for every source document.
- `Working Notes/Sources/`: the original documents.
- `Working Notes/Outputs/`: analyses, primers, datasets and artifacts produced in chats.
- `Inbox/`: drop new Markdown files (or zips of them) here to ingest.
- `_Build/`: the build and ingest script (`build.py`) and its state.

## Adding new material

Put files in `Inbox/`, then run:

```
python _Build/build.py start ingest
```

This needs Python 3 and a logged-in Claude CLI. `python _Build/build.py status` shows progress. After ingesting, commit and push so the rest of the team gets the update.

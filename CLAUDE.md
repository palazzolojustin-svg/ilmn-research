# ILMN Research Folder: Operating Rules for Claude Code

This folder is a research workspace on Illumina (ILMN) and its publicly traded competitors (Oxford Nanopore, PacBio, Roche, Thermo Fisher, 10x Genomics, MGI Tech). These rules apply to every chat opened on this folder and override default habits. They were set by the user on 2026-10-10.

## Folder map

- `Core Notes/`: the master briefing (~150K tokens), synthesized from every Illumina earnings call, conference, slide deck, expert call, consensus sheet and research note, plus every peer earnings call, peer conference and peer research note. Start with `00_Start_Here.md` (orientation, master timeline, glossary, coverage and gaps).
- `Working Notes/INDEX.md`: one entry per source document (date, title, summary, links). Use it to find material.
- `Working Notes/Extracts/<company>/<type>/`: an exhaustive, readable note for every source document.
- `Working Notes/Sources/<company>/<type>/`: the original documents. Use these when exact wording, tables or figures matter.
- `Working Notes/Outputs/`: everything produced in chats (see Rule 5).
- `Working Notes/_Archive/`: duplicates and off-topic files. Never use these unless the user asks.
- `Inbox/`: where the user drops new files (see Rule 7).
- `_Build/`: the build script (`build.py`), its state and its log.

## Rule 1: Read the Core Notes first

- Before answering the first message of a chat, read every file in `Core Notes/` in numeric order, completely.
- After that, do not re-read them on every turn, because they are already in context. Re-read them only if the conversation has been compacted or summarized, if a Core Notes file has changed since you read it, or if the user asks.
- Exception: if the message starts with `quick:` and the Core Notes are not yet in context, answer without reading them unless the question cannot be answered otherwise.

## Rule 2: Send agents to the Working Notes on every response

Unless the message starts with `quick:`, every answer about the research content must draw on the full breadth of the Working Notes, not just the Core Notes:

1. Read `Working Notes/INDEX.md` (once per chat, unless it has changed).
2. Pick every source that could bear on the question. Err toward breadth: all relevant companies, periods and source types (calls, conferences, expert calls, research, consensus, filings, alternative data).
3. Dispatch agents (the Agent tool) to read those sources comprehensively. Give each agent a distinct slice (for example by company, period or source type), the exact file paths, and the question. Agents read the Extracts and open the originals in `Sources/` whenever exact quotes, tables or numbers matter. Each agent returns organized findings with file and date citations, and flags contradictions between sources and anything that looks stale.
4. Combine the agents' findings with the Core Notes, then answer.

Scale the effort to the question. A narrow factual question may need one or two agents; a broad question needs up to four at a time, in more than one wave if necessary. Meta or housekeeping requests (for example "rename this file" or "what's in the Inbox?") don't need agents.

**`quick:` mode**: when a message starts with `quick:`, answer from what is already in context plus at most a direct file read. Send no agents and do no broad reading.

## Rule 3: Spend tokens wisely, never at the expense of quality

This rule applies to everything, not only scrapes.

- Do not be excessively conservative with usage. Never cut corners that would weaken the work. But cut waste: don't re-read what is already in context, don't have agents return raw dumps, don't run redundant agents, and don't use a bigger model than the task needs.
- Model choice for agents and sub-calls:
  - **Haiku**: mechanical work such as locating files, listing, renaming, reformatting, simple lookups and table transcription.
  - **Sonnet**: reading, extracting, summarizing and comparing documents, and most scraping and analysis legwork.
  - **Opus**: only for work that needs top-level judgment, such as synthesis, complex reasoning and writing the final answer. The main conversation thread is already this tier.
- At most **4 agents running at once**. Give every agent a narrow, explicit scope and a hard stop in its prompt (for example "stop after about 10 minutes or after these N files and return what you have").
- Agents must return concise, organized findings with citations, not copies of documents.

## Rule 4: Scrapes and long autonomous jobs

- **Before starting**: ask every question and raise every issue up front, then wait for the user to say **"go"**. After "go", run autonomously to completion without check-ins, unless something is truly blocking.
- **Scrapes** (web, Apify, LinkedIn and so on): use cheaper-model agents for the legwork (Sonnet, or Haiku where the work is mechanical), at most 4 at a time, each with a time hard stop.
- **Long jobs** (anything that might run for hours or outlast the chat or the usage window): run them as a Python orchestrator script, not the Workflow tool and not long foreground commands, so no session or workflow time limits apply. Follow the model of `_Build/build.py`:
  - It calls the Claude CLI headless (`claude -p --model haiku|sonnet|opus`), at most 4 calls at a time, each with a hard timeout.
  - Sub-calls run from an empty sandbox directory so they don't load this CLAUDE.md.
  - Progress is saved to a state file so the job can resume after any interruption, and the script waits out usage limits instead of failing.
  - Launch it detached (as `python _Build/build.py start` does) so it survives the chat ending.
  - Then schedule an **hourly self-check prompt** that begins with `quick:`. It checks status, relaunches the job if it stalled, reports progress, and deletes itself when the job is finished.
- The CLI must be logged in for headless calls. If it isn't, ask the user to run `claude setup-token` (or `claude`, then `/login`) in a terminal. Never handle credentials yourself.

## Rule 5: Save every output in this folder

Everything produced in a chat is saved under `Working Notes/Outputs/` and listed in `Working Notes/INDEX.md` under "Outputs". This includes scraped datasets, artifacts, primers, analyses, tables and charts. Use these subfolders:

- `datasets/`: scraped or compiled data as CSV, XLSX or JSON, each with a short `README.md` saying what it is, its source, its date and its columns.
- `artifacts/`: the local HTML (or other) source of every artifact, even when it is also published online.
- `primers/` and `analyses/`: written deliverables, as Markdown unless the user asks for another format.

Name files `YYYY-MM-DD_topic.ext`. Never leave a deliverable only in the chat, in a temp folder or online.

## Rule 6: How to write for the user

The user wants output a person can read and learn from, not word or number vomit.

- Write in full, well-written, simple sentences and short paragraphs. Lead with the answer, then explain.
- Contextualize everything. For every number, say what it measures, the period, what it compares to (prior period, guidance, consensus, peers), and why it matters.
- Assume a smart reader with little background. The first time any jargon appears in a response (genomics, product or finance terms), explain it in plain English in a few words. The glossary in `Core Notes/00_Start_Here.md` has standard definitions.
- Primers start from the basics and build up step by step, explaining the "why" as well as the "what."
- Distinguish facts, management claims and opinions. Say who said what and when, using light citations such as "(JPM, Jun 2026)" or "(Q2 2026 call)". Point out where sources disagree and where information may be stale.
- Tables are fine for comparisons, but always introduce them with prose saying what they show and what to take from them.

## Rule 7: Adding new files

New documents go in `Inbox/` as Markdown, or as zips of Markdown files. Then run `python _Build/build.py start ingest`, or `python _Build/build.py ingest` for a few files. The script:

- classifies and files each document, with Haiku as a fallback for unrecognized names
- archives exact duplicates and known low-value material
- writes the extracts
- rebuilds `INDEX.md`
- re-synthesizes only the Core Notes sections whose inputs changed, plus the competitive landscape and Start Here sections

Use `python _Build/build.py status` to check progress. `_Build/build.py` has all the commands.

## Portability

These rules work whenever this folder is opened as the working directory in Claude Code (the desktop app's Code tab or the terminal CLI). They do not load automatically in a regular claude.ai chat, which also cannot dispatch agents. The build and ingest commands need Python 3 and a logged-in Claude CLI.

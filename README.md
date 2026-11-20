# sanjar — Hermes Agent docs expert

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) profile distribution. The agent knows the
complete official documentation at <https://hermes-agent.nousresearch.com/docs> (all 252 pages, shipped
offline in the `hermes-docs` skill) and answers questions about installing, configuring, using and
extending Hermes with exact commands and links to the source page.

## Install

```bash
hermes profile install https://github.com/nF-2403-Teamwork/sanjar.git
sanjar setup      # API keys / model, if this machine has none yet
sanjar chat
```

It also appears in the Hermes dashboard / desktop app profile switcher as **sanjar**.

Update later with `hermes profile update sanjar` (your memories, sessions and `.env` are never touched).

## Contents

| Path | What |
|---|---|
| `SOUL.md` | Persona: Hermes documentation expert, answers from the docs, cites URLs |
| `skills/hermes-docs/SKILL.md` | How to look things up |
| `skills/hermes-docs/references/INDEX.md` | The site's `llms.txt` — every page with URL and summary |
| `skills/hermes-docs/references/docs/` | One Markdown file per docs page (path = URL path) |
| `skills/hermes-docs/scripts/split_docs.py` | Rebuilds the snapshot from `llms-full.txt` |
| `config.yaml` | Model and runtime defaults |
| `distribution.yaml` | Distribution manifest |

## Refresh the docs snapshot

```bash
curl -fsSL https://hermes-agent.nousresearch.com/docs/llms-full.txt -o llms-full.txt
curl -fsSL https://hermes-agent.nousresearch.com/docs/llms.txt -o skills/hermes-docs/references/INDEX.md
rm -rf skills/hermes-docs/references/docs
python skills/hermes-docs/scripts/split_docs.py llms-full.txt skills/hermes-docs/references/docs
```

Snapshot taken: 2026-11-20.

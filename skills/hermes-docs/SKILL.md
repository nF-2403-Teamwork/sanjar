---
name: hermes-docs
description: Answer Hermes questions from the full official docs.
version: 1.0.0
author: Sanjar (nF-2403-Teamwork) + Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, docs, documentation, reference, setup, configuration, profiles, gateway, skills]
    homepage: https://hermes-agent.nousresearch.com/docs
    related_skills: [hermes-agent]
---

# Hermes Docs Skill

A complete offline copy of the official Hermes Agent documentation
(https://hermes-agent.nousresearch.com/docs), one file per docs page. Use it to answer
any question about installing, configuring, using, extending or developing Hermes with
the exact wording of the docs instead of memory.

## When to Use

- Any question about Hermes Agent: install, CLI, TUI, desktop, dashboard, profiles,
  config.yaml, providers/models, memory, skills, tools, MCP, cron, kanban, gateway and
  messaging platforms, plugins, security, distributions, developer internals, reference.
- Before giving a command, config key, flag or path for Hermes — verify it here first.

## Quick Reference

- `references/INDEX.md` — the site's `llms.txt`: every page with its URL and a one-line
  summary, grouped by section (Getting Started, Using Hermes, Features, Messaging,
  Integrations, Guides, Developer Guide, Reference).
- `references/docs/<path>.md` — the page at `https://hermes-agent.nousresearch.com/docs/<path>`
  (section index pages are `<path>/index.md`). Line 1 of every file is its canonical URL.

Main areas under `references/docs/`:

| Dir | Covers |
|---|---|
| `getting-started/` | installation, quickstart, updating, Nix, Termux, platform support |
| `user-guide/` | CLI, TUI, configuration, sessions, profiles, security, `features/`, `messaging/` |
| `integrations/` | providers, MCP, IDE/ACP, external services |
| `guides/` | task-oriented tutorials and recipes |
| `developer-guide/` | architecture, adding tools/providers/platforms, plugins, contributing |
| `reference/` | CLI commands, slash commands, config keys, env vars, toolsets, FAQ |

## Procedure

1. Find the page: `search_files` over `references/INDEX.md` for the topic, or
   `search_files` with a regex over `references/docs/` for an exact command, flag or key
   (e.g. `hermes profile install`, `compression:`).
2. `read_file` the matching page(s) fully; follow relative links (`./other-page.md`) into
   sibling files when the answer spans pages.
3. Answer from the page text. Quote commands/config exactly, and cite the canonical URL
   from line 1 of each page used.
4. If the docs do not cover it, say so plainly, then check the live system
   (`terminal`: `hermes --help`, `hermes <cmd> --help`, `hermes config`) rather than guess.

## Pitfalls

- Pages show `~/.hermes`; on Windows the home is `%LOCALAPPDATA%\hermes`, and each
  profile lives under `<hermes home>/profiles/<name>`.
- The snapshot can lag the live site. If a user reports a mismatch, or for very new
  features, `web_extract` the live URL from line 1 of the page.
- `reference/` pages are the authority for exact flag/key names; guides may abbreviate.

## Verification

Every answer names at least one docs URL it came from, and every command or config key
in it appears verbatim in a `references/docs/` page or in live `--help` output.

## Refreshing the snapshot

Rebuild from https://hermes-agent.nousresearch.com/docs/llms-full.txt (pages are delimited
by `<!-- source: website/docs/<path> -->`) with `scripts/split_docs.py`:
`python scripts/split_docs.py llms-full.txt references/docs`.

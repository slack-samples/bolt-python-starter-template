# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## What This Is

A generic Bolt for Python template app used to build Slack apps.

## Slack Plugin

To install the Slack plugin for your coding agent, follow [Claude Code, Codex, Cursor, and Other Coding Agents](./README.md#claude-code-codex-cursor-and-other-coding-agents) in the README.

## Slack Skills

Slack skills are pre-installed in `.agents/skills` (and `.claude/skills` for Claude Code). Use them for Slack work. If the Slack plugin is installed, prefer its `slack:` skills, such as `slack:block-kit`, which may be newer.

## Before you finish

Run `ruff check .`, `ruff format --check .`, and `pytest`. CI runs the same on every PR.

## Code Style

- Snake-case filenames
- No code comments. Make the code explain itself with clear names, tests, or types. Put the reason for a change in the PR description.

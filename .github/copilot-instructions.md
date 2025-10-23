<!-- .github/copilot-instructions.md: guidance for AI coding agents working on this repo -->
# head-cli — Copilot instructions

This repository is a tiny Python CLI (a simplified `head` implementation) packaged with setuptools. The goal of these notes is to give an AI coding agent the immediate, practical knowledge needed to make safe, correct edits.

- Big picture
  - Single-package CLI located in `head_cli/`.
  - Primary implementation: `head_cli/main.py` — a Click-based command `main(file, lines, number, color)` that reads a file and prints the first N lines.
  - Packaging: `setup.py` declares a console script `head-cli = head_cli.__main__:main`. Note: there is no `head_cli/__main__.py` in the repo — the implementation lives in `head_cli/main.py`. When changing entrypoints, either update `setup.py` to point to `head_cli.main:main` or add a `__main__.py` that imports/forwards to `main()`.

- Important files
  - `head_cli/main.py` — CLI logic and options. Examples of patterns to follow: uses `click.command`, option short/long forms (`-n/--lines`), and flags (`--number`, `--color`). Error handling prints to stderr with `click.echo(..., err=True)`.
  - `setup.py` — package metadata and `console_scripts`. Changing CLI export requires updating this file.
  - `pyproject.toml` — minimal PEP517 build-system declaration (setuptools backend).
  - `Dockerfile` — builds a container by installing build deps, running `python setup.py develop`, and then `pip install -e .`; ENTRYPOINT is `head-cli`. Be cautious: the Dockerfile assumes the console script name from `setup.py` is valid at runtime.

- Developer workflows (how to run / validate changes)
  - Local dev install (editable):
    - python -m pip install --upgrade pip setuptools wheel
    - python -m pip install -e .
    - Run the CLI: `head-cli <file>` (after install) or run directly `python head_cli/main.py <file>` for quick checks.
  - Container build: Dockerfile uses Debian slim image and installs build tools; it expects `head-cli` entrypoint to be available after install. If you change the console_script, update the Dockerfile's ENTRYPOINT.
  - Quick runtime example (useful for tests or debugging): `python head_cli/main.py README.md -n 5 --number`

- Project-specific conventions and gotchas for agents
  - Keep the Click interface stable: CLI flags are user-facing and used in the Docker ENTRYPOINT.
  - Packaging vs implementation mismatch: `setup.py` points to `head_cli.__main__:main` but implementation is in `head_cli/main.py`. Fixes should prefer the least disruptive change (usually change `setup.py` to `head_cli.main:main`) and include a short note in the commit message.
  - Use `click.echo(..., err=True)` when emitting errors (matches existing style).
  - Small, focused changes only — this repo is intentionally tiny. Avoid introducing heavy frameworks or extra top-level packages.

- Tests and lint
  - There are no tests or linters in the repo. When adding tests, prefer `pytest` and use `click.testing.CliRunner` to call `main()` directly (example):
    - from click.testing import CliRunner
      runner = CliRunner()
      result = runner.invoke(main, ["README.md", "-n", "3"])

- Integration and dependencies
  - Only declared runtime dependency is `click` (see `setup.py`). Keep changes to dependency list minimal and update `setup.py` accordingly.

- When you change behavior
  - Update `head_cli/main.py` and run locally with `python head_cli/main.py` or install editable and run `head-cli` to validate end-to-end behavior.
  - If you modify the console entrypoint, update `setup.py` and `Dockerfile` ENTRYPOINT where applicable.

If any part of this repo's intent is unclear (for example, whether the author intended `__main__.py` vs `main.py` as the exported entrypoint), ask a short clarifying question before making large changes.

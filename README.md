# Python Playground

![Tests](https://github.com/weilini/python-playground/actions/workflows/tests.yml/badge.svg)

A hands-on software engineering portfolio project demonstrating production-ready QA and backend development practices.

---

## About This Project

This repository is a hands-on software engineering portfolio project built to production standards: layered automated tests, continuous integration, static analysis, and clear documentation. Every module has tests, every change goes through CI, and every design decision is documented.

Current focus: Software Engineering / Platform Engineering
Long-term goal: Continuously building my knowledge and skills, and growing this GitHub portfolio with real, working projects

---

## What's Inside

### `src/` — Python learning modules

| Module | What I learned |
|--------|----------------|
| `basics.py` | Variables, types, f-strings, functions |
| `data_structures.py` | Lists, dicts, sets, comprehensions |
| `functions.py` | Default args, `*args`, `**kwargs` |
| `file_io.py` | File handling, JSON, error handling |
| `oop_basics.py` | Classes, objects, `self` |
| `oop_advanced.py` | Inheritance, polymorphism |
| `decorators.py` | Function decorators |
| `api_client.py` | REST API calls with `requests` |
| `todo/` | A CLI To-Do app with JSON persistence |
| `utils/` | Shared utilities (math, string, file) |

### `pages/` — Page Object Model

- `base_page.py` — shared navigation and URL/title helpers
- `login_page.py` — LoginPage (login, logout, assertions)
- `checkboxes_page.py` — CheckboxesPage
- `dropdown_page.py` — DropdownPage


### `tests/` — Automated tests

- **244 passing tests** (52 e2e skipped by default)
- Uses **pytest**, **fixtures**, **parametrize**, **mocking**
- **64% code coverage** (unit + API tests)
- `tests/api/` — 55 API tests using `responses` for mocking (7 files)
- `tests/e2e/` — 52 Playwright UI tests (skipped in CI; run locally with `RUN_E2E=1`)
- **Total: 296 tests collected**

### `docs/` — Learning notes

- `qa-fundamentals.md` — QA theory
- `istqb-notes.md` — ISTQB CTFL study notes (6 chapters)
- `api-testing-notes.md` — REST API testing
- `mock-exam-1.md` — Mock exam results
- `playwright-notes.md` — Playwright assertion patterns (Day 4)
- `playwright-pom.md` — Page Object Model (Day 5)
- `playwright-fixtures.md` — pytest fixtures + conftest (Day 6)

### `qa/` — QA artifacts

- `postman-collection.json` — 19 Postman assertions for JSONPlaceholder API

### `dsa-practice/` — Data Structures & Algorithms

- LeetCode solutions (in progress)

---

## Tech Stack

- **Language:** Python 3.12
- **Testing:** pytest, pytest-cov, responses (mock), jsonschema (validation)
- **Code quality:** Black, Ruff, mypy, pre-commit
- **CI/CD:** GitHub Actions (test on Python 3.11 + 3.12)
- **Tools:** Git, Linux (Ubuntu), VS Code, Postman

---

## Setup

```bash
# Clone
git clone git@github.com:weilini/python-playground.git
cd python-playground

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

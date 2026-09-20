# Python Playground

![Tests](https://github.com/weilini/python-playground/actions/workflows/tests.yml/badge.svg)

A personal learning repository documenting my transition from **IT Support** into **QA Engineering** and **Software Engineering**.

---

## About This Project

After 7+ years in IT support, system administration, and software QA, I decided to make a deliberate career transition into software engineering. This repository is my learning log — every commit, every test, and every note reflects that journey.

**My path:**
- **Background:** IT Support, System Administration, SQL DBA
- **Current focus:** QA Engineering (ISTQB CTFL in progress)
- **Long-term goal:** Software Engineering / Platform Engineering

I'm not just learning — I'm building. Every module has tests. Every change goes through CI. Every lesson is documented.

---

## What's Inside

### `src/` — Python learning modules

| Module | What I learned |
|--------|----------------|
| `basics.py` | Variables, types, f-strings, functions |
| `collections.py` | Lists, dicts, sets, comprehensions |
| `functions.py` | Default args, `*args`, `**kwargs` |
| `file_io.py` | File handling, JSON, error handling |
| `oop_basics.py` | Classes, objects, `self` |
| `oop_advanced.py` | Inheritance, polymorphism |
| `decorators.py` | Function decorators |
| `api_client.py` | REST API calls with `requests` |
| `todo/` | A CLI To-Do app with JSON persistence |
| `utils/` | Shared utilities (math, string, file) |

### `tests/` — Automated tests

- **179 tests** across 14 test files
- Uses **pytest**, **fixtures**, **parametrize**, **mocking**
- **61% code coverage**

### `docs/` — Learning notes

- `qa-fundamentals.md` — QA theory
- `istqb-notes.md` — ISTQB CTFL study notes (6 chapters)
- `api-testing-notes.md` — REST API testing
- `mock-exam-1.md` — Mock exam results

### `qa/` — QA artifacts

- `postman-collection.json` — 19 Postman assertions for JSONPlaceholder API

### `dsa-practice/` — Data Structures & Algorithms

- LeetCode solutions (in progress)

---

## Tech Stack

- **Language:** Python 3.12
- **Testing:** pytest, pytest-cov
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

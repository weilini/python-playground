# Python Playground

![Tests](https://github.com/weilini/python-playground/actions/workflows/tests.yml/badge.svg)

A hands-on software engineering portfolio project demonstrating production-ready QA and backend development practices.

---

## About This Project

This repository is a software engineering portfolio project built to production standards: layered automated tests, continuous integration, static analysis, and clear documentation. Every module has tests, every change goes through CI, and every design decision is documented.

**Current focus:** Software Engineering / Platform Engineering  
**Long-term goal:** Continuously building my knowledge and skills, and growing this GitHub portfolio with real, working projects.

---

## Project Structure

The codebase is organized by purpose to separate application logic, UI testing, and documentation:

- **`src/`** — Core application and utility modules.
  - Includes Python fundamentals (`basics.py`, `data_structures.py`), advanced concepts (`oop_advanced.py`, `decorators.py`), a REST API client (`api_client.py`), and a CLI To-Do app (`todo/`).
- **`pages/`** — Page Object Model (POM) implementations for UI tests (Login, Checkboxes, Dropdown).
- **`tests/`** — 296 automated tests across three layers.
  - **API Tests:** 55 tests using `responses` for mocking.
  - **E2E Tests:** 52 Playwright UI tests.
  - **Unit Tests:** 64% code coverage.
  - Uses `pytest` with fixtures, parametrization, and mocking.
- **`docs/`** — Engineering and QA documentation.
  - Includes Playwright POM patterns, API testing guides, and ISTQB CTFL study notes.
- **`qa/`** — QA artifacts, including a Postman collection with 19 assertions for API validation.
- **`dsa_practice/`** — Ongoing Data Structures & Algorithms practice (LeetCode).

---

## Tech Stack

- **Language:** Python 3.12
- **Testing:** pytest, pytest-cov, responses (mock), jsonschema (validation), Playwright (UI)
- **Code Quality:** Black (formatting), Ruff (linting), mypy (type checking), pre-commit hooks
- **CI/CD:** GitHub Actions (runs on Python 3.11 and 3.12)
- **Tools:** Git, Linux (Ubuntu), VS Code, Postman

---

## Setup & Installation

To run this project locally:

```bash
# 1. Clone the repository
git clone git@github.com:weilini/python-playground.git
cd python-playground

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Run the test suite
pytest
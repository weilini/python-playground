# Stage 4 Complete — QA Automation (Playwright)

**Date:** 2026-09-21
**Duration:** 7 days
**Status:** ✅ Complete

---

## What I Learned

### Day 1 — Playwright Basics
- Installing Playwright + Chromium
- `page.goto()`, `expect()` basics
- First test against python.org
- Understanding browser context and pages

### Day 2 — Locators
- `get_by_role`, `get_by_label`, `get_by_text`, `get_by_placeholder`
- CSS selectors and `locator()`
- Strict mode violations → `exact=True`, `.first`, `.nth(n)`
- Login flow with `get_by_label` for accessible selectors

### Day 3 — Forms + Inputs
- `fill()`, `clear()`, `press()`
- Dropdowns: `select_option(value=..., label=...)`
- Checkboxes: `check()`, `uncheck()`, `is_checked()`
- File uploads: `set_input_files()`
- Keyboard: `press("Enter")`, `press("Tab")`
- Clicking links by text and role

### Day 4 — Assertions Deep Dive
- Web-first (auto-retrying) assertions vs non-retrying Python asserts
- `to_have_text`, `to_be_visible`, `to_be_enabled`, `to_have_value`
- `to_have_count`, `not_to_be_visible`
- Soft assertions: `expect.soft()` — collect multiple failures
- Custom timeouts
- Why `time.sleep()` is never needed with web-first assertions

### Day 5 — Page Object Model
- `pages/` folder structure
- `BasePage` with `open()` (returns `Self` for chaining)
- Page objects: `LoginPage`, `CheckboxesPage`, `DropdownPage`
- Class-level locators (defined once)
- Fluent methods returning `self`
- `to_have_url` needs `re.compile()` for pattern matching
- `typing.Self` for base-class methods that return `self`

### Day 6 — Fixtures + conftest
- `pytest.fixture` — reusable setup
- `conftest.py` — auto-available fixtures, no imports
- Fixtures returning page objects
- Fixture scopes (function default; session/module/class)
- "3+ tests" rule for extracting fixtures
- Tests read like behaviour specs, not setup

### Day 7 — Review + Release
- Full suite review
- Documentation of the sprint
- Tagged release `v0.4.0`

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Days completed | 7 |
| New e2e tests | 52 |
| Page objects created | 4 (Base + 3 pages) |
| Fixtures created | 3 |
| Docs written | 3 (playwright-notes, playwright-pom, playwright-fixtures) |
| CI fix commits | 1 (install Playwright browsers) |
| Flakiness fixes | 1 (homepage timeout) |
| Git commits | 7 |

---

## Skills Mastered

| Category | Skills |
|----------|--------|
| **Playwright** | Navigation, locators, forms, assertions, auto-wait |
| **Architecture** | Page Object Model, BasePage inheritance, fluent API |
| **pytest** | Fixtures, conftest, dependency injection |
| **Typing** | `typing.Self`, method chaining |
| **CI** | Playwright browsers in GitHub Actions |
| **Debugging** | Strict mode, timeouts, flaky tests |

---

## Deliverables

- ✅ `tests/e2e/` — 5 test files, 52 tests
- ✅ `pages/` — 4 page objects
- ✅ `tests/e2e/conftest.py` — 3 fixtures
- ✅ `docs/playwright-notes.md` — assertion notes
- ✅ `docs/playwright-pom.md` — POM notes
- ✅ `docs/playwright-fixtures.md` — fixture notes
- ✅ CI green with Playwright browser install
- ✅ Tag: `v0.4.0`

---

## Key Debugging Lessons

1. **CI needs `playwright install`** — tests pass locally but fail on GitHub runners without it
2. **`to_have_url` needs `re.compile()`** — a plain string is treated as an exact match
3. **`-> Self` for fluent interfaces** — mypy can't follow subclass chaining without it
4. **`exact=True` / `.first` / `.nth(n)`** — strict mode requires disambiguation
5. **`wait_until="domcontentloaded"`** — lighter than `"load"`, better for CI
6. **Pre-commit auto-fixes** — re-stage after hook modifications
7. **External sites can be slow** — python.org occasionally exceeds 30s on CI
8. **Fixtures reduce boilerplate** — one line saved per test, ×10 tests = clean

---

## What This Sprint Proves

A working, professional-grade UI test suite:
- Page Object Model architecture
- pytest fixtures for setup
- Type-checked (mypy strict)
- Linted (ruff, 9 rule sets)
- Formatted (black)
- CI on Python 3.11 + 3.12
- 52 UI tests + 179 unit/API tests
- Published CI badge

This is the same tooling used by professional QA teams.

---

## Next Steps

**Remaining Stage 4 topics:**
- API automation (Python `requests` deep dive)
- Selenium basics (comparison to Playwright)
- Load testing (Locust / k6)
- Test reporting (Allure)
- DSA: LeetCode problems daily (parallel)

**Then Stage 5 — Portfolio projects**

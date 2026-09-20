# Career Transition — Progress Tracker

**Name:** Lini Wei
**Location:** Cork, Ireland
**Background:** 7+ years IT Support / SysAdmin / SQL DBA
**Current role:** Business System Developer at Logitech (contract ends Sept 2026)
**Goal:** QA Engineer (primary, 6-9 months) → SWE (long-term, 12+ months)
**Status:** Stamp 4, no visa sponsorship needed

**Repo:** github.com/weilini/python-playground
**Local path:** ~/projects/python-playground
**ISTQB CTFL exam:** November 2026 (voucher purchased)

---

## Overall Roadmap

- Stage 1: Environment setup — COMPLETE (Sep 13, 2026)
- Stage 2: Python fundamentals — COMPLETE (117 tests, tag v0.2.0)
- Stage 2.5: QA foundations — PARTIAL (W1-4 done; ISTQB review deferred to Nov)
- Stage 3: Testing & tooling — COMPLETE (179 tests, tag v0.3.0)
- Stage 4: QA Automation + DSA — IN PROGRESS
- Stage 5: Portfolio projects — TODO
- Stage 6: CV + interview prep — TODO
- Stage 7: Apply + land first job — TODO
- Stage 8: On-the-job + growth — TODO

---

## Stage 4 Detail

Playwright sprint (7 days):

- Day 1: Playwright basics — COMPLETE
- Day 2: Playwright locators — COMPLETE
- Day 3: Forms + inputs — COMPLETE
- Day 4: Assertions deep dive — COMPLETE
- Day 5: Page Object Model — COMPLETE
- Day 6: Fixtures + conftest — NEXT
- Day 7: Review + commit — TODO

After Playwright sprint:

- TODO: API automation (Python requests deep dive)
- TODO: Selenium basics
- TODO: Load testing (Locust / k6)
- TODO: Test reporting (Allure)
- TODO: DSA: LeetCode daily (parallel side track)

---

## Repo Structure (as of Day 5)

- `.github/workflows/tests.yml` — CI (Python 3.11 + 3.12 + Playwright install)
- `.pre-commit-config.yaml` — 8 hooks
- `pyproject.toml` — Ruff, Black, mypy, pytest config
- `README.md` — CI badge + personal story
- `PROGRESS.md` — THIS FILE
- `docs/` — playwright-notes (Day 4), playwright-pom (Day 5), ISTQB notes, QA notes
- `pages/` — base_page, login_page, checkboxes_page, dropdown_page
- `src/` — 13 modules
- `tests/e2e/` — test_homepage (4), test_locators (12), test_forms (14), test_assertions (12), test_pom_login (10)
- `tests/` — 15 more files, 179 unit/API tests
- `dsa-practice/two_sum.py`

**Test count:** ~231 (179 unit/API + 52 e2e)
**Coverage:** 61% (unit only)

---

## Recent Commits (Stage 4)

- f446177 fix: increase homepage test timeout and use domcontentloaded
- c42a81f feat: add Page Object Model and POM-based tests (Stage 4 Day 5)
- 7a183f8 feat: add Playwright assertion tests (Stage 4 Day 4)
- 99fd59a ci: install Playwright browsers in GitHub Actions
- eb96664 feat: add Playwright form tests (Stage 4 Day 3)

**CI status:** green (latest run)
**Tags:** v0.2.0 (Stage 2), v0.3.0 (Stage 3)

---

## Repo Structure (as of Day 5)

- `.github/workflows/tests.yml` — CI (Python 3.11 + 3.12 + Playwright install)
- `.pre-commit-config.yaml` — 8 hooks
- `pyproject.toml` — Ruff, Black, mypy, pytest config
- `README.md` — CI badge + personal story
- `PROGRESS.md` — THIS FILE
- `docs/` — playwright-notes (Day 4), playwright-pom (Day 5), ISTQB notes, QA notes
- `pages/` — base_page, login_page, checkboxes_page, dropdown_page
- `src/` — 13 modules
- `tests/e2e/` — test_homepage (4), test_locators (12), test_forms (14), test_assertions (12), test_pom_login (10)
- `tests/` — 15 more files, 179 unit/API tests
- `dsa-practice/two_sum.py`

**Test count:** ~231 (179 unit/API + 52 e2e)
**Coverage:** 61% (unit only)

---

## Recent Commits (Stage 4)

- f446177 fix: increase homepage test timeout and use domcontentloaded
- c42a81f feat: add Page Object Model and POM-based tests (Stage 4 Day 5)
- 7a183f8 feat: add Playwright assertion tests (Stage 4 Day 4)
- 99fd59a ci: install Playwright browsers in GitHub Actions
- eb96664 feat: add Playwright form tests (Stage 4 Day 3)

**CI status:** green (latest run)
**Tags:** v0.2.0 (Stage 2), v0.3.0 (Stage 3)

---

## Key Lessons Learned

- requests must be in pyproject.toml — CI fails silently without it
- Pre-commit auto-fixes files — re-run git add then git commit
- Playwright strict mode: exact=True, .first, .nth(n)
- to_have_title() accepts regex strings; to_have_url() needs re.compile()
- Use -> Self when a base method returns self for chaining
- python.org in CI sometimes >30s — use wait_until="domcontentloaded", timeout=60_000
- Never name files after stdlib modules
- Always activate venv at session start

---

## Next Session — Start Here

**Say:** "Let's do Stage 4 Day 6 — Fixtures + conftest"

Day 6 plan:

- Create tests/e2e/conftest.py
- Add fixtures: login_page, checkboxes_page, dropdown_page
- Refactor test_pom_login.py to use fixtures
- Notes: docs/playwright-fixtures.md
- Commit: feat: add pytest fixtures and conftest (Stage 4 Day 6)

After Day 6: Day 7 (review + STAGE4_COMPLETE.md + tag v0.4.0)

---

## Environment

- OS: Ubuntu 24.04.5 LTS
- Python: 3.12.3
- Git: 2.43.0
- VS Code: 1.137.0
- pytest: 9.1.1
- Playwright: pytest-playwright 0.9.0, Chromium
- Virtual env: .venv (always active)

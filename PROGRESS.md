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
- Stage 4: QA Automation + DSA — IN PROGRESS (Playwright sprint complete; API/Selenium/load/DSA remaining)
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
- Day 6: Fixtures + conftest — COMPLETE
- Day 7: Review + commit — COMPLETE

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
**Tags:** v0.2.0 (Stage 2), v0.3.0 (Stage 3), v0.4.0 (Stage 4 Playwright sprint)

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
**Tags:** v0.2.0 (Stage 2), v0.3.0 (Stage 3), v0.4.0 (Stage 4 Playwright sprint)

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

**Stage 4 Playwright sprint is COMPLETE** (Days 1–7, tag v0.4.0).

**Next sprint choices (pick one when ready):**

1. **API automation** — Python requests deep dive
   - Most valuable for QA job listings
   - Builds on your existing api_client.py and Postman work
   - Recommended next

2. **Selenium basics** — comparison to Playwright
   - Many legacy QA teams still use Selenium
   - Short sprint (~2-3 days)

3. **Load testing** — Locust or k6
   - Non-functional testing
   - Nice to have, not urgent

4. **Test reporting** — Allure
   - Pretty reports for CI
   - Short sprint

5. **DSA practice** — LeetCode daily (parallel side track)
   - Runs alongside any sprint
   - Not a "block" — always on

**Recommended:** Start API automation sprint, run DSA daily in parallel.

---

## Environment

- OS: Ubuntu 24.04.5 LTS
- Python: 3.12.3
- Git: 2.43.0
- VS Code: 1.137.0
- pytest: 9.1.1
- Playwright: pytest-playwright 0.9.0, Chromium
- Virtual env: .venv (always active)

---

## Parallel Tracks (all phases)

These run alongside the main stages — small, ongoing habits.

### DSA (LeetCode)

- Cadence: 3-5 problems/week, 45 min each
- Method: try yourself (15 min) -> hints (5 min) -> solution (10 min) -> rewrite from scratch (10 min) -> explain out loud (5 min)
- Order: follow NeetCode 150 (arrays -> two pointers -> sliding window -> stacks -> binary search -> linked lists -> trees -> DP)
- Location: dsa-practice/<pattern>/<problem>.py with tests + time/space complexity in docstring
- Review: Sunday, re-solve one older problem from memory
- Milestones: 50 problems (Nov 2026), 100 (Jan 2027), 150 (Mar 2027)

### Career Networking

- 1 LinkedIn message/week to a QA/SWE person in Cork
- 1 coffee chat/month with someone in the industry
- 1 Cork tech meetup/quarter (Python, DevOps, QA)
- English writing polish: cover letters, PR descriptions, docs

### ISTQB CTFL

- Exam: November 2026 (voucher purchased)
- Weak areas to review: Ch 3 (Static Testing), Ch 4 (Test Design)
- Target: 65%+ (currently 67-72% on mocks)

### Trevor Plan (mentor + potential referral)

Trevor Desmond — Sr SWE Manager, Acuity Cork. 30+ years in IT dev, built teams.
Former manager, warm relationship.

- Now: send career-advice message (not asking for job yet)
- +1 month: update with progress
- +2 months: update + ask about his team
- +3 months: apply or ask for referral
- +6 months: follow up if no role yet

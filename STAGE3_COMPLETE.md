# Stage 3 Complete — Testing & Tooling

**Date:** 2026-09-20
**Duration:** 7 days
**Status:** ✅ Complete

---

## What I Learned

### Day 1 — pytest Fixtures
- `@pytest.fixture` decorator
- Built-in fixtures: `tmp_path`, `capsys`
- Custom fixtures
- Fixture dependencies
- `yield` fixtures (setup + teardown)
- Fixture scopes: function, class, module, session

### Day 2 — pytest Parametrize
- `@pytest.mark.parametrize` decorator
- Parameter name lists
- Multiple inputs per test
- Error case testing with `pytest.raises`
- Test IDs (`ids=[...]`)
- Multiple parametrize (cartesian product)

### Day 3 — pytest Mocking
- What mocking is
- `@patch` decorator
- `Mock()` objects
- `mock.return_value` and `mock.side_effect`
- `mock.call_args` verification
- Why mocking matters (fast, stable, CI-friendly)

### Day 4 — CI/CD with GitHub Actions
- GitHub Actions workflow (YAML)
- Triggers: push, pull_request
- Matrix builds (Python 3.11 + 3.12)
- Debugging CI failures
- Dependency management
- CI badge in README

### Day 5 — Pre-commit Hooks
- `.pre-commit-config.yaml`
- 8 hooks: trailing-whitespace, end-of-file-fixer, check-yaml,
  check-added-large-files, check-merge-conflict, black, ruff, mypy

### Day 6 — Linting & Formatting
- Ruff as fast linter
- 9 rule sets: E, W, F, I, N, UP, B, C4, SIM
- Configuration in pyproject.toml
- Per-file ignores
- Black vs Ruff format

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Days completed | 7 |
| Tests written | 179 |
| Test coverage | 61% |
| Pre-commit hooks | 8 |
| Ruff rule sets | 9 |
| Python versions tested | 2 (3.11, 3.12) |
| Git commits | 14 |

---

## Skills Mastered

| Category | Skills |
|----------|--------|
| **Testing** | pytest fixtures, parametrize, mocking |
| **CI/CD** | GitHub Actions, matrix builds, CI badges |
| **Quality** | Pre-commit, Ruff, Black, mypy |
| **Config** | pyproject.toml, per-file rules |

---

## Deliverables

- pytest fixtures demo (9 tests)
- pytest parametrize demo (35 test cases)
- pytest mocking demo (8 tests)
- GitHub Actions CI (Python 3.11 + 3.12)
- Pre-commit hooks (8 hooks)
- Ruff configuration (9 rule sets)
- CI badge in README

---

## Next Steps

**Stage 4 — QA Automation + DSA**
- Playwright for UI automation
- API automation (Python requests deep dive)
- Selenium basics
- Load testing (Locust / k6)
- Test reporting (Allure)
- DSA: LeetCode problems daily

---

## Reflection

Over the past 7 days, I went from basic testing to professional-grade
testing infrastructure. My project now has:

- Automated tests that run on every push
- Quality checks that run before every commit
- Linting with 9 rule sets
- Type checking with mypy
- Formatting with Black

**This is the same tooling used by professional software teams.**

Ready for Stage 4. 🚀

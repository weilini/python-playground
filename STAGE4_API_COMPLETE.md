# Stage 4 — API Automation Complete

**Date:** 2026-10-12
**Duration:** 7 days
**Status:** ✅ Complete

---

## What I Learned

### Day 1 — Mock Testing with `responses`
- Why mocked tests are better than hitting real APIs
- `responses` library — intercepts HTTP calls
- `@responses.activate` decorator
- `responses.calls` — inspect what was actually sent
- Speed: 15s (real API) → 1.8s (mocked)

### Day 2 — Authentication + Headers
- Bearer token auth (`Authorization: Bearer <token>`)
- Basic auth (base64-encoded `user:pass`)
- API key in custom headers (`X-API-Key`)
- Testing 401 vs 403 error paths
- Verifying headers on outgoing requests

### Day 3 — Parametrize + Error Handling
- `@pytest.mark.parametrize` — one test, many inputs
- 3 test functions → 18 test cases
- Error scenarios:
  - HTTP errors (4xx / 5xx)
  - Timeouts
  - Connection failures
  - Invalid JSON responses
  - Empty response bodies

### Day 4 — Session-Based Client + Fixtures
- `requests.Session` — connection reuse
- `APIClient` class — encapsulates base URL, timeout, auth
- `conftest.py` fixtures (`api`, `authed_api`)
- Generator return type for fixtures with `yield`
- Cleaner tests: setup lives in fixtures, not in every test

### Day 5 — Retry Logic
- `urllib3.Retry` configuration
- Retry only transient errors (5xx, timeouts, connection failures)
- Don't retry client errors (4xx) — pointless
- Don't retry non-idempotent methods (POST) — risky
- Exponential backoff (0.5s → 1s → 2s)
- `contextlib.suppress` instead of `try/except/pass`

### Day 6 — JSON Schema Validation
- Validating response *structure*, not just values
- `jsonschema` library
- Schema defines: required fields, types, additional properties
- Catch missing fields, wrong types, unexpected fields
- Pairs with value assertions — different jobs

### Day 7 — Review + Release
- Full suite review (244 passed, 52 skipped)
- Documentation
- Tagged release `v0.5.0`

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Days completed | 7 |
| New API tests | 45 (from 10 → 55) |
| Total project tests | 296 (244 passed + 52 skipped) |
| Coverage | 64% |
| New dependencies | `responses`, `jsonschema` |
| Git commits | 8 |

---

## Skills Mastered

| Category | Skills |
|----------|--------|
| **Mocking** | `responses`, intercepting HTTP calls |
| **Auth** | Bearer, Basic, API Key |
| **Testing** | Parametrize, error paths, edge cases |
| **Architecture** | `APIClient` class, `conftest.py` fixtures |
| **Resilience** | Retry strategy, exponential backoff |
| **Validation** | JSON Schema for structural checks |
| **CI** | Fast, reliable pipelines (~50s) |

---

## Deliverables

- ✅ `tests/api/` — 7 test files, 55 tests
- ✅ `src/api_client.py` — extended with `APIClient` class, retry logic, schemas
- ✅ `tests/api/conftest.py` — shared fixtures
- ✅ CI fix — e2e tests now skipped by default (`RUN_E2E=1` to enable)
- ✅ Tag: `v0.5.0`

---

## Key Debugging Lessons

1. **CI takes 22 min with e2e hitting external sites** — fix: skip e2e by default, use `RUN_E2E=1` to opt in
2. **`GitHub` DNS fails, browser succeeds** — Python's `socket` doesn't use browser proxies
3. **mypy is strict about `dict`** — `dict[str, str | int]` is needed, not `dict[str, object]`
4. **Generator fixtures need `Generator[Type, None, None]`** — not just `Type`
5. **Ruff rejects `try/except/pass`** — use `contextlib.suppress` instead
6. **Pre-commit auto-fixes files** — re-stage after hook modifications
7. **`responses` needs one entry per retry attempt** — else the retry logic can't mock properly

---

## What This Sprint Proves

A production-grade API test suite:

- Fast (55 tests in 0.5s)
- Reliable (no external dependencies)
- Comprehensive (auth, retries, schemas, error paths)
- Professional structure (fixtures, base client, schemas)
- CI-friendly (~50s end-to-end)

This is the same approach used by QA teams at scale.

---

## Next Steps

**Stage 4 remaining topics:**
- Selenium basics (comparison to Playwright)
- Load testing (Locust / k6)
- Test reporting (Allure)
- DSA practice (ongoing)

**Then Stage 5 — Portfolio projects**

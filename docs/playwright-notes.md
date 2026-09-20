# Playwright — Assertion Notes (Stage 4 Day 4)

## Two kinds of assertions

| Type | Retries? | Use when |
|------|----------|----------|
| `expect(locator)...` (web-first) | ✅ Auto-retries up to 5s | UI state that may take time to settle |
| `assert x == y` (Python) | ❌ Instant | Values already in hand, or pure logic |

**Rule of thumb:** if you're asserting on a **locator**, use `expect()`.
If you're asserting on a **plain value**, use `assert`.

## Why auto-retry matters

Flaky tests usually come from timing. `expect()` polls the DOM until the
assertion passes or times out. This removes the need for `time.sleep()`.

```python
# Bad — race condition
time.sleep(2)
assert page.locator("#finish h4").inner_text() == "Hello World!"

# Good — auto-retries, exits early when true
expect(page.locator("#finish h4")).to_have_text("Hello World!")

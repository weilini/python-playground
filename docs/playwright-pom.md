# Playwright — Page Object Model Notes (Stage 4 Day 5)

## What POM is

Page Object Model (POM) puts each page's **locators** and **actions**
into a dedicated class. Tests then use those classes instead of touching
raw selectors.

## Why use POM

- **Single source of truth** — if the login page changes, fix `LoginPage`
  once, not every test
- **Readable tests** — `login.login(user, pw)` beats `page.fill("#username", ...)`
- **Reusable** — many tests can use the same page object
- **Testable** — page object logic can be unit-tested separately

## Structure we use

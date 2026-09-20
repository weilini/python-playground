# Playwright — Fixtures & conftest Notes (Stage 4 Day 6)

## What a pytest fixture is

A fixture is a reusable setup function. Declare it once, and pytest
injects its return value into any test that lists it as a parameter.

```python
@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page).open()

def test_something(login_page: LoginPage) -> None:
    login_page.login("user", "pw")   # page already open

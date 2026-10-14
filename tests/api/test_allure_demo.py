"""Allure reporting demo.

Demonstrates Allure annotations for richer HTML reports.
"""

import allure
import responses
from requests.exceptions import HTTPError

from src.api_client import BASE_URL, get_post


@allure.feature("API Client")
@allure.story("Get Post")
class TestGetPostWithAllure:
    """Demonstrates Allure annotations."""

    @allure.title("GET /posts/1 returns the correct post")
    @allure.description(
        "Tests that get_post(1) returns the post with id=1 "
        "when the API responds with 200 and valid JSON."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @responses.activate
    def test_get_post_success(self) -> None:
        with allure.step("Register mocked response"):
            responses.get(
                f"{BASE_URL}/posts/1",
                json={"id": 1, "title": "Allure Demo", "body": "Body", "userId": 1},
                status=200,
            )

        with allure.step("Call get_post(1)"):
            post = get_post(1)

        with allure.step("Verify the response"):
            assert post["id"] == 1
            assert post["title"] == "Allure Demo"

    @allure.title("GET /posts/9999 returns 404 → raises HTTPError")
    @allure.description(
        "Tests that a 404 response causes get_post to raise HTTPError "
        "via raise_for_status()."
    )
    @allure.severity(allure.severity_level.NORMAL)
    @responses.activate
    def test_get_post_404(self) -> None:
        with allure.step("Register 404 mocked response"):
            responses.get(f"{BASE_URL}/posts/9999", status=404)

        with allure.step("Expect HTTPError"):
            try:
                get_post(9999)
            except HTTPError:
                pass
            else:
                raise AssertionError("Expected HTTPError")

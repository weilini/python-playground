"""Locust load test for JSONPlaceholder API.

Simulates multiple users hitting API endpoints concurrently.

Run interactively (web UI):
    locust -f tests/load/locustfile.py --host=https://jsonplaceholder.typicode.com

Run headless (CLI):
    locust -f tests/load/locustfile.py \
        --host=https://jsonplaceholder.typicode.com \
        --headless --users 5 --spawn-rate 1 --run-time 20s
"""

from locust import HttpUser, between, task


class JSONPlaceholderUser(HttpUser):
    """Simulated user hitting JSONPlaceholder API."""

    wait_time = between(1, 3)  # wait 1-3 seconds between tasks

    @task(3)
    def get_post(self) -> None:
        """GET a single post — weighted 3x (most common)."""
        self.client.get("/posts/1")

    @task(2)
    def get_all_posts(self) -> None:
        """GET all posts — weighted 2x."""
        self.client.get("/posts")

    @task(1)
    def create_post(self) -> None:
        """POST a new post — weighted 1x."""
        self.client.post(
            "/posts",
            json={"title": "Load Test", "body": "Testing", "userId": 1},
        )

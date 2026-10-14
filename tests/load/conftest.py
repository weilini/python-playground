"""pytest config for tests/load/.

Tells pytest not to collect locustfile.py — it's a Locust load test
script, not a pytest test file.
"""

collect_ignore = ["locustfile.py"]

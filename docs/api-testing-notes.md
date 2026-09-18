# API Testing Notes

Learning API testing for QA — Stage 2.5 Week 3.

---

## What is an API?

**API = Application Programming Interface**

A way for two software systems to talk to each other.

**Real-world analogy:**
- You (client) order from a menu (API)
- Kitchen (server) cooks
- Waiter (API) brings food
- You don't go into the kitchen

**Software example:**
- Mobile app asks weather API "What's the temperature in Cork?"
- API responds: `{"temperature": 15, "condition": "cloudy"}`

**Why APIs matter for QA:**
- Mobile apps talk to backends via API
- Web apps load data via API
- QA engineers test APIs directly (faster than UI)

---

## What is REST?

**REST = Representational State Transfer**

Rules for building APIs. Most modern APIs are REST.

**Principles:**
- Stateless — each request has all needed info
- Client-server — client and server are separate
- Uses HTTP methods — GET, POST, PUT, DELETE
- Resources identified by URLs — `/users/123`

**URL structure:**
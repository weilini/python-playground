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


**Save (`Ctrl + S`).**

---

## STEP 4 — Quiz Myself

**Answer these 5 questions:**

1. What are the 5 HTTP methods and what do they do?  - ET (read), POST (create), PUT (replace full), PATCH (modify partial), DELETE (remove)
2. What does status code 404 mean? 401? 500? - 404 = Not Found; 401 = Unauthorized; 500 = Internal Server Error
3. What's the difference between PUT and PATCH? -  PUT replaces full object; PATCH modifies part
4. Why is API testing faster than UI testing? - PI tests skip the browser — just HTTP requests, so they're faster and more stable
5. What is JSON used for? - JSON is a data format for APIs — most modern APIs use it to send/receive data


</details>

**If you got 4/5 → ready for Day 2.**

---

## STEP 5 — Commit to GitHub

```bash
git status
git add docs/api-testing-notes.md
git commit -m "docs: add API testing fundamentals (Stage 2.5 Week 3 Day 1)"
git push
git --no-pager log --oneline -5

---

## HTTP Methods — Deep Dive

### GET — Read Data

- Purpose: Retrieve data
- Safe: Yes
- Idempotent: Yes
- Body: No

**Example:**


**What to test:**
- 200 for valid ID
- 404 for invalid ID
- 401 if auth required
- Correct data returned

---

### POST — Create Data

- Purpose: Create new resource
- Safe: No
- Idempotent: No (POST twice = 2 resources)
- Body: Yes

**Example:**


**What to test:**
- 201 for valid data
- 400 for invalid data
- 401 without auth
- Resource has correct fields
- POST twice creates 2 resources

---

### PUT — Replace Full Resource

- Purpose: Replace entire resource
- Safe: No
- Idempotent: Yes
- Body: Yes (full object)

**Example:**


**What to test:**
- 200 for valid data
- All fields updated
- PUT twice = same result

---

### PATCH — Modify Partial Resource

- Purpose: Modify specific fields
- Safe: No
- Idempotent: Depends
- Body: Yes (partial)

**Example:**


**What to test:**
- 200 for valid partial data
- Only specified fields updated
- Other fields unchanged

---

### DELETE — Remove Resource

- Purpose: Remove resource
- Safe: No
- Idempotent: Yes
- Body: Usually no

**Example:**


**What to test:**
- 204 for valid ID
- 404 for invalid ID
- Resource is gone (GET returns 404)
- DELETE twice returns 404 second time

---

## Idempotency

**Idempotent = doing it twice = same as doing it once.**

| Method | Idempotent? |
|--------|-------------|
| GET | ✅ Yes |
| POST | ❌ No |
| PUT | ✅ Yes |
| PATCH | ⚠️ Depends |
| DELETE | ✅ Yes |

**Why it matters:**
- Retry safety
- Network failure handling
- Test reproducibility

---

## Safe vs Unsafe Methods

**Safe = doesn't change server state.**

| Safe | Unsafe |
|------|--------|
| GET | POST |
| HEAD | PUT |
| OPTIONS | PATCH |
| | DELETE |

---

## Headers in API Testing

| Header | Purpose | Example |
|--------|---------|---------|
| Content-Type | Format of body | application/json |
| Accept | Expected response format | application/json |
| Authorization | Auth credentials | Bearer token123 |
| User-Agent | Client info | PostmanRuntime/7.32 |
| Cache-Control | Caching rules | no-cache |

---

## Testing Each Method — To-Do API Example

| Test | Method | Expected |
|------|--------|----------|
| Get all tasks | GET /tasks | 200, list |
| Get one task | GET /tasks/1 | 200, single |
| Get invalid task | GET /tasks/9999 | 404 |
| Create task | POST /tasks | 201, new with ID |
| Create missing title | POST /tasks | 400 |
| Update task (full) | PUT /tasks/1 | 200, all fields |
| Update task (partial) | PATCH /tasks/1 | 200, only specified |
| Delete task | DELETE /tasks/1 | 204 |
| Get deleted task | GET /tasks/1 | 404 |
| Create without auth | POST /tasks | 401 |

---

## Practice Questions — HTTP Methods

### Q1: Which method is idempotent but not safe?  - c

A. GET
B. POST
C. PUT
D. None

**Answer:** C

---

### Q2: What's the difference between PUT and PATCH?  - b

A. They're the same
B. PUT replaces full resource; PATCH modifies part 
C. PUT is for create; PATCH is for update
D. PUT is safe; PATCH is unsafe

**Answer:** B

---

### Q3: What status code does a successful POST return?  - b

A. 200
B. 201
C. 204
D. 404

**Answer:** B

---

### Q4: What status code does a successful DELETE return? - c

A. 200
B. 201
C. 204
D. 404

**Answer:** C

---

### Q5: Why is POST not idempotent? - b

A. It's unsafe
B. Each POST creates a new resource
C. It requires a body
D. It doesn't have a status code

**Answer:** B

---

## My Score: _4/5

## Questions I Have

- [ ] What's the difference between PATCH implementations?
- [ ] How do I test idempotency in Postman?

## Common Confusion — Status Codes

**WRONG:** "201 = invalid data, 200 = valid data"

**RIGHT:**
- 200 = OK (GET/PUT/PATCH success)
- 201 = Created (POST success)
- 204 = No Content (DELETE success)
- 400 = Bad Request (invalid data)
- 401 = Unauthorized
- 403 = Forbidden
- 404 = Not Found
- 500 = Server Error

**Rule:** 2xx = success. 4xx = client error. 5xx = server error.
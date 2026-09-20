# QA Fundamentals

Personal notes from my QA learning journey.

---

## QA vs Testing vs QC

| Term | Meaning | Focus |
|------|---------|-------|
| QA (Quality Assurance) | Process-focused — prevents defects | Building quality in |
| QC (Quality Control) | Product-focused — finds defects | Checking quality |
| Testing | Activity — executing tests | Running test cases |

**In practice:** Most job titles use "QA" to mean both QA and testing.

---

## The 7 Testing Principles (ISTQB)

1. **Testing shows presence of defects, not absence** — Tests find bugs; they can't prove no bugs exist
2. **Exhaustive testing is impossible** — Can't test everything; prioritize
3. **Early testing saves time and money** — Bugs found early are cheaper to fix
4. **Defect clustering** — Most bugs are in a few modules
5. **Pesticide paradox** — Running the same tests repeatedly stops finding new bugs
6. **Testing is context-dependent** — Different software needs different testing
7. **Absence-of-errors fallacy** — No bugs ≠ useful software

---

## The Testing Process

1. **Planning** — What, when, who
2. **Monitoring** — Track progress
3. **Analysis** — Identify test conditions
4. **Design** — Create test cases
5. **Implementation** — Prepare data/scripts
6. **Execution** — Run tests
7. **Completion** — Report results

Simplified: **Plan → Design → Execute → Report**

---

## Test Case Structure

| Element | Description |
|---------|-------------|
| ID | Unique identifier (TC-001) |
| Title | Brief description |
| Preconditions | What must be true before |
| Steps | Numbered actions |
| Expected Result | What should happen |
| Actual Result | What actually happened |
| Status | Pass / Fail |

---

## Defect Lifecycle

New → Assigned → In Progress → Fixed → Ready for Retest → Closed
                                     ↓
                                 Reopened
                                     ↓
                                 Deferred

**Key terms:**
- **Severity** — impact of the bug (Critical/High/Medium/Low)
- **Priority** — urgency to fix (High/Medium/Low)
- **Status** — current state in the lifecycle

**Example:**
- High severity, low priority: Typo in legal disclaimer
- Low severity, high priority: Logo wrong color on homepage

---

## Testing Types

| Type | Tests | Example |
|------|-------|---------|
| Unit | One function | `calculate_age()` |
| Integration | Multiple units | Login → database |
| System | Whole system | Entire app |
| Acceptance | User requirements | Client confirms |

**I've done:** Unit testing (pytest tests in Python Playground)

---

## Questions I Have

- [ ] What is the difference between severity and priority in practice?
**Severity** = technical impact of the bug
**Priority** = business urgency to fix

Examples:
- Payment crash: High severity, High priority
- Typo in ToS: Low severity, Low priority
- Logo wrong color: Low severity, High priority (CEO sees it)
- Crash on Windows XP: High severity, Low priority

**Key:** QA assigns severity; PM assigns priority.

- [ ] How do I write good test cases? (need examples)
5 rules:
1. Clear title
2. Specific steps
3. Explicit expected result
4. Independent
5. Repeatable

Structure:
- ID, Title, Preconditions, Steps, Expected Result, Actual Result, Status

Styles: Step-by-step, Gherkin (BDD), Exploratory

- [ ] What is a test plan?
Document describing how testing will be done for a project.

Sections: Scope, Objectives, Approach, Resources, Schedule, Risks, Entry/Exit criteria

- [ ] What is a test strategy vs test plan?

	Test Strategy	Test Plan
|---|---------------|-----------|
| Level | Organization-wide | Project-specific |
| When | Long-term | Sprint/release |
| Who | QA Manager | QA Lead |
| Reusable | Yes | No |

Strategy = "How we test in general"
Plan = "How we'll test THIS project"
---

## Resources

- ISTQB CTFL 4.0 Syllabus (official)
- Ministry of Testing
- Real World Testing with Python

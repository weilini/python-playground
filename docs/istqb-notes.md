# ISTQB CTFL Notes

My notes from studying the ISTQB Certified Tester Foundation Level (CTFL) 4.0 syllabus.

---

## Chapter 1 — Fundamentals of Testing

### What is Testing?

**ISTQB definition:**
> Testing is a set of activities to discover defects and evaluate the quality of software artifacts.

**In practice:**
- Find defects (bugs)
- Evaluate quality
- Not just clicking buttons — a structured process

### Why Testing is Necessary

- Find defects early (cheaper to fix)
- Ensure quality (users expect working software)
- Reduce risk (financial, safety, reputation)
- Meet requirements (legal, contractual)
- Build confidence

**Real-world failures:**
- Ariane 5 rocket (1996) — software bug, $370M loss
- Therac-25 (1980s) — killed patients
- Knight Capital (2012) — $440M in 45 minutes

### Testing vs Debugging

| Activity | Who | Purpose |
|----------|-----|---------|
| Testing | QA / Testers | Find defects |
| Debugging | Developers | Fix defects |

Flow: Test → Find → Report → Debug → Fix → Retest → Close

### QA vs QC vs Testing

| Term | Focus | Who |
|------|-------|-----|
| Testing | Activity | Testers |
| QC | Product | Testers/inspectors |
| QA | Process | Everyone |

- QA = prevent defects
- QC = detect defects
- Testing = activity supporting both

### The 7 Testing Principles

1. **Testing shows presence, not absence of defects** — can find bugs, can't prove no bugs
2. **Exhaustive testing is impossible** — can't test everything; prioritize
3. **Early testing saves time and money** — find bugs early
4. **Defect clustering** — bugs cluster in few modules
5. **Pesticide paradox** — same tests stop finding new bugs; update them
6. **Testing is context-dependent** — different software, different testing
7. **Absence-of-errors fallacy** — no bugs ≠ useful software

### The Testing Process (7 Activities)

1. Test Planning — scope, approach, resources
2. Test Monitoring & Control — track progress
3. Test Analysis — identify test conditions
4. Test Design — create test cases
5. Test Implementation — prepare data/scripts
6. Test Execution — run tests
7. Test Completion — report, archive

Simplified: Plan → Design → Execute → Report

### Testware

Any artifact created during testing:
- Test plan
- Test case
- Test data
- Test script
- Defect report
- Test summary report

### Roles in Testing

| Role | Responsibility |
|------|----------------|
| Test Manager | Plans, monitors, controls |
| Tester/QA Engineer | Designs, executes |
| Developer | Fixes bugs, unit tests |
| Business Analyst | Defines requirements |
| Product Owner | Prioritizes features |
| User/Customer | Accepts product |

---

## Key Takeaways from Chapter 1

- Testing is a **structured process**, not random clicking
- QA prevents defects, QC detects defects
- 7 principles guide all testing
- Testing process has 7 activities
- Testware is every artifact you create

---

## Questions I Still Have

- [ ] How do test managers measure testing progress?
- [ ] What's the difference between test analysis and test design?
- [ ] How do roles differ in Agile vs Waterfall?

---

## Exam Prep Notes

- **Testing vs Debugging:** Testing finds defects, debugging fixes them
- **7 principles:** presence not absence, exhaustive impossible, early testing,defect clustering, pesticide paradox,context-dependent,absence-of-errors fallacy. 
- **Testing process:** 7 activitises - test planing, test monitoring&control. test analysis, test design, test implementation, test execution, test completion
- **Testware:** all artifacts from resting: test plan, test case, teste data, test script, defect report

## Chapter 1 — Key Terms (from Syllabus)

| Term | Definition |
|------|------------|
| Coverage | Degree to which specified coverage items have been exercised by a test suite |
| Debugging | Finding and fixing the cause of failures |
| Defect | A flaw in a component or system that can cause failure |
| Error | A human action that produces an incorrect result |
| Failure | Deviation of the component or system from its expected result |
| Quality | Degree to which a component, system, or process meets requirements |
| Quality Assurance | Activities to ensure quality is built into the process |
| Root Cause | Primary reason for a problem |
| Test Object | The work product being tested |
| Testing | Set of activities to discover defects and evaluate quality |

**Important distinction:**
- **Error** → human mistake
- **Defect / Bug** → flaw in the code or document
- **Failure** → software deviates from expected behavior
- **Root Cause** → underlying reason for the defect

---

## Chapter 2 — Testing Throughout the SDLC

### What is SDLC?

**SDLC = Software Development Life Cycle**

Phases:
1. Requirements — What should it do?
2. Design — How will we build it?
3. Development — Write the code
4. Testing — Does it work?
5. Deployment — Release to users
6. Maintenance — Fix bugs, add features

### SDLC Models

| Model | Characteristics | Testing |
|-------|-----------------|---------|
| **Waterfall** | Sequential | Testing after development |
| **V-Model** | Sequential + testing planned | Each dev phase has matching test phase |
| **Agile** | Iterative, sprints | Testing in every sprint |
| **DevOps** | Continuous cycle | Testing is continuous (CI/CD) |

### Test Levels

| Level | Tests | Who | Example |
|-------|-------|-----|---------|
| Component/Unit | Functions, classes | Developers | `test_greet()` |
| Integration | Components together | Devs + QA | Login → database |
| System | Whole system | QA | Full user journey |
| Acceptance | User requirements | Users/QA | Client sign-off |

### Test Types

**By what they test:**
- Functional — features
- Non-functional — performance, security, usability

**By how they're designed:**
- Black-box — no knowledge of internals
- White-box — know the code
- Gray-box — some knowledge

### Confirmation vs Regression Testing

| Type | Purpose |
|------|---------|
| Confirmation | Verify the specific bug is fixed |
| Regression | Verify nothing else broke |

**Both are needed after any change.**

### Maintenance Testing

Testing changes to already-released software.

When: bug fixes, new features, environment changes, data migrations.

Two aspects:
1. Impact analysis — what might break?
2. Regression testing — re-test affected areas

### Key Terms (Chapter 2)

| Term | Definition |
|------|------------|
| SDLC | Software Development Life Cycle |
| V-Model | Sequential model with testing planned alongside development |
| Agile | Iterative development with sprints |
| DevOps | Continuous development + operations |
| Test Level | Unit, Integration, System, Acceptance |
| Functional Testing | Tests what the system does |
| Non-functional Testing | Tests how the system performs |
| Black-box Testing | Testing without knowing internals |
| White-box Testing | Testing with knowledge of code |
| Regression Testing | Re-testing to ensure changes didn't break anything |
| Confirmation Testing | Re-testing a specific bug fix |
| Maintenance Testing | Testing changes to released software |

Quiz Yourself

Answer these 5 questions:

    What are the 4 SDLC models?  -  Waterfall, V-Model, Agile, DevOps

    What are the 4 test levels (smallest to largest)?  - Unit, Integration, System, Acceptance

    What's the difference between Black-box and White-box testing?  - Black-box: no knowledge of internals; White-box: know the code

    What's the difference between Confirmation and Regression testing?  - Confirmation: verify a specific bug fix; Regression: verify nothing else broke

    When does Maintenance testing happen?  - When changes are made to released software (bug fixes, new features, environment changes)

---

## Chapter 3 — Static Testing

### What is Static Testing?

Testing **without executing the code**.

| | Static | Dynamic |
|---|--------|---------|
| Runs code? | No | Yes |
| When | Before/during coding | After code written |
| Finds | Defects in docs, code, requirements | Defects in behavior |
| Examples | Reviews, static analysis | Unit tests, manual testing |

**I've done static testing** — using ruff, black, mypy.

### Why Static Testing Matters

- Find defects early (before code runs)
- Cheaper to fix
- Covers non-code artifacts (requirements, design)
- Finds different bugs than dynamic testing

### Types of Static Testing

1. **Reviews** — humans examine artifacts
2. **Static Analysis** — tools analyze code

### Reviews — 4 Types

| Type | Formality | Leader | Who |
|------|-----------|--------|-----|
| Informal Review | Low | Anyone | 1–2 people |
| Walkthrough | Medium | Author | Author + peers |
| Technical Review | Medium-High | Trained moderator | Peers + experts |
| Inspection | High | Trained moderator | Formal team |

**In practice:** Pull request reviews, peer code reviews.

### Review Process (5 Activities)

1. Planning — what, who, when
2. Initiation — distribute materials
3. Individual Preparation — reviewers study
4. Review Meeting — team discusses
5. Rework & Follow-up — fix and verify

Most reviews skip steps; formal inspections follow all 5.

### Roles in Reviews

| Role | Responsibility |
|------|----------------|
| Author | Created the artifact |
| Moderator | Runs the meeting |
| Reviewer | Finds defects |
| Scribe | Records findings |
| Manager | Decides what to review |

### Static Analysis (Tool-Based)

Tools analyze code without running it.

| Tool | Finds |
|------|-------|
| Ruff | Style, potential bugs |
| mypy | Type errors |
| Bandit | Security vulnerabilities |
| Black | Formatting |

**Tools I use:** Ruff, Black, mypy.

### What Static Analysis Finds

- Unused imports
- Undefined variables
- Type mismatches
- Security issues
- Complexity warnings

### What Static Analysis Can't Find

- Runtime errors
- Logic errors (code works but wrong)
- Performance issues
- UI issues

**Static complements dynamic — use both.**

### Static vs Dynamic Testing

| | Static | Dynamic |
|---|--------|---------|
| Finds | Code smells, style, potential bugs | Behavior, runtime errors |
| When | Before running | After running |
| Cost | Cheaper | More expensive |
| Tools | Linters, type checkers | Test frameworks |
| Covers | Code, docs, requirements | Executable software |

### Key Terms (Chapter 3)

| Term | Definition |
|------|------------|
| Static Testing | Testing without executing code |
| Review | Human examination of an artifact |
| Static Analysis | Tool-based code analysis |
| Walkthrough | Author-led review |
| Technical Review | Peer review with technical experts |
| Inspection | Formal, structured review |
| Linter | Tool that finds code issues |
| Type Checker | Tool that verifies types |


Quiz Myself 

Answer these 5 questions:

    What's the difference between static and dynamic testing?- Static: no code execution; Dynamic: runs the code

    Name 3 types of reviews. - Informal review, Walkthrough, Technical review, Inspection

    What's the difference between a walkthrough and an inspection?  - Walkthrough: author-led, informal; Inspection: formal, moderator-led

    Name 3 static analysis tools you've used.  - Ruff, Black, mypy (or Bandit, ESLint, etc.)

    What can static analysis NOT find?  - Runtime errors, logic errors, performance issues, UI issues

    ---

## Chapter 4 — Test Analysis and Design (MOST IMPORTANT — 30%)

### Why Test Design Techniques Matter

- Can't test everything
- Pick best test cases from infinite possibilities
- Find bugs efficiently
- Justify testing (systematic, not ad-hoc)

### The 5 Techniques

| # | Technique | When to use |
|---|-----------|-------------|
| 1 | Equivalence Partitioning | Any input domain |
| 2 | Boundary Value Analysis | Numeric ranges, dates |
| 3 | Decision Table Testing | Complex business rules |
| 4 | State Transition Testing | Workflows, state machines |
| 5 | Use Case Testing | User journeys |

### 1. Equivalence Partitioning (EP)

Divide inputs into partitions where all values behave the same.
Test **one value** from each partition.

**Example — Age (valid: 18–65):**

| Partition | Range | Test value |
|-----------|-------|------------|
| Invalid (low) | < 18 | 15 |
| Valid | 18–65 | 30 |
| Invalid (high) | > 65 | 70 |

3 test cases instead of infinite.

### 2. Boundary Value Analysis (BVA)

Test values at and just outside each boundary.

**Example — Age (valid: 18–65):**

Test values: 17, 18, 19, 64, 65, 66

| | EP | BVA |
|---|-----|-----|
| Tests | One per partition | At boundaries |
| Finds | Partition bugs | Edge-case bugs |

**Use both together.**

### 3. Decision Table Testing

When business rules have multiple conditions, use a table.

**Example — Loan approval:**

| Condition | R1 | R2 | R3 | R4 |
|-----------|----|----|----|----|
| Age ≥ 18 | Y | Y | N | N |
| Income ≥ €30k | Y | N | Y | N |
| Action: Approve | ✅ | ❌ | ❌ | ❌ |

4 rules → 4 test cases.

**Login with 3 conditions:** 8 rules → 8 test cases.

### 4. State Transition Testing

Systems have states. Test transitions between states.

**Example — ATM:**

States: Idle → Card Inserted → PIN Entered → Transaction → Eject Card → Idle

Test transitions:
- Idle → Insert card → Card Inserted
- Card Inserted → Enter PIN (wrong ×3) → Card Blocked
- PIN Entered → Complete → Eject Card

**Why it works:** Catches invalid transitions.

### 5. Use Case Testing

Test end-to-end user journeys, not individual features.

**Example — Buy a product:**

Main flow:
1. Search product
2. Add to cart
3. Enter shipping
4. Enter payment
5. Confirm order

Alternative flows:
- Product out of stock → error
- Invalid payment → error
- User cancels → cart preserved

Test cases = main flow + alternatives.

### Coverage

| Type | Measures |
|------|----------|
| Statement | % of code lines executed |
| Branch | % of if/else branches taken |
| Decision | % of decision outcomes tested |
| Path | % of code paths tested |

**I measure statement coverage in pytest** (60% in my project).

### Choosing the Right Technique

| Situation | Use |
|-----------|-----|
| Numeric input | EP + BVA |
| Complex business rules | Decision table |
| Workflows | State transition |
| User journeys | Use case |

**In practice:** Combine techniques.

### Key Terms (Chapter 4)

| Term | Definition |
|------|------------|
| Equivalence Partitioning | Divide inputs into groups with same behavior |
| Boundary Value Analysis | Test values at boundaries |
| Decision Table | Table of conditions and actions |
| State Transition | Diagram of states and transitions |
| Use Case | End-to-end user journey |
| Coverage | How much of the system tests exercise |
| Statement Coverage | % of code lines executed |
| Branch Coverage | % of if/else branches taken |

### Examples I've Written

**Example 1 — EP + BVA for my Python function `calculate_age(birth_year, current_year)`:**

| Partition | Range | Test value |
|-----------|-------|------------|
| birth_year > current_year | Invalid | (2030, 2026) |
| birth_year == current_year | Valid | (2026, 2026) |
| birth_year < current_year | Valid | (1990, 2026) |

BVA:
- birth_year = current_year - 1 (yesterday)
- birth_year = current_year (today)
- birth_year = current_year + 1 (tomorrow → error)

**Example 2 — Decision table for login:**

| Condition | R1 | R2 | R3 | R4 |
|-----------|----|----|----|----|
| Valid email | Y | Y | N | N |
| Valid password | Y | N | Y | N |
| Action: Login | ✅ | ❌ | ❌ | ❌ |

Quiz Myself

Answer these 5 questions:

    When do you use Equivalence Partitioning? - When testing input domains (any input with multiple partitions)

    What's the difference between EP and BVA?  - EP: test one value per partition; BVA: test values at boundaries

    When do you use Decision Table testing?  - When business rules have multiple conditions

    What does a state transition diagram show?  - States and transitions between them

    What's the difference between statement coverage and branch coverage? - Statement: % of code lines executed; Branch: % of if/else branches taken
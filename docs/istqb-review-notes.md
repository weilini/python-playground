# ISTQB Review Notes

Review and practice notes for ISTQB CTFL exam preparation.

---

## Week 2 — Day 1: Chapters 1–2 Review

### Chapter 1 — Quick Recall

**The 7 Testing Principles:**
1. Testing shows presence, not absence of defects
2. Exhaustive testing is impossible
3. Early testing saves time and money
4. Defect clustering
5. Pesticide paradox
6. Testing is context-dependent
7. Absence-of-errors fallacy

**QA vs QC vs Testing:**
- QA = process (prevent defects)
- QC = product (detect defects)
- Testing = activity

**Testing vs Debugging:**
- Testing = finds defects (QA does this)
- Debugging = fixes defects (developers do this)

**7 Testing Activities:**
1. Test Planning
2. Test Monitoring & Control
3. Test Analysis
4. Test Design
5. Test Implementation
6. Test Execution
7. Test Completion

**Key terms:**
- Error = human mistake
- Defect = flaw in code
- Failure = software deviates from expected
- Root Cause = underlying reason

---

### Chapter 2 — Quick Recall

**SDLC Models:**
| Model | Testing |
|-------|---------|
| Waterfall | After development |
| V-Model | Alongside development |
| Agile | In every sprint |
| DevOps | Continuous |

**4 Test Levels:**
1. Unit (component)
2. Integration
3. System
4. Acceptance

**Test Types:**
- Functional vs Non-functional
- Black-box vs White-box vs Gray-box

**Confirmation vs Regression:**
- Confirmation = verify specific bug fix
- Regression = verify nothing else broke

**Maintenance Testing:**
- Happens after release (bug fixes, new features, environment changes)

---

## Practice Questions — Chapters 1–2

### Q1: Which testing principle states that testing can show defects exist but not that they don't?  B

A. Defect clustering
B. Testing shows presence, not absence of defects
C. Pesticide paradox
D. Absence-of-errors fallacy

**Answer:** B

---

### Q2: What is the difference between QA and QC? B

A. QA is product-focused, QC is process-focused
B. QA is process-focused, QC is product-focused
C. They are the same thing
D. QA is for developers, QC is for testers

**Answer:** B

---

### Q3: In which SDLC model is testing planned alongside development?  B

A. Waterfall
B. V-Model
C. Agile
D. DevOps

**Answer:** B

---

### Q4: Which test level tests the whole system end-to-end?  C

A. Unit testing
B. Integration testing
C. System testing
D. Acceptance testing

**Answer:** C

---

### Q5: What is the difference between confirmation and regression testing?  B

A. They are the same
B. Confirmation = verify fix; Regression = verify nothing else broke
C. Confirmation = verify nothing else broke; Regression = verify fix
D. Confirmation is manual; Regression is automated

**Answer:** B

---

### Q6: Which activity identifies WHAT to test? B

A. Test Design
B. Test Analysis
C. Test Implementation
D. Test Execution

**Answer:** B

---
  
### Q7: What is a defect?  B

A. A human mistake
B. A flaw in a component or system
C. Software deviating from expected behavior
D. The underlying reason for a problem

**Answer:** B

---

### Q8: Which testing type has NO knowledge of internal code? C

A. White-box testing
B. Gray-box testing
C. Black-box testing
D. Unit testing

**Answer:** C

---

## My Score: 8/8

## Weak Areas Identified:
- [ ] List any topics I got wrong

## Questions to Review:
- [ ] Note topics I need to re-read

---

## Week 2 — Day 2: Chapters 3–4 Review

### Chapter 3 — Quick Recall

**Static vs Dynamic Testing:**
- Static: no code execution (reviews, static analysis)
- Dynamic: code executes (unit tests, manual testing)

**4 Review Types:**
| Type | Formality | Leader |
|------|-----------|--------|
| Informal | Low | Anyone |
| Walkthrough | Medium | Author |
| Technical Review | Medium-High | Trained moderator |
| Inspection | High | Trained moderator |

**Review Process (5 activities):**
1. Planning
2. Initiation
3. Individual Preparation
4. Review Meeting
5. Rework & Follow-up

**Review Roles:**
- Author, Moderator, Reviewer, Scribe, Manager

**Static Analysis Tools:**
- Ruff (style, bugs)
- mypy (types)
- Bandit (security)

**What static analysis can find:**
- Unused imports
- Type mismatches
- Security issues
- Complexity warnings

**What it can't find:**
- Runtime errors
- Logic errors
- Performance issues
- UI issues

---

### Chapter 4 — Quick Recall

**The 5 Test Design Techniques:**

1. **Equivalence Partitioning (EP)** — divide inputs into partitions, test one value each
2. **Boundary Value Analysis (BVA)** — test values at boundaries
3. **Decision Table Testing** — test combinations of conditions
4. **State Transition Testing** — test state changes
5. **Use Case Testing** — test end-to-end user journeys

**EP + BVA Example — Age (valid: 18–65):**

| Partition | Range | Test value |
|-----------|-------|------------|
| Invalid low | < 18 | 15 |
| Valid | 18–65 | 30 |
| Invalid high | > 65 | 70 |

**BVA values:** 17, 18, 19, 64, 65, 66

**Coverage Types:**
- Statement: % of code lines executed
- Branch: % of if/else branches taken
- Decision: % of decision outcomes tested
- Path: % of code paths tested

---

## Practice Questions — Chapters 3–4

### Q1: Which testing technique divides inputs into groups with the same behavior? B

A. Boundary Value Analysis
B. Equivalence Partitioning
C. Decision Table Testing
D. State Transition Testing

**Answer:** B

---

### Q2: Which technique tests values at the edges of partitions?  B

A. Equivalence Partitioning
B. Boundary Value Analysis
C. Use Case Testing
D. Static Analysis

**Answer:** B

---

### Q3: When would you use Decision Table Testing?  B

A. Testing numeric inputs
B. Testing complex business rules with multiple conditions
C. Testing state changes
D. Testing user journeys

**Answer:** B

---

### Q4: Which review type is the most formal?  D

A. Informal Review
B. Walkthrough
C. Technical Review
D. Inspection

**Answer:** D

---

### Q5: What is the FIRST activity in the formal review process?  c

A. Preparation
B. Review Meeting
C. Planning
D. Rework

**Answer:** C

---

### Q6: Which technique would you use to test an ATM machine? c

A. Equivalence Partitioning
B. Decision Table Testing
C. State Transition Testing
D. Boundary Value Analysis

**Answer:** C

---

### Q7: What does statement coverage measure?  b

A. % of if/else branches taken
B. % of code lines executed
C. % of decision outcomes tested
D. % of code paths tested

**Answer:** B

---

### Q8: What can static analysis NOT find? c

A. Unused imports
B. Type mismatches
C. Runtime errors
D. Security issues

**Answer:** C

---

## My Score: _8/8

## Weak Areas Identified:
- [ ] List any topics I got wrong

## Questions to Review:
- [ ] Note topics I need to re-read

---

## Week 2 — Day 3: Chapters 5–6 Review

### Chapter 5 — Quick Recall

**Test Plan contents:**
- Scope, Objectives, Approach, Resources, Schedule, Risks, Entry/Exit criteria

**Risk-Based Testing:**
Risk = Probability × Impact

| Probability | Impact | Risk | Priority |
|-------------|--------|------|----------|
| High | High | Critical | Test first |
| High | Low | Medium | Test |
| Low | High | Medium | Test |
| Low | Low | Low | Skip or light |

**Monitoring vs Control:**
- Monitoring = track progress
- Control = adjust plan

**Defect Lifecycle:**
New → Assigned → In Progress → Fixed → Ready for Retest → Closed
                                            ↓
                                        Reopened

**Defect Report includes:**
- ID, Title
- Severity (technical impact)
- Priority (business urgency)
- Steps to reproduce
- Expected vs Actual
- Environment
- Attachments

**Test Estimation Techniques:**
1. Expert judgment
2. Ratio-based (e.g., 30% of dev time)
3. Work breakdown

**Roles:**
| Role | Responsibility |
|------|----------------|
| Test Manager | Owns plan, reports status |
| Test Lead | Leads team, designs tests |
| Tester | Executes, reports bugs |
| Developer | Fixes bugs, unit tests |
| Product Owner | Prioritizes features/bugs |

---

### Chapter 6 — Quick Recall

**Tool Categories (9):**
1. Test Management — Jira, TestRail
2. Defect Management — Jira, Bugzilla
3. Static Analysis — Ruff, mypy, SonarQube
4. Test Design — test generators
5. Test Execution — pytest, Selenium, Playwright
6. Coverage — pytest-cov, JaCoCo
7. Performance — JMeter, Locust, k6
8. CI/CD — GitHub Actions, Jenkins
9. Monitoring — Prometheus, Grafana

**Automation Benefits:**
- Speed (1000 tests in seconds)
- Repeatability
- Coverage
- Cost savings
- Regression testing
- CI/CD integration

**Automation Risks:**
- High initial cost
- Maintenance burden
- False confidence
- Wrong tests automated
- Tool complexity
- Not suitable for everything

**When NOT to automate:**
- Exploratory testing
- UX testing
- One-time tests
- Unstable features

**Testing Pyramid:**


**Tool Selection Criteria:**
Fit, cost, learning curve, integration, support, scalability, compatibility

---

## Practice Questions — Chapters 5–6

### Q1: What does Risk = Probability × Impact help with? b

A. Deciding which tests to automate
B. Prioritizing testing by risk
C. Estimating test effort
D. Monitoring test progress

**Answer:** B

---

### Q2: What is the difference between monitoring and control? b

A. They are the same
B. Monitoring tracks progress; Control adjusts the plan
C. Monitoring is for developers; Control is for testers
D. Monitoring is manual; Control is automated

**Answer:** B

---

### Q3: What is the FIRST state in the defect lifecycle? c

A. Assigned
B. In Progress
C. New
D. Fixed

**Answer:** C

---

### Q4: Which is NOT a benefit of test automation? c

A. Speed
B. Repeatability
C. Low initial cost
D. Regression testing

**Answer:** C

---

### Q5: According to the testing pyramid, which type of test should you have the MOST of? c

A. UI tests
B. Integration tests
C. Unit tests
D. Performance tests

**Answer:** C

---

### Q6: What is the difference between severity and priority? b

A. They are the same
B. Severity = technical impact; Priority = business urgency
C. Severity = business urgency; Priority = technical impact
D. Severity is for bugs; Priority is for features

**Answer:** B

---

### Q7: Which test estimation technique is based on development time?  b

A. Expert judgment
B. Ratio-based
C. Work breakdown
D. Risk-based

**Answer:** B

---

### Q8: Which tool would you use to test an API?  c

A. Selenium
B. Playwright
C. Postman
D. JMeter

**Answer:** C

---

## My Score: _8/8

## Weak Areas Identified:
- [ ] List any topics I got wrong

## Questions to Review:
- [ ] Note topics I need to re-read

---

## Week 4 — Chapters 3-4 Deep Review

### Chapter 3 — Static Testing

**4 Review Types:**
| Type | Formality | Leader |
|------|-----------|--------|
| Informal | Low | Anyone |
| Walkthrough | Medium | Author |
| Technical Review | Medium-High | Trained moderator |
| Inspection | High | Trained moderator |

**5 Activities:** Planning → Initiation → Preparation → Meeting → Rework

**5 Roles:** Author, Moderator, Reviewer, Scribe, Manager

**Static Analysis Tools:** Ruff, mypy, Bandit

**Can find:** unused imports, type mismatches, security issues
**Cannot find:** runtime errors, logic errors, performance issues

### Chapter 4 — Test Design

**EP:** Divide inputs; test one value per partition
**BVA:** Test values at boundaries
**Decision Table:** 2^n rules (n = conditions)
**State Transition:** Test state changes
**Use Case:** Test end-to-end user journeys

**Coverage:** Statement, Branch, Decision, Path

---

## Practice Questions — Chapters 3-4 (Deep Review)

### Q1: Who leads a walkthrough?

A. Trained moderator
B. Author
C. Scribe
D. Manager

**Answer:** B

---

### Q2: Which review type is the most formal?

A. Informal Review
B. Walkthrough
C. Technical Review
D. Inspection

**Answer:** D

---

### Q3: What is the FIRST activity in the review process?

A. Preparation
B. Review Meeting
C. Planning
D. Rework

**Answer:** C

---

### Q4: What is the role of a scribe?

A. Creates the artifact
B. Runs the review meeting
C. Records findings
D. Provides resources

**Answer:** C

---

### Q5: What can static analysis NOT find?

A. Unused imports
B. Type mismatches
C. Runtime errors
D. Security issues

**Answer:** C

---

### Q6: For age (valid 18-65), which are BVA values?

A. 30
B. 18 only
C. 17, 18, 19, 64, 65, 66
D. 0, 50, 100

**Answer:** C

---

### Q7: How many rules in a decision table with 4 conditions?

A. 4
B. 8
C. 12
D. 16

**Answer:** D (2^4 = 16)

---

### Q8: Which technique for an ATM machine?

A. Equivalence Partitioning
B. Decision Table
C. State Transition
D. Use Case

**Answer:** C

---

### Q9: What does branch coverage measure?

A. % of code lines executed
B. % of if/else branches taken
C. % of decision outcomes tested
D. % of code paths tested

**Answer:** B

---

### Q10: What is the key difference between EP and BVA?

A. EP tests boundaries; BVA tests partitions
B. EP tests one value per partition; BVA tests at boundaries
C. They are the same
D. EP is manual; BVA is automated

**Answer:** B

---

## My Score: __/10

## Weak Areas Identified:
- [ ] [任何做错的题]

## Questions to Review:
- [ ] [需要重读的章节]
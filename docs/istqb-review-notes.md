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
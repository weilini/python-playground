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
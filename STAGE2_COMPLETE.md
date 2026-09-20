# Stage 2 Complete — Python Fundamentals

**Date:** 2026-09-16
**Duration:** 10 days
**Status:** ✅ Complete

---

## What I Learned

### Day 1 — Variables, Types, and Functions
- Variables, data types (str, int, float, bool)
- Type hints, f-strings
- Basic arithmetic operators
- Defensive programming with raise ValueError

### Day 2 — Collections
- Lists, dictionaries, sets, tuples
- List comprehensions
- Set operations
- Dictionary methods

### Day 3 — Functions in Depth
- Default and keyword arguments
- *args and **kwargs
- Higher-order functions

### Day 4 — Files, JSON, and Error Handling
- Reading and writing text files
- with open() context manager
- JSON serialization
- try/except error handling

### Day 5 — Object-Oriented Programming Basics
- Classes and objects
- __init__ constructor
- The self keyword
- Instance attributes and methods

### Day 6 — Advanced OOP
- Inheritance and super()
- Method overriding
- Polymorphism
- __str__ and __repr__

### Day 7 — Modules and Packages
- Modules and packages
- Absolute vs relative imports
- python -m module.name
- The if __name__ == pattern

### Day 8 — Decorators
- Functions as first-class objects
- Writing decorators
- @decorator syntax
- functools.wraps

### Day 9 — Comprehensive Mini-Project: CLI To-Do App
- Built a complete command-line application
- Package structure: src/todo/
- @dataclass for clean data classes
- JSON persistence to ~/.todo.json
- Full test coverage for logic

### Day 10 — Review and Consolidation
- Ran full test suite (117 tests)
- Analyzed coverage report (60%)
- Wrote this milestone document
- Tagged release v0.2.0

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Days completed | 10 |
| Python functions written | 40+ |
| Classes written | 5 |
| Decorators written | 3 |
| Test files | 12 |
| Tests passing | 117 |
| Test coverage | 60% |
| Git commits | 15 |
| GitHub repositories | 1 (public) |

---

## Key Debugging Lessons

1. Standard library name conflicts — never name files after stdlib modules
2. python -m vs python file.py — use -m for modules that import from other modules
3. try/except variable scoping — both branches must assign the same variable
4. Regex matching in pytest.raises — use (?i) for case-insensitive
5. git add . — stage everything
6. VS Code nested folder bug — type ONLY the filename in New File
7. Indentation is structural, not cosmetic
8. Test structure matters — every def test needs a body

---

## Deliverables

- github.com/weilini/python-playground — 15+ commits
- CLI To-Do application — python -m src.todo
- 117 passing tests
- 60% code coverage
- Professional project structure

---

## Next Steps

**Stage 2.5 — QA Foundations (3 weeks)**
- Testing theory
- ISTQB CTFL concepts
- Manual testing practice
- API testing with Postman

**Then Stage 3 — Testing & Tooling**
- Advanced pytest
- CI/CD with GitHub Actions
- Pre-commit hooks

---

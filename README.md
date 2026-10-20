# Teach Me This — beginner-first coding courses

Plain-language, beginner-first course material for people learning to code for AI.
Every lesson is written so a total beginner can read it out loud and understand it.

## Courses

| Course | Status | Start here |
|--------|--------|------------|
| AI Engineering — 6 weeks | In progress | [courses/ai-engineering/](courses/ai-engineering/README.md) |

More courses get added as their own folder under `courses/`.

## How the teaching works

Each lesson is a small, runnable file with comments on nearly every line. The order matters:

1. You are told **what** you are about to build and **why** it matters.
2. You type the code yourself — copy-paste is disallowed by design.
3. You break it on purpose and read the error.
4. Each day closes with one question to answer and one small change to make yourself.

Code rules the lessons follow:
- Under 10 lines whenever possible.
- Descriptive variable names (`height_metres`, not `h`).
- Never a solution without an explanation of why it works.
- Errors are treated as the lesson, not as failure.

## Add a new course

```
courses/<course-name>/
  README.md      <- roadmap table, one row per week
  week1_*/PLAN.md
  week1_*/lessons/01_*.py
```

Write each lesson as if the reader has never opened a terminal.

## Requirements

- Python 3.10 or newer. Check with `python --version`.
- No API keys needed for the first week.

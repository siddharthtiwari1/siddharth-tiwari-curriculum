# Instructor Reference: Session 11.1 — Lab: Evaluate Your Document Assistant

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full lecture script will follow `templates/lecture-script-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 2: Generative AI for the Enterprise |
| Session | 11.1 (Week 11) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan); Google Sheets (free) |

## Topics

- Building a golden test set (an eval set): fixed questions with known right answers
- Three ways to grade answers: a person (human-graded), a second AI model acting as judge (model-graded), or a match against the expected answer (reference-based)
- Pass rate as a baseline
- Re-testing after every change, to catch answers that got worse (a regression)
- Writing up the result against cost, latency and data residency
- Hands-on: Build a 15-question golden test set, decide for each question whether a person, a second AI model or a match against the expected answer grades it, run it against your Dify assistant before and after a change, and write up the result

## Learning objectives

- Construct a fixed eval set of inputs and expected outputs for a stated LLM task
- Classify an evaluation as reference-based, model-graded or human-graded
- Compute the pass rate of an eval suite and record it as a quality baseline
- Explain why manual spot-checking cannot detect a regression in an LLM application

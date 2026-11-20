# Instructor Reference: Session 8.2 — Build a Document Assistant in Dify

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full lecture script will follow `templates/lecture-script-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 2: Generative AI for the Enterprise |
| Session | 8.2 (Week 8) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan); Google AI Studio (free model key) |

## Topics

- Planning the assistant: documents, questions, freshness (how often the documents change)
- Setting up Dify (a free visual tool for building AI assistants without code): a model key is a private password, then loading your documents into a knowledge base
- Building the assistant
- Choosing how many document passages it checks per question
- Showing the source behind each answer
- Hands-on: Plan and build a document assistant in Dify over five of your own non-confidential documents, test that each answer shows its source, try two passage-count settings and record how many passages each returns, then ask the same question with the knowledge base switched off and compare the two answers

## Learning objectives

- Design a retrieval-augmented system for a stated corpus, question type and freshness requirement
- Build a no-code document assistant over uploaded documents and test that each answer shows its source passage
- Configure an application credential so a workflow node authenticates successfully
- Configure how many document matches a no-code assistant retrieves per question

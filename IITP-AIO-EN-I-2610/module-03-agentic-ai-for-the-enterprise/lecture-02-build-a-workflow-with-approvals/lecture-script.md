# Instructor Reference: Session 12.1 — Build a Workflow with Approvals

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full lecture script will follow `templates/lecture-script-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 12.1 (Week 12) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan) |

## Topics

- A workflow is a trigger (the event that starts it) plus steps
- Conditional branching: a router step, or node, that sends each case down one path or another
- Error handling and retries
- A human approval step before an irreversible action
- Which actions need approval: reversibility
- Reading a failed run
- Hands-on: Build a small workflow in Dify that starts from a form, either a refund request or a college admissions office approving an offer letter, with a branch, a retry and a human approval step, then break it on purpose and read the failed run

## Learning objectives

- Describe a trigger-action workflow as an event source followed by a sequence of steps
- Implement conditional branching in a workflow using a filter or router node
- Configure error handling and retries on a node calling an unreliable service
- Configure a human approval step that pauses a workflow before an irreversible action
- Justify a human approval gate for a stated action by its reversibility
- Debug a failed workflow run using its execution log

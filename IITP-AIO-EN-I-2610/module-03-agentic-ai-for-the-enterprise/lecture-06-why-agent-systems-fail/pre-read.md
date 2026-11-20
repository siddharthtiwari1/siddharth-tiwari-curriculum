# Why Agent Systems Fail

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full pre-read will follow `templates/pre-read-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 14.1 (Week 14) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan) |

## Topics

- Reading a run history: repeated tool-call loops
- The wrong tool chosen
- Lost context: earlier steps dropping out of what the agent reads
- Agents talking in circles
- Hands-on: Read the supplied run histories of a faulty agent team and diagnose its four failures, then import the supplied faulty agent into Dify, fix one failure and re-run three test requests to check the fix

## Learning objectives

- Debug an agent that repeatedly calls the same tool without progressing
- Diagnose a run in which the agent selected the wrong tool for the task
- Diagnose an agent failure caused by earlier steps dropping out of context
- Diagnose a multi-agent run where two agents exchange messages without progressing

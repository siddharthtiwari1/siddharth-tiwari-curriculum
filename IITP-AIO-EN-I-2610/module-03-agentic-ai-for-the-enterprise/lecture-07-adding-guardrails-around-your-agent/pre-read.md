# Adding Guardrails Around Your Agent

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full pre-read will follow `templates/pre-read-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 14.2 (Week 14) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan) |

## Topics

- Where guardrails sit in the request path (the route from a user's question to the answer)
- Input guardrail: a sorting step (a question classifier in Dify) that blocks requests
- Output guardrail: a check on the answer before it is shown
- Refusal messages that say what the agent can still help with
- Testing your guardrails with attacking prompts
- Hands-on: In Dify, add a question classifier that sends off-topic and injected requests to a refusal message and an answer check that swaps in a safe fallback, then test both with five attacking prompts (messages written to trick the agent)

## Learning objectives

- Explain where input and output guardrails sit in the request path
- Configure a no-code guardrail that blocks an off-topic or injected request before the agent acts on it
- Configure a no-code output guardrail that replaces an unsafe answer with a safe fallback message
- Test an LLM application against a set of adversarial prompts

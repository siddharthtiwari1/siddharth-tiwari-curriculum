# Instructor Reference: Session 17.2 — Lab: Control and Test Your Agent

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full lecture script will follow `templates/lecture-script-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 17.2 (Week 17) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan); Google Sheets (free) |

## Topics

- Scenario testing, including a case with no suitable tool
- Plan versus available tools: does the agent's plan only use tools it really has
- Attacking prompts against your guardrails
- Closing a guardrail gap
- Hands-on: Write six test scenarios for your Dify agent, including one with no suitable tool and two attacking prompts, run them and close one guardrail gap using your autonomy matrix (with the supplied severity and reversibility rule) and vendor checklist

## Learning objectives

- Test an agent against scenarios including one with no suitable tool available
- Evaluate an agent's plan against the tools actually available to it
- Test an LLM application against a set of adversarial prompts
- Classify each step of a workflow as AI-alone, AI-with-approval or human-only by severity and reversibility
- Configure a no-code guardrail that blocks an off-topic or injected request before the agent acts on it

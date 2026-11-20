# Build Your First Agent with Tools

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full pre-read will follow `templates/pre-read-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 12.2 (Week 12) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan, CurrentTime tool and the DuckDuckGo search tool (no key needed)) |

## Topics

- Workflow or agent: who decides the next step
- Tool use and function calling: the model asks for a tool, the tool's result comes back
- The agent loop: think, act, observe, repeat (called ReAct)
- Why a loop needs a stopping rule
- Limits on iterations (rounds of the loop) and tool calls
- Hands-on: Build an agent in Dify with a stated goal and two tools, the built-in time tool and a search tool, set an iteration limit, run a three-step competitor-research task and read every loop step

## Learning objectives

- Compare a fixed chain with an agent loop by who decides the next step
- Trace a single tool-calling round trip from model request to returned result
- Trace a ReAct loop through its thought, action and observation steps
- Explain why an agent loop needs an explicit stopping condition
- Configure a stopping rule limiting an agent's iterations and total tool calls
- Build a no-code agent with a stated goal and two tools

# Approving What an Agent May Touch

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full pre-read will follow `templates/pre-read-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 3: Agentic AI for the Enterprise |
| Session | 13.1 (Week 13) |
| Duration | 120 min |
| Tools | Dify Sandbox (Free plan); Google Sheets (free) |

## Topics

- MCP (Model Context Protocol, a protocol being an agreed set of rules for connecting): one standard way to plug tools into agents
- Connecting an agent (the MCP client) to an MCP server, a tool supplier that speaks MCP
- Calling a connected tool and reading its result
- Tool servers you do not control
- Limiting which tools an agent may call, and setting its role
- Which company systems an agent may touch
- Hands-on: Connect your Dify agent to a supplied MCP server (paste the address the instructor gives you), call one tool, restrict the agent to that tool, then fill a system-access approval sheet for three company systems

## Learning objectives

- Describe what MCP provides that a bespoke API integration does not
- Configure an MCP client to connect to a running server
- Call a tool exposed by a connected MCP server and inspect its result
- Explain the risk of connecting a client to an untrusted MCP server
- Configure the role and permitted tools of a no-code agent
- Justify the permissions granted to an MCP server by its tools' side effects

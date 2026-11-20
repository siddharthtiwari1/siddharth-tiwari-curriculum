# Instructor Reference: Session 6.2 — How LLMs Work and Go Wrong

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full lecture script will follow `templates/lecture-script-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 2: Generative AI for the Enterprise |
| Session | 6.2 (Week 6) |
| Duration | 120 min |
| Tools | ChatGPT (Free plan); Claude (Free plan); OpenAI Tokenizer (free, in the browser) |

## Topics

- How an LLM produces an answer, one next word (token) at a time
- Tokens (word pieces), the context window (how much it reads) and temperature (how much answers vary)
- Why fluent text can still be wrong: hallucination
- Spotting invented names (hallucinated entities) and citations
- Which outputs need a human reviewer: how serious, how reversible
- Hands-on: Count the tokens in a supplied document on a free tokenizer page (a site that splits text into tokens) and compare with a model's context window, then ask a chatbot for sources on a niche topic and check each citation. If time allows, check one AI summary of supplied meeting notes line by line against the notes

## Learning objectives

- Describe next-token prediction as the mechanism that produces an LLM response
- Describe how a tokenizer splits text into subword tokens
- Explain what a context window limits and what counts against it
- Predict how raising temperature changes the variability of an output
- Explain why a model can produce fluent text that is factually wrong
- Analyze a generated answer to identify hallucinated entities and citations
- Evaluate which automated decisions need a human reviewer, justifying by severity and reversibility

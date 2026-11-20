# Making AI Answer from Your Documents

> **Status: not yet written.** This is the session brief from the curriculum CSV. The full pre-read will follow `templates/pre-read-template.md`.

| | |
|---|---|
| Batch | IITP-AIO-EN-I-2610 |
| Module | Module 2: Generative AI for the Enterprise |
| Session | 8.1 (Week 8) |
| Duration | 120 min |
| Tools | NotebookLM (free); ChatGPT (Free plan) |

## Topics

- Why RAG (retrieval-augmented generation: the AI looks up your documents before it answers)
- The steps of RAG: load the documents, search them, answer from what was found (a grounded answer)
- RAG compared with pasting every document (the whole corpus) into a long context window
- Where RAG fails
- Hands-on: Ask a chatbot a question about a supplied policy without the document, then ask NotebookLM with the document loaded, and compare the answers and citations

## Learning objectives

- Explain why a language model needs retrieval to answer from private or recent documents
- Describe the steps a grounded AI assistant takes: load documents, search them, then answer using what it found
- Compare retrieval with pasting a whole corpus into a long context window
- Identify the failure modes of a retrieval-augmented system

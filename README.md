# Siddharth Tiwari — pre-reads and lecture scripts

Course content for the batches I author as SME. Each batch is a top-level folder (batch id from the INI sheet).

## Repository layout

```
siddharth-tiwari-curriculum/
├── README.md
├── templates/
│   ├── pre-read-template.md
│   └── lecture-script-template.md
├── <batch-id>/
│   ├── module-01-<topic>/
│   │   ├── lecture-01-<topic>/
│   │   │   ├── pre-read.md
│   │   │   ├── lecture-script.md
│   │   │   └── data/          # optional; files the session hands to learners
│   │   └── ...
│   └── ...
└── ...
```

Naming: lowercase and hyphens only, numbered modules and lectures, and the same two file names in every lecture folder (`pre-read.md`, `lecture-script.md`). Optional assets for a session (`data/`, `images/`) live inside that session's lecture folder.

**Templates** under `templates/` are reference skeletons only. Session files in batch folders are the source of truth.

## Batches in this repo

| Batch id |
|---|
| `IITP-AIO-EN-I-2610` |

<!-- course-map:start -->

## Full course map — IITP-AIO-EN-I-2610

Every numbered teaching session from the curriculum CSV (v7). Masterclasses, revision, evaluation and capstone sessions are not SME-authored and are not listed.

| Module | Sessions | Written |
|:--|:-:|:-:|
| Module 1: AI Fundamentals and Driving Adoption | 11 | 11 / 11 |
| Module 2: Generative AI for the Enterprise | 10 | 0 / 10 |
| Module 3: Agentic AI for the Enterprise | 13 | 0 / 13 |
| Module 4: AI in Marketing and Finance | 10 | 0 / 10 |
| Module 5: AI in Operations, Customer Experience and People Functions | 6 | 0 / 6 |
| Module 6: Responsible AI, Governance and AI Business Models | 6 | 0 / 6 |

### Module 1: AI Fundamentals and Driving Adoption

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 1.1 | [What AI, ML and GenAI Are](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-01-what-ai-ml-and-genai-are/) | ChatGPT (Free plan); Claude (Free plan); Gemini (Free plan) | Written |
| 02 | 1.2 | [How Machines Learn from Examples](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-02-how-machines-learn-from-examples/) | Teachable Machine (free, in the browser) | Written |
| 03 | 2.1 | [Supervised Learning: Predicting from Examples](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-03-supervised-learning-predicting-from-examples/) | ChatGPT (Free plan, file upload and data analysis); Google Sheets (free) | Written |
| 04 | 2.2 | [Unsupervised Learning: Finding Groups](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-04-unsupervised-learning-finding-groups/) | ChatGPT (Free plan, file upload) | Written |
| 05 | 3.1 | [Machine Learning Behind Everyday Business Decisions](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-05-machine-learning-behind-everyday-business-decisions/) | Gemini (Free plan, with Google Search); Google Sheets (free) | Written |
| 06 | 3.2 | [Deep Learning and Neural Networks](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-06-deep-learning-and-neural-networks/) | TensorFlow Playground (free, in the browser) | Written |
| 07 | 4.1 | [Transformers and Today's LLMs](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-07-transformers-and-todays-llms/) | ChatGPT (Free plan); Gemini (Free plan) | Written |
| 08 | 4.2 | [Why AI Took Off](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-08-why-ai-took-off/) | Google Sheets (free) | Written |
| 09 | 5.1 | [Assessing Your Organisation's AI Maturity](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-09-assessing-your-organisations-ai-maturity/) | Google Sheets (free) | Written |
| 10 | 5.2 | [Building the Business Case for AI](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-10-building-the-business-case-for-ai/) | Google Sheets (free); ChatGPT (Free plan) | Written |
| 11 | 6.1 | [Lab: Write Your Organisation's AI Snapshot](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-11-lab-write-your-organisations-ai-snapshot/) | Google Sheets (free); Google Docs (free) | Written |

### Module 2: Generative AI for the Enterprise

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 6.2 | [How LLMs Work and Go Wrong](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-01-how-llms-work-and-go-wrong/) | ChatGPT (Free plan); Claude (Free plan); OpenAI Tokenizer (free, in the browser) | Brief only |
| 02 | 7.1 | [Writing Prompts That Get Reliable Answers](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-02-writing-prompts-that-get-reliable-answers/) | ChatGPT (Free plan); Claude (Free plan) | Brief only |
| 03 | 7.2 | [Image, Audio and Video AI](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-03-image-audio-and-video-ai/) | Gemini (Free plan, a few image generations a day); ElevenLabs (Free plan, non-commercial use); instructor demo of a video model such as Veo or Sora | Brief only |
| 04 | 8.1 | [Making AI Answer from Your Documents](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-04-making-ai-answer-from-your-documents/) | NotebookLM (free); ChatGPT (Free plan) | Brief only |
| 05 | 8.2 | [Build a Document Assistant in Dify](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-05-build-a-document-assistant-in-dify/) | Dify Sandbox (Free plan); Google AI Studio (free model key) | Brief only |
| 06 | 9.1 | [Choosing How to Customise an AI](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-06-choosing-how-to-customise-an-ai/) | Google Sheets (free) | Brief only |
| 07 | 9.2 | [Open Models and Private AI](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-07-open-models-and-private-ai/) | Google AI Studio (free, Gemma open model); ChatGPT (Free plan); instructor demo of an open model in LM Studio (free); LMArena (free, in the browser); Artificial Analysis (free, in the browser) | Brief only |
| 08 | 10.1 | [Choosing a GenAI Platform and Vendor](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-08-choosing-a-genai-platform-and-vendor/) | Google Sheets (free); Google Docs (free); supplied price table (from the OpenAI, Anthropic and Google price pages) | Brief only |
| 09 | 10.2 | [Safe, Honest AI Use at Work](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-09-safe-honest-ai-use-at-work/) | ChatGPT (Free plan); Claude (Free plan); Google Docs (free) | Brief only |
| 10 | 11.1 | [Lab: Evaluate Your Document Assistant](IITP-AIO-EN-I-2610/module-02-generative-ai-for-the-enterprise/lecture-10-lab-evaluate-your-document-assistant/) | Dify Sandbox (Free plan); Google Sheets (free) | Brief only |

### Module 3: Agentic AI for the Enterprise

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 11.2 | [How AI Agents Think and Act](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-01-how-ai-agents-think-and-act/) | Dify Sandbox (Free plan); instructor demo of a ready-made agent product such as ChatGPT agent mode | Brief only |
| 02 | 12.1 | [Build a Workflow with Approvals](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-02-build-a-workflow-with-approvals/) | Dify Sandbox (Free plan) | Brief only |
| 03 | 12.2 | [Build Your First Agent with Tools](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-03-build-your-first-agent-with-tools/) | Dify Sandbox (Free plan, CurrentTime tool and the DuckDuckGo search tool (no key needed)) | Brief only |
| 04 | 13.1 | [Approving What an Agent May Touch](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-04-approving-what-an-agent-may-touch/) | Dify Sandbox (Free plan); Google Sheets (free) | Brief only |
| 05 | 13.2 | [Building a Team of Agents](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-05-building-a-team-of-agents/) | Dify Sandbox (Free plan); instructor walkthrough of the A2A protocol | Brief only |
| 06 | 14.1 | [Why Agent Systems Fail](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-06-why-agent-systems-fail/) | Dify Sandbox (Free plan) | Brief only |
| 07 | 14.2 | [Adding Guardrails Around Your Agent](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-07-adding-guardrails-around-your-agent/) | Dify Sandbox (Free plan) | Brief only |
| 08 | 15.1 | [Deciding What AI May Do Alone](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-08-deciding-what-ai-may-do-alone/) | Google Sheets (free) | Brief only |
| 09 | 15.2 | [Publish and Monitor Your AI Assistant](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-09-publish-and-monitor-your-ai-assistant/) | Dify Sandbox (Free plan); Google Sheets (free) | Brief only |
| 10 | 16.1 | [Vibe Coding a Front End](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-10-vibe-coding-a-front-end/) | Google AI Studio (Build mode, free to start); Lovable (Free plan, 5 build credits a day); Dify Sandbox (Free plan) | Brief only |
| 11 | 16.2 | [Choosing an Agentic AI Vendor](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-11-choosing-an-agentic-ai-vendor/) | Google Sheets (free) | Brief only |
| 12 | 17.1 | [Costing AI and Deciding on ROI](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-12-costing-ai-and-deciding-on-roi/) | Google Sheets (free) | Brief only |
| 13 | 17.2 | [Lab: Control and Test Your Agent](IITP-AIO-EN-I-2610/module-03-agentic-ai-for-the-enterprise/lecture-13-lab-control-and-test-your-agent/) | Dify Sandbox (Free plan); Google Sheets (free) | Brief only |

### Module 4: AI in Marketing and Finance

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 18.1 | [Using AI to Find Customer Segments](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-01-using-ai-to-find-customer-segments/) | ChatGPT (Free plan, file upload and data analysis) | Brief only |
| 02 | 18.2 | [Using AI to Plan Campaign Spend](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-02-using-ai-to-plan-campaign-spend/) | Google Sheets (free); ChatGPT (Free plan) | Brief only |
| 03 | 19.1 | [Using AI for Pricing and Recommendations](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-03-using-ai-for-pricing-and-recommendations/) | Google Sheets (free) | Brief only |
| 04 | 19.2 | [Leading Marketing with GenAI Content](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-04-leading-marketing-with-genai-content/) | Gemini (Free plan, a few image generations a day); ChatGPT (Free plan); ElevenLabs (Free plan, non-commercial use) | Brief only |
| 05 | 20.1 | [Using AI for Market Research](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-05-using-ai-for-market-research/) | NotebookLM (free); Gemini (Free plan, with Google Search) | Brief only |
| 06 | 20.2 | [Using AI in Financial Planning](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-06-using-ai-in-financial-planning/) | ChatGPT (Free plan); Google Sheets (free) | Brief only |
| 07 | 21.1 | [Controls for AI in Finance](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-07-controls-for-ai-in-finance/) | Google Sheets (free); Google Docs (free) | Brief only |
| 08 | 21.2 | [Using AI to Manage Risk](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-08-using-ai-to-manage-risk/) | ChatGPT (Free plan); Google Sheets (free) | Brief only |
| 09 | 22.1 | [Quantifying AI Impact and Comparing Vendors](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-09-quantifying-ai-impact-and-comparing-vendors/) | Google Sheets (free) | Brief only |
| 10 | 22.2 | [Lab: Defend Your AI Business Case](IITP-AIO-EN-I-2610/module-04-ai-in-marketing-and-finance/lecture-10-lab-defend-your-ai-business-case/) | Google Slides (free) | Brief only |

### Module 5: AI in Operations, Customer Experience and People Functions

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 23.1 | [AI in Operations and Supply Chain](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-01-ai-in-operations-and-supply-chain/) | ChatGPT (Free plan, file upload and data analysis); Google Sheets (free) | Brief only |
| 02 | 23.2 | [AI in Customer Support](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-02-ai-in-customer-support/) | Gemini (Free plan); Google Sheets (free) | Brief only |
| 03 | 24.1 | [AI for Multilingual and Voice Customers](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-03-ai-for-multilingual-and-voice-customers/) | Gemini (Free plan, Gems, voice input and Live) | Brief only |
| 04 | 24.2 | [AI in Hiring and HR](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-04-ai-in-hiring-and-hr/) | ChatGPT (Free plan, file upload) | Brief only |
| 05 | 25.1 | [AI for Contracts and Documents](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-05-ai-for-contracts-and-documents/) | Gemini (Free plan, image and file upload); ChatGPT (Free plan, file upload) | Brief only |
| 06 | 25.2 | [Lab: Decide Where AI Fits](IITP-AIO-EN-I-2610/module-05-ai-in-operations-customer-experience-and-people-functions/lecture-06-lab-decide-where-ai-fits/) | Google Slides (free) | Brief only |

### Module 6: Responsible AI, Governance and AI Business Models

| # | Session | Title | Tools used (from the curriculum CSV) | Status |
|:-:|:-:|:--|:--|:-:|
| 01 | 26.1 | [Spotting Bias in AI Systems](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-01-spotting-bias-in-ai-systems/) | ChatGPT (Free plan); Claude (Free plan); Google Sheets (free) | Brief only |
| 02 | 26.2 | [Fairness, Explaining and Owning AI Decisions](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-02-fairness-explaining-and-owning-ai-decisions/) | Google Sheets (free) | Brief only |
| 03 | 27.1 | [DPDP and EU AI Act Duties](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-03-dpdp-and-eu-ai-act-duties/) | Google Docs (free) | Brief only |
| 04 | 27.2 | [AI Governance in Practice](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-04-ai-governance-in-practice/) | Google Docs (free) | Brief only |
| 05 | 28.1 | [Lab: Review an AI System](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-05-lab-review-an-ai-system/) | Google Docs (free); Google Sheets (free) | Brief only |
| 06 | 28.2 | [AI Business Models and Where Next](IITP-AIO-EN-I-2610/module-06-responsible-ai-governance-and-ai-business-models/lecture-06-ai-business-models-and-where-next/) | Google Sheets (free); Gemini (Free plan, with Google Search) | Brief only |

<!-- course-map:end -->

## Curriculum CSV (local, not in this repo)

Folder names and lecture titles come from the batch's INI curriculum export. Columns used:

| Column | Use in content |
|---|---|
| Session Title | Folder name and verbatim lecture title |
| Topics | Pre-read "Topics you will meet"; the lecture topics |
| LO_Statement | Verbatim learning objectives in the lecture Agenda and Closing |
| Tools Used | Runtime and platform; the script must use the same tools |

## Data files

Files in a lecture's `data/` folder are invented practice data. `make_data.py` regenerates them (`python make_data.py`, needs Pillow for the shape images). Instructor-only answer keys (`*_ANSWERS.csv`) are not in this repo: `make_data.py` writes them next to the learner files, so keep them with the instructor.

## Authoring checklist (before push)

1. Every lecture folder has exactly `pre-read.md` and `lecture-script.md`.
2. Session title and LOs match the curriculum CSV word for word.
3. Plain language, no topics that have not been taught yet.
4. Every code output and number checked; charts saved under `images/` with a new filename when regenerated.

**Remote:** [github.com/siddharthtiwari1/siddharth-tiwari-curriculum](https://github.com/siddharthtiwari1/siddharth-tiwari-curriculum)

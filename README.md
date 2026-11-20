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

## IITP-AIO-EN-I-2610 — Module 1: AI Fundamentals and Driving Adoption

| # | Session | Title | Tools used (from the curriculum CSV) | Data |
|:-:|:-:|:--|:--|:-:|
| 01 | 1.1 | [What AI, ML and GenAI Are](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-01-what-ai-ml-and-genai-are/) | ChatGPT (Free plan); Claude (Free plan); Gemini (Free plan) |  |
| 02 | 1.2 | [How Machines Learn from Examples](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-02-how-machines-learn-from-examples/) | Teachable Machine (free, in the browser) | yes |
| 03 | 2.1 | [Supervised Learning: Predicting from Examples](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-03-supervised-learning-predicting-from-examples/) | ChatGPT (Free plan, file upload and data analysis); Google Sheets (free) | yes |
| 04 | 2.2 | [Unsupervised Learning: Finding Groups](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-04-unsupervised-learning-finding-groups/) | ChatGPT (Free plan, file upload) | yes |
| 05 | 3.1 | [Machine Learning Behind Everyday Business Decisions](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-05-machine-learning-behind-everyday-business-decisions/) | Gemini (Free plan, with Google Search); Google Sheets (free) |  |
| 06 | 3.2 | [Deep Learning and Neural Networks](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-06-deep-learning-and-neural-networks/) | TensorFlow Playground (free, in the browser) |  |
| 07 | 4.1 | [Transformers and Today's LLMs](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-07-transformers-and-todays-llms/) | ChatGPT (Free plan); Gemini (Free plan) |  |
| 08 | 4.2 | [Why AI Took Off](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-08-why-ai-took-off/) | Google Sheets (free) | yes |
| 09 | 5.1 | [Assessing Your Organisation's AI Maturity](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-09-assessing-your-organisations-ai-maturity/) | Google Sheets (free) |  |
| 10 | 5.2 | [Building the Business Case for AI](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-10-building-the-business-case-for-ai/) | Google Sheets (free); ChatGPT (Free plan) |  |
| 11 | 6.1 | [Lab: Write Your Organisation's AI Snapshot](IITP-AIO-EN-I-2610/module-01-ai-fundamentals-and-driving-adoption/lecture-11-lab-write-your-organisations-ai-snapshot/) | Google Sheets (free); Google Docs (free) |  |

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

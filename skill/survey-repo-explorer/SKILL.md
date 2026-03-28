---
name: "survey-repo-explorer"
description: "Extracts categorized paper links from survey README and builds a local knowledgebase workflow. Invoke when user wants systematic literature exploration from a survey repo."
---

# Survey Repo Explorer

## Purpose
This skill turns a survey repository README paper list into a structured local knowledgebase for scientific investigation, including parsing, export, downloading, reading optimization, and evidence tracking.

## When To Invoke
Invoke this skill when the user asks to:
- mine paper links from a survey README
- build category-based paper datasets locally
- batch download papers and organize PDFs by topic
- run objective literature tracking and reporting workflows
- summarize paper distribution with a simple CLI

## 0. Initialization
Before any extraction or file generation, ask the user:
1. Reading goal (scientific question or objective)
2. Preferred categories
3. Depth level (breadth scan vs deep reading)
4. Output preferences

Proceed only after capturing these preferences.

## 1. Primary Workflow
1. Parse README by category headings.
2. Extract metadata with emphasis on canonical paper links.
3. Build the local knowledgebase directory.
4. Export per-category metadata into CSV and TXT.
5. Generate scripts under `tools/` for extraction, downloading, optimization, and statistics.
6. Maintain `AGENTS.md` and `REPORT.md` for process and findings.

## Directory Contract
Use this structure:

```text
./survey2knowledgebase/
  categories/
    <category>/
      csv/
        papers.csv
      txt/
        papers.txt
      pdf/
        <year>-<short_name>.pdf
  tools/
    extract_from_readme.py
    download_pdfs.py
    pdf_optimize.py
    stats_cli.py
  AGENTS.md
  REPORT.md
```

## Execution Boundary
- Generate and save required files and scripts in the workspace.
- Provide runnable commands for the user to execute.
- Do not auto-run downloading scripts unless the user explicitly asks for execution.

## Data Export Rules
- One CSV and one TXT per category.
- Store files inside each category directory, separated by file type (`csv/`, `txt/`, `pdf/`).
- Required fields: `short_name`, `title`, `category`, `year`, `month`, `venue`, `paper_url`, `source_type`, `code_url`, `data_url`.
- `short_name` rule: `FirstAuthorLastName_FirstImportantTitleWord` (example: `Vaswani_Attention`).
- Preserve original links exactly.
- If multiple paper links exist, choose the strongest canonical paper link in this order: DOI > ACL > OpenReview > arXiv > Website.
- Use chunked parsing for long README files to avoid truncation and extraction errors.

## PDF Download Rules
- Download PDFs into `./survey2knowledgebase/categories/<category>/pdf/`.
- Keep deterministic filenames: `<year>-<short_name>.pdf`.
- Skip existing files unless `--force` is set.
- Use randomized rate limiting between requests (`time.sleep` in 2–5s range).
- Use retry and error handling for network failures and 403/404 responses.
- Save failures into `./survey2knowledgebase/tools/download_errors.log`.

## PDF Reading Optimization Tools
Generate utilities for:
- text extraction to markdown
- section split by headings
- chunking for long-context agent reading
- keyword indexing for quick retrieval
- prefer robust libraries such as PyMuPDF or pdfplumber when available in the environment

## Research Records
`AGENTS.md` must record:
- objective, scope, extraction source, steps taken, and toolchain decisions
- reproducibility details (commands, paths, parameters)

`REPORT.md` must record:
- key scientific findings from user dialogues and extracted papers
- objective statements with evidence
- each claim linked to paper title and local file path

## Citation Requirements
- Always cite paper title and local file link together.
- Keep tone objective, falsifiable, and evidence-based.
- Separate observation from hypothesis.

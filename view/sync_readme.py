#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatically sync papers from YAML data files to README.md.
Generate a complete paper list organized by categories.

Usage:
    python view/sync_readme.py
"""
import re
import sys
import os
from pathlib import Path
import yaml
from typing import List, Dict

# Set Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
README_PATH = ROOT / "README.md"

# shields.io badge URLs
ARXIV_BADGE = "https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white"
OPENREVIEW_BADGE = "https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white"
ACL_BADGE = "https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white"
DOI_BADGE = "https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white"
WEBSITE_BADGE = "https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white"
GITHUB_BADGE = "https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white"
HF_BADGE = "https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white"

# Category definitions
CATEGORIES = {
    "evaluation_datasets": {
        "title": "📊 Evaluation Datasets",
        "yaml": "papers_evaluation_datasets.yaml",
        "description": "Benchmarks for evaluating issue resolution systems"
    },
    "training_datasets": {
        "title": "🎯 Training Datasets",
        "yaml": "papers_training_datasets.yaml",
        "description": "Datasets for training issue resolution agents"
    },
    "single_agent": {
        "title": "🤖 Single-Agent Systems",
        "yaml": "papers_single_agent.yaml",
        "description": "Individual autonomous agents for issue resolution"
    },
    "multi_agent": {
        "title": "👥 Multi-Agent Systems",
        "yaml": "papers_multi_agent.yaml",
        "description": "Collaborative multi-agent frameworks"
    },
    "workflow": {
        "title": "🔄 Workflow-Based Methods",
        "yaml": "papers_workflow.yaml",
        "description": "Structured pipeline approaches"
    },
    "tool": {
        "title": "🛠️ Tool-Augmented Methods",
        "yaml": "papers_tool.yaml",
        "description": "Methods leveraging external tools"
    },
    "memory": {
        "title": "🧠 Memory-Enhanced Methods",
        "yaml": "papers_memory.yaml",
        "description": "Systems with memory mechanisms"
    },
    "sft": {
        "title": "📚 Supervised Fine-Tuning (SFT)",
        "yaml": "papers_sft.yaml",
        "description": "Models trained via supervised learning"
    },
    "rl": {
        "title": "🎮 Reinforcement Learning (RL)",
        "yaml": "papers_rl.yaml",
        "description": "Models trained via reinforcement learning"
    },
    "inference_scaling": {
        "title": "⚡ Inference-Time Scaling",
        "yaml": "papers_inference_scaling.yaml",
        "description": "Methods for scaling at inference time"
    },
    "data_collection": {
        "title": "📥 Data Collection Methods",
        "yaml": "papers_data_collection.yaml",
        "description": "Techniques for collecting training data"
    },
    "data_synthesis": {
        "title": "🔬 Data Synthesis Methods",
        "yaml": "papers_data_synthesis.yaml",
        "description": "Approaches for synthetic data generation"
    },
    "data_analysis": {
        "title": "📈 Data Analysis",
        "yaml": "papers_data_analysis.yaml",
        "description": "Analysis of datasets and benchmarks"
    },
    "methods_analysis": {
        "title": "🔍 Methods Analysis",
        "yaml": "papers_methods_analysis.yaml",
        "description": "Comparative analysis of different methods"
    }
}

# Regex to match comment blocks
PAPERS_BLOCK_RE = re.compile(
    r"<!-- START PAPERS -->(.*?)<!-- END PAPERS -->",
    re.DOTALL
)

TABLES_BLOCK_RE = re.compile(
    r"<!-- START TABLES -->(.*?)<!-- END TABLES -->",
    re.DOTALL
)

USAGE_BLOCK_RE = re.compile(
    r"<!-- START USAGE -->(.*?)<!-- END USAGE -->",
    re.DOTALL
)


def load_yaml(path: Path) -> List[Dict]:
    """Load YAML file and return list of entries."""
    if not path.exists():
        print(f"[WARN] {path} does not exist, skipping.", file=sys.stderr)
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        return data
    except Exception as ex:
        print(f"[ERR] Failed to load {path}: {ex}", file=sys.stderr)
        return []


def badge_arxiv(url: str) -> str:
    """Generate arXiv badge."""
    if not url:
        return ""
    return f'[![arXiv]({ARXIV_BADGE})]({url})'


def badge_openreview(url: str) -> str:
    """Generate OpenReview badge."""
    if not url:
        return ""
    return f'[![OpenReview]({OPENREVIEW_BADGE})]({url})'


def badge_acl(url: str) -> str:
    """Generate ACL Anthology badge."""
    if not url:
        return ""
    return f'[![ACL]({ACL_BADGE})]({url})'


def badge_doi(url: str) -> str:
    """Generate DOI badge."""
    if not url:
        return ""
    return f'[![DOI]({DOI_BADGE})]({url})'


def badge_website(url: str) -> str:
    """Generate Website badge."""
    if not url:
        return ""
    return f'[![Website]({WEBSITE_BADGE})]({url})'


def badge_github(url: str) -> str:
    """Generate GitHub badge."""
    if not url:
        return ""
    return f'[![GitHub]({GITHUB_BADGE})]({url})'


def badge_huggingface(url: str) -> str:
    """Generate HuggingFace badge."""
    if not url:
        return ""
    return f'[![HuggingFace]({HF_BADGE})]({url})'


def count_unique_papers() -> int:
    """Count unique papers across all categories."""
    unique_papers = set()
    
    for category_id, category_info in CATEGORIES.items():
        yaml_file = category_info["yaml"]
        yaml_path = DATA_DIR / yaml_file
        
        entries = load_yaml(yaml_path)
        if not entries:
            continue
        
        for entry in entries:
            # Use short_name as primary identifier
            # Fall back to title if no short_name
            short_name = entry.get('short_name', '').strip()
            title = entry.get('title', '').strip()
            if short_name:
                unique_papers.add(('short_name', short_name.lower()))
            elif title:
                unique_papers.add(('title', title.lower()))
    
    return len(unique_papers)


def render_paper_item(entry: Dict) -> str:
    """Render a single paper as a list item."""
    short_name = entry.get("short_name", "").strip()
    full_title = entry.get("title", "").strip()
    month = str(entry.get("month", "")).strip()
    links = entry.get("links", {}) or {}

    arxiv = links.get("arxiv", "")
    openreview = links.get("openreview", "")
    acl = links.get("acl", "")
    doi = links.get("doi", "")
    website = links.get("website", "")
    github = links.get("github", "")
    huggingface = links.get("huggingface", "")

    # Date prefix (YYYY-MM) shown at the front of the entry
    date_prefix = f"`({month})` " if month else ""

    # Build paper entry
    if short_name == full_title:
        item = f"- {date_prefix}**{short_name}**"
    else:
        item = f"- {date_prefix}**{short_name}**: {full_title}"
    
    # Add badges (in priority order)
    badges = []
    if arxiv:
        badges.append(badge_arxiv(arxiv))
    if openreview:
        badges.append(badge_openreview(openreview))
    if acl:
        badges.append(badge_acl(acl))
    if doi:
        badges.append(badge_doi(doi))
    if website:
        badges.append(badge_website(website))
    if github:
        badges.append(badge_github(github))
    if huggingface:
        badges.append(badge_huggingface(huggingface))
    
    if badges:
        item += " " + " ".join(badges)
    
    return item


def generate_papers_section() -> str:
    """Generate the complete paper list section."""
    # Start with empty line to separate from comment marker
    content = ["\n## 📚 Complete Paper List\n"]
    
    # Track unique works for accurate count
    unique_papers = set()
    
    for category_id, category_info in CATEGORIES.items():
        yaml_file = category_info["yaml"]
        yaml_path = DATA_DIR / yaml_file
        
        entries = load_yaml(yaml_path)
        if not entries:
            continue
        
        # Add category title and description
        content.append(f"\n### {category_info['title']}\n")
        content.append(f"*{category_info['description']}*\n")
        
        # Sort entries newest-first; entries without a month fall to the bottom
        entries = sorted(
            entries,
            key=lambda e: str(e.get('month') or ''),
            reverse=True
        )

        # Render paper list and track unique works
        for entry in entries:
            content.append(render_paper_item(entry))
            # Use short_name as primary identifier (represents different works/systems)
            # Fall back to title if no short_name
            short_name = entry.get('short_name', '').strip()
            title = entry.get('title', '').strip()
            if short_name:
                unique_papers.add(('short_name', short_name.lower()))
            elif title:
                unique_papers.add(('title', title.lower()))
        
        paper_count = len(entries)
        print(f"  ✓ {category_info['title']}: {paper_count} papers")
    
    # Add summary at the beginning with unique count
    total_unique = len(unique_papers)
    summary = f"\n> **Total: {total_unique} works** across {len(CATEGORIES)} categories\n"
    content.insert(1, summary)
    
    # Add empty line at the end to separate from comment marker
    return "\n".join(content) + "\n"


def generate_tables_section() -> str:
    """Generate the tables section from tables.md file."""
    tables_md = ROOT / "docs" / "tables.md"
    
    if not tables_md.exists():
        print("[WARN] tables.md not found, skipping tables section")
        return "\n\nNo tables available yet.\n"
    
    try:
        content_text = tables_md.read_text(encoding="utf-8")
        
        # Extract content after the first "---" separator
        # Skip the page title and intro text
        lines = content_text.split('\n')
        start_idx = 0
        for i, line in enumerate(lines):
            if line.strip() == '---' and i > 0:
                start_idx = i + 1
                break
        
        if start_idx > 0:
            # Get the tables content
            table_content = '\n'.join(lines[start_idx:])
            return f"\n## 📋 Statistical Tables\n\nComprehensive tables and statistics about issue resolution datasets, methods, and benchmarks.\n\n{table_content}\n"
        else:
            return "\n\nNo tables available yet.\n"
    
    except Exception as e:
        print(f"[WARN] Failed to read tables.md: {e}")
        return "\n\nNo tables available yet.\n"


def generate_usage_section() -> str:
    """Generate usage instructions section."""
    return """\n## 🚀 Quick Start

```bash
# First time: install dependencies
pip install flask flask-cors sqlalchemy pyyaml requests

# Full update + start admin server
# (refreshes news, re-renders README/docs, builds static site, then serves)
python start.py

# Or force re-import from YAML/CSV first
python start.py --init
```

Open **http://localhost:5000/admin** to manage papers, datasets, and methods.

| Command | Description |
|---------|-------------|
| `python start.py` | Full update (news + render + build) then start server |
| `python start.py --init` | Re-import from YAML/CSV, then full update + start |
| `python start.py --no-update` | Start server without running update steps |
| `python start.py --port 8080` | Use a custom port |
| `python start.py --news` | Refresh Recent Papers section only and exit |
| `python start.py --render` | Re-render README/docs from DB only and exit |
| `python start.py --build` | Build static site (mkdocs) only and exit |

---
"""


def update_readme() -> bool:
    """Update the paper list, tables, and usage instructions in README.md file."""
    if not README_PATH.exists():
        print(f"[ERROR] {README_PATH} does not exist!", file=sys.stderr)
        return False
    
    content = README_PATH.read_text(encoding="utf-8")
    
    # Check if papers markers exist
    if "<!-- START PAPERS -->" not in content:
        print("[ERROR] <!-- START PAPERS --> marker not found in README.md!", file=sys.stderr)
        print("Please add the following markers to README.md:")
        print("\n<!-- START PAPERS -->")
        print("<!-- END PAPERS -->")
        return False
    
    # Count unique papers
    unique_count = count_unique_papers()
    print(f"\n📊 Total unique works: {unique_count}")
    
    # Update paper count badge
    new_content = re.sub(
        r'(!\[Papers Count\]\(https://img\.shields\.io/badge/papers-)\d+(-green\?style=for-the-badge&logo=googlescholar&logoColor=white\))',
        rf'\g<1>{unique_count}\g<2>',
        content
    )
    
    # Update abstract text: "Based on a systematic review of **XXX papers"
    new_content = re.sub(
        r'(Based on a systematic review of \*\*)\d+( papers and online resources\*\*)',
        rf'\g<1>{unique_count}\g<2>',
        new_content
    )
    
    # Generate new papers section
    papers_section = generate_papers_section()
    
    # Replace papers content
    new_content = PAPERS_BLOCK_RE.sub(
        f"<!-- START PAPERS -->{papers_section}<!-- END PAPERS -->",
        new_content
    )
    
    # Update tables section if markers exist
    if "<!-- START TABLES -->" in new_content:
        print("\n📊 Updating tables section...")
        tables_section = generate_tables_section()
        new_content = TABLES_BLOCK_RE.sub(
            f"<!-- START TABLES -->{tables_section}<!-- END TABLES -->",
            new_content
        )
    
    # Update usage section if markers exist
    if "<!-- START USAGE -->" in new_content:
        print("\n📖 Updating usage section...")
        usage_section = generate_usage_section()
        new_content = USAGE_BLOCK_RE.sub(
            f"<!-- START USAGE -->{usage_section}<!-- END USAGE -->",
            new_content
        )
    
    # Write back to file
    if new_content != content:
        README_PATH.write_text(new_content, encoding="utf-8")
        print("\n✓ README.md updated successfully!")
        return True
    else:
        print("\nNo changes to README.md.")
        return True


def main():
    """Main function."""
    print("=" * 70)
    print("  Syncing YAML data to README.md")
    print("=" * 70)
    print()
    
    success = update_readme()
    
    print()
    print("=" * 70)
    if success:
        print("  Sync completed successfully!")
    else:
        print("  Sync failed. Please check error messages.")
    print("=" * 70)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())


#!/usr/bin/env python3
"""
Auto-render paper lists from YAML data files to Markdown documents.
Uses shields.io style image badges.

Usage:
    python view/render_papers.py
"""
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"

# Category list for counting unique papers
CATEGORIES = [
    "evaluation_datasets", "training_datasets", "single_agent", "multi_agent",
    "workflow", "tool", "memory", "sft", "rl", "inference_scaling",
    "data_collection", "data_synthesis", "data_analysis", "methods_analysis"
]

# shields.io badge URLs (different platforms use different colors and icons)
ARXIV_BADGE = "https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white"
OPENREVIEW_BADGE = "https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white"
ACL_BADGE = "https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white"
DOI_BADGE = "https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white"
WEBSITE_BADGE = "https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white"
GITHUB_BADGE = "https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white"
HF_BADGE = "https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white"

# Regex pattern: <!-- START PAPERS:xxx --> ... <!-- END PAPERS:xxx -->
BLOCK_RE = re.compile(
    r"<!-- START PAPERS:(\w+) -->(.*?)<!-- END PAPERS:\1 -->",
    re.DOTALL
)


def badge_arxiv(url: str) -> str:
    """Generate arXiv badge."""
    if not url:
        return ""
    return f'[![arXiv]({ARXIV_BADGE})]({url}){{: target="_blank" }}'


def badge_openreview(url: str) -> str:
    """Generate OpenReview badge."""
    if not url:
        return ""
    return f'[![OpenReview]({OPENREVIEW_BADGE})]({url}){{: target="_blank" }}'


def badge_acl(url: str) -> str:
    """Generate ACL Anthology badge."""
    if not url:
        return ""
    return f'[![ACL]({ACL_BADGE})]({url}){{: target="_blank" }}'


def badge_doi(url: str) -> str:
    """Generate DOI badge."""
    if not url:
        return ""
    return f'[![DOI]({DOI_BADGE})]({url}){{: target="_blank" }}'


def badge_website(url: str) -> str:
    """Generate Website badge."""
    if not url:
        return ""
    return f'[![Website]({WEBSITE_BADGE})]({url}){{: target="_blank" }}'


def badge_github(url: str) -> str:
    """Generate GitHub badge."""
    if not url:
        return ""
    return f'[![GitHub]({GITHUB_BADGE})]({url}){{: target="_blank" }}'


def badge_huggingface(url: str) -> str:
    """Generate HuggingFace badge."""
    if not url:
        return ""
    return f'[![HuggingFace]({HF_BADGE})]({url}){{: target="_blank" }}'


def load_yaml(path: Path) -> list:
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


def count_unique_papers() -> int:
    """Count unique papers across all categories."""
    unique_papers = set()
    
    for category_id in CATEGORIES:
        yaml_file = f"papers_{category_id}.yaml"
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


def render_paper_item(entry: dict) -> str:
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

    # If short name equals full title, show only once
    if short_name == full_title:
        item = f"* {date_prefix}**{short_name}**"
    else:
        item = f"* {date_prefix}**{short_name}**: {full_title}"
    
    # Add badges (priority: arXiv > OpenReview > ACL > DOI > Website > GitHub > HuggingFace)
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


def render_section(section_id: str) -> str:
    """Render all papers from YAML file as Markdown list."""
    yaml_file = f"papers_{section_id}.yaml"
    path = DATA_DIR / yaml_file
    entries = load_yaml(path)
    
    if not entries:
        return f"\n<!-- No papers found in {yaml_file} -->\n"

    # Sort newest-first; entries without a month fall to the bottom
    entries = sorted(
        entries,
        key=lambda e: str(e.get('month') or ''),
        reverse=True
    )

    items = [render_paper_item(e) for e in entries]
    content = "\n".join(items)
    
    return f"\n{content}\n"


def update_markdown_file(filepath: Path, update_badge: bool = False) -> int:
    """Update paper lists in Markdown file. Returns number of blocks updated."""
    if not filepath.exists():
        print(f"[WARN] {filepath} does not exist, skipping.", file=sys.stderr)
        return 0
    
    original_content = filepath.read_text(encoding="utf-8")
    content = original_content
    
    # Update paper count badge and abstract if requested (for index.md)
    if update_badge:
        unique_count = count_unique_papers()
        print(f"  [INFO] Total unique works: {unique_count}")
        # Update the badge in the HTML img tag
        content = re.sub(
            r'(<img src="https://img\.shields\.io/badge/papers-)\d+(-green\?style=for-the-badge&logo=googlescholar&logoColor=white")',
            rf'\g<1>{unique_count}\g<2>',
            content
        )
        # Update abstract text: "Based on a systematic review of XXX papers"
        content = re.sub(
            r'(Based on a systematic review of )\d+( papers and online resources)',
            rf'\g<1>{unique_count}\g<2>',
            content
        )
    
    def replace_block(match):
        section_id = match.group(1)
        md = render_section(section_id)
        entries = load_yaml(DATA_DIR / f"papers_{section_id}.yaml")
        print(f"  [OK] {section_id}: {len(entries)} papers")
        return f"<!-- START PAPERS:{section_id} -->{md}<!-- END PAPERS:{section_id} -->"
    
    new_content, count = BLOCK_RE.subn(replace_block, content)
    
    # Write if anything changed (badge or paper blocks)
    if new_content != original_content:
        filepath.write_text(new_content, encoding="utf-8")
    
    return count


def update_about_page():
    """Update paper count in about.md."""
    about_file = DOCS_DIR / "about.md"
    if not about_file.exists():
        return
    
    content = about_file.read_text(encoding="utf-8")
    unique_count = count_unique_papers()
    
    # Update: "Based on a systematic review of XXX papers"
    new_content = re.sub(
        r'(Based on a systematic review of )\d+( papers and online resources)',
        rf'\g<1>{unique_count}\g<2>',
        content
    )
    
    if new_content != content:
        about_file.write_text(new_content, encoding="utf-8")
        print(f"  [INFO] Updated about.md with {unique_count} papers")


def main():
    """Main function: update all document files."""
    print("=" * 60)
    print("Auto-updating paper lists (shields.io style badges)")
    print("=" * 60)
    
    doc_files = [
        (DOCS_DIR / "index.md", True),  # Update badge for index.md
        (DOCS_DIR / "methods.md", False),
        (DOCS_DIR / "data.md", False),
        (DOCS_DIR / "analysis.md", False),
    ]
    
    total_blocks = 0
    
    for doc_file, update_badge in doc_files:
        if doc_file.exists():
            print(f"\nProcessing {doc_file.name}:")
            count = update_markdown_file(doc_file, update_badge=update_badge)
            total_blocks += count
            if count == 0:
                print(f"  [INFO] No <!-- START PAPERS:xxx --> markers found")
    
    # Update about.md
    print(f"\nProcessing about.md:")
    update_about_page()
    
    print("\n" + "=" * 60)
    print(f"Done! Updated {total_blocks} paper blocks.")
    print("=" * 60)


if __name__ == "__main__":
    main()

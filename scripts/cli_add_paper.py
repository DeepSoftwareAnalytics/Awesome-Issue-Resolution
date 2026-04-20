#!/usr/bin/env python3
"""
Non-interactive CLI for adding papers to the survey database.
Supports adding to SQLite DB (which syncs to YAML on --sync).

Usage:
    python scripts/cli_add_paper.py --short-name SWE-bench --title "SWE-bench: ..." \\
        --authors "Carlos Deng et al." --venue "ICLR 2024" --year 2024 \\
        --category single_agent --arxiv https://arxiv.org/abs/... \\
        --github https://github.com/... --sync

    # Or use --yaml to write directly to YAML (no DB):
    python scripts/cli_add_paper.py --short-name TestPaper --title "Test" \\
        --authors "Author" --venue "arXiv" --year 2024 \\
        --category single_agent --yaml-only

    # List recent papers:
    python scripts/cli_add_paper.py --list --category single_agent

    # Search papers:
    python scripts/cli_add_paper.py --search "SWE-bench"

    # Show categories:
    python scripts/cli_add_paper.py --categories
"""

import argparse
import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Setup path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "app"))

# Minimal dependencies (sqlite3 is stdlib)
import sqlite3
import yaml

# =============================================================================
# Config
# =============================================================================

DATA_DIR = ROOT / "app" / "data"
DATABASE_PATH = DATA_DIR / "database" / "survey.db"
YAML_DIR = DATA_DIR

CATEGORIES = {
    "evaluation_datasets": "📊 Evaluation Datasets",
    "training_datasets": "🎯 Training Datasets",
    "single_agent": "🤖 Single-Agent Systems",
    "multi_agent": "👥 Multi-Agent Systems",
    "workflow": "🔄 Workflow-Based Methods",
    "tool": "🛠️ Tool-Augmented Methods",
    "memory": "🧠 Memory-Enhanced Methods",
    "sft": "📚 Supervised Fine-Tuning (SFT)",
    "rl": "🎮 Reinforcement Learning (RL)",
    "inference_scaling": "⚡ Inference-Time Scaling",
    "data_collection": "📥 Data Collection Methods",
    "data_synthesis": "🔬 Data Synthesis Methods",
    "data_analysis": "📈 Data Analysis",
    "methods_analysis": "🔍 Methods Analysis",
    "others": "🧩 Others",
    "uncategorized": "❓ Uncategorized",
}


# =============================================================================
# Database helpers
# =============================================================================

def get_db():
    """Get SQLite connection."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(str(DATABASE_PATH))


def paper_to_db(paper: dict, category: str, conn=None) -> int:
    """Insert paper into DB, return paper_id."""
    close = conn is None
    conn = conn or get_db()
    now = datetime.now().isoformat()

    # Parse month from year if not provided
    month = paper.get('month', f"{paper.get('year', '2024')}-01")

    try:
        cursor = conn.execute("""
            INSERT INTO papers 
            (short_name, title, authors, venue, year, month, category, 
             github_link, huggingface_link, arxiv_link, openreview_link, doi_link, website_link,
             created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            paper.get('short_name', ''),
            paper.get('title', ''),
            paper.get('authors', ''),
            paper.get('venue', ''),
            str(paper.get('year', '')),
            month,
            category,
            paper.get('github'),
            paper.get('huggingface'),
            paper.get('arxiv'),
            paper.get('openreview'),
            paper.get('doi'),
            paper.get('website'),
            now, now
        ))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f"⚠️  Paper already exists: {paper.get('short_name', 'unknown')}")
        print(f"    Error: {e}")
        return -1
    finally:
        if close:
            conn.close()


def list_papers_db(category: str = None, limit: int = 20, offset: int = 0) -> list:
    """List papers from DB."""
    conn = get_db()
    if category:
        rows = conn.execute("""
            SELECT id, short_name, title, authors, COALESCE(venue,'-') as venue, year, COALESCE(month,'') as month, category
            FROM papers WHERE category LIKE ? 
            ORDER BY month DESC LIMIT ? OFFSET ?
        """, (f'%{category}%', limit, offset)).fetchall()
    else:
        rows = conn.execute("""
            SELECT id, short_name, title, authors, COALESCE(venue,'-') as venue, year, COALESCE(month,'') as month, category
            FROM papers ORDER BY month DESC LIMIT ? OFFSET ?
        """, (limit, offset)).fetchall()
    conn.close()
    return rows


def search_papers_db(keyword: str) -> list:
    """Search papers by keyword."""
    conn = get_db()
    pattern = f"%{keyword}%"
    rows = conn.execute("""
        SELECT id, short_name, title, authors, COALESCE(venue,'-') as venue, year, COALESCE(month,'') as month, category
        FROM papers 
        WHERE short_name LIKE ? OR title LIKE ? OR authors LIKE ?
        ORDER BY month DESC LIMIT 50
    """, (pattern, pattern, pattern)).fetchall()
    conn.close()
    return rows


def paper_to_yaml_file(paper: dict, category: str):
    """Append paper to YAML file (for --yaml-only mode)."""
    yaml_file = YAML_DIR / f"papers_{category}.yaml"
    
    # Load existing
    if yaml_file.exists():
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or []
    else:
        data = []
    
    # Check duplicate
    short_name = paper.get('short_name', '').lower()
    for p in data:
        if p.get('short_name', '').lower() == short_name:
            print(f"⚠️  Duplicate short_name '{paper['short_name']}' in {yaml_file.name}")
            return False
    
    data.append(paper)
    
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return True


def sync_db_to_yaml(conn=None):
    """Sync all DB papers back to YAML files."""
    close = conn is None
    conn = conn or get_db()
    
    rows = conn.execute("SELECT short_name, title, authors, venue, year, month, category, github_link, huggingface_link, arxiv_link, openreview_link, doi_link, website_link FROM papers").fetchall()
    
    # Group by category
    by_cat = {}
    for row in rows:
        (short_name, title, authors, venue, year, month, category, 
         github, hf, arxiv, openreview, doi, website) = row
        links = {}
        if arxiv: links['arxiv'] = arxiv
        if github: links['github'] = github
        if hf: links['huggingface'] = hf
        if openreview: links['openreview'] = openreview
        if doi: links['doi'] = doi
        if website: links['website'] = website
        
        paper = {
            'short_name': short_name,
            'title': title,
            'authors': authors,
            'venue': venue or '-',
            'year': str(year) if year else '',
            'month': month or '',
            'links': links,
        }
        
        cats = [c.strip() for c in category.split(',') if c.strip()]
        for cat in cats:
            if cat not in by_cat:
                by_cat[cat] = []
            by_cat[cat].append(paper)
    
    # Write each category YAML
    for cat, papers in by_cat.items():
        yaml_file = YAML_DIR / f"papers_{cat}.yaml"
        # Preserve existing papers not in DB (those without paper_id)
        existing = []
        if yaml_file.exists():
            with open(yaml_file, 'r', encoding='utf-8') as f:
                existing = yaml.safe_load(f) or []
        
        # Merge (DB wins on duplicates by short_name)
        existing_names = {p.get('short_name', '').lower() for p in existing}
        for p in papers:
            if p['short_name'].lower() not in existing_names:
                existing.append(p)
        
        # Sort by month
        existing.sort(key=lambda p: p.get('month', '0'), reverse=True)
        
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(existing, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    if close:
        conn.close()
    print(f"✅ Synced {len(rows)} papers to YAML files")
    return True


# =============================================================================
# Init DB schema (if needed)
# =============================================================================

def init_db_schema(conn=None):
    """Create DB tables if they don't exist."""
    close = conn is None
    conn = conn or get_db()
    schema = (ROOT / "app" / "data" / "database" / "schema.sql").read_text()
    conn.executescript(schema)
    conn.commit()
    if close:
        conn.close()


# =============================================================================
# CLI
# =============================================================================

def print_paper_row(row, idx=0):
    id, short_name, title, authors, venue, year, month, category = row
    title_short = title[:60] + '...' if len(title) > 60 else title
    print(f"  [{id}] {short_name}")
    print(f"       {title_short}")
    print(f"       {authors[:50]}{'...' if len(authors) > 50 else ''}")
    print(f"       {venue} | {year} | {month} | {category}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Add/search/list papers in the Awesome-Issue-Resolution survey.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add a paper to DB
  python scripts/cli_add_paper.py \\
      --short-name SWE-bench \\
      --title "SWE-bench: Task-Oriented Evaluation of Software Engineering Agents" \\
      --authors "Carlos Deng et al." \\
      --venue "ICLR 2024" \\
      --year 2024 \\
      --category single_agent \\
      --arxiv https://arxiv.org/abs/...

  # Add and sync to YAML immediately
  python scripts/cli_add_paper.py --short-name Test --title "Test" --authors "A" \\
      --venue "arXiv" --year 2024 --category single_agent --sync

  # Write directly to YAML (no DB)
  python scripts/cli_add_paper.py --short-name Test --title "Test" --authors "A" \\
      --venue "arXiv" --year 2024 --category single_agent --yaml-only

  # List recent papers
  python scripts/cli_add_paper.py --list

  # Search
  python scripts/cli_add_paper.py --search "SWE"
"""
    )
    
    # Paper fields
    parser.add_argument('--short-name', '--short_name', dest='short_name')
    parser.add_argument('--title')
    parser.add_argument('--authors')
    parser.add_argument('--venue', default='')
    parser.add_argument('--year', type=int, default=2024)
    parser.add_argument('--month', default='')
    parser.add_argument('--category', default='single_agent',
                        help=f"Category ID. Options: {', '.join(CATEGORIES.keys())}")
    
    # Links
    parser.add_argument('--arxiv')
    parser.add_argument('--github')
    parser.add_argument('--huggingface', '--hf')
    parser.add_argument('--openreview')
    parser.add_argument('--doi')
    parser.add_argument('--website')
    
    # Actions
    parser.add_argument('--list', action='store_true', help='List recent papers')
    parser.add_argument('--search', metavar='KEYWORD', help='Search papers')
    parser.add_argument('--categories', action='store_true', help='Show category list')
    parser.add_argument('--sync', action='store_true', help='Sync DB → YAML after adding')
    parser.add_argument('--yaml-only', action='store_true', help='Write directly to YAML (skip DB)')
    parser.add_argument('--limit', type=int, default=20, help='Max papers to list (default: 20)')
    parser.add_argument('--init-db', action='store_true', help='Initialize DB schema')
    
    args = parser.parse_args()

    # Validate
    if args.init_db:
        init_db_schema()
        print("✅ DB schema initialized")
        return 0

    if args.categories:
        print("Available categories:")
        for cat_id, cat_name in CATEGORIES.items():
            print(f"  {cat_id:30s} {cat_name}")
        return 0

    if args.list:
        rows = list_papers_db(limit=args.limit)
        if not rows:
            print("No papers found.")
        else:
            print(f"Recent papers (showing {len(rows)}):\n")
            for i, row in enumerate(rows):
                print_paper_row(row, i)
        return 0

    if args.search:
        rows = search_papers_db(args.search)
        if not rows:
            print(f"No papers found matching '{args.search}'")
        else:
            print(f"Found {len(rows)} papers:\n")
            for i, row in enumerate(rows):
                print_paper_row(row, i)
        return 0

    # Add paper
    if not args.title and not args.list and not args.search:
        parser.print_help()
        print("\n⚠️  No action specified. Use --list, --search, --categories, or provide paper fields to add.")
        return 1

    if args.short_name and args.title:
        paper = {
            'short_name': args.short_name,
            'title': args.title,
            'authors': args.authors or '',
            'venue': args.venue or '-',
            'year': str(args.year),
            'month': args.month or f"{args.year}-01",
            'links': {},
        }
        if args.arxiv: paper['links']['arxiv'] = args.arxiv
        if args.github: paper['links']['github'] = args.github
        if args.huggingface: paper['links']['huggingface'] = args.huggingface
        if args.openreview: paper['links']['openreview'] = args.openreview
        if args.doi: paper['links']['doi'] = args.doi
        if args.website: paper['links']['website'] = args.website

        if args.yaml_only:
            ok = paper_to_yaml_file(paper, args.category)
            if ok:
                print(f"✅ Added '{paper['short_name']}' → {YAML_DIR}/papers_{args.category}.yaml")
            return 0

        # DB mode
        if not DATABASE_PATH.exists():
            print("⚠️  DB not initialized. Run: python scripts/cli_add_paper.py --init-db")
            print("    Or use --yaml-only to write directly to YAML.")
            return 1

        conn = get_db()
        pid = paper_to_db(paper, args.category, conn)
        conn.close()

        if pid > 0:
            print(f"✅ Added paper '{paper['short_name']}' (DB id={pid}) → category={args.category}")
            if args.sync:
                sync_db_to_yaml()
                print("✅ Synced DB → YAML")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())

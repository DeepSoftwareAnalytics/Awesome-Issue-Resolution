#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch import papers from CSV template.

Usage:
    python scripts/batch_import.py <csv_file>
"""
import sys
import os
import csv
from pathlib import Path
import yaml

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
TEMPLATES_DIR = ROOT / "templates"

VALID_CATEGORIES = [
    "evaluation_datasets", "training_datasets", "single_agent", "multi_agent",
    "workflow", "tool", "memory", "sft", "rl", "inference_scaling",
    "data_collection", "data_synthesis", "data_analysis", "methods_analysis"
]


def load_yaml_file(category_id):
    """Load existing YAML file"""
    yaml_file = DATA_DIR / f"papers_{category_id}.yaml"
    if not yaml_file.exists():
        return []
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or []
    except Exception as e:
        print(f"❌ Error loading {yaml_file}: {e}")
        return []


def save_yaml_file(category_id, data):
    """Save YAML file"""
    yaml_file = DATA_DIR / f"papers_{category_id}.yaml"
    try:
        with open(yaml_file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        return True
    except Exception as e:
        print(f"❌ Error saving {yaml_file}: {e}")
        return False


def check_duplicate(paper, papers):
    """Check for duplicate papers"""
    short_name_lower = paper.get('short_name', '').strip().lower()
    title_lower = paper.get('title', '').strip().lower()
    
    for existing in papers:
        existing_short = existing.get('short_name', '').strip().lower()
        existing_title = existing.get('title', '').strip().lower()
        
        if short_name_lower == existing_short:
            return 'short_name', existing.get('short_name')
        if title_lower == existing_title:
            return 'title', existing.get('title')
    
    return None, None


def parse_csv_line(line, line_num):
    """Parse a CSV line into paper dict"""
    if len(line) < 6:
        print(f"❌ Line {line_num}: Need at least 6 fields (category, short_name, title, authors, venue, year)")
        return None
    
    category_id = line[0].strip()
    if category_id not in VALID_CATEGORIES:
        print(f"❌ Line {line_num}: Invalid category '{category_id}'")
        return None
    
    paper = {
        'short_name': line[1].strip() if len(line) > 1 else '',
        'title': line[2].strip() if len(line) > 2 else '',
        'authors': line[3].strip() if len(line) > 3 and line[3].strip() != '-' else '',
        'venue': line[4].strip() if len(line) > 4 and line[4].strip() != '-' else '',
        'year': line[5].strip() if len(line) > 5 else '',
        'links': {}
    }
    
    if not paper['short_name'] or not paper['title'] or not paper['year']:
        print(f"❌ Line {line_num}: short_name, title, and year are required")
        return None
    
    # Parse links
    link_types = ['arxiv', 'github', 'huggingface', 'openreview', 'acl', 'doi', 'website']
    for i, link_type in enumerate(link_types):
        if len(line) > 6 + i:
            url = line[6 + i].strip()
            if url and url != '-':
                paper['links'][link_type] = url
    
    return category_id, paper


def import_papers_from_csv(csv_file):
    """Import papers from CSV file"""
    if not csv_file.exists():
        print(f"❌ File not found: {csv_file}")
        return False
    
    print("=" * 70)
    print("  📥 Batch Import Papers from CSV")
    print("=" * 70)
    print(f"\nReading: {csv_file}\n")
    
    # Parse CSV
    papers_by_category = {}
    line_num = 0
    skipped = 0
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                line_num += 1
                
                # Skip empty lines and comments
                if not line or not line[0].strip() or line[0].strip().startswith('#'):
                    continue
                
                result = parse_csv_line(line, line_num)
                if not result:
                    skipped += 1
                    continue
                
                category_id, paper = result
                if category_id not in papers_by_category:
                    papers_by_category[category_id] = []
                papers_by_category[category_id].append(paper)
    
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return False
    
    if not papers_by_category:
        print("❌ No valid papers found in CSV")
        return False
    
    # Preview
    print(f"Found {sum(len(p) for p in papers_by_category.values())} papers across {len(papers_by_category)} categories")
    if skipped > 0:
        print(f"⚠️  Skipped {skipped} invalid lines")
    print()
    
    for category_id, papers in papers_by_category.items():
        print(f"  {category_id}: {len(papers)} papers")
    
    print("\n" + "=" * 70)
    response = input("Continue with import? [Y/n]: ").strip().lower()
    if response not in ('', 'y', 'yes'):
        print("❌ Cancelled")
        return False
    
    # Import papers
    total_added = 0
    total_skipped = 0
    
    for category_id, new_papers in papers_by_category.items():
        print(f"\n📂 Processing {category_id}...")
        existing_papers = load_yaml_file(category_id)
        
        added = 0
        for paper in new_papers:
            # Check duplicate
            dup_type, dup_value = check_duplicate(paper, existing_papers)
            if dup_type:
                print(f"  ⚠️  Duplicate {dup_type}: {paper['short_name']} (skipped)")
                total_skipped += 1
                continue
            
            existing_papers.append(paper)
            print(f"  ✅ Added: {paper['short_name']}")
            added += 1
        
        if added > 0:
            if save_yaml_file(category_id, existing_papers):
                print(f"  💾 Saved {added} papers to {category_id}.yaml")
                total_added += added
            else:
                print(f"  ❌ Failed to save {category_id}.yaml")
    
    print("\n" + "=" * 70)
    print(f"✅ Import complete!")
    print(f"   Added: {total_added} papers")
    if total_skipped > 0:
        print(f"   Skipped: {total_skipped} duplicates")
    print("=" * 70)
    
    # Offer to run update scripts
    print()
    response = input("🔄 Run update scripts now? [Y/n]: ").strip().lower()
    if response in ('', 'y', 'yes'):
        import subprocess
        print("\n▶ Rendering papers...")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "render_papers.py")])
        print("\n▶ Syncing README...")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_readme.py")])
        print("\n✅ Update complete!")
    
    return True


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python scripts/batch_import.py <csv_file>")
        print("\nExample:")
        print("  python scripts/batch_import.py templates/papers_template.csv")
        print("  python scripts/batch_import.py my_papers.csv")
        return 1
    
    csv_file = Path(sys.argv[1])
    return 0 if import_papers_from_csv(csv_file) else 1


if __name__ == "__main__":
    sys.exit(main())


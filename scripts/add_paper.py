#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive script to add/edit papers in YAML data files.

Usage:
    python scripts/add_paper.py
"""
import sys
import os
import subprocess
from pathlib import Path
import yaml

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import config
DATA_DIR = config.DATA_DIR

# Available paper categories
CATEGORIES = {
    "1": ("evaluation_datasets", "📊 Evaluation Datasets"),
    "2": ("training_datasets", "🎯 Training Datasets"),
    "3": ("single_agent", "🤖 Single-Agent Systems"),
    "4": ("multi_agent", "👥 Multi-Agent Systems"),
    "5": ("workflow", "🔄 Workflow-Based Methods"),
    "6": ("tool", "🛠️ Tool-Augmented Methods"),
    "7": ("memory", "🧠 Memory-Enhanced Methods"),
    "8": ("sft", "📚 Supervised Fine-Tuning (SFT)"),
    "9": ("rl", "🎮 Reinforcement Learning (RL)"),
    "10": ("inference_scaling", "⚡ Inference-Time Scaling"),
    "11": ("data_collection", "📥 Data Collection Methods"),
    "12": ("data_synthesis", "🔬 Data Synthesis Methods"),
    "13": ("data_analysis", "📈 Data Analysis"),
    "14": ("methods_analysis", "🔍 Methods Analysis"),
    "15": ("others", "🧩 Others"),
}


def print_banner():
    """Print welcome banner"""
    print("=" * 70)
    print("  📝 Add/Edit Paper - Awesome Issue Resolution")
    print("=" * 70)
    print()


def load_yaml_file(category_id):
    """Load YAML file"""
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


def select_mode():
    """Select operation mode"""
    print("Select mode:")
    print("  [1] Add new paper")
    print("  [2] Edit existing paper")
    print()
    while True:
        choice = input("Enter mode (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("❌ Invalid choice.")


def select_category():
    """Select paper category"""
    print("\n📂 Select category:")
    for key, (_, desc) in CATEGORIES.items():
        print(f"  [{key:>2}] {desc}")
    
    print()
    while True:
        choice = input("Category number: ").strip()
        if choice in CATEGORIES:
            category_id, category_name = CATEGORIES[choice]
            print(f"✓ Selected: {category_name}\n")
            return category_id
        print("❌ Invalid choice.")


def search_papers(papers, keyword):
    """Search papers by keyword"""
    results = []
    keyword_lower = keyword.lower()
    for idx, paper in enumerate(papers):
        short_name = paper.get('short_name', '').lower()
        title = paper.get('title', '').lower()
        if keyword_lower in short_name or keyword_lower in title:
            results.append((idx, paper))
    return results


def display_paper(paper, index=None):
    """Display paper information"""
    if index is not None:
        print(f"\n[{index}] Paper:")
    else:
        print("\nPaper:")
    print(f"  Short Name: {paper.get('short_name', 'N/A')}")
    print(f"  Title: {paper.get('title', 'N/A')}")
    print(f"  Authors: {paper.get('authors', 'N/A')}")
    print(f"  Venue: {paper.get('venue', 'N/A')}")
    print(f"  Year: {paper.get('year', 'N/A')}")
    links = paper.get('links', {})
    if links:
        print("  Links:")
        for link_type, url in links.items():
            print(f"    - {link_type}: {url}")


def collect_paper_info_bulk():
    """Collect paper information in bulk"""
    print("📋 Enter paper information (multi-line mode)")
    print("Format: short_name | title | authors | venue | year | arxiv | github | huggingface | openreview | acl | doi | website")
    print("Empty fields: use '-' or leave blank")
    print("Example: SWE-bench | Title Here | Authors | arXiv 2024 | 2024 | https://arxiv.org/... | - | - | - | - | - | -")
    print("(Press Enter twice to finish)\n")
    
    lines = []
    while True:
        line = input().strip()
        if not line:
            if lines:
                break
            else:
                continue
        lines.append(line)
    
    if not lines:
        return None
    
    # Parse the input
    parts = [p.strip() for p in lines[0].split('|')]
    if len(parts) < 5:
        print("❌ Invalid format. Need at least: short_name | title | authors | venue | year")
        return None
    
    paper = {
        'short_name': parts[0] if parts[0] and parts[0] != '-' else '',
        'title': parts[1] if len(parts) > 1 and parts[1] != '-' else '',
        'authors': parts[2] if len(parts) > 2 and parts[2] != '-' else '',
        'venue': parts[3] if len(parts) > 3 and parts[3] != '-' else '',
        'year': parts[4] if len(parts) > 4 and parts[4] != '-' else '',
        'links': {}
    }
    
    # Parse links
    link_types = ['arxiv', 'github', 'huggingface', 'openreview', 'acl', 'doi', 'website']
    for i, link_type in enumerate(link_types):
        if len(parts) > 5 + i and parts[5 + i] and parts[5 + i] != '-':
            paper['links'][link_type] = parts[5 + i]
    
    return paper


def edit_paper_interactive(paper):
    """Edit paper interactively"""
    print("\nEdit paper (press Enter to keep current value):")
    
    new_paper = {}
    new_paper['short_name'] = input(f"Short Name [{paper.get('short_name', '')}]: ").strip() or paper.get('short_name', '')
    new_paper['title'] = input(f"Title [{paper.get('title', '')}]: ").strip() or paper.get('title', '')
    new_paper['authors'] = input(f"Authors [{paper.get('authors', '')}]: ").strip() or paper.get('authors', '')
    new_paper['venue'] = input(f"Venue [{paper.get('venue', '')}]: ").strip() or paper.get('venue', '')
    new_paper['year'] = input(f"Year [{paper.get('year', '')}]: ").strip() or paper.get('year', '')
    
    # Links
    new_paper['links'] = paper.get('links', {}).copy()
    print("\nLinks (press Enter to skip):")
    for link_type in ['arxiv', 'github', 'huggingface', 'openreview', 'acl', 'doi', 'website']:
        current = new_paper['links'].get(link_type, '')
        prompt = f"  {link_type} [{current}]: " if current else f"  {link_type}: "
        url = input(prompt).strip()
        if url:
            new_paper['links'][link_type] = url
        elif not current and url == '':
            # Keep empty if was empty
            pass
    
    return new_paper


def check_duplicate(paper, papers, exclude_idx=None):
    """Check for duplicate papers"""
    short_name_lower = paper.get('short_name', '').strip().lower()
    title_lower = paper.get('title', '').strip().lower()
    
    for idx, existing in enumerate(papers):
        if exclude_idx is not None and idx == exclude_idx:
            continue
        
        existing_short = existing.get('short_name', '').strip().lower()
        existing_title = existing.get('title', '').strip().lower()
        
        if short_name_lower == existing_short:
            return 'short_name', existing.get('short_name')
        if title_lower == existing_title:
            return 'title', existing.get('title')
    
    return None, None


def run_update_scripts():
    """Run update scripts"""
    print("\n" + "=" * 70)
    print("📋 Running update scripts...")
    print("=" * 70)
    
    # Render papers
    print("\n▶ Rendering papers...")
    try:
        subprocess.run([sys.executable, str(config.script('render_papers'))], check=True)
        print("  ✅ Success")
    except:
        print("  ⚠️ Warning")
    
    # Sync README
    print("\n▶ Syncing README...")
    try:
        subprocess.run([sys.executable, str(config.script('sync_readme'))], check=True)
        print("  ✅ Success")
    except:
        print("  ⚠️ Warning")
    
    # Build website
    print("\n▶ Building website...")
    try:
        subprocess.run(["mkdocs", "build"], check=True)
        print("  ✅ Success")
    except:
        print("  ⚠️ mkdocs not installed or failed")
    
    print("\n" + "=" * 70)
    print("✅ Update complete!")
    print("=" * 70)


def main():
    """Main function"""
    print_banner()
    
    mode = select_mode()
    category_id = select_category()
    papers = load_yaml_file(category_id)
    
    if mode == '1':
        # Add new paper
        print("Choose input method:")
        print("  [1] Bulk input (one line with |)")
        print("  [2] Interactive input")
        input_mode = input("\nInput method (1-2): ").strip()
        
        if input_mode == '1':
            paper = collect_paper_info_bulk()
            if not paper:
                print("❌ Cancelled")
                return 1
        else:
            paper = edit_paper_interactive({})
        
        # Check duplicate
        dup_type, dup_value = check_duplicate(paper, papers)
        if dup_type:
            print(f"\n⚠️  Duplicate {dup_type} detected: {dup_value}")
            if input("Continue anyway? [y/N]: ").strip().lower() != 'y':
                print("❌ Cancelled")
                return 0
        
        # Preview and confirm
        display_paper(paper)
        if input("\n✓ Add this paper? [Y/n]: ").strip().lower() not in ('', 'y', 'yes'):
            print("❌ Cancelled")
            return 0
        
        papers.append(paper)
        if save_yaml_file(category_id, papers):
            print(f"\n✅ Paper added! Total: {len(papers)}")
        else:
            return 1
    
    else:
        # Edit existing paper
        if not papers:
            print("❌ No papers in this category")
            return 1
        
        keyword = input("Search keyword (short name or title): ").strip()
        results = search_papers(papers, keyword)
        
        if not results:
            print("❌ No papers found")
            return 1
        
        print(f"\nFound {len(results)} paper(s):")
        for idx, (paper_idx, paper) in enumerate(results):
            display_paper(paper, idx)
        
        if len(results) == 1:
            selected = 0
        else:
            while True:
                try:
                    selected = int(input(f"\nSelect paper (0-{len(results)-1}): ").strip())
                    if 0 <= selected < len(results):
                        break
                except:
                    pass
                print("❌ Invalid selection")
        
        paper_idx, old_paper = results[selected]
        print("\n" + "=" * 70)
        print("Current paper:")
        display_paper(old_paper)
        
        new_paper = edit_paper_interactive(old_paper)
        
        # Check duplicate (exclude self)
        dup_type, dup_value = check_duplicate(new_paper, papers, exclude_idx=paper_idx)
        if dup_type:
            print(f"\n⚠️  Duplicate {dup_type} detected: {dup_value}")
            if input("Continue anyway? [y/N]: ").strip().lower() != 'y':
                print("❌ Cancelled")
                return 0
        
        # Preview and confirm
        print("\n" + "=" * 70)
        print("Updated paper:")
        display_paper(new_paper)
        
        if input("\n✓ Save changes? [Y/n]: ").strip().lower() not in ('', 'y', 'yes'):
            print("❌ Cancelled")
            return 0
        
        papers[paper_idx] = new_paper
        if save_yaml_file(category_id, papers):
            print("\n✅ Paper updated!")
        else:
            return 1
    
    # Ask to run update scripts
    if input("\n🔄 Run update scripts? [Y/n]: ").strip().lower() in ('', 'y', 'yes'):
        run_update_scripts()
    
    print("\n📋 Next steps:")
    print("   git add . && git commit -m 'Update papers'")
    print("   git push")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

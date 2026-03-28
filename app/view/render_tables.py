#!/usr/bin/env python3
"""
Render CSV tables to Markdown format for README and website
Input: data/tables/*.csv
Output: Markdown tables in README.md and docs/tables.md

Usage:
    python view/render_tables.py
"""
import sys
import csv
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import config

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')


# Table metadata mapping
TABLE_INFO = {
    'table1': {
        'title': 'Evaluation & Training Datasets',
        'description': 'A comprehensive survey and statistical overview of issue resolution datasets. We categorize these datasets based on programming language, modality support, source repositories, data scale (Amount), and the availability of reproducible execution environments.'
    },
    'table2': {
        'title': 'Training Trajectory Datasets',
        'description': 'A survey of trajectory datasets used for agent training or analysis. We list the programming language, number of source repositories, and total trajectories for each dataset.'
    },
    'table3': {
        'title': 'SFT-based Methods',
        'description': 'Overview of SFT-based methods for issue resolution. This table categorizes models by their base architecture and training scaffold (Sorted by Performance).'
    },
    'table4': {
        'title': 'RL-based Methods',
        'description': 'A comprehensive overview of specialized models for issue resolution, categorized by parameter size. The table details each model\'s base architecture, the training scaffold used for rollout, the type of reward signal employed (Outcome vs. Process), and their performance results (Res. %) on issue resolution benchmarks.'
    },
    'table5': {
        'title': 'General Foundation Models',
        'description': 'Overview of general foundation models evaluated on issue resolution. The table details the specific inference scaffolds (e.g., OpenHands, Agentless) employed during the evaluation process to achieve the reported results.'
    }
}


def parse_link_cell(cell):
    """Convert link commands in a cell to Markdown badges"""
    if not cell or cell == '-':
        return cell
    
    links = []
    
    # Extract GitHub links
    gh_pattern = r'\\ghlink\{([^}]+)\}'
    for match in re.finditer(gh_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        links.append(f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({url})')
    
    # Extract HuggingFace links
    hf_pattern = r'\\hflink\{([^}]+)\}'
    for match in re.finditer(hf_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        links.append(f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({url})')
    
    # Extract website/blog links
    blog_pattern = r'\\bloglink\{([^}]+)\}'
    for match in re.finditer(blog_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        # Determine link type based on URL
        if 'drive.google.com' in url or '/datasets/' in url:
            link_text = 'data'
        elif 'blog' in url or 'news' in url:
            link_text = 'blog'
        elif 'arxiv.org' in url:
            link_text = 'paper'
        elif 'github.io' in url:
            link_text = 'website'
        elif 'modelscope' in url:
            link_text = 'model'
        else:
            link_text = 'link'
        links.append(f'[![Website](https://img.shields.io/badge/Website-{link_text}-5B9BD5?logo=googlechrome&logoColor=white)]({url})')
    
    if links:
        return ' '.join(links)
    
    return cell


def csv_to_markdown(csv_file, table_name):
    """Convert a CSV file to Markdown table"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    # Get table info
    info = TABLE_INFO.get(table_name, {})
    title = info.get('title', table_name)
    description = info.get('description', '')
    
    # Build Markdown
    md_lines = []
    md_lines.append(f"### {title}")
    md_lines.append("")
    if description:
        md_lines.append(f"_{description}_")
        md_lines.append("")
    
    # Table header
    header_line = '| ' + ' | '.join(f"**{h}**" for h in headers) + ' |'
    separator_line = '|' + '---|' * len(headers)
    
    md_lines.append(header_line)
    md_lines.append(separator_line)
    
    # Table rows
    for row in rows:
        # Process cells
        processed_row = []
        for i, cell in enumerate(row):
            # Parse link commands for link columns (usually last few columns)
            if '\\ghlink' in cell or '\\hflink' in cell or '\\bloglink' in cell:
                cell = parse_link_cell(cell)
            # Handle checkmarks and crosses
            cell = cell.replace('\\ding{51}', '✅')
            cell = cell.replace('\\ding{55}', '❌')
            # Handle math
            cell = re.sub(r'\$\\times\$', '×', cell)
            # Clean any remaining LaTeX
            cell = re.sub(r'\$([^$]+)\$', r'\1', cell)
            
            processed_row.append(cell)
        
        row_line = '| ' + ' | '.join(processed_row) + ' |'
        md_lines.append(row_line)
    
    return '\n'.join(md_lines)


def generate_all_tables_md():
    """Generate combined Markdown file with all tables"""
    tables_dir = config.DATA_DIR / 'tables'
    csv_files = sorted(tables_dir.glob('table*.csv'))
    
    if not csv_files:
        print("❌ No CSV files found!")
        return None
    
    all_tables = []
    all_tables.append("# Survey Tables")
    all_tables.append("")
    
    for csv_file in csv_files:
        table_name = csv_file.stem
        table_md = csv_to_markdown(csv_file, table_name)
        all_tables.append(table_md)
        all_tables.append("")
        all_tables.append("---")
        all_tables.append("")
    
    return '\n'.join(all_tables)


def sync_to_website():
    """Sync tables to docs/tables.md"""
    all_tables_content = generate_all_tables_md()
    
    if not all_tables_content:
        return False
    
    # Create tables.md content
    tables_md_content = """# Tables & Resources

This page contains statistical tables and resources from our comprehensive survey on Issue Resolution in Software Engineering.

---

"""
    tables_md_content += all_tables_content.replace('# Survey Tables\n\n', '')
    
    # Write to docs/tables.md
    tables_md_path = config.DOCS_DIR / 'tables.md'
    tables_md_path.write_text(tables_md_content, encoding='utf-8')
    
    print("✓ Synced to docs/tables.md")
    return True


def sync_to_readme():
    """Sync tables to README.md"""
    all_tables_content = generate_all_tables_md()
    
    if not all_tables_content:
        return False
    
    # Read README
    readme_path = ROOT / 'README.md'
    if not readme_path.exists():
        print("❌ README.md not found!")
        return False
    
    readme_content = readme_path.read_text(encoding='utf-8')
    
    # Find tables section
    tables_start = readme_content.find('<!-- START TABLES -->')
    tables_end = readme_content.find('<!-- END TABLES -->')
    
    if tables_start == -1 or tables_end == -1:
        print("❌ Tables markers not found in README.md!")
        return False
    
    # Replace tables section
    new_readme = (
        readme_content[:tables_start + len('<!-- START TABLES -->')] +
        '\n\n' +
        all_tables_content.replace('# Survey Tables\n\n', '') +
        '\n' +
        readme_content[tables_end:]
    )
    
    # Write back
    readme_path.write_text(new_readme, encoding='utf-8')
    
    print("✓ Synced to README.md")
    return True


def main():
    print("\n" + "="*70)
    print("  Rendering Tables from CSV")
    print("="*70 + "\n")
    
    # Sync to website
    print("📊 Generating tables for website...")
    if not sync_to_website():
        return False
    
    # Sync to README
    print("📊 Generating tables for README...")
    if not sync_to_readme():
        return False
    
    print("\n" + "="*70)
    print("  Rendering Complete!")
    print("="*70 + "\n")
    
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)


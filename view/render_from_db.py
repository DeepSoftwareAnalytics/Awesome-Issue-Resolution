#!/usr/bin/env python3
"""
Render Markdown tables from SQLite Database
Input: database/survey.db
Output: Markdown tables in README.md and docs/tables.md

Usage:
    python view/render_from_db.py
"""
import sys
from pathlib import Path

# Add project root to path for imports
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models import (
    Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel,
    get_session
)

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')


# Table metadata
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


def render_links(links_dict):
    """Render links as Markdown badges"""
    links = []

    if links_dict.get('github'):
        links.append(f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({links_dict["github"]})')

    if links_dict.get('huggingface'):
        hf_links = links_dict['huggingface'].split(', ') if isinstance(links_dict['huggingface'], str) else [links_dict['huggingface']]
        for hf_link in hf_links:
            links.append(f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({hf_link})')

    if links_dict.get('website'):
        links.append(f'[![Website](https://img.shields.io/badge/Website-link-5B9BD5?logo=googlechrome&logoColor=white)]({links_dict["website"]})')

    if links_dict.get('code'):
        links.append(f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({links_dict["code"]})')

    if links_dict.get('data'):
        links.append(f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({links_dict["data"]})')

    if links_dict.get('model'):
        links.append(f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({links_dict["model"]})')

    return ' '.join(links) if links else '-'


def generate_table1():
    """Generate Evaluation & Training Datasets table"""
    session = get_session()

    single_pl = session.query(Dataset).filter_by(category='single-pl').all()
    multi_pl = session.query(Dataset).filter_by(category='multi-pl').all()

    md_lines = []
    md_lines.append(f"### {TABLE_INFO['table1']['title']}")
    md_lines.append("")
    md_lines.append(f"_{TABLE_INFO['table1']['description']}_")
    md_lines.append("")

    md_lines.append('| **Dataset** | **Language** | **Multimodal** | **Repos** | **Amount** | **Environment** | **Link** |')
    md_lines.append('|---|---|---|---|---|---|---|')

    md_lines.append('| **Single-PL Datasets** |  |  |  |  |  |  |')
    for dataset in single_pl:
        links = render_links({
            'github': dataset.github_link,
            'huggingface': dataset.huggingface_link,
            'website': dataset.website_link
        })
        md_lines.append(f'| {dataset.name} | {dataset.language or "-"} | {dataset.multimodal or "?"} | {dataset.repos or "-"} | {dataset.amount or "-"} | {dataset.environment or "?"} | {links} |')

    md_lines.append('| **Multi-PL Datasets** |  |  |  |  |  |  |')
    for dataset in multi_pl:
        links = render_links({
            'github': dataset.github_link,
            'huggingface': dataset.huggingface_link,
            'website': dataset.website_link
        })
        md_lines.append(f'| {dataset.name} | {dataset.language or "-"} | {dataset.multimodal or "?"} | {dataset.repos or "-"} | {dataset.amount or "-"} | {dataset.environment or "?"} | {links} |')

    return '\n'.join(md_lines)


def generate_table2():
    """Generate Training Trajectory Datasets table"""
    session = get_session()
    datasets = session.query(TrainingDataset).all()

    md_lines = []
    md_lines.append(f"### {TABLE_INFO['table2']['title']}")
    md_lines.append("")
    md_lines.append(f"_{TABLE_INFO['table2']['description']}_")
    md_lines.append("")

    md_lines.append('| **Dataset** | **Language** | **Repos** | **Amount** | **Link** |')
    md_lines.append('|---|---|---|---|---|')

    for dataset in datasets:
        links = render_links({
            'github': dataset.github_link,
            'huggingface': dataset.huggingface_link
        })
        md_lines.append(f'| {dataset.name} | {dataset.language or "-"} | {dataset.repos or "-"} | {dataset.amount or "-"} | {links} |')

    return '\n'.join(md_lines)


def generate_table3():
    """Generate SFT Methods table"""
    session = get_session()
    methods = session.query(SFTMethod).order_by(SFTMethod.resolution_percent.desc()).all()

    md_lines = []
    md_lines.append(f"### {TABLE_INFO['table3']['title']}")
    md_lines.append("")
    md_lines.append(f"_{TABLE_INFO['table3']['description']}_")
    md_lines.append("")

    md_lines.append('| **Model Name** | **Base Model** | **Size** | **Arch.** | **Training Scaffold** | **Res.(%)** | **Code** | **Data** | **Model** |')
    md_lines.append('|---|---|---|---|---|---|---|---|---|')

    for method in methods:
        code_link = f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({method.code_link})' if method.code_link else '-'
        data_link = f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({method.data_link})' if method.data_link else '-'
        model_link = f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({method.model_link})' if method.model_link else '-'
        md_lines.append(f'| {method.model_name} | {method.base_model or "-"} | {method.size or "-"} | {method.architecture or "-"} | {method.training_scaffold or "-"} | {method.resolution_percent or "-"} | {code_link} | {data_link} | {model_link} |')

    return '\n'.join(md_lines)


def generate_table4():
    """Generate RL Methods table"""
    session = get_session()
    methods = session.query(RLMethod).order_by(RLMethod.resolution_percent.desc()).all()

    md_lines = []
    md_lines.append(f"### {TABLE_INFO['table4']['title']}")
    md_lines.append("")
    md_lines.append(f"_{TABLE_INFO['table4']['description']}_")
    md_lines.append("")

    md_lines.append('| **Model Name** | **Base Model** | **Size** | **Arch.** | **Train. Scaffold** | **Reward** | **Res.(%)** | **Code** | **Data** | **Model** |')
    md_lines.append('|---|---|---|---|---|---|---|---|---|---|')

    size_groups = {
        '560B Models (MoE)': [],
        '72B Models': [],
        '32B Models': [],
        '14B Models': [],
        '7-8B Models': []
    }

    for method in methods:
        size = method.size or ''
        if '560B' in size or '309B' in size:
            size_groups['560B Models (MoE)'].append(method)
        elif '72B' in size or '70B' in size:
            size_groups['72B Models'].append(method)
        elif '32B' in size or '36B' in size or '30B' in size:
            size_groups['32B Models'].append(method)
        elif '14B' in size:
            size_groups['14B Models'].append(method)
        elif '7B' in size or '8B' in size or '9B' in size:
            size_groups['7-8B Models'].append(method)
        else:
            size_groups['32B Models'].append(method)

    for group_name, group_methods in size_groups.items():
        if group_methods:
            md_lines.append(f'| **{group_name}** |  |  |  |  |  |  |  |  |  |')
            for method in group_methods:
                code_link = f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({method.code_link})' if method.code_link else '-'
                data_link = f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({method.data_link})' if method.data_link else '-'
                model_link = f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({method.model_link})' if method.model_link else '-'
                md_lines.append(f'| {method.model_name} | {method.base_model or "-"} | {method.size or "-"} | {method.architecture or "-"} | {method.training_scaffold or "-"} | {method.reward_type or "-"} | {method.resolution_percent or "-"} | {code_link} | {data_link} | {model_link} |')

    return '\n'.join(md_lines)


def generate_table5():
    """Generate Foundation Models table"""
    session = get_session()
    db_models = session.query(FoundationModel).order_by(FoundationModel.resolution_percent.desc()).all()

    md_lines = []
    md_lines.append(f"### {TABLE_INFO['table5']['title']}")
    md_lines.append("")
    md_lines.append(f"_{TABLE_INFO['table5']['description']}_")
    md_lines.append("")

    md_lines.append('| **Model Name** | **Size** | **Arch.** | **Inf. Scaffold** | **Reward** | **Res.(%)** | **Code** | **Model** |')
    md_lines.append('|---|---|---|---|---|---|---|---|')

    for model in db_models:
        code_link = f'[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({model.code_link})' if model.code_link else '-'

        model_link = '-'
        if model.model_link:
            if 'huggingface.co' in model.model_link:
                model_link = f'[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({model.model_link})'
            elif 'modelscope' in model.model_link:
                model_link = f'[![Website](https://img.shields.io/badge/Website-model-5B9BD5?logo=googlechrome&logoColor=white)]({model.model_link})'
            else:
                model_link = f'[![Website](https://img.shields.io/badge/Website-link-5B9BD5?logo=googlechrome&logoColor=white)]({model.model_link})'

        md_lines.append(f'| {model.model_name} | {model.size or "-"} | {model.architecture or "-"} | {model.inference_scaffold or "-"} | {model.reward_type or "-"} | {model.resolution_percent or "-"} | {code_link} | {model_link} |')

    return '\n'.join(md_lines)


def generate_all_tables_md():
    """Generate combined Markdown with all tables"""
    all_tables = []
    all_tables.append("# Survey Tables")
    all_tables.append("")

    print("  Generating Table 1 (Datasets)...")
    all_tables.append(generate_table1())
    all_tables.append("")
    all_tables.append("---")
    all_tables.append("")

    print("  Generating Table 2 (Training Datasets)...")
    all_tables.append(generate_table2())
    all_tables.append("")
    all_tables.append("---")
    all_tables.append("")

    print("  Generating Table 3 (SFT Methods)...")
    all_tables.append(generate_table3())
    all_tables.append("")
    all_tables.append("---")
    all_tables.append("")

    print("  Generating Table 4 (RL Methods)...")
    all_tables.append(generate_table4())
    all_tables.append("")
    all_tables.append("---")
    all_tables.append("")

    print("  Generating Table 5 (Foundation Models)...")
    all_tables.append(generate_table5())
    all_tables.append("")
    all_tables.append("---")
    all_tables.append("")

    return '\n'.join(all_tables)


def sync_to_website():
    """Sync tables to docs/tables.md"""
    all_tables_content = generate_all_tables_md()

    tables_md_content = """# Tables & Resources

This page contains statistical tables and resources from our comprehensive survey on Issue Resolution in Software Engineering.

---

"""
    tables_md_content += all_tables_content.replace('# Survey Tables\n\n', '')

    tables_md_path = ROOT / 'docs' / 'tables.md'
    tables_md_path.write_text(tables_md_content, encoding='utf-8')

    print("[OK] Synced to docs/tables.md")
    return True


def update_paper_counts():
    """Update paper count badges and text in README.md and docs/index.md."""
    import re
    session = get_session()
    count = session.query(Paper).count()
    session.close()

    updated = []
    for filepath in [ROOT / 'README.md', ROOT / 'docs' / 'index.md']:
        if not filepath.exists():
            continue
        content = filepath.read_text(encoding='utf-8')
        original = content

        content = re.sub(r'papers-\d+-green', f'papers-{count}-green', content)
        content = re.sub(
            r'\*\*\d+ papers and online resources\*\*',
            f'**{count} papers and online resources**', content
        )
        content = re.sub(r'Total: \d+ works', f'Total: {count} works', content)
        content = re.sub(
            r'> \*\*Total: \d+ works\*\*',
            f'> **Total: {count} works**', content
        )

        if content != original:
            filepath.write_text(content, encoding='utf-8')
            updated.append(filepath.name)

    if updated:
        print(f"[OK] Updated paper count to {count} in: {', '.join(updated)}")
    else:
        print(f"[OK] Paper count already up-to-date ({count})")
    return True


def sync_to_readme():
    """Sync tables and paper counts to README.md"""
    all_tables_content = generate_all_tables_md()

    readme_path = ROOT / 'README.md'
    if not readme_path.exists():
        print("[ERROR] README.md not found!")
        return False

    readme_content = readme_path.read_text(encoding='utf-8')

    tables_start = readme_content.find('<!-- START TABLES -->')
    tables_end = readme_content.find('<!-- END TABLES -->')

    if tables_start == -1 or tables_end == -1:
        print("[ERROR] Tables markers not found in README.md!")
        return False

    new_readme = (
        readme_content[:tables_start + len('<!-- START TABLES -->')] +
        '\n\n' +
        all_tables_content.replace('# Survey Tables\n\n', '') +
        '\n' +
        readme_content[tables_end:]
    )

    readme_path.write_text(new_readme, encoding='utf-8')
    print("[OK] Synced tables to README.md")

    # Also update paper counts across all docs
    update_paper_counts()
    return True


def main():
    print("\n" + "=" * 70)
    print("  Rendering Tables from Database")
    print("=" * 70 + "\n")

    db_path = ROOT / 'database' / 'survey.db'
    if not db_path.exists():
        print("[ERROR] Database not found! Run 'python start.py --init' first.")
        return False

    print("[INFO] Generating tables for website...")
    if not sync_to_website():
        return False

    print("[INFO] Generating tables for README...")
    if not sync_to_readme():
        return False

    print("\n" + "=" * 70)
    print("  Rendering Complete!")
    print("=" * 70 + "\n")

    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

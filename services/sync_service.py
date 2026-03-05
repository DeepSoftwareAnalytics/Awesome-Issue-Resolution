"""
Data Sync Service
Bidirectional sync between database and YAML/CSV files
"""
import sys
import yaml
import csv
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel, get_session


def export_papers_to_yaml():
    """Export paper data to YAML files.

    Papers with multi-label categories (e.g. "sft, training_datasets") are
    written into EVERY matching single-category YAML file so that sync_readme.py
    picks them up correctly.
    """
    session = get_session()

    # Collect papers per individual (single) category
    categories: dict = {}
    papers = session.query(Paper).all()

    for paper in papers:
        paper_data = {
            'short_name': paper.short_name,
            'title': paper.title,
            'authors': paper.authors,
            'year': paper.year,
            'venue': paper.venue,
        }

        if paper.month:
            paper_data['month'] = paper.month
        if paper.abstract:
            paper_data['abstract'] = paper.abstract

        # Build links dict
        links = {}
        if paper.arxiv_link:      links['arxiv']       = paper.arxiv_link
        if paper.github_link:     links['github']      = paper.github_link
        if paper.huggingface_link:links['huggingface'] = paper.huggingface_link
        if paper.website_link:    links['website']     = paper.website_link
        if paper.doi_link:        links['doi']         = paper.doi_link
        if paper.openreview_link: links['openreview']  = paper.openreview_link
        if links:
            paper_data['links'] = links

        # Split comma-separated multi-label categories and add to each
        raw_cats = paper.category or ''
        single_cats = [c.strip() for c in raw_cats.split(',') if c.strip()]
        if not single_cats:
            single_cats = ['uncategorized']

        for cat in single_cats:
            categories.setdefault(cat, []).append(paper_data)

    # Save one YAML file per individual category
    data_dir = Path('data')
    for category, papers_list in categories.items():
        # Sort by month descending so YAML files are newest-first
        papers_list.sort(key=lambda p: p.get('month', '') or '', reverse=True)
        file_path = data_dir / f'papers_{category}.yaml'
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(papers_list, f, allow_unicode=True, sort_keys=False,
                      default_flow_style=False)

    session.close()
    return len(papers)


def export_datasets_to_csv():
    """Export datasets to CSV (writes to data/export/, NOT data/tables/ which is the LaTeX source of truth)"""
    session = get_session()
    datasets = session.query(Dataset).order_by(Dataset.category, Dataset.id).all()

    Path('data/export').mkdir(parents=True, exist_ok=True)
    csv_file = Path('data/export/table1.csv')

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Dataset', 'Language', 'Multimodal', 'Repos', 'Amount', 'Environment', 'Link'])

        # Single-PL category
        writer.writerow(['**Single-PL Datasets**', '', '', '', '', '', ''])
        single_pl = [d for d in datasets if d.category == 'single-pl']
        for dataset in single_pl:
            links = []
            if dataset.github_link:
                links.append(f'\\ghlink{{{dataset.github_link}}}')
            if dataset.huggingface_link:
                for hf in dataset.huggingface_link.split(', '):
                    links.append(f'\\hflink{{{hf}}}')
            if dataset.website_link:
                links.append(f'\\bloglink{{{dataset.website_link}}}')

            link_str = ' '.join(links) if links else '-'

            writer.writerow([
                dataset.name,
                dataset.language or '-',
                dataset.multimodal or '?',
                dataset.repos or '-',
                dataset.amount or '-',
                dataset.environment or '?',
                link_str
            ])

        # Multi-PL category
        writer.writerow(['**Multi-PL Datasets**', '', '', '', '', '', ''])
        multi_pl = [d for d in datasets if d.category == 'multi-pl']
        for dataset in multi_pl:
            links = []
            if dataset.github_link:
                links.append(f'\\ghlink{{{dataset.github_link}}}')
            if dataset.huggingface_link:
                for hf in dataset.huggingface_link.split(', '):
                    links.append(f'\\hflink{{{hf}}}')
            if dataset.website_link:
                links.append(f'\\bloglink{{{dataset.website_link}}}')

            link_str = ' '.join(links) if links else '-'

            writer.writerow([
                dataset.name,
                dataset.language or '-',
                dataset.multimodal or '?',
                dataset.repos or '-',
                dataset.amount or '-',
                dataset.environment or '?',
                link_str
            ])

    return len(datasets)


def export_training_datasets_to_csv():
    """Export training datasets to CSV (writes to data/export/, NOT data/tables/ which is the LaTeX source of truth)"""
    session = get_session()
    datasets = session.query(TrainingDataset).all()

    Path('data/export').mkdir(parents=True, exist_ok=True)
    csv_file = Path('data/export/table2.csv')

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Dataset', 'Language', 'Repos', 'Amount', 'Link'])

        for dataset in datasets:
            links = []
            if dataset.github_link:
                links.append(f'\\ghlink{{{dataset.github_link}}}')
            if dataset.huggingface_link:
                links.append(f'\\hflink{{{dataset.huggingface_link}}}')

            link_str = ' '.join(links) if links else '-'

            writer.writerow([
                dataset.name,
                dataset.language or '-',
                dataset.repos or '-',
                dataset.amount or '-',
                link_str
            ])

    return len(datasets)


def export_sft_methods_to_csv():
    """Export SFT methods to CSV (writes to data/export/, NOT data/tables/ which is the LaTeX source of truth)"""
    session = get_session()
    methods = session.query(SFTMethod).order_by(SFTMethod.resolution_percent.desc()).all()

    Path('data/export').mkdir(parents=True, exist_ok=True)
    csv_file = Path('data/export/table3.csv')

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model Name', 'Base Model', 'Size', 'Arch.', 'Training Scaffold', 'Res.(%)', 'Code', 'Data', 'Model'])

        for method in methods:
            code = f'\\ghlink{{{method.code_link}}}' if method.code_link else '-'
            data = f'\\hflink{{{method.data_link}}}' if method.data_link else '-'
            model = f'\\hflink{{{method.model_link}}}' if method.model_link else '-'

            writer.writerow([
                method.model_name,
                method.base_model or '-',
                method.size or '-',
                method.architecture or '-',
                method.training_scaffold or '-',
                method.resolution_percent if method.resolution_percent else '-',
                code,
                data,
                model
            ])

    return len(methods)


def export_rl_methods_to_csv():
    """Export RL methods to CSV (writes to data/export/, NOT data/tables/ which is the LaTeX source of truth)"""
    session = get_session()
    methods = session.query(RLMethod).order_by(RLMethod.resolution_percent.desc()).all()

    Path('data/export').mkdir(parents=True, exist_ok=True)
    csv_file = Path('data/export/table4.csv')

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model Name', 'Base Model', 'Size', 'Arch.', 'Train. Scaffold', 'Reward', 'Res.(%)', 'Code', 'Data', 'Model'])

        # Group by size
        size_groups = {
            '560B': [m for m in methods if m.size and ('560B' in m.size or '309B' in m.size)],
            '72B': [m for m in methods if m.size and ('72B' in m.size or '70B' in m.size)],
            '32B': [m for m in methods if m.size and ('32B' in m.size or '36B' in m.size or '30B' in m.size)],
            '14B': [m for m in methods if m.size and '14B' in m.size],
            '7-8B': [m for m in methods if m.size and ('7B' in m.size or '8B' in m.size or '9B' in m.size)]
        }

        for group_name, group_methods in size_groups.items():
            if group_methods:
                writer.writerow([f'**{group_name} Models**' if '560B' in group_name else f'**{group_name} Models**', '', '', '', '', '', '', '', '', ''])
                for method in group_methods:
                    code = f'\\ghlink{{{method.code_link}}}' if method.code_link else '-'
                    data = f'\\hflink{{{method.data_link}}}' if method.data_link else '-'
                    model = f'\\hflink{{{method.model_link}}}' if method.model_link else '-'

                    writer.writerow([
                        method.model_name,
                        method.base_model or '-',
                        method.size or '-',
                        method.architecture or '-',
                        method.training_scaffold or '-',
                        method.reward_type or '-',
                        method.resolution_percent if method.resolution_percent else '-',
                        code,
                        data,
                        model
                    ])

    return len(methods)


def export_foundation_models_to_csv():
    """Export foundation models to CSV (writes to data/export/, NOT data/tables/ which is the LaTeX source of truth)"""
    session = get_session()
    models = session.query(FoundationModel).order_by(FoundationModel.resolution_percent.desc()).all()

    Path('data/export').mkdir(parents=True, exist_ok=True)
    csv_file = Path('data/export/table5.csv')

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model Name', 'Size', 'Arch.', 'Inf. Scaffold', 'Reward', 'Res.(%)', 'Code', 'Model'])

        for model in models:
            code = f'\\ghlink{{{model.code_link}}}' if model.code_link else '-'

            # Model link may be HuggingFace or Website
            model_link = '-'
            if model.model_link:
                if 'huggingface.co' in model.model_link:
                    model_link = f'\\hflink{{{model.model_link}}}'
                elif 'modelscope' in model.model_link:
                    model_link = f'\\bloglink{{{model.model_link}}}'
                else:
                    model_link = f'\\bloglink{{{model.model_link}}}'

            writer.writerow([
                model.model_name,
                model.size or '-',
                model.architecture or '-',
                model.inference_scaffold or '-',
                model.reward_type or '-',
                model.resolution_percent if model.resolution_percent else '-',
                code,
                model_link
            ])

    return len(models)


def sync_all_to_data():
    """Sync all data to data folder"""
    results = {}

    print("\n" + "=" * 70)
    print("[INFO] Syncing database to data folder")
    print("=" * 70 + "\n")

    # Export papers
    print("[INFO] Papers: Exporting...")
    results['papers'] = export_papers_to_yaml()
    print(f"[OK] Exported {results['papers']} papers\n")

    # Export datasets
    print("[INFO] Datasets: Exporting (table1)...")
    results['datasets'] = export_datasets_to_csv()
    print(f"[OK] Exported {results['datasets']} datasets\n")

    # Export training datasets
    print("[INFO] Training Datasets: Exporting (table2)...")
    results['training_datasets'] = export_training_datasets_to_csv()
    print(f"[OK] Exported {results['training_datasets']} training datasets\n")

    # Export SFT methods
    print("[INFO] SFT Methods: Exporting (table3)...")
    results['sft_methods'] = export_sft_methods_to_csv()
    print(f"[OK] Exported {results['sft_methods']} SFT methods\n")

    # Export RL methods
    print("[INFO] RL Methods: Exporting (table4)...")
    results['rl_methods'] = export_rl_methods_to_csv()
    print(f"[OK] Exported {results['rl_methods']} RL methods\n")

    # Export foundation models
    print("[INFO] Foundation Models: Exporting (table5)...")
    results['foundation_models'] = export_foundation_models_to_csv()
    print(f"[OK] Exported {results['foundation_models']} foundation models\n")

    print("=" * 70)
    print(f"[OK] Sync complete! Total: {sum(results.values())} records")
    print("=" * 70 + "\n")

    return results


if __name__ == '__main__':
    results = sync_all_to_data()
    print(f"[OK] Sync complete: Papers={results['papers']}, Datasets={results['datasets']}, Training={results['training_datasets']}, SFT={results['sft_methods']}, RL={results['rl_methods']}, Foundation={results['foundation_models']}")

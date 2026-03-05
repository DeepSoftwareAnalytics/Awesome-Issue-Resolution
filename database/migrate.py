#!/usr/bin/env python3
"""
Data Migration Script: CSV/YAML → SQLite Database
Import data from data/tables/*.csv and data/papers_*.yaml into SQLite
"""
import sys
import csv
import yaml
import re
from pathlib import Path

# Ensure project root is on sys.path so `models` package can be found
# regardless of the working directory when this script is invoked
sys.path.insert(0, str(Path(__file__).parent.parent))

from models import (
    Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel,
    init_db, get_session
)

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')


def parse_links(cell):
    """Parse link commands from CSV cell"""
    links = {'github': [], 'huggingface': [], 'website': []}
    
    if not cell or cell == '-':
        return links
    
    # Extract GitHub links
    gh_pattern = r'\\ghlink\{([^}]+)\}'
    for match in re.finditer(gh_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        links['github'].append(url)
    
    # Extract HuggingFace links
    hf_pattern = r'\\hflink\{([^}]+)\}'
    for match in re.finditer(hf_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        links['huggingface'].append(url)
    
    # Extract website/blog links
    blog_pattern = r'\\bloglink\{([^}]+)\}'
    for match in re.finditer(blog_pattern, cell):
        url = match.group(1).replace('|||AMP|||', '&')
        links['website'].append(url)
    
    return links


def migrate_papers():
    """Migrate YAML paper files to database"""
    session = get_session()
    papers_dir = Path('data')
    yaml_files = sorted(papers_dir.glob('papers_*.yaml'))
    
    total_papers = 0
    
    for yaml_file in yaml_files:
        category = yaml_file.stem.replace('papers_', '')
        print(f"  Processing {yaml_file.name} (category: {category})...")
        
        with open(yaml_file, 'r', encoding='utf-8') as f:
            papers_data = yaml.safe_load(f)
        
        if not papers_data:
            continue
        
        for paper_data in papers_data:
            # Check if paper already exists
            existing = session.query(Paper).filter_by(
                short_name=paper_data['short_name']
            ).first()
            
            if existing:
                print(f"    Skipping duplicate: {paper_data['short_name']}")
                continue
            
            # Extract links
            links = paper_data.get('links', {})
            
            paper = Paper(
                short_name=paper_data['short_name'],
                title=paper_data['title'],
                authors=paper_data['authors'],
                year=paper_data['year'],
                venue=paper_data['venue'],
                category=category,
                abstract=paper_data.get('abstract'),
                arxiv_link=links.get('arxiv'),
                github_link=links.get('github'),
                huggingface_link=links.get('huggingface'),
                website_link=links.get('website'),
                doi_link=links.get('doi'),
                openreview_link=links.get('openreview')
            )
            
            session.add(paper)
            total_papers += 1
        
        session.commit()
    
    print(f"[OK] Migrated {total_papers} papers")


def migrate_table1_datasets():
    """Migrate table1.csv (Evaluation & Training Datasets) to database"""
    session = get_session()
    csv_file = Path('data/tables/table1.csv')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        current_category = 'single-pl'
        
        for row in reader:
            dataset_name = row['Dataset'].strip()
            
            # Handle category headers
            if dataset_name.startswith('**'):
                if 'Multi-PL' in dataset_name:
                    current_category = 'multi-pl'
                continue
            
            # Skip empty rows
            if not dataset_name or dataset_name == '-':
                continue
            
            # Parse links
            links = parse_links(row['Link'])
            
            dataset = Dataset(
                name=dataset_name,
                language=row['Language'] if row['Language'] != '-' else None,
                multimodal=row['Multimodal'] if row['Multimodal'] != '-' else None,
                repos=row['Repos'] if row['Repos'] != '-' else None,
                amount=row['Amount'] if row['Amount'] != '-' else None,
                environment=row['Environment'] if row['Environment'] != '-' else None,
                category=current_category,
                github_link=links['github'][0] if links['github'] else None,
                huggingface_link=', '.join(links['huggingface']) if links['huggingface'] else None,
                website_link=links['website'][0] if links['website'] else None
            )
            
            try:
                session.add(dataset)
                session.commit()
                count += 1
            except Exception as e:
                session.rollback()
                print(f"    [ERROR] Error adding {dataset_name}: {e}")
    
    print(f"[OK] Migrated {count} datasets")


def migrate_table2_training_datasets():
    """Migrate table2.csv (Training Trajectory Datasets) to database"""
    session = get_session()
    csv_file = Path('data/tables/table2.csv')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            dataset_name = row['Dataset'].strip()
            
            # Skip headers or empty rows
            if not dataset_name or dataset_name == '-':
                continue
            
            # Parse links
            links = parse_links(row['Link'])
            
            dataset = TrainingDataset(
                name=dataset_name,
                language=row['Language'] if row['Language'] != '-' else None,
                repos=row['Repos'] if row['Repos'] != '-' else None,
                amount=row['Amount'] if row['Amount'] != '-' else None,
                github_link=links['github'][0] if links['github'] else None,
                huggingface_link=', '.join(links['huggingface']) if links['huggingface'] else None
            )
            
            try:
                session.add(dataset)
                session.commit()
                count += 1
            except Exception as e:
                session.rollback()
                print(f"    [ERROR] Error adding {dataset_name}: {e}")
    
    print(f"[OK] Migrated {count} training datasets")


def migrate_table3_sft_methods():
    """Migrate table3.csv (SFT Methods) to database"""
    session = get_session()
    csv_file = Path('data/tables/table3.csv')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            model_name = row['Model Name'].strip()
            
            # Skip empty rows
            if not model_name or model_name == '-':
                continue
            
            # Parse resolution percentage
            res_percent = None
            if row['Res.(%)'] and row['Res.(%)'] != '-':
                try:
                    res_percent = float(row['Res.(%)'])
                except ValueError:
                    pass
            
            # Parse links
            code_links = parse_links(row['Code'])
            data_links = parse_links(row['Data'])
            model_links = parse_links(row['Model'])
            
            method = SFTMethod(
                model_name=model_name,
                base_model=row['Base Model'] if row['Base Model'] != '-' else None,
                size=row['Size'] if row['Size'] != '-' else None,
                architecture=row['Arch.'] if row['Arch.'] != '-' else None,
                training_scaffold=row['Training Scaffold'] if row['Training Scaffold'] != '-' else None,
                resolution_percent=res_percent,
                code_link=code_links['github'][0] if code_links['github'] else None,
                data_link=data_links['huggingface'][0] if data_links['huggingface'] else None,
                model_link=model_links['huggingface'][0] if model_links['huggingface'] else None
            )
            
            try:
                session.add(method)
                session.commit()
                count += 1
            except Exception as e:
                session.rollback()
                print(f"    [ERROR] Error adding {model_name}: {e}")
    
    print(f"[OK] Migrated {count} SFT methods")


def migrate_table4_rl_methods():
    """Migrate table4.csv (RL Methods) to database"""
    session = get_session()
    csv_file = Path('data/tables/table4.csv')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            model_name = row['Model Name'].strip()
            
            # Skip category headers and empty rows
            if model_name.startswith('**') or not model_name or model_name == '-':
                continue
            
            # Parse resolution percentage
            res_percent = None
            if row['Res.(%)'] and row['Res.(%)'] != '-':
                try:
                    res_percent = float(row['Res.(%)'])
                except ValueError:
                    pass
            
            # Parse links
            code_links = parse_links(row['Code'])
            data_links = parse_links(row['Data'])
            model_links = parse_links(row['Model'])
            
            method = RLMethod(
                model_name=model_name,
                base_model=row['Base Model'] if row['Base Model'] != '-' else None,
                size=row['Size'] if row['Size'] != '-' else None,
                architecture=row['Arch.'] if row['Arch.'] != '-' else None,
                training_scaffold=row['Train. Scaffold'] if row['Train. Scaffold'] != '-' else None,
                reward_type=row['Reward'] if row['Reward'] != '-' else None,
                resolution_percent=res_percent,
                code_link=code_links['github'][0] if code_links['github'] else None,
                data_link=data_links['huggingface'][0] if data_links['huggingface'] else None,
                model_link=model_links['huggingface'][0] if model_links['huggingface'] else None
            )
            
            try:
                session.add(method)
                session.commit()
                count += 1
            except Exception as e:
                session.rollback()
                print(f"    [ERROR] Error adding {model_name}: {e}")
    
    print(f"[OK] Migrated {count} RL methods")


def migrate_table5_foundation_models():
    """Migrate table5.csv (Foundation Models) to database"""
    session = get_session()
    csv_file = Path('data/tables/table5.csv')
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            model_name = row['Model Name'].strip()
            
            # Skip empty rows
            if not model_name or model_name == '-':
                continue
            
            # Parse resolution percentage
            res_percent = None
            if row['Res.(%)'] and row['Res.(%)'] != '-':
                try:
                    res_percent = float(row['Res.(%)'])
                except ValueError:
                    pass
            
            # Parse links
            code_links = parse_links(row['Code'])
            model_links = parse_links(row['Model'])
            
            model = FoundationModel(
                model_name=model_name,
                size=row['Size'] if row['Size'] != '-' else None,
                architecture=row['Arch.'] if row['Arch.'] != '-' else None,
                inference_scaffold=row['Inf. Scaffold'] if row['Inf. Scaffold'] != '-' else None,
                reward_type=row['Reward'] if row['Reward'] != '-' else None,
                resolution_percent=res_percent,
                code_link=code_links['github'][0] if code_links['github'] else None,
                model_link=model_links['huggingface'][0] if model_links['huggingface'] else (model_links['website'][0] if model_links['website'] else None)
            )
            
            try:
                session.add(model)
                session.commit()
                count += 1
            except Exception as e:
                session.rollback()
                print(f"    [ERROR] Error adding {model_name}: {e}")
    
    print(f"[OK] Migrated {count} foundation models")


def add_missing_columns():
    """Add any columns that exist in the model but are missing from the DB (safe to re-run)."""
    from models import get_engine
    import sqlalchemy as sa
    engine = get_engine()
    with engine.connect() as conn:
        inspector = sa.inspect(engine)
        existing = {col['name'] for col in inspector.get_columns('papers')}
        if 'featured' not in existing:
            conn.execute(sa.text('ALTER TABLE papers ADD COLUMN featured BOOLEAN DEFAULT 0'))
            conn.commit()
            print("[OK] Added 'featured' column to papers table")


def main():
    print("\n" + "="*70)
    print("  Data Migration: CSV/YAML → SQLite")
    print("="*70 + "\n")
    
    # Initialize database
    print("[INFO] Initializing database...")
    init_db()

    # Add any new columns to existing tables
    print("[INFO] Checking for schema updates...")
    add_missing_columns()
    
    # Migrate data
    print("\n[INFO] Migrating papers from YAML files...")
    migrate_papers()
    
    print("\n[INFO] Migrating datasets from table1.csv...")
    migrate_table1_datasets()
    
    print("\n[INFO] Migrating training datasets from table2.csv...")
    migrate_table2_training_datasets()
    
    print("\n[INFO] Migrating SFT methods from table3.csv...")
    migrate_table3_sft_methods()
    
    print("\n[INFO] Migrating RL methods from table4.csv...")
    migrate_table4_rl_methods()
    
    print("\n[INFO] Migrating foundation models from table5.csv...")
    migrate_table5_foundation_models()
    
    print("\n" + "="*70)
    print("  Migration Complete!")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()

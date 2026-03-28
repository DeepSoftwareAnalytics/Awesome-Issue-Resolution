#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate and sort table data according to specific rules.

Usage:
    python scripts/validate_tables.py
"""
import sys
import os
import csv
from pathlib import Path

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import config
TABLES_DIR = config.DATA_DIR / "tables"


def parse_number(value):
    """Parse number from string (handles 1,234 format)"""
    if not value or value.strip() in ['-', '']:
        return 0
    try:
        # Remove commas and parse
        return float(value.replace(',', ''))
    except:
        return 0


def validate_and_sort_table1(file_path):
    """
    Table 1: Datasets
    Rules:
    1. Categorize by language: Single-PL vs Multi-PL
    2. Sort by whether it's single or multi-language
    """
    print("\n📊 Validating Table 1: Datasets")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Separate headers and data
    single_pl = []
    multi_pl = []
    
    for row in rows:
        dataset = row.get('Dataset', '').strip()
        language = row.get('Language', '').strip()
        
        # Skip section headers
        if dataset.startswith('**'):
            continue
        
        # Categorize by language
        if ',' in language or '+' in language or language.lower() in ['multilingual', 'multi-language']:
            multi_pl.append(row)
        else:
            single_pl.append(row)
    
    print(f"  ✓ Single-PL datasets: {len(single_pl)}")
    print(f"  ✓ Multi-PL datasets: {len(multi_pl)}")
    
    # Write back with proper categorization
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write Single-PL section
        if single_pl:
            writer.writerow({k: '**Single-PL Datasets**' if k == 'Dataset' else '' for k in fieldnames})
            writer.writerows(single_pl)
        
        # Write Multi-PL section
        if multi_pl:
            writer.writerow({k: '**Multi-PL Datasets**' if k == 'Dataset' else '' for k in fieldnames})
            writer.writerows(multi_pl)
    
    print("  ✅ Table 1 validated and sorted")


def validate_and_sort_table2(file_path):
    """
    Table 2: Trajectory Datasets
    Rules:
    1. Sort by Amount (descending)
    """
    print("\n📊 Validating Table 2: Trajectory Datasets")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Sort by Amount (descending)
    rows.sort(key=lambda x: parse_number(x.get('Amount', '0')), reverse=True)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} trajectory datasets by Amount (descending)")
    print("  ✅ Table 2 validated and sorted")


def validate_and_sort_table3(file_path):
    """
    Table 3: SFT Models
    Rules:
    1. Sort by Res.% (resolved rate, descending)
    """
    print("\n📊 Validating Table 3: SFT Models")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Sort by Res.% (descending)
    rows.sort(key=lambda x: parse_number(x.get('Res.(%)', '0')), reverse=True)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} SFT models by Res.% (descending)")
    print("  ✅ Table 3 validated and sorted")


def extract_param_size(size_str):
    """Extract parameter size for sorting (e.g., '72B' -> 72, '1T' -> 1000, '309B-A15B' -> 309)"""
    if not size_str or size_str.strip() in ['-', '']:
        return 0
    
    # Extract first number and unit
    import re
    match = re.search(r'(\d+(?:\.\d+)?)\s*([BT])', size_str.upper())
    if match:
        num = float(match.group(1))
        unit = match.group(2)
        if unit == 'T':
            return num * 1000  # Convert T to B
        return num
    return 0


def validate_and_sort_table4(file_path):
    """
    Table 4: RL Models
    Rules:
    1. Categorize by model parameter size (560B, 72B, 32B, etc.)
    2. Sort by Res.% (resolved rate, descending) within each category
    """
    print("\n📊 Validating Table 4: RL Models")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Categorize by parameter size
    categories = {}
    for row in rows:
        model_name = row.get('Model Name', '').strip()
        
        # Skip existing category headers
        if model_name.startswith('**'):
            continue
        
        size = row.get('Size', '').strip()
        param_size = extract_param_size(size)
        
        # Determine category
        if param_size >= 500:
            category = '560B Models (MoE)'
        elif param_size >= 70:
            category = '72B Models'
        elif param_size >= 30:
            category = '32B Models'
        elif param_size >= 20:
            category = '22B Models'
        elif param_size >= 14:
            category = '14B Models'
        elif param_size >= 7:
            category = '7-8B Models'
        else:
            category = 'Other Models'
        
        if category not in categories:
            categories[category] = []
        categories[category].append(row)
    
    # Sort within each category by Res.% (descending)
    for category in categories:
        categories[category].sort(key=lambda x: parse_number(x.get('Res.(%)', '0')), reverse=True)
    
    # Define category order (largest to smallest)
    category_order = ['560B Models (MoE)', '72B Models', '32B Models', '22B Models', '14B Models', '7-8B Models', 'Other Models']
    
    # Write back with categorization
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for category in category_order:
            if category in categories:
                # Write category header
                header_row = {k: f'**{category}**' if k == 'Model Name' else '' for k in fieldnames}
                writer.writerow(header_row)
                # Write models in this category
                writer.writerows(categories[category])
    
    print(f"  ✓ Categorized into {len(categories)} size categories")
    for category in category_order:
        if category in categories:
            print(f"    - {category}: {len(categories[category])} models")
    print("  ✅ Table 4 validated and sorted")


def validate_and_sort_table5(file_path):
    """
    Table 5: General Models (Foundation/General-purpose models)
    Rules:
    1. Sort by Res.% (resolved rate, descending)
    """
    print("\n📊 Validating Table 5: General Models")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Sort by Res.% (descending)
    rows.sort(key=lambda x: parse_number(x.get('Res.(%)', '0')), reverse=True)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} general models by Res.% (descending)")
    print("  ✅ Table 5 validated and sorted")


def main():
    """Main function"""
    print("=" * 70)
    print("  🔍 Validating and Sorting Tables")
    print("=" * 70)
    
    validators = {
        'table1.csv': validate_and_sort_table1,
        'table2.csv': validate_and_sort_table2,
        'table3.csv': validate_and_sort_table3,
        'table4.csv': validate_and_sort_table4,
        'table5.csv': validate_and_sort_table5,
    }
    
    for filename, validator in validators.items():
        file_path = TABLES_DIR / filename
        if file_path.exists():
            try:
                validator(file_path)
            except Exception as e:
                print(f"  ❌ Error processing {filename}: {e}")
        else:
            print(f"\n⚠️  {filename} not found, skipping")
    
    print("\n" + "=" * 70)
    print("  ✅ Validation complete!")
    print("=" * 70)
    print("\n[TIP] Run 'python app/view/render_tables.py' to update the website")


if __name__ == "__main__":
    main()


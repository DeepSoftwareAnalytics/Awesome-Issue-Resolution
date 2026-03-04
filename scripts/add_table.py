#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive script to update table data from LaTeX sources.

Usage:
    python scripts/add_table.py
"""
import sys
import os
import subprocess
from pathlib import Path

# Set Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
CSV_DIR = ROOT / "data" / "tables"


def print_header():
    """Print script header."""
    print("=" * 70)
    print("  📊 Add/Update Table Data")
    print("=" * 70)
    print()


def list_csv_tables():
    """List all CSV table files."""
    if not CSV_DIR.exists():
        CSV_DIR.mkdir(parents=True, exist_ok=True)
    
    csv_files = sorted(CSV_DIR.glob("table*.csv"))
    return csv_files


def show_instructions():
    """Show usage instructions."""
    print("📋 This script helps you manage statistical tables.\n")
    print("Current workflow:")
    print("  1. Edit CSV files in: data/tables/")
    print("  2. Run this script to render and sync")
    print("  3. Changes will be synced to README and website\n")
    
    csv_files = list_csv_tables()
    
    print(f"📄 CSV tables: {len(csv_files)}")
    for f in csv_files:
        print(f"   - {f.name}")
    print()


def run_conversion():
    """Run the table rendering and sync pipeline."""
    print("=" * 70)
    print("  🔄 Running table update pipeline...")
    print("=" * 70)
    print()
    
    # Step 1: Validate and sort tables
    print("▶ [Step 1/3] Validating and sorting tables...")
    try:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_tables.py")],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode == 0:
            print("  ✅ Success")
        else:
            print(f"  ⚠️ Warning: {result.stderr}")
    except Exception as e:
        print(f"  ⚠️ Warning: {e}")
    print()
    
    # Step 2: Render tables to Markdown
    print("▶ [Step 2/3] Rendering tables to Markdown...")
    try:
        result = subprocess.run(
            [sys.executable, str(ROOT / "view" / "render_tables.py")],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode == 0:
            print("  ✅ Success")
        else:
            print(f"  ⚠️ Warning: {result.stderr}")
    except Exception as e:
        print(f"  ⚠️ Warning: {e}")
    print()
    
    # Step 3: Sync to README
    print("▶ [Step 3/3] Syncing to README...")
    try:
        result = subprocess.run(
            [sys.executable, str(ROOT / "view" / "sync_readme.py")],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode == 0:
            print("  ✅ Success")
        else:
            print(f"  ⚠️ Warning: {result.stderr}")
    except Exception as e:
        print(f"  ⚠️ Warning: {e}")
    print()
    
    print("=" * 70)
    print("  ✅ Table update complete!")
    print("=" * 70)
    print()
    print("📋 Next steps:")
    print("   1. Review changes: git status")
    print("   2. Preview website: mkdocs serve")
    print("   3. Commit changes: git add . && git commit -m 'Update tables'")
    print()


def main():
    """Main function."""
    print_header()
    show_instructions()
    
    print("=" * 70)
    response = input("🔄 Render tables and update website? [Y/n]: ").strip().lower()
    
    if response in ('', 'y', 'yes'):
        print()
        run_conversion()
        return 0
    else:
        print("\n❌ Cancelled.")
        return 0


if __name__ == "__main__":
    sys.exit(main())


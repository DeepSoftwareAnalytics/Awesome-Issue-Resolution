#!/bin/bash

echo "============================================"
echo "  Awesome Issue Resolution - Tools"
echo "============================================"
echo ""
echo "[1] Add Paper"
echo "[2] Add Table"
echo "[3] Batch Import"
echo "[4] Sync & Build"
echo "[5] Exit"
echo ""
read -p "Select option (1-5): " choice

case $choice in
    1)
        echo ""
        python3 scripts/add_paper.py
        ;;
    2)
        echo ""
        python3 scripts/add_table.py
        ;;
    3)
        echo ""
        read -p "CSV file path (or press Enter for template): " csv_file
        if [ -z "$csv_file" ]; then
            csv_file="templates/papers_template.csv"
        fi
        python3 scripts/batch_import.py "$csv_file"
        ;;
    4)
        echo ""
        echo "[1/4] Rendering papers..."
        python3 scripts/render_papers.py || exit 1
        echo "[2/4] Generating citation..."
        python3 scripts/generate_citation.py || exit 1
        echo "[3/4] Syncing README..."
        python3 scripts/sync_readme.py || exit 1
        echo "[4/4] Building website..."
        mkdocs build
        echo ""
        echo "✅ Complete! Preview: mkdocs serve"
        ;;
    5)
        exit 0
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac

echo ""


@echo off
chcp 65001 >nul 2>&1
setlocal

echo ============================================
echo   Awesome Issue Resolution - Tools
echo ============================================
echo.
echo [1] Add Paper
echo [2] Add Table
echo [3] Batch Import
echo [4] Sync ^& Build
echo [5] Exit
echo.
set /p choice="Select option (1-5): "

if "%choice%"=="1" (
    echo.
    python scripts/add_paper.py
) else if "%choice%"=="2" (
    echo.
    python scripts/add_table.py
) else if "%choice%"=="3" (
    echo.
    set /p csv_file="CSV file path (or press Enter for template): "
    if "!csv_file!"=="" (
        set csv_file=templates\papers_template.csv
    )
    python scripts/batch_import.py "!csv_file!"
) else if "%choice%"=="4" (
    echo.
    echo [1/4] Rendering papers...
    python scripts/render_papers.py || goto error
    echo [2/4] Generating citation...
    python scripts/generate_citation.py || goto error
    echo [3/4] Syncing README...
    python scripts/sync_readme.py || goto error
    echo [4/4] Building website...
    mkdocs build
    echo.
    echo ✅ Complete! Preview: mkdocs serve
) else if "%choice%"=="5" (
    exit /b 0
) else (
    echo Invalid option
    goto error
)

echo.
pause
exit /b 0

:error
echo.
echo ❌ Failed
pause
exit /b 1


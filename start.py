#!/usr/bin/env python3
"""
Awesome Issue Resolution - Project Startup Script

Default (no flags): initialises DB if needed, refreshes news, re-renders
Markdown from DB, builds the static site, then launches the admin server.

Usage:
    python start.py              # Full update + start admin server (port 5000)
    python start.py --port 8080  # Same, on a custom port
    python start.py --init       # Force re-import from YAML/CSV, then full update + start
    python start.py --build      # Build static site only and exit
    python start.py --news       # Refresh news section only and exit
    python start.py --render     # Re-render README/docs from DB only and exit
    python start.py --no-update  # Skip update steps, just start the server
"""
import sys
import os
import argparse
import subprocess
from pathlib import Path

# Ensure project root is on the path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')


def check_dependencies():
    """Check that required packages are installed."""
    missing = []
    packages = {
        'flask': 'flask',
        'flask_cors': 'flask-cors',
        'sqlalchemy': 'sqlalchemy',
        'yaml': 'pyyaml',
        'requests': 'requests',
    }
    for module, pip_name in packages.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print('[ERROR] Missing dependencies:')
        for p in missing:
            print(f'        pip install {p}')
        print('\nInstall all at once:')
        print('  pip install ' + ' '.join(missing))
        sys.exit(1)


def init_database(force: bool = False):
    """Initialize the SQLite database from YAML/CSV files."""
    db_path = ROOT / 'database' / 'survey.db'

    if db_path.exists() and not force:
        print('[OK] Database already exists:', db_path.name)
        return

    print('[INFO] Initializing database from data files...')
    result = subprocess.run(
        [sys.executable, 'database/migrate.py'],
        cwd=str(ROOT)
    )
    if result.returncode != 0:
        print('[ERROR] Database initialization failed.')
        sys.exit(1)
    print('[OK] Database initialized.')


def update_news():
    """Refresh the This Month's Papers section in docs/news.md and README.md."""
    print('[INFO] Refreshing monthly news section...')
    result = subprocess.run(
        [sys.executable, 'scripts/update_news.py'],
        cwd=str(ROOT)
    )
    if result.returncode == 0:
        print('[OK] News section updated.')
    else:
        print('[WARN] News update encountered an error (non-fatal).')
    return result.returncode


def render_markdown():
    """Re-render README.md and docs/ tables from the database."""
    print('[INFO] Rendering Markdown from database...')
    result = subprocess.run(
        [sys.executable, 'view/render_from_db.py'],
        cwd=str(ROOT)
    )
    if result.returncode == 0:
        print('[OK] Markdown rendered.')
    else:
        print('[WARN] Markdown render encountered an error (non-fatal).')
    return result.returncode


def build_site():
    """Run mkdocs build."""
    print('[INFO] Building static site with MkDocs...')
    result = subprocess.run(['mkdocs', 'build'], cwd=str(ROOT))
    if result.returncode == 0:
        print('[OK] Static site built to site/')
    else:
        print('[WARN] MkDocs build failed. Make sure mkdocs is installed:')
        print('  pip install mkdocs mkdocs-material')
    return result.returncode


def run_full_update():
    """Run the full update pipeline: news -> render -> build."""
    update_news()
    render_markdown()
    build_site()


def start_server(port: int = 5000):
    """Start the Flask admin server."""
    import config
    config.PORT = port

    print()
    print('=' * 60)
    print('  Awesome Issue Resolution - Admin Server')
    print('=' * 60)
    print(f'  [SERVER] http://localhost:{port}/')
    print(f'  [ADMIN]  http://localhost:{port}/admin')
    print(f'  [API]    http://localhost:{port}/api/stats')
    print('=' * 60)
    print()

    from app import app
    app.run(debug=config.DEBUG, host=config.HOST, port=port)


def main():
    parser = argparse.ArgumentParser(
        description='Awesome Issue Resolution - Project Manager'
    )
    parser.add_argument(
        '--init', action='store_true',
        help='Force re-import data from YAML/CSV into the database'
    )
    parser.add_argument(
        '--build', action='store_true',
        help='Build the static site (mkdocs build) and exit'
    )
    parser.add_argument(
        '--news', action='store_true',
        help='Refresh the This Month\'s Papers section only and exit'
    )
    parser.add_argument(
        '--render', action='store_true',
        help='Re-render README/docs from DB only and exit'
    )
    parser.add_argument(
        '--no-update', dest='no_update', action='store_true',
        help='Skip all update steps and start the server immediately'
    )
    parser.add_argument(
        '--port', type=int, default=5000,
        help='Port for the admin server (default: 5000)'
    )
    args = parser.parse_args()

    # Always check dependencies first
    check_dependencies()

    # --- Single-action flags (run task and exit) ---

    if args.build:
        sys.exit(build_site())

    if args.news:
        sys.exit(update_news())

    if args.render:
        sys.exit(render_markdown())

    # --- Server startup ---

    # Initialize (or re-import) the database
    init_database(force=args.init)

    if not args.no_update:
        # Full update pipeline before serving
        print()
        print('[INFO] Running pre-start update pipeline...')
        run_full_update()
        print()

    start_server(port=args.port)


if __name__ == '__main__':
    main()

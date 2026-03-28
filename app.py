#!/usr/bin/env python3
"""
Awesome Issue Resolution - Unified Application Server
MVC Architecture: Flask app serving both admin interface and API
"""
from flask import Flask, send_from_directory
from flask_cors import CORS
import sys
import os
import argparse
import subprocess
from pathlib import Path
import config

ROOT = Path(__file__).resolve().parent

if str(config.APP_DIR) not in sys.path:
    sys.path.insert(0, str(config.APP_DIR))


def create_app():
    app = Flask(
        __name__,
        template_folder=str(config.ADMIN_TEMPLATE_DIR),
        static_folder=str(config.ADMIN_STATIC_DIR),
        static_url_path='/admin/static'
    )
    CORS(app)

    from controllers.api_controller import api
    from controllers.admin_controller import admin as admin_bp
    app.register_blueprint(api)
    app.register_blueprint(admin_bp)
    return app


app = create_app()


@app.route('/')
def home():
    """Serve static site homepage"""
    try:
        return send_from_directory(config.SITE_DIR, 'index.html')
    except Exception:
        return """
        <h1>Welcome to Awesome Issue Resolution</h1>
        <p><a href="/admin">Admin Interface</a></p>
        <p><a href="/api/stats">API Documentation</a></p>
        <p>Note: Run <code>mkdocs build</code> to generate static site</p>
        """, 200


@app.route('/<path:path>')
def serve_static(path):
    """Serve mkdocs static site files.
    Tries the path as-is, then appends /index.html for directory URLs.
    """
    site = config.SITE_DIR
    if (site / path).is_file():
        return send_from_directory(site, path)
    for candidate in [path.rstrip('/') + '/index.html', path + '/index.html']:
        if (site / candidate).is_file():
            return send_from_directory(site, candidate)
    try:
        return send_from_directory(site, path)
    except Exception:
        if (site / '404.html').is_file():
            return send_from_directory(site, '404.html'), 404
        return "Not found", 404


def check_dependencies():
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


def run_python_task(script_name: str) -> int:
    result = subprocess.run(
        [sys.executable, str(config.script(script_name))],
        cwd=str(ROOT)
    )
    return result.returncode


def init_database(force: bool = False):
    db_path = config.DATABASE_PATH
    if db_path.exists() and not force:
        print('[OK] Database already exists:', db_path.name)
        return
    print('[INFO] Initializing database from data files...')
    if run_python_task('migrate') != 0:
        print('[ERROR] Database initialization failed.')
        sys.exit(1)
    print('[OK] Database initialized.')


def update_news():
    print('[INFO] Refreshing Recent Papers news section...')
    returncode = run_python_task('update_news')
    if returncode == 0:
        print('[OK] News section updated.')
    else:
        print('[WARN] News update encountered an error (non-fatal).')
    return returncode


def render_markdown():
    print('[INFO] Rendering Markdown from database...')
    returncode = run_python_task('render_from_db')
    if returncode == 0:
        print('[OK] Markdown rendered.')
    else:
        print('[WARN] Markdown render encountered an error (non-fatal).')
    return returncode


def export_admin_json():
    print('[INFO] Exporting admin JSON...')
    returncode = run_python_task('export_admin_json')
    if returncode == 0:
        print('[OK] Admin JSON exported.')
    else:
        print('[WARN] Admin JSON export encountered an error (non-fatal).')
    return returncode


def build_site():
    print('[INFO] Building static site with MkDocs...')
    result = subprocess.run(['mkdocs', 'build'], cwd=str(ROOT))
    if result.returncode == 0:
        print(f'[OK] Static site built to {config.SITE_DIR.relative_to(ROOT)}/')
    else:
        print('[WARN] MkDocs build failed. Make sure mkdocs is installed:')
        print('  pip install mkdocs mkdocs-material')
    return result.returncode


def run_full_update():
    update_news()
    render_markdown()
    export_admin_json()
    build_site()


def run_server(port: int = 5000):
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
    app.run(debug=config.DEBUG, host=config.HOST, port=port)


def main():
    if sys.platform == 'win32':
        os.system('chcp 65001 >nul 2>&1')

    parser = argparse.ArgumentParser(description='Awesome Issue Resolution - Project Manager')
    parser.add_argument('--init', action='store_true', help='Force re-import data from YAML/CSV into the database')
    parser.add_argument('--build', action='store_true', help='Build the static site (mkdocs build) and exit')
    parser.add_argument('--news', action='store_true', help='Refresh the Recent Papers section only and exit')
    parser.add_argument('--render', action='store_true', help='Re-render README/docs from DB only and exit')
    parser.add_argument('--no-update', dest='no_update', action='store_true', help='Skip all update steps and start the server immediately')
    parser.add_argument('--port', type=int, default=5000, help='Port for the admin server (default: 5000)')
    args = parser.parse_args()

    check_dependencies()

    if args.build:
        sys.exit(build_site())
    if args.news:
        sys.exit(update_news())
    if args.render:
        sys.exit(render_markdown())

    init_database(force=args.init)
    if not args.no_update:
        print()
        print('[INFO] Running pre-start update pipeline...')
        run_full_update()
        print()
    run_server(port=args.port)


if __name__ == '__main__':
    main()

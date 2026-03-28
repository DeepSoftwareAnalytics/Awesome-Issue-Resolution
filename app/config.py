from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / 'app'

DATA_DIR = APP_DIR / 'data'
DATABASE_DIR = DATA_DIR / 'database'
DATABASE_PATH = DATABASE_DIR / 'survey.db'
DATABASE_URL = f'sqlite:///{DATABASE_PATH}'

DOCS_DIR = APP_DIR / 'docs'
SITE_DIR = APP_DIR / 'site'
MODELS_DIR = APP_DIR / 'models'
SERVICES_DIR = APP_DIR / 'services'
CONTROLLERS_DIR = APP_DIR / 'controllers'
VIEW_DIR = APP_DIR / 'view'

ADMIN_DIR = VIEW_DIR / 'admin'
ADMIN_TEMPLATE_DIR = ADMIN_DIR / 'templates'
ADMIN_STATIC_DIR = ADMIN_DIR / 'static'

SCRIPTS_DIR = BASE_DIR / 'scripts'
PYTHON_SCRIPTS = {
    'migrate': DATABASE_DIR / 'migrate.py',
    'render_from_db': VIEW_DIR / 'render_from_db.py',
    'sync_readme': VIEW_DIR / 'sync_readme.py',
    'render_papers': VIEW_DIR / 'render_papers.py',
    'render_tables': VIEW_DIR / 'render_tables.py',
    'update_news': SCRIPTS_DIR / 'update_news.py',
    'export_admin_json': SCRIPTS_DIR / 'export_admin_json.py',
    'validate_tables': SCRIPTS_DIR / 'validate_tables.py',
}


def script(name: str) -> Path:
    return PYTHON_SCRIPTS[name]


API_PREFIX = '/api'
ADMIN_PREFIX = '/admin'

HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

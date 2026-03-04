"""
Application Configuration
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# Database configuration
DATABASE_PATH = BASE_DIR / 'database' / 'survey.db'
DATABASE_URL = f'sqlite:///{DATABASE_PATH}'

# Data directories
DATA_DIR = BASE_DIR / 'data'
DOCS_DIR = BASE_DIR / 'docs'
SITE_DIR = BASE_DIR / 'site'

# Admin interface
ADMIN_TEMPLATE_DIR = BASE_DIR / 'admin' / 'templates'
ADMIN_STATIC_DIR = BASE_DIR / 'admin' / 'static'

# API configuration
API_PREFIX = '/api'
ADMIN_PREFIX = '/admin'

# Server configuration
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

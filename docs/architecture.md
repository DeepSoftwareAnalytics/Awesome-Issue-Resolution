# System Architecture

## Overview

The Awesome Issue Resolution project uses an **MVC (Model-View-Controller)** architecture with Flask as the web framework and SQLite as the database backend.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Client Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Web Browser  │  │  API Client  │  │ CLI Scripts  │      │
│  │  (Admin UI)  │  │  (REST API)  │  │   (Tools)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────┬────────────────┬─────────────────┬────────────┘
             │                │                 │
             ▼                ▼                 ▼
┌─────────────────────────────────────────────────────────────┐
│                      Application Layer                       │
│                         (app.py)                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Flask Application Core                    │  │
│  │  • Unified entry point                                 │  │
│  │  • Blueprint registration                              │  │
│  │  • CORS configuration                                  │  │
│  │  • Static file serving                                 │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────┬────────────────┬─────────────────┬────────────┘
             │                │                 │
             ▼                ▼                 ▼
┌────────────────┐  ┌──────────────────┐  ┌─────────────────┐
│  Controllers/  │  │    Services/     │  │     Models/     │
│                │  │                  │  │                 │
│ • API Routes   │  │ • Sync Service   │  │ • Paper         │
│ • Admin Routes │  │ • ArXiv Service  │  │ • Dataset       │
│                │  │ • Business Logic │  │ • Method        │
└────────┬───────┘  └────────┬─────────┘  └────────┬────────┘
         │                   │                     │
         └───────────────────┴─────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   SQLite DB  │  │  YAML Files  │  │  CSV Files   │      │
│  │  (Primary)   │←→│  (Backup)    │←→│  (Backup)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Application Core (`app.py`)

**Responsibilities:**
- Initialize Flask application
- Register blueprints (controllers)
- Configure CORS
- Serve static site preview
- Entry point for development server

**Key Code:**
```python
from flask import Flask
from controllers.api_controller import api
from controllers.admin_controller import admin

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(admin)
```

### 2. Configuration (`config.py`)

**Responsibilities:**
- Centralize all configuration settings
- Define paths and directories
- Server settings (host, port, debug)

**Key Settings:**
```python
DATABASE_PATH = 'database/survey.db'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
```

### 3. Models Layer (`models/`)

**File Structure:**
```
models/
├── __init__.py         # Package exports
├── database.py         # DB engine, session, init
├── paper.py            # Paper model
├── dataset.py          # Dataset models (Eval, Training)
└── method.py           # Method models (SFT, RL, Foundation)
```

**Responsibilities:**
- Define database schema using SQLAlchemy ORM
- Provide data access methods
- Handle database connections

**Example Model:**
```python
class Paper(Base):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = Column(String)
    year = Column(Integer)
    ...
```

### 4. Controllers Layer (`controllers/`)

**File Structure:**
```
controllers/
├── __init__.py
├── api_controller.py       # REST API endpoints
└── admin_controller.py     # Admin interface routes
```

**Responsibilities:**
- Handle HTTP requests
- Validate input data
- Call services for business logic
- Return responses (JSON/HTML)

**Example Controller:**
```python
@api.route('/papers', methods=['GET'])
def get_papers():
    # Parse query params
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    
    # Call service/model
    session = get_session()
    query = session.query(Paper)
    if search:
        query = query.filter(Paper.title.contains(search))
    
    # Return JSON response
    return jsonify({
        'items': [p.to_dict() for p in query.all()],
        'total': query.count()
    })
```

### 5. Services Layer (`services/`)

**File Structure:**
```
services/
├── __init__.py
└── sync_service.py         # DB ↔ YAML/CSV sync
```

**Responsibilities:**
- Complex business logic
- Data transformation
- External API integration
- File I/O operations

**Example Service:**
```python
def export_papers_to_yaml():
    """Export paper data to YAML files"""
    session = get_session()
    papers = session.query(Paper).all()
    
    # Group by category
    by_category = {}
    for paper in papers:
        category = paper.category or 'Uncategorized'
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(paper.to_yaml_dict())
    
    # Write to YAML files
    for category, papers in by_category.items():
        filename = f'data/papers_{category.lower().replace(" ", "_")}.yaml'
        with open(filename, 'w') as f:
            yaml.dump(papers, f)
```

### 6. View Layer (`admin/`)

**File Structure:**
```
admin/
├── templates/
│   └── papers.html         # HTML templates
└── static/
    ├── css/                # Stylesheets
    ├── js/
    │   └── admin.js        # Frontend logic
    └── images/             # Assets
```

**Responsibilities:**
- Render HTML pages
- Handle user interactions
- Call API endpoints
- Update UI dynamically

**Example Frontend Code:**
```javascript
async function loadPapers() {
    const response = await fetch('/api/papers');
    const data = await response.json();
    renderTable(data.items);
}

async function updatePaper(id, updates) {
    const response = await fetch(`/api/papers/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates)
    });
    return await response.json();
}
```

---

## Data Flow Diagrams

### 1. Read Operation (GET)

```
User Request → Admin Controller → Models → Database
                                     ↓
                              Query Results
                                     ↓
                              JSON Response
                                     ↓
User Browser ← Admin Controller ← Format Data
```

### 2. Write Operation (POST/PUT)

```
User Input → Admin UI (JS) → API Controller → Validate
                                    ↓
                              Models → Database
                                    ↓
                              Success Response
                                    ↓
Admin UI ← Updated Data ← API Controller
```

### 3. Data Synchronization

```
Database Records
      ↓
Sync Service (services/sync_service.py)
      ↓
  ┌───┴───┐
  ↓       ↓
YAML    CSV
Files   Files
```

---

## Design Patterns

### 1. MVC Pattern
- **Model**: Database schema and data access
- **View**: HTML templates and frontend JavaScript
- **Controller**: Request routing and response handling

### 2. Blueprint Pattern (Flask)
- Modular route registration
- Clean separation of API and admin routes
- Easy to add new blueprints

### 3. Repository Pattern
- Models abstract database access
- `get_session()` provides database sessions
- Clean separation from business logic

### 4. Service Layer Pattern
- Complex logic moved to services
- Reusable across controllers
- Easier to test

---

## Database Schema

### Core Tables

```sql
-- Papers table
CREATE TABLE papers (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT,
    venue TEXT,
    year INTEGER,
    month TEXT,
    category TEXT,
    arxiv_link TEXT,
    doi_link TEXT,
    github_links TEXT,
    huggingface_links TEXT,
    ...
);

-- FTS5 index for full-text search
CREATE VIRTUAL TABLE papers_fts USING fts5(
    title, authors, venue, content='papers'
);
```

### Relationships

```
Papers (1:N with links stored as JSON/CSV strings)
Datasets (Eval/Training)
Methods (SFT/RL/Foundation)
```

---

## Security Architecture

### Current Implementation (Development)
- ❌ No authentication
- ❌ No authorization
- ✅ CORS enabled for all origins
- ✅ Debug mode enabled

### Production Recommendations

```python
# Add authentication middleware
from flask_login import LoginManager, login_required

# Add rate limiting
from flask_limiter import Limiter

# Disable debug mode
DEBUG = False

# Restrict CORS
CORS(app, origins=['https://trusted-domain.com'])

# Use production WSGI server
# gunicorn app:app -w 4 -b 0.0.0.0:5000
```

---

## Performance Considerations

### Current Optimizations
1. **Database Indexes**: FTS5 for full-text search
2. **Pagination**: API returns paginated results
3. **Lazy Loading**: Frontend loads data on demand
4. **Efficient Queries**: SQLAlchemy query optimization

### Future Improvements
1. Add Redis caching for API responses
2. Implement query result caching
3. Use CDN for static assets
4. Add database connection pooling
5. Implement lazy loading for large datasets

---

## Scalability

### Current Capacity
- **Records**: Handles 10,000+ records efficiently
- **Concurrent Users**: 10-50 (Flask development server)
- **Database Size**: ~10 MB (SQLite limit: 281 TB)

### Scaling Options

**1. Horizontal Scaling:**
```
Load Balancer
     │
     ├─── Flask Instance 1
     ├─── Flask Instance 2
     └─── Flask Instance 3
          │
     Shared Database (PostgreSQL)
```

**2. Vertical Scaling:**
- Upgrade to PostgreSQL/MySQL
- Use production WSGI server (Gunicorn)
- Add Redis for session/cache storage
- Implement database replication

---

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Vanilla JS, HTML5, CSS3 | User interface |
| **Visualization** | Chart.js | Data charts |
| **Web Framework** | Flask 3.x | HTTP server |
| **ORM** | SQLAlchemy 2.x | Database abstraction |
| **Database** | SQLite + FTS5 | Data storage & search |
| **Static Site** | MkDocs + Material | Documentation |
| **Deployment** | GitHub Pages | Static hosting |

---

## Development Workflow

### 1. Local Development

```bash
# Terminal 1: Start Flask server
python app.py

# Terminal 2: Preview static site
mkdocs serve

# Terminal 3: Run tests
python test_database.py
```

### 2. Adding New Features

**Add a new model:**
```python
# models/new_model.py
from models.database import Base

class NewModel(Base):
    __tablename__ = 'new_models'
    ...
```

**Add API endpoints:**
```python
# controllers/api_controller.py
@api.route('/new-models', methods=['GET'])
def get_new_models():
    ...
```

**Add admin page:**
```python
# controllers/admin_controller.py
@admin.route('/new-models')
def new_models_page():
    return render_template('new_models.html')
```

### 3. Testing

```bash
# Test imports
python -c "from models import Paper; print('OK')"

# Test database
python test_database.py

# Test API (with server running)
curl http://localhost:5000/api/stats
```

### 4. Deployment

```bash
# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy

# Or push to GitHub (auto-deploys)
git push origin main
```

---

## Error Handling Strategy

### API Errors
```python
@api.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

@api.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500
```

### Frontend Errors
```javascript
async function apiCall(url, options) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        showToast('Operation failed: ' + error.message, 'error');
        throw error;
    }
}
```

---

## Logging Strategy

### Current Implementation
```python
# Simple print statements
print("[INFO] Server starting...")
print("[OK] Database connected")
print("[ERROR] Failed to fetch data")
```

### Production Recommendation
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Server starting...")
```

---

## File Organization Philosophy

### Models (`models/`)
- **What**: Database schema definitions
- **When to edit**: Adding new data types, changing schema
- **Dependencies**: SQLAlchemy

### Controllers (`controllers/`)
- **What**: HTTP request handlers
- **When to edit**: Adding new endpoints, changing routes
- **Dependencies**: Flask, models

### Services (`services/`)
- **What**: Business logic and data operations
- **When to edit**: Complex operations, external integrations
- **Dependencies**: Models, external APIs

### Admin (`admin/`)
- **What**: User interface
- **When to edit**: UI changes, new features
- **Dependencies**: API endpoints

### Scripts (`scripts/`)
- **What**: Standalone utilities
- **When to edit**: Adding CLI tools, batch operations
- **Dependencies**: Models

---

## API Design Philosophy

### RESTful Principles
- Use HTTP methods correctly (GET, POST, PUT, DELETE)
- Use plural nouns for resources (`/papers` not `/paper`)
- Use status codes appropriately
- Return JSON for all API responses

### Endpoint Naming
```
GET    /api/papers          # List papers
GET    /api/papers/{id}     # Get paper by ID
POST   /api/papers          # Create paper
PUT    /api/papers/{id}     # Update paper
DELETE /api/papers/{id}     # Delete paper
```

### Response Format
```json
{
  "items": [...],           // For list endpoints
  "total": 188,
  "page": 1,
  "per_page": 10,
  "pages": 19
}
```

---

## Testing Strategy

### Unit Tests (Future)
```python
# tests/test_models.py
def test_paper_creation():
    paper = Paper(title="Test", year=2025)
    assert paper.title == "Test"

# tests/test_api.py
def test_get_papers(client):
    response = client.get('/api/papers')
    assert response.status_code == 200
```

### Integration Tests (Future)
```python
def test_paper_workflow(client, db):
    # Create
    response = client.post('/api/papers', json={...})
    paper_id = response.json['id']
    
    # Read
    response = client.get(f'/api/papers/{paper_id}')
    assert response.status_code == 200
    
    # Update
    response = client.put(f'/api/papers/{paper_id}', json={...})
    assert response.status_code == 200
    
    # Delete
    response = client.delete(f'/api/papers/{paper_id}')
    assert response.status_code == 200
```

---

## Deployment Architectures

### Development (Current)
```
Flask Dev Server (port 5000)
├── /admin → Admin UI
├── /api → REST API
└── / → Static site preview
```

### Production Option 1: Split Services
```
GitHub Pages (Static Site)
    - Public access
    - No backend needed
    
Internal Server (Admin + API)
    - Private network only
    - Authentication required
```

### Production Option 2: Unified with Auth
```
Nginx (Reverse Proxy)
    │
    ├─→ / (Static Site) → Served by Nginx
    │
    └─→ /admin, /api → Gunicorn (Flask)
                        - Authentication required
                        - Rate limiting enabled
```

---

## Key Architectural Decisions

### Why Flask?
- ✅ Lightweight and flexible
- ✅ Easy to learn and use
- ✅ Rich ecosystem (extensions)
- ✅ Perfect for small-to-medium projects

### Why SQLite?
- ✅ Zero configuration
- ✅ Single file database
- ✅ Built-in FTS5 for full-text search
- ✅ Sufficient for current scale
- ✅ Easy to backup/version control

### Why MVC?
- ✅ Industry-standard pattern
- ✅ Clear separation of concerns
- ✅ Easier to maintain and test
- ✅ Better code organization

### Why Keep Static Site?
- ✅ GitHub Pages is free
- ✅ No backend hosting cost
- ✅ Better SEO and performance
- ✅ Works offline (after download)

### Why Unified App?
- ✅ Single server for development
- ✅ Easier to deploy
- ✅ Consistent environment
- ✅ Simplified configuration

---

## Extension Points

### Adding a New Data Model

1. Create model file in `models/`:
```python
# models/author.py
from models.database import Base

class Author(Base):
    __tablename__ = 'authors'
    ...
```

2. Add to `models/__init__.py`:
```python
from .author import Author
```

3. Create migration:
```python
# database/migrate.py
def migrate_authors():
    ...
```

4. Add API endpoints:
```python
# controllers/api_controller.py
@api.route('/authors')
def get_authors():
    ...
```

5. Add admin page:
```python
# controllers/admin_controller.py
@admin.route('/authors')
def authors():
    return render_template('authors.html')
```

### Adding External Service Integration

```python
# services/external_service.py
import requests

def fetch_metadata(doi):
    """Fetch paper metadata from CrossRef API"""
    url = f'https://api.crossref.org/works/{doi}'
    response = requests.get(url)
    return response.json()
```

---

## Best Practices

### 1. Code Organization
- Keep files focused and small (<500 lines)
- One class per file for models
- Group related routes in controllers
- Put complex logic in services

### 2. Error Handling
- Always validate user input
- Use try-except for external API calls
- Return appropriate HTTP status codes
- Log errors for debugging

### 3. Database Operations
- Always use sessions properly
- Close sessions after use (`get_session()` handles this)
- Use transactions for multiple operations
- Add indexes for frequently queried fields

### 4. Frontend
- Use vanilla JavaScript (no framework overhead)
- Minimize dependencies
- Handle errors gracefully
- Show loading states

### 5. Documentation
- Keep architecture docs up-to-date
- Comment complex logic
- Maintain API documentation
- Write clear commit messages

---

## Monitoring and Debugging

### Development Mode
```python
# Flask debug mode provides:
- Auto-reload on code changes
- Detailed error pages
- Interactive debugger
```

### Production Monitoring (Future)
```python
# Add logging
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Add metrics
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)

# Add error tracking
from sentry_sdk import init as sentry_init
sentry_init(dsn='...')
```

---

## Summary

The refactored architecture provides:
- ✅ Clear separation of concerns
- ✅ Easier maintenance and testing
- ✅ Better scalability
- ✅ Improved developer experience
- ✅ Production-ready structure
- ✅ Backward compatible with existing workflows

For detailed API documentation, see `docs/api.md`.  
For refactoring details, see `REFACTORING_SUMMARY.md`.  
For quick start guide, see `QUICKSTART.md`.

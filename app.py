#!/usr/bin/env python3
"""
Awesome Issue Resolution - Unified Application Server
MVC Architecture: Flask app serving both admin interface and API
"""
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from pathlib import Path
import config

# Initialize Flask app
app = Flask(
    __name__,
    template_folder=str(config.ADMIN_TEMPLATE_DIR),
    static_folder=str(config.ADMIN_STATIC_DIR),
    static_url_path='/admin/static'
)
CORS(app)

# Register blueprints
from controllers.api_controller import api
from controllers.admin_controller import admin as admin_bp
app.register_blueprint(api)
app.register_blueprint(admin_bp)


# Admin routes are handled by admin_controller blueprint


# ============================================================================
# Static Site Preview (Local development only)
# ============================================================================

@app.route('/')
def home():
    """Serve static site homepage"""
    try:
        return send_from_directory(config.SITE_DIR, 'index.html')
    except:
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
    # Try exact path first (e.g. stylesheets/extra.css, images/logo.png)
    if (site / path).is_file():
        return send_from_directory(site, path)
    # For directory-style URLs (e.g. /paper/ or /paper), serve index.html
    for candidate in [path.rstrip('/') + '/index.html', path + '/index.html']:
        if (site / candidate).is_file():
            return send_from_directory(site, candidate)
    # Last resort: let send_from_directory raise its own 404
    try:
        return send_from_directory(site, path)
    except Exception:
        # Serve mkdocs 404 page if available
        if (site / '404.html').is_file():
            return send_from_directory(site, '404.html'), 404
        return "Not found", 404


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("  Awesome Issue Resolution - Database Management System")
    print("="*70)
    print(f"\n[SERVER] Starting at http://localhost:{config.PORT}")
    print(f"[ADMIN] Admin Interface: http://localhost:{config.PORT}/admin")
    print(f"[API] API Endpoint: http://localhost:{config.PORT}/api/stats")
    print(f"[SITE] Static Site: http://localhost:{config.PORT}/\n")
    
    app.run(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT
    )

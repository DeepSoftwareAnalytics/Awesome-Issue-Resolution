"""
API Controller
REST API endpoints for survey database
"""
from flask import Blueprint, jsonify, request
from sqlalchemy import or_, func, desc
import subprocess
import os
from models import Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel, get_session

api = Blueprint('api', __name__, url_prefix='/api')
session = get_session()


# ============================================================================
# Helper Functions
# ============================================================================

def paginate(query, page=1, per_page=50):
    """Paginate query results"""
    total = query.count()
    items = query.limit(per_page).offset((page - 1) * per_page).all()
    return {
        'items': [item.to_dict() for item in items],
        'total': total,
        'page': page,
        'per_page': per_page,
        'pages': (total + per_page - 1) // per_page
    }


# ============================================================================
# Papers API
# ============================================================================

@api.route('/papers', methods=['GET'])
def get_papers():
    """Get all papers with optional filters"""
    query = session.query(Paper)

    # Filters
    category = request.args.get('category')
    year = request.args.get('year')
    month = request.args.get('month')
    search = request.args.get('search')

    if category:
        query = query.filter(
            or_(
                Paper.category == category,
                Paper.category.like(f'{category},%'),
                Paper.category.like(f'%,{category}'),
                Paper.category.like(f'%,{category},%')
            )
        )

    if year:
        query = query.filter(Paper.month.like(f'{year}-%'))

    if month:
        query = query.filter(Paper.month == month)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Paper.title.like(search_term),
                Paper.authors.like(search_term),
                Paper.short_name.like(search_term),
                Paper.venue.like(search_term)
            )
        )

    # Sorting — default: newest first by month (YYYY-MM string sorts correctly)
    sort_by = request.args.get('sort_by', 'month')
    sort_order = request.args.get('sort_order', 'desc')

    if sort_by in ('year', 'month'):
        # Sort nulls last: papers without a month fall to the bottom
        if sort_order == 'desc':
            query = query.order_by(Paper.month.is_(None), desc(Paper.month))
        else:
            query = query.order_by(Paper.month.isnot(None), Paper.month)
    elif sort_by == 'title':
        query = query.order_by(desc(Paper.title) if sort_order == 'desc' else Paper.title)

    # Pagination
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/papers/<int:paper_id>', methods=['GET'])
def get_paper(paper_id):
    """Get a single paper by ID"""
    paper = session.query(Paper).get(paper_id)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404
    return jsonify(paper.to_dict())


@api.route('/papers', methods=['POST'])
def create_paper():
    """Create a new paper"""
    data = request.json

    try:
        # Derive year from month (YYYY-MM) if not explicitly provided
        month_val = data.get('month') or ''
        year_val = data.get('year')
        if not year_val and month_val and len(month_val) >= 4:
            try:
                year_val = int(month_val[:4])
            except ValueError:
                pass

        paper = Paper(
            short_name=data['short_name'],
            title=data['title'],
            authors=data['authors'],
            year=year_val,
            month=month_val or None,
            venue=data['venue'],
            category=data['category'],
            abstract=data.get('abstract'),
            arxiv_link=data.get('arxiv_link'),
            github_link=data.get('github_link'),
            huggingface_link=data.get('huggingface_link'),
            website_link=data.get('website_link'),
            doi_link=data.get('doi_link'),
            openreview_link=data.get('openreview_link')
        )
        session.add(paper)
        session.commit()
        return jsonify(paper.to_dict()), 201
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/papers/<int:paper_id>', methods=['PUT'])
def update_paper(paper_id):
    """Update a paper"""
    paper = session.query(Paper).get(paper_id)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404

    data = request.json

    try:
        for key, value in data.items():
            if hasattr(paper, key):
                setattr(paper, key, value)

        # If month is updated, automatically update year
        if 'month' in data and data['month']:
            month_value = data['month']
            if '-' in month_value:
                year_from_month = int(month_value.split('-')[0])
                paper.year = year_from_month

        session.commit()
        return jsonify(paper.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/papers/<int:paper_id>/toggle-featured', methods=['POST'])
def toggle_featured(paper_id):
    """Toggle the featured flag on a paper"""
    paper = session.query(Paper).get(paper_id)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404
    try:
        paper.featured = not bool(paper.featured)
        session.commit()
        return jsonify({'id': paper.id, 'featured': bool(paper.featured)})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/papers/<int:paper_id>', methods=['DELETE'])
def delete_paper(paper_id):
    """Delete a paper"""
    paper = session.query(Paper).get(paper_id)
    if not paper:
        return jsonify({'error': 'Paper not found'}), 404

    try:
        session.delete(paper)
        session.commit()
        return jsonify({'message': 'Paper deleted'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# Datasets API
# ============================================================================

@api.route('/datasets', methods=['GET'])
def get_datasets():
    """Get all datasets with optional filters"""
    query = session.query(Dataset)

    # Filters
    language = request.args.get('language')
    category = request.args.get('category')
    search = request.args.get('search')

    if language:
        query = query.filter(Dataset.language.like(f"%{language}%"))

    if category:
        query = query.filter(Dataset.category == category)

    if search:
        search_term = f"%{search}%"
        query = query.filter(Dataset.name.like(search_term))

    # Pagination
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/datasets/<int:dataset_id>', methods=['GET'])
def get_dataset(dataset_id):
    """Get a single dataset by ID"""
    dataset = session.query(Dataset).get(dataset_id)
    if not dataset:
        return jsonify({'error': 'Dataset not found'}), 404
    return jsonify(dataset.to_dict())


@api.route('/datasets/<int:dataset_id>', methods=['PUT'])
def update_dataset(dataset_id):
    dataset = session.query(Dataset).get(dataset_id)
    if not dataset:
        return jsonify({'error': 'Dataset not found'}), 404
    data = request.json
    try:
        for key, value in data.items():
            if hasattr(dataset, key):
                setattr(dataset, key, value)
        session.commit()
        return jsonify(dataset.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/datasets/<int:dataset_id>', methods=['DELETE'])
def delete_dataset(dataset_id):
    dataset = session.query(Dataset).get(dataset_id)
    if not dataset:
        return jsonify({'error': 'Dataset not found'}), 404
    try:
        session.delete(dataset)
        session.commit()
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# Training Datasets API
# ============================================================================

@api.route('/training-datasets', methods=['GET'])
def get_training_datasets():
    """Get all training datasets"""
    query = session.query(TrainingDataset)

    search = request.args.get('search')
    if search:
        search_term = f"%{search}%"
        query = query.filter(TrainingDataset.name.like(search_term))

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/training-datasets/<int:item_id>', methods=['GET'])
def get_training_dataset(item_id):
    item = session.query(TrainingDataset).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(item.to_dict())


@api.route('/training-datasets/<int:item_id>', methods=['PUT'])
def update_training_dataset(item_id):
    item = session.query(TrainingDataset).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    try:
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        session.commit()
        return jsonify(item.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/training-datasets/<int:item_id>', methods=['DELETE'])
def delete_training_dataset(item_id):
    item = session.query(TrainingDataset).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    try:
        session.delete(item)
        session.commit()
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# SFT Methods API
# ============================================================================

@api.route('/sft-methods', methods=['GET'])
def get_sft_methods():
    """Get all SFT methods with optional filters"""
    query = session.query(SFTMethod)

    # Filters
    search = request.args.get('search')
    min_resolution = request.args.get('min_resolution')

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                SFTMethod.model_name.like(search_term),
                SFTMethod.base_model.like(search_term)
            )
        )

    if min_resolution:
        query = query.filter(SFTMethod.resolution_percent >= float(min_resolution))

    # Sort by resolution (descending)
    query = query.order_by(desc(SFTMethod.resolution_percent))

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/sft-methods/<int:item_id>', methods=['GET'])
def get_sft_method(item_id):
    item = session.query(SFTMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(item.to_dict())


@api.route('/sft-methods/<int:item_id>', methods=['PUT'])
def update_sft_method(item_id):
    item = session.query(SFTMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    try:
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        session.commit()
        return jsonify(item.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/sft-methods/<int:item_id>', methods=['DELETE'])
def delete_sft_method(item_id):
    item = session.query(SFTMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    try:
        session.delete(item)
        session.commit()
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# RL Methods API
# ============================================================================

@api.route('/rl-methods', methods=['GET'])
def get_rl_methods():
    """Get all RL methods with optional filters"""
    query = session.query(RLMethod)

    # Filters
    search = request.args.get('search')
    min_resolution = request.args.get('min_resolution')
    reward_type = request.args.get('reward_type')

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                RLMethod.model_name.like(search_term),
                RLMethod.base_model.like(search_term)
            )
        )

    if min_resolution:
        query = query.filter(RLMethod.resolution_percent >= float(min_resolution))

    if reward_type:
        query = query.filter(RLMethod.reward_type == reward_type)

    # Sort by resolution (descending)
    query = query.order_by(desc(RLMethod.resolution_percent))

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/rl-methods/<int:item_id>', methods=['GET'])
def get_rl_method(item_id):
    item = session.query(RLMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(item.to_dict())


@api.route('/rl-methods/<int:item_id>', methods=['PUT'])
def update_rl_method(item_id):
    item = session.query(RLMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    try:
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        session.commit()
        return jsonify(item.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/rl-methods/<int:item_id>', methods=['DELETE'])
def delete_rl_method(item_id):
    item = session.query(RLMethod).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    try:
        session.delete(item)
        session.commit()
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# Foundation Models API
# ============================================================================

@api.route('/foundation-models', methods=['GET'])
def get_foundation_models():
    """Get all foundation models with optional filters"""
    query = session.query(FoundationModel)

    # Filters
    search = request.args.get('search')
    min_resolution = request.args.get('min_resolution')

    if search:
        search_term = f"%{search}%"
        query = query.filter(FoundationModel.model_name.like(search_term))

    if min_resolution:
        query = query.filter(FoundationModel.resolution_percent >= float(min_resolution))

    # Sort by resolution (descending)
    query = query.order_by(desc(FoundationModel.resolution_percent))

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))

    return jsonify(paginate(query, page, per_page))


@api.route('/foundation-models/<int:item_id>', methods=['GET'])
def get_foundation_model(item_id):
    item = session.query(FoundationModel).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(item.to_dict())


@api.route('/foundation-models/<int:item_id>', methods=['PUT'])
def update_foundation_model(item_id):
    item = session.query(FoundationModel).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    try:
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        session.commit()
        return jsonify(item.to_dict())
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


@api.route('/foundation-models/<int:item_id>', methods=['DELETE'])
def delete_foundation_model(item_id):
    item = session.query(FoundationModel).get(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    try:
        session.delete(item)
        session.commit()
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400


# ============================================================================
# Statistics API
# ============================================================================

# Category groups that map to the three survey sections
DATA_CATS     = {'evaluation_datasets', 'training_datasets', 'data_collection', 'data_synthesis'}
METHODS_CATS  = {'sft', 'rl', 'single_agent', 'multi_agent', 'tool', 'workflow', 'memory', 'inference_scaling'}
ANALYSIS_CATS = {'data_analysis', 'methods_analysis'}


def _count_papers_matching_cats(cat_set):
    """Count papers whose (possibly comma-separated) category field overlaps with cat_set."""
    total = 0
    rows = session.query(Paper.category).all()
    for (cat_str,) in rows:
        if not cat_str:
            continue
        tags = {t.strip() for t in cat_str.split(',')}
        if tags & cat_set:
            total += 1
    return total


@api.route('/stats', methods=['GET'])
def get_stats():
    """Get database statistics"""
    stats = {
        'papers': {
            'total': session.query(Paper).count(),
            'data_total': _count_papers_matching_cats(DATA_CATS),
            'methods_total': _count_papers_matching_cats(METHODS_CATS),
            'analysis_total': _count_papers_matching_cats(ANALYSIS_CATS),
            'by_category': {},
            'by_year': {},
            'by_month': {}
        },
        'datasets': {
            'total': session.query(Dataset).count(),
            'by_language': {},
            'by_category': {}
        },
        'methods': {
            'sft_total': session.query(SFTMethod).count(),
            'rl_total': session.query(RLMethod).count(),
            'foundation_total': session.query(FoundationModel).count()
        }
    }

    # Papers by category
    paper_categories = session.query(
        Paper.category, func.count(Paper.id)
    ).group_by(Paper.category).all()
    stats['papers']['by_category'] = {cat: count for cat, count in paper_categories}

    # Papers by year
    paper_years = session.query(
        Paper.year, func.count(Paper.id)
    ).group_by(Paper.year).order_by(Paper.year).all()
    stats['papers']['by_year'] = {year: count for year, count in paper_years}

    # Papers by month
    paper_months = session.query(
        Paper.month, func.count(Paper.id)
    ).filter(Paper.month.isnot(None)).group_by(Paper.month).order_by(Paper.month).all()
    stats['papers']['by_month'] = {month: count for month, count in paper_months if month}

    # Datasets by language
    dataset_languages = session.query(
        Dataset.language, func.count(Dataset.id)
    ).group_by(Dataset.language).all()
    stats['datasets']['by_language'] = {lang: count for lang, count in dataset_languages if lang}

    # Datasets by category
    dataset_categories = session.query(
        Dataset.category, func.count(Dataset.id)
    ).group_by(Dataset.category).all()
    stats['datasets']['by_category'] = {cat: count for cat, count in dataset_categories if cat}

    return jsonify(stats)


@api.route('/stats/filtered', methods=['GET'])
def get_stats_filtered():
    """Get by_month paper counts for a filtered paper set"""
    query = session.query(Paper)

    year = request.args.get('year')
    category = request.args.get('category')
    search = request.args.get('search')

    if year:
        query = query.filter(Paper.month.like(f'{year}-%'))

    if category:
        query = query.filter(
            or_(
                Paper.category == category,
                Paper.category.like(f'{category},%'),
                Paper.category.like(f'%,{category},%'),
                Paper.category.like(f'%,{category}'),
            )
        )

    if search:
        term = f'%{search}%'
        query = query.filter(
            or_(
                Paper.title.like(term),
                Paper.short_name.like(term),
                Paper.authors.like(term),
            )
        )

    query = query.filter(Paper.month.isnot(None))

    paper_months = session.query(
        Paper.month, func.count(Paper.id)
    ).filter(
        Paper.month.isnot(None)
    )

    # Re-apply same filters on the aggregation query
    if year:
        paper_months = paper_months.filter(Paper.month.like(f'{year}-%'))
    if category:
        paper_months = paper_months.filter(
            or_(
                Paper.category == category,
                Paper.category.like(f'{category},%'),
                Paper.category.like(f'%,{category},%'),
                Paper.category.like(f'%,{category}'),
            )
        )
    if search:
        term = f'%{search}%'
        paper_months = paper_months.filter(
            or_(
                Paper.title.like(term),
                Paper.short_name.like(term),
                Paper.authors.like(term),
            )
        )

    paper_months = paper_months.group_by(Paper.month).order_by(Paper.month).all()
    by_month = {month: count for month, count in paper_months if month}

    return jsonify({'by_month': by_month})


# ============================================================================
# Search API
# ============================================================================

@api.route('/search', methods=['GET'])
def search():
    """Global search across all tables"""
    query_text = request.args.get('q', '')
    if not query_text:
        return jsonify({'results': []})

    results = {
        'papers': [],
        'datasets': [],
        'methods': []
    }

    search_term = f"%{query_text}%"

    # Search papers
    papers = session.query(Paper).filter(
        or_(
            Paper.title.like(search_term),
            Paper.authors.like(search_term),
            Paper.short_name.like(search_term)
        )
    ).limit(10).all()
    results['papers'] = [p.to_dict() for p in papers]

    # Search datasets
    datasets = session.query(Dataset).filter(
        Dataset.name.like(search_term)
    ).limit(10).all()
    results['datasets'] = [d.to_dict() for d in datasets]

    # Search methods
    sft_methods = session.query(SFTMethod).filter(
        SFTMethod.model_name.like(search_term)
    ).limit(5).all()
    rl_methods = session.query(RLMethod).filter(
        RLMethod.model_name.like(search_term)
    ).limit(5).all()
    results['methods'] = [m.to_dict() for m in sft_methods + rl_methods]

    return jsonify(results)


# ============================================================================
# Sync Endpoints
# ============================================================================

@api.route('/sync-to-data', methods=['POST'])
def sync_to_data():
    """Export database to YAML/CSV files"""
    try:
        # Import sync service functions
        from services.sync_service import (
            export_papers_to_yaml, export_datasets_to_csv,
            export_training_datasets_to_csv, export_sft_methods_to_csv,
            export_rl_methods_to_csv, export_foundation_models_to_csv
        )
        
        # Execute export functions
        export_papers_to_yaml()
        export_datasets_to_csv()
        export_training_datasets_to_csv()
        export_sft_methods_to_csv()
        export_rl_methods_to_csv()
        export_foundation_models_to_csv()
        
        return jsonify({
            'success': True,
            'message': 'Data exported successfully to YAML/CSV files'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@api.route('/import-from-data', methods=['POST'])
def import_from_data():
    """Import data from YAML/CSV files to database"""
    try:
        result = subprocess.run(
            ['python', 'database/migrate.py'],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Data imported successfully from YAML/CSV files'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.stderr
            }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@api.route('/fetch-arxiv', methods=['POST'])
def fetch_arxiv():
    """Fetch paper information from arXiv link"""
    try:
        data = request.get_json()
        arxiv_link = data.get('arxiv_link', '')
        
        if not arxiv_link:
            return jsonify({'error': 'arXiv link is required'}), 400
        
        # Extract arXiv ID
        import re
        arxiv_id_match = re.search(r'(\d{4}\.\d{4,5})', arxiv_link)
        if not arxiv_id_match:
            return jsonify({'error': 'Invalid arXiv link'}), 400
        
        arxiv_id = arxiv_id_match.group(1)
        
        # Fetch from arXiv API
        import requests
        import xml.etree.ElementTree as ET
        
        api_url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
        response = requests.get(api_url, timeout=10)
        
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch from arXiv'}), 500
        
        # Parse XML
        root = ET.fromstring(response.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entry = root.find('atom:entry', ns)
        if entry is None:
            return jsonify({'error': 'Paper not found on arXiv'}), 404
        
        # Extract information
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        
        authors = []
        for author in entry.findall('atom:author', ns):
            name = author.find('atom:name', ns).text
            authors.append(name)
        
        published = entry.find('atom:published', ns).text[:10]  # YYYY-MM-DD
        year = published[:4]
        month = published[:7]  # YYYY-MM
        
        # Generate venue
        venue = f'arXiv preprint arXiv:{arxiv_id}'
        
        return jsonify({
            'title': title,
            'authors': ', '.join(authors),
            'venue': venue,
            'year': int(year),
            'month': month,
            'arxiv_link': f'https://arxiv.org/abs/{arxiv_id}'
        })
        
    except requests.Timeout:
        return jsonify({'error': 'Request timeout'}), 408
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@api.route('/build-website', methods=['POST'])
def build_website():
    """Run mkdocs build"""
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=project_root
        )

        if result.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Website built successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.stderr or result.stdout or 'Build failed'
            }), 500
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Build timed out'
        }), 504
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@api.route('/render-from-db', methods=['POST'])
def render_from_db():
    """Run view/render_from_db.py"""
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        script_path = os.path.join(project_root, 'view', 'render_from_db.py')

        result = subprocess.run(
            ['python', script_path],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=project_root
        )

        if result.returncode == 0:
            return jsonify({
                'success': True,
                'message': 'Rendered from database successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': result.stderr or result.stdout or 'Render failed'
            }), 500
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Render timed out'
        }), 504
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

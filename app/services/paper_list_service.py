import re
from collections import Counter
from pathlib import Path

import yaml
from sqlalchemy import desc, or_, func, literal

from models import Paper


DEFAULT_PRIORITIES = ['arxiv', 'openreview', 'doi', 'website', 'github', 'huggingface']


def parse_int(value, default=None):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def normalize_arxiv_link(link):
    if not link:
        return ''
    return re.sub(r'arxiv\.org/(abs|html)/', 'arxiv.org/pdf/', link)


def parse_priorities(raw):
    if isinstance(raw, str):
        items = raw.split(',')
    else:
        items = raw or []
    priorities = [p.strip().lower() for p in items if p and p.strip().lower() in DEFAULT_PRIORITIES]
    return priorities or DEFAULT_PRIORITIES


def select_primary_link(links, priorities):
    for key in priorities:
        value = (links or {}).get(key) or ''
        if not value:
            continue
        if key == 'arxiv':
            return normalize_arxiv_link(value)
        return value
    return ''


def build_agent_markdown(items, q):
    lines = [
        '## Paper Context Bundle',
        f'Query: {q or "N/A"}',
        f'Count: {len(items)}',
        '',
        '### Papers'
    ]
    for idx, item in enumerate(items, 1):
        lines.append(f"{idx}. **{item['short_name']}** ({item.get('month') or item.get('year') or 'N/A'})")
        lines.append(f"   - Title: {item['title']}")
        lines.append(f"   - Authors: {item['authors']}")
        lines.append(f"   - Category: {item.get('category') or ''}")
        lines.append(f"   - Primary Link: {item.get('primary_link') or ''}")
    return '\n'.join(lines)


def build_filtered_paper_query(session, q='', category='', year_from=None, year_to=None):
    query = session.query(Paper)
    if q:
        term = f'%{q}%'
        query = query.filter(
            or_(
                Paper.title.like(term),
                Paper.authors.like(term),
                Paper.short_name.like(term),
                Paper.venue.like(term),
                Paper.abstract.like(term)
            )
        )

    if category:
        cats = [c.strip() for c in category.split(',') if c.strip()]
        if cats:
            normalized_db_category = func.replace(func.coalesce(Paper.category, ''), ' ', '')
            wrapped = literal(',') + normalized_db_category + literal(',')
            query = query.filter(or_(*[wrapped.like(f'%,{cat},%') for cat in cats]))

    if year_from is not None:
        query = query.filter(Paper.year >= year_from)
    if year_to is not None:
        query = query.filter(Paper.year <= year_to)
    return query


def get_paper_list_payload(session, q='', category='', year_from=None, year_to=None, top_k=20, link_priority=None):
    top_k = max(1, min(parse_int(top_k, 20), 200))
    priorities = parse_priorities(link_priority)

    query = build_filtered_paper_query(
        session=session,
        q=q,
        category=category,
        year_from=parse_int(year_from),
        year_to=parse_int(year_to)
    )
    papers = query.order_by(desc(Paper.featured), Paper.month.is_(None), desc(Paper.month), desc(Paper.id)).limit(top_k).all()

    items = []
    links = []
    seen = set()
    for paper in papers:
        data = paper.to_dict()
        primary_link = select_primary_link(data.get('links') or {}, priorities)
        item = {
            'id': data.get('id'),
            'short_name': data.get('short_name'),
            'title': data.get('title'),
            'authors': data.get('authors'),
            'year': data.get('year'),
            'month': data.get('month'),
            'venue': data.get('venue'),
            'category': data.get('category'),
            'featured': data.get('featured', False),
            'primary_link': primary_link,
            'links': data.get('links') or {}
        }
        items.append(item)
        if primary_link and primary_link not in seen:
            seen.add(primary_link)
            links.append(primary_link)

    return {
        'query': {
            'q': q or '',
            'category': category or '',
            'year_from': parse_int(year_from),
            'year_to': parse_int(year_to),
            'top_k': top_k,
            'link_priority': priorities
        },
        'count': len(items),
        'items': items,
        'links': links,
        'context_markdown': build_agent_markdown(items, q)
    }


def get_paper_redundancy_report(session, data_dir='data'):
    db_rows = session.query(Paper.short_name, Paper.title).all()
    db_short_names = [r[0] for r in db_rows if r[0]]
    db_titles = [r[1].strip().lower() for r in db_rows if r[1]]

    db_short_name_dups = sorted([name for name, count in Counter(db_short_names).items() if count > 1])
    db_title_dups = sorted([title for title, count in Counter(db_titles).items() if count > 1])

    local_short_names = []
    local_titles = []
    yaml_files = sorted(Path(data_dir).glob('papers_*.yaml'))
    for file_path in yaml_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            rows = yaml.safe_load(f) or []
        for row in rows:
            short_name = (row.get('short_name') or '').strip()
            title = (row.get('title') or '').strip().lower()
            if short_name:
                local_short_names.append(short_name)
            if title:
                local_titles.append(title)

    local_short_name_dups = sorted([name for name, count in Counter(local_short_names).items() if count > 1])
    local_title_dups = sorted([title for title, count in Counter(local_titles).items() if count > 1])

    db_set = set(db_short_names)
    local_set = set(local_short_names)
    only_in_db = sorted(db_set - local_set)
    only_in_local = sorted(local_set - db_set)

    return {
        'db': {
            'paper_count': len(db_rows),
            'duplicate_short_names': db_short_name_dups,
            'duplicate_titles': db_title_dups
        },
        'local': {
            'yaml_file_count': len(yaml_files),
            'paper_count': len(local_short_names),
            'duplicate_short_names': local_short_name_dups,
            'duplicate_titles': local_title_dups
        },
        'drift': {
            'only_in_db': only_in_db,
            'only_in_local': only_in_local,
            'only_in_db_count': len(only_in_db),
            'only_in_local_count': len(only_in_local)
        }
    }

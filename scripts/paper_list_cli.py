#!/usr/bin/env python3
import argparse
import csv
import json
import sys
from io import StringIO
from pathlib import Path
from sqlalchemy import desc

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
APP_ROOT = ROOT / 'app'
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from models import Paper, get_session
from services.paper_list_service import (
    build_filtered_paper_query,
    get_paper_list_payload,
    get_paper_redundancy_report,
    parse_priorities,
    select_primary_link,
)


NOTEBOOKLM_PROMPT = """You are a rigorous research synthesis assistant.
Use only the sources in this notebook to answer questions.
When citing evidence, quote exact claims and provide the corresponding source URL.
If evidence is insufficient or conflicting, explicitly say so and list what is missing.
Prefer structured outputs: summary, key findings, disagreements, and open questions."""


def build_csv_output(items):
    buffer = StringIO()
    writer = csv.writer(buffer, lineterminator='\n')
    writer.writerow([
        'id', 'short_name', 'title', 'authors', 'year', 'month', 'venue',
        'category', 'featured', 'primary_link', 'arxiv_link', 'openreview_link',
        'doi_link', 'website_link', 'github_link', 'huggingface_link', 'abstract'
    ])
    for item in items:
        links = item.get('links') or {}
        writer.writerow([
            item.get('id'),
            item.get('short_name') or '',
            item.get('title') or '',
            item.get('authors') or '',
            item.get('year') or '',
            item.get('month') or '',
            item.get('venue') or '',
            item.get('category') or '',
            bool(item.get('featured')),
            item.get('primary_link') or '',
            links.get('arxiv') or '',
            links.get('openreview') or '',
            links.get('doi') or '',
            links.get('website') or '',
            links.get('github') or '',
            links.get('huggingface') or '',
            item.get('abstract') or ''
        ])
    return buffer.getvalue()


def split_links(value):
    if not value:
        return []
    return [part.strip() for part in str(value).split(',') if part.strip()]


def build_notebooklm_txt_output(items):
    all_links = []
    seen = set()
    for item in items:
        links = item.get('links') or {}
        candidates = []
        for key in ('arxiv', 'openreview', 'doi', 'website', 'github', 'huggingface'):
            candidates.extend(split_links(links.get(key)))
        for link in candidates:
            if link not in seen:
                seen.add(link)
                all_links.append(link)
    lines = [NOTEBOOKLM_PROMPT, '', 'SOURCE LINKS']
    lines.extend(all_links)
    return '\n'.join(lines)


def get_filtered_items(session, args):
    priorities = parse_priorities(args.link_priority)
    query = build_filtered_paper_query(
        session=session,
        q=args.q,
        category=args.category,
        year_from=args.year_from,
        year_to=args.year_to
    ).order_by(desc(Paper.featured), Paper.month.is_(None), desc(Paper.month), desc(Paper.id))
    if not args.all:
        query = query.limit(max(1, args.top_k))
    papers = query.all()

    items = []
    for paper in papers:
        data = paper.to_dict()
        data['primary_link'] = select_primary_link(data.get('links') or {}, priorities)
        items.append(data)
    return items


def main():
    parser = argparse.ArgumentParser(prog='paper-list-cli')
    parser.add_argument('--q', default='')
    parser.add_argument('--category', default='')
    parser.add_argument('--year-from', dest='year_from', default=None)
    parser.add_argument('--year-to', dest='year_to', default=None)
    parser.add_argument('--top-k', dest='top_k', default=20, type=int)
    parser.add_argument('--format', choices=['json', 'markdown', 'links', 'csv', 'notebooklm_txt'], default='json')
    parser.add_argument('--link-priority', default='arxiv,openreview,doi,website,github,huggingface')
    parser.add_argument('--redundancy-report', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--output', default='')
    args = parser.parse_args()

    session = get_session()
    if args.redundancy_report:
        result = get_paper_redundancy_report(session=session)
        output = json.dumps(result, ensure_ascii=False, indent=2)
    elif args.format in ('csv', 'notebooklm_txt'):
        items = get_filtered_items(session, args)
        if args.format == 'csv':
            output = build_csv_output(items)
        else:
            output = build_notebooklm_txt_output(items)
    else:
        result = get_paper_list_payload(
            session=session,
            q=args.q,
            category=args.category,
            year_from=args.year_from,
            year_to=args.year_to,
            top_k=args.top_k,
            link_priority=args.link_priority
        )
        if args.format == 'markdown':
            output = result['context_markdown']
        elif args.format == 'links':
            output = '\n'.join(result['links'])
        else:
            output = json.dumps(result, ensure_ascii=False, indent=2)
    session.close()

    if args.output:
        with open(args.output, 'w', encoding='utf-8', newline='\n') as f:
            f.write(output)
    else:
        print(output)


if __name__ == '__main__':
    main()

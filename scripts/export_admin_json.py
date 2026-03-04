#!/usr/bin/env python3
"""
Export the database to docs/admin/data.json for the static admin page.
Run automatically during CI before mkdocs build.

Usage:
    python scripts/export_admin_json.py
"""
import sys
import json
import os
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')

from models import Paper, Dataset, TrainingDataset, SFTMethod, RLMethod, FoundationModel, get_session

OUT_PATH = ROOT / 'docs' / 'admin' / 'data.json'


def export():
    session = get_session()

    papers = []
    for p in session.query(Paper).order_by(Paper.month.desc().nullslast(), Paper.id.desc()).all():
        links = {}
        if p.arxiv_link:       links['arxiv']       = p.arxiv_link
        if p.github_link:      links['github']      = p.github_link
        if p.huggingface_link: links['huggingface'] = p.huggingface_link
        if p.openreview_link:  links['openreview']  = p.openreview_link
        if p.website_link:     links['website']     = p.website_link
        if p.doi_link:         links['doi']         = p.doi_link
        papers.append({
            'id':         p.id,
            'short_name': p.short_name or '',
            'title':      p.title or '',
            'authors':    p.authors or '',
            'venue':      p.venue or '',
            'month':      p.month or '',
            'category':   p.category or '',
            'links':      links,
        })

    datasets = []
    for d in session.query(Dataset).order_by(Dataset.name).all():
        links = {}
        if d.github_link:      links['github']      = d.github_link
        if d.huggingface_link: links['huggingface'] = d.huggingface_link
        if d.website_link:     links['website']     = d.website_link
        datasets.append({
            'id':          d.id,
            'name':        d.name or '',
            'language':    d.language or '',
            'multimodal':  d.multimodal or '',
            'environment': d.environment or '',
            'repos':       d.repos or '',
            'amount':      d.amount or '',
            'category':    d.category or '',
            'links':       links,
        })

    training = []
    for t in session.query(TrainingDataset).order_by(TrainingDataset.name).all():
        links = {}
        if t.github_link:      links['github']      = t.github_link
        if t.huggingface_link: links['huggingface'] = t.huggingface_link
        training.append({
            'id':       t.id,
            'name':     t.name or '',
            'language': t.language or '',
            'repos':    t.repos or '',
            'amount':   t.amount or '',
            'links':    links,
        })

    sft = []
    for m in session.query(SFTMethod).order_by(SFTMethod.resolution_percent.desc().nullslast()).all():
        links = {}
        if m.code_link:  links['github'] = m.code_link
        if m.model_link: links['huggingface'] = m.model_link
        sft.append({
            'id':                  m.id,
            'model_name':          m.model_name or '',
            'base_model':          m.base_model or '',
            'training_scaffold':   m.training_scaffold or '',
            'resolution_percent':  str(m.resolution_percent) if m.resolution_percent is not None else '',
            'links':               links,
        })

    rl = []
    for m in session.query(RLMethod).order_by(RLMethod.resolution_percent.desc().nullslast()).all():
        links = {}
        if m.code_link:  links['github'] = m.code_link
        if m.model_link: links['huggingface'] = m.model_link
        rl.append({
            'id':                  m.id,
            'model_name':          m.model_name or '',
            'size':                m.size or '',
            'architecture':        m.architecture or '',
            'training_scaffold':   m.training_scaffold or '',
            'reward_type':         m.reward_type or '',
            'resolution_percent':  str(m.resolution_percent) if m.resolution_percent is not None else '',
            'links':               links,
        })

    foundation = []
    for m in session.query(FoundationModel).order_by(FoundationModel.resolution_percent.desc().nullslast()).all():
        links = {}
        if m.code_link:  links['github'] = m.code_link
        if m.model_link: links['huggingface'] = m.model_link
        foundation.append({
            'id':                  m.id,
            'model_name':          m.model_name or '',
            'size':                m.size or '',
            'architecture':        m.architecture or '',
            'inference_scaffold':  m.inference_scaffold or '',
            'reward_type':         m.reward_type or '',
            'resolution_percent':  str(m.resolution_percent) if m.resolution_percent is not None else '',
            'links':               links,
        })

    session.close()

    # Category counts from papers
    from collections import Counter
    DATA_CATS     = {'evaluation_datasets','training_datasets','data_collection','data_synthesis'}
    METHODS_CATS  = {'sft','rl','single_agent','multi_agent','tool','workflow','memory','inference_scaling'}
    ANALYSIS_CATS = {'data_analysis','methods_analysis'}

    def count_cat(cat_set):
        return sum(1 for p in papers if {t.strip() for t in p['category'].split(',') if t.strip()} & cat_set)

    data = {
        'generated': date.today().isoformat(),
        'stats': {
            'total':    len(papers),
            'data':     count_cat(DATA_CATS),
            'methods':  count_cat(METHODS_CATS),
            'analysis': count_cat(ANALYSIS_CATS),
        },
        'papers':           papers,
        'datasets':         datasets,
        'training_datasets': training,
        'sft_methods':      sft,
        'rl_methods':       rl,
        'foundation_models': foundation,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'[OK] Exported {len(papers)} papers, {len(datasets)} datasets, '
          f'{len(sft)+len(rl)} methods → {OUT_PATH.relative_to(ROOT)}')


if __name__ == '__main__':
    export()

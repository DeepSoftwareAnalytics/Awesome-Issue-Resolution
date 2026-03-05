#!/usr/bin/env python3
"""
Update the "Recent Papers" section in docs/news.md and sync the
News block in README.md.

The "Recent Papers" block is driven by the `featured` flag on papers in the
database.  Use the Admin UI star button to pin/unpin papers.

The legacy per-month query functions (query_papers, find_most_recent_month,
resolve_month, build_this_month_block) are kept for reference but are no
longer called by default.

Usage:
    python scripts/update_news.py              # update Recent Papers from DB
    python scripts/update_news.py --no-readme  # update news.md only
    python scripts/update_news.py --month 2026-02  # (legacy) show a specific month
"""
import re
import sys
import argparse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

if sys.platform == 'win32':
    import os
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

NEWS_PATH = ROOT / "docs" / "news.md"
README_PATH = ROOT / "README.md"

START_RECENT = "<!-- START_RECENT_PAPERS -->"
END_RECENT = "<!-- END_RECENT_PAPERS -->"
START_NEWS = "<!-- START NEWS -->"
END_NEWS = "<!-- END NEWS -->"


# ---------------------------------------------------------------------------
# Featured papers (new default behaviour)
# ---------------------------------------------------------------------------

def query_featured_papers() -> list[dict]:
    """Return all papers with featured=True, sorted by month descending then title."""
    from models import Paper, get_session
    session = get_session()
    papers = (
        session.query(Paper)
        .filter(Paper.featured == True)  # noqa: E712
        .order_by(Paper.month.desc(), Paper.title)
        .all()
    )
    result = []
    for p in papers:
        result.append({
            "short_name": p.short_name or "",
            "title": p.title or "",
            "authors": p.authors or "",
            "venue": p.venue or "",
            "month": p.month or "",
            "arxiv_link": p.arxiv_link or "",
            "github_link": p.github_link or "",
        })
    session.close()
    return result


def build_recent_papers_block(papers: list[dict]) -> str:
    """Render the Recent Papers block content (between sentinel comments).
    Papers are sorted by month descending (newest first).
    """
    if not papers:
        return "*No featured papers yet. Use the Admin UI star button to pin papers here.*"

    sorted_papers = sorted(papers, key=lambda p: p.get("month") or "", reverse=True)
    lines = []
    for p in sorted_papers:
        short = p["short_name"]
        title = p["title"]
        link = p["arxiv_link"] or ""
        badge = make_badge(link)
        name_part = f"**{short}**" if short else f"**{title}**"
        lines.append(f"- {name_part}: {title} {badge}".rstrip())

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Legacy per-month functions (kept but not called by default)
# ---------------------------------------------------------------------------

def query_papers(month: str) -> list[dict]:
    """(Legacy) Return papers published in the given YYYY-MM month."""
    from models import Paper, get_session
    session = get_session()
    papers = (
        session.query(Paper)
        .filter(Paper.month == month)
        .order_by(Paper.title)
        .all()
    )
    result = []
    for p in papers:
        result.append({
            "short_name": p.short_name or "",
            "title": p.title or "",
            "authors": p.authors or "",
            "venue": p.venue or "",
            "arxiv_link": p.arxiv_link or "",
            "github_link": p.github_link or "",
        })
    session.close()
    return result


def find_most_recent_month() -> str | None:
    """(Legacy) Return the most recent YYYY-MM that has at least one paper in the DB."""
    from models import Paper, get_session
    session = get_session()
    row = (
        session.query(Paper.month)
        .filter(Paper.month.isnot(None))
        .group_by(Paper.month)
        .order_by(Paper.month.desc())
        .first()
    )
    session.close()
    return row[0] if row else None


def resolve_month(requested: str) -> tuple[str, bool]:
    """(Legacy) Resolve which month to display, falling back if needed."""
    papers = query_papers(requested)
    if papers:
        return requested, False
    fallback = find_most_recent_month()
    if fallback and fallback != requested:
        print(f"[INFO] No papers in {requested}; falling back to {fallback}")
        return fallback, True
    return requested, False


def build_this_month_block(month: str, papers: list[dict], is_fallback: bool = False) -> str:
    """(Legacy) Render the this-month section content."""
    if not papers:
        return f"*No papers tracked for {month} yet.*"
    heading = f"**{len(papers)} paper(s) — {month}**"
    lines = [heading, ""]
    for p in papers:
        short = p["short_name"]
        title = p["title"]
        link = p["arxiv_link"] or ""
        badge = make_badge(link)
        name_part = f"**{short}**" if short else f"**{title}**"
        lines.append(f"- {name_part}: {title} {badge}".rstrip())
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------

BADGE_ARXIV = "https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white"
BADGE_OPENREVIEW = "https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white"
BADGE_ACL = "https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white"
BADGE_DOI = "https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white"
BADGE_WEBSITE = "https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white"


def make_badge(link: str) -> str:
    """Return a shields.io Markdown badge for the given paper link."""
    if not link:
        return ""
    if "arxiv.org" in link:
        return f"[![arXiv]({BADGE_ARXIV})]({link})"
    if "openreview.net" in link:
        return f"[![OpenReview]({BADGE_OPENREVIEW})]({link})"
    if "aclanthology.org" in link:
        return f"[![ACL]({BADGE_ACL})]({link})"
    if "doi.org" in link:
        return f"[![DOI]({BADGE_DOI})]({link})"
    return f"[![Website]({BADGE_WEBSITE})]({link})"


def replace_block(text: str, start_marker: str, end_marker: str, new_content: str) -> str:
    """Replace content between start_marker and end_marker (exclusive)."""
    pattern = re.compile(
        rf"({re.escape(start_marker)})\n.*?({re.escape(end_marker)})",
        re.DOTALL,
    )
    replacement = rf"\1\n{new_content}\n\2"
    result, n = pattern.subn(replacement, text)
    if n == 0:
        raise ValueError(f"Markers not found: {start_marker!r} / {end_marker!r}")
    return result


# ---------------------------------------------------------------------------
# File update functions
# ---------------------------------------------------------------------------

def update_news_md(papers: list[dict]) -> None:
    """Rewrite the RECENT_PAPERS block in docs/news.md."""
    text = NEWS_PATH.read_text(encoding="utf-8")
    block = build_recent_papers_block(papers)
    text = replace_block(text, START_RECENT, END_RECENT, block)
    NEWS_PATH.write_text(text, encoding="utf-8")
    print(f"[OK] Updated docs/news.md ({len(papers)} featured papers)")


def sync_news_to_readme() -> None:
    """Copy the full news.md content into the README NEWS block."""
    news_text = NEWS_PATH.read_text(encoding="utf-8")
    readme_text = README_PATH.read_text(encoding="utf-8")
    body = re.sub(r"^#\s.*\n", "", news_text, count=1).lstrip("\n")
    readme_text = replace_block(readme_text, START_NEWS, END_NEWS, body.rstrip("\n"))
    README_PATH.write_text(readme_text, encoding="utf-8")
    print("[OK] Synced news section to README.md")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update the Recent Papers news section from DB")
    parser.add_argument(
        "--month",
        default=None,
        help="(Legacy) Show a specific YYYY-MM month instead of featured papers",
    )
    parser.add_argument(
        "--no-readme",
        action="store_true",
        help="Skip syncing to README.md",
    )
    args = parser.parse_args()

    if args.month:
        # Legacy path: show papers for a specific month
        month, is_fallback = resolve_month(args.month)
        papers_legacy = query_papers(month)
        print(f"[INFO] (Legacy month mode) Found {len(papers_legacy)} paper(s) for {month}")
        text = NEWS_PATH.read_text(encoding="utf-8")
        block = build_this_month_block(month, papers_legacy, is_fallback)
        # Write into the recent papers block using the same markers
        text = replace_block(text, START_RECENT, END_RECENT, block)
        NEWS_PATH.write_text(text, encoding="utf-8")
        print(f"[OK] Updated docs/news.md for {month} ({len(papers_legacy)} papers)")
    else:
        papers = query_featured_papers()
        print(f"[INFO] Found {len(papers)} featured paper(s)")
        update_news_md(papers)

    if not args.no_readme:
        sync_news_to_readme()


if __name__ == "__main__":
    main()

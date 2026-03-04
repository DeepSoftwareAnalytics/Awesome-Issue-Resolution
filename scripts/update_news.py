#!/usr/bin/env python3
"""
Update the "This Month's Papers" section in docs/news.md and sync the
News block in README.md.

Usage:
    python scripts/update_news.py              # update current calendar month
    python scripts/update_news.py --month 2026-02  # update a specific month
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

START_THIS_MONTH = "<!-- START_THIS_MONTH -->"
END_THIS_MONTH = "<!-- END_THIS_MONTH -->"
START_NEWS = "<!-- START NEWS -->"
END_NEWS = "<!-- END NEWS -->"


def query_papers(month: str) -> list[dict]:
    """Return papers published in the given YYYY-MM month."""
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
    """Return the most recent YYYY-MM that has at least one paper in the DB."""
    from models import Paper, get_session
    from sqlalchemy import func
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
    """
    Resolve which month to display.

    Returns (month_to_show, is_fallback).
    If *requested* has no papers, falls back to the most recent month that does.
    """
    papers = query_papers(requested)
    if papers:
        return requested, False

    fallback = find_most_recent_month()
    if fallback and fallback != requested:
        print(f"[INFO] No papers in {requested}; falling back to {fallback}")
        return fallback, True

    return requested, False


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


def build_this_month_block(month: str, papers: list[dict], is_fallback: bool = False) -> str:
    """Render the this-month section content (between sentinel comments)."""
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
        title_part = f"{title}"
        lines.append(f"- {name_part}: {title_part} {badge}".rstrip())

    return "\n".join(lines)


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


def update_news_md(month: str, papers: list[dict], is_fallback: bool = False) -> None:
    """Rewrite the THIS_MONTH block in docs/news.md."""
    text = NEWS_PATH.read_text(encoding="utf-8")
    block = build_this_month_block(month, papers, is_fallback)
    text = replace_block(text, START_THIS_MONTH, END_THIS_MONTH, block)
    NEWS_PATH.write_text(text, encoding="utf-8")
    print(f"[OK] Updated docs/news.md for {month} ({len(papers)} papers)")


def sync_news_to_readme() -> None:
    """Copy the full news.md content into the README NEWS block."""
    news_text = NEWS_PATH.read_text(encoding="utf-8")
    readme_text = README_PATH.read_text(encoding="utf-8")

    # Strip the top-level heading from news.md when embedding
    # (README has its own heading)
    body = re.sub(r"^#\s.*\n", "", news_text, count=1).lstrip("\n")

    readme_text = replace_block(readme_text, START_NEWS, END_NEWS, body.rstrip("\n"))
    README_PATH.write_text(readme_text, encoding="utf-8")
    print("[OK] Synced news section to README.md")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update the News section with this month's papers")
    parser.add_argument(
        "--month",
        default=date.today().strftime("%Y-%m"),
        help="Month to query in YYYY-MM format (default: current month)",
    )
    parser.add_argument(
        "--no-readme",
        action="store_true",
        help="Skip syncing to README.md",
    )
    args = parser.parse_args()

    month, is_fallback = resolve_month(args.month)
    papers = query_papers(month)
    print(f"[INFO] Found {len(papers)} paper(s) for {month}")

    update_news_md(month, papers, is_fallback)

    if not args.no_readme:
        sync_news_to_readme()


if __name__ == "__main__":
    main()

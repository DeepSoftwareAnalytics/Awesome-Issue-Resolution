#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate citation section from citation.bib file
This script automatically updates the citation section in README.md and docs/cite.md
"""
import sys
import os
import re
from pathlib import Path

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import config
CITATION_BIB = config.DOCS_DIR / "citation.bib"
README_PATH = ROOT / "README.md"
CITE_PATH = config.DOCS_DIR / "cite.md"


def parse_bibtex(bib_file):
    """Parse BibTeX file and extract citation information"""
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract entry type and key
    entry_match = re.search(r'@(\w+)\{([^,]+),', content)
    if not entry_match:
        return None
    
    entry_type = entry_match.group(1)
    cite_key = entry_match.group(2)
    
    # Extract fields
    fields = {}
    
    # Title
    title_match = re.search(r'title\s*=\s*\{([^}]+)\}', content)
    if title_match:
        fields['title'] = title_match.group(1).strip()
    
    # Authors
    author_match = re.search(r'author\s*=\s*\{([^}]+)\}', content)
    if author_match:
        authors_raw = author_match.group(1).strip()
        # Split by "and" and format
        authors_list = [a.strip() for a in authors_raw.split(' and ')]
        fields['authors'] = authors_list
    
    # Year
    year_match = re.search(r'year\s*=\s*\{([^}]+)\}', content)
    if year_match:
        fields['year'] = year_match.group(1).strip()
    
    # Journal/Venue
    journal_match = re.search(r'journal\s*=\s*\{([^}]+)\}', content)
    if journal_match:
        fields['journal'] = journal_match.group(1).strip()
    
    # DOI
    doi_match = re.search(r'doi\s*=\s*\{([^}]+)\}', content)
    dor_match = re.search(r'dor\s*=\s*\{([^}]+)\}', content)
    if doi_match:
        fields['doi'] = doi_match.group(1).strip()
    elif dor_match:
        fields['doi'] = dor_match.group(1).strip()
    
    # Publisher
    publisher_match = re.search(r'publisher\s*=\s*\{([^}]+)\}', content)
    if publisher_match:
        fields['publisher'] = publisher_match.group(1).strip()
    
    # Page
    page_match = re.search(r'page\s*=\s*\{([^}]+)\}', content)
    if page_match:
        fields['page'] = page_match.group(1).strip()
    
    return {
        'entry_type': entry_type,
        'cite_key': cite_key,
        'fields': fields
    }


def format_authors(authors_list):
    """Format author list for display"""
    if len(authors_list) <= 3:
        return ', '.join(authors_list)
    else:
        return ', '.join(authors_list[:3]) + ', et al.'


def generate_citation_markdown(bib_data):
    """Generate markdown citation text"""
    if not bib_data:
        return ""
    
    fields = bib_data['fields']
    cite_key = bib_data['cite_key']
    
    # Format authors
    authors = format_authors(fields.get('authors', []))
    
    # Format title
    title = fields.get('title', 'Untitled')
    
    # Format year
    year = fields.get('year', 'n.d.')
    
    # Format journal/venue
    journal = fields.get('journal', '')
    
    # Format DOI
    doi = fields.get('doi', '')
    doi_link = f"https://doi.org/{doi}" if doi else ""
    
    # Generate markdown
    md = []
    md.append(f"**{authors}** ({year}). *{title}*. {journal}.")
    if doi_link:
        md.append(f" DOI: [{doi}]({doi_link})")
    
    return ' '.join(md)


def generate_bibtex_block(bib_file):
    """Read and format BibTeX content for display"""
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.strip()


def update_readme_citation(bib_data):
    """Update citation section in README.md"""
    if not README_PATH.exists():
        print("❌ README.md not found!")
        return False
    
    content = README_PATH.read_text(encoding='utf-8')
    
    # Generate citation markdown
    citation_md = generate_citation_markdown(bib_data)
    bibtex_block = generate_bibtex_block(CITATION_BIB)
    
    # Create the new citation section
    new_citation = f"""## 📄 Citation

If you use this project or related survey in your research or system, please cite the following:

{citation_md}

**BibTeX:**

```bibtex
{bibtex_block}
```

Once published on arXiv or at a conference, please replace the entry with the official citation information (authors, DOI/arXiv ID, conference name, etc.)."""
    
    # Replace citation section
    pattern = r'## 📄 Citation.*?(?=\n---\n|## 🙏|\Z)'
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_citation, content, flags=re.DOTALL)
        README_PATH.write_text(new_content, encoding='utf-8')
        print("✓ Updated citation in README.md")
        return True
    else:
        print("⚠️ Citation section not found in README.md")
        return False


def update_cite_page(bib_data):
    """Update or create cite.md page"""
    citation_md = generate_citation_markdown(bib_data)
    bibtex_block = generate_bibtex_block(CITATION_BIB)
    
    cite_content = f"""# Citation

If you find this survey helpful for your research or project, please consider citing our work:

## Formatted Citation

{citation_md}

## BibTeX

```bibtex
{bibtex_block}
```

## Other Formats

### APA
{format_authors(bib_data['fields'].get('authors', []))} ({bib_data['fields'].get('year', 'n.d.')}). {bib_data['fields'].get('title', 'Untitled')}. *{bib_data['fields'].get('journal', '')}*.

### MLA
{format_authors(bib_data['fields'].get('authors', []))}. "{bib_data['fields'].get('title', 'Untitled')}." *{bib_data['fields'].get('journal', '')}* ({bib_data['fields'].get('year', 'n.d.')}).

---

## How to Cite

1. **In academic papers**: Use the BibTeX entry above
2. **In blog posts or articles**: Use the formatted citation
3. **In GitHub repositories**: Link to our repository: `https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution`

---

**Note**: This citation information is automatically generated from `docs/citation.bib`. If the paper is published on arXiv or at a conference, the citation will be updated accordingly.
"""
    
    CITE_PATH.write_text(cite_content, encoding='utf-8')
    print("✓ Updated docs/cite.md")
    return True


def main():
    """Main function"""
    print("=" * 70)
    print("  Generating Citation from BibTeX")
    print("=" * 70)
    print()
    
    # Check if citation.bib exists
    if not CITATION_BIB.exists():
        print(f"❌ {CITATION_BIB} not found!")
        return False
    
    # Parse BibTeX
    print("📚 Parsing citation.bib...")
    bib_data = parse_bibtex(CITATION_BIB)
    
    if not bib_data:
        print("❌ Failed to parse BibTeX file!")
        return False
    
    print(f"  ✓ Parsed citation: {bib_data['cite_key']}")
    print(f"  ✓ Title: {bib_data['fields'].get('title', 'N/A')}")
    print()
    
    # Update README.md
    print("📝 Updating README.md...")
    update_readme_citation(bib_data)
    print()
    
    # Update cite.md
    print("📝 Updating docs/cite.md...")
    update_cite_page(bib_data)
    print()
    
    # Update paper.md
    print("📝 Updating docs/paper.md...")
    paper_path = config.DOCS_DIR / "paper.md"
    if paper_path.exists():
        try:
            content = paper_path.read_text(encoding='utf-8')
            bibtex_str = generate_bibtex_block(CITATION_BIB)
            citation_block = f"""If you use this project or related survey in your research or system, please cite the following BibTeX:

```bibtex
{bibtex_str}
```

Once published on arXiv or at a conference, please replace the entry with the official citation information (authors, DOI/arXiv ID, conference name, etc.)."""
            
            pattern = re.compile(r'(<!-- START CITATION -->).*?(<!-- END CITATION -->)', re.DOTALL)
            new_content = pattern.sub(f'\\1\n{citation_block}\n\\2', content)
            
            if new_content != content:
                paper_path.write_text(new_content, encoding='utf-8')
                print("✓ Updated citation in paper.md")
            else:
                print("[WARN] Citation markers not found in paper.md")
        except Exception as e:
            print(f"[ERROR] Failed to update paper.md: {e}")
    print()
    
    print("=" * 70)
    print("  ✅ Citation generation complete!")
    print("=" * 70)
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


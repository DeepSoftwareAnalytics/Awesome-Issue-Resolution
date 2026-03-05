# Admin Interface

<div class="admonition info" markdown="1">

The **Admin Interface** is a local web application that runs on your own machine. It cannot be hosted on GitHub Pages because it requires a live database and Python backend.

</div>

## What it does

The admin panel (served by Flask at `http://localhost:5000/admin`) provides:

- **Browse & search** all 196+ papers, datasets, and methods
- **Inline editing** — click any cell to edit it directly in the table
- **Add new entries** with arXiv auto-fill (paste an arXiv URL to auto-populate metadata)
- **Multi-select export** — select papers and export as CSV or copy links for NotebookLM
- **Sync & build** — export DB → YAML/CSV, or rebuild the static documentation site

## How to run it locally

```bash
# 1. Clone the repository
git clone https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution.git
cd Awesome-Issue-Resolution

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the admin server
#    (automatically refreshes news, re-renders docs, and builds the site)
python start.py
```

Then open **[http://localhost:5000/admin](http://localhost:5000/admin)** in your browser.

## Quick reference

| Command | Description |
|---------|-------------|
| `python start.py` | Full update + start server (port 5000) |
| `python start.py --init` | Re-import from YAML/CSV, then full update + start |
| `python start.py --no-update` | Start server immediately without update steps |
| `python start.py --news` | Refresh "Recent Papers" section only |
| `python start.py --render` | Re-render README/docs from DB only |
| `python start.py --build` | Build static site only |

## Looking for the paper database?

Use the **[Tables & Resources](../tables/)** page to browse statistical tables, or the **[Full Paper List](../#-complete-paper-list)** in the main page.

To search and export papers interactively, run the admin locally as described above.

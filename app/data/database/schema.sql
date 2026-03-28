-- Survey Database Schema for Awesome Issue Resolution
-- SQLite Database Design

-- Papers table (from YAML files)
CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_name TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    year TEXT NOT NULL,
    venue TEXT NOT NULL,
    category TEXT NOT NULL,  -- e.g., 'sft', 'rl', 'data_analysis', etc.
    abstract TEXT,
    arxiv_link TEXT,
    github_link TEXT,
    huggingface_link TEXT,
    website_link TEXT,
    doi_link TEXT,
    openreview_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datasets table (from table1.csv)
CREATE TABLE IF NOT EXISTS datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    language TEXT,
    multimodal TEXT,
    repos TEXT,
    amount TEXT,
    environment TEXT,
    category TEXT,  -- 'single-pl' or 'multi-pl'
    github_link TEXT,
    huggingface_link TEXT,
    website_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Training Trajectory Datasets table (from table2.csv)
CREATE TABLE IF NOT EXISTS training_datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    language TEXT,
    repos TEXT,
    amount TEXT,
    github_link TEXT,
    huggingface_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SFT Methods table (from table3.csv)
CREATE TABLE IF NOT EXISTS sft_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT UNIQUE NOT NULL,
    base_model TEXT,
    size TEXT,
    architecture TEXT,
    training_scaffold TEXT,
    resolution_percent REAL,
    code_link TEXT,
    data_link TEXT,
    model_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- RL Methods table (from table4.csv)
CREATE TABLE IF NOT EXISTS rl_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT UNIQUE NOT NULL,
    base_model TEXT,
    size TEXT,
    architecture TEXT,
    training_scaffold TEXT,
    reward_type TEXT,
    resolution_percent REAL,
    code_link TEXT,
    data_link TEXT,
    model_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Foundation Models table (from table5.csv)
CREATE TABLE IF NOT EXISTS foundation_models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT UNIQUE NOT NULL,
    size TEXT,
    architecture TEXT,
    inference_scaffold TEXT,
    reward_type TEXT,
    resolution_percent REAL,
    code_link TEXT,
    model_link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Full-text search indexes
CREATE VIRTUAL TABLE IF NOT EXISTS papers_fts USING fts5(
    short_name, title, authors, venue, abstract,
    content='papers',
    content_rowid='id'
);

-- Triggers to keep FTS index updated
CREATE TRIGGER IF NOT EXISTS papers_ai AFTER INSERT ON papers BEGIN
    INSERT INTO papers_fts(rowid, short_name, title, authors, venue, abstract)
    VALUES (new.id, new.short_name, new.title, new.authors, new.venue, new.abstract);
END;

CREATE TRIGGER IF NOT EXISTS papers_ad AFTER DELETE ON papers BEGIN
    DELETE FROM papers_fts WHERE rowid = old.id;
END;

CREATE TRIGGER IF NOT EXISTS papers_au AFTER UPDATE ON papers BEGIN
    UPDATE papers_fts SET
        short_name = new.short_name,
        title = new.title,
        authors = new.authors,
        venue = new.venue,
        abstract = new.abstract
    WHERE rowid = new.id;
END;

-- Indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_papers_year ON papers(year);
CREATE INDEX IF NOT EXISTS idx_papers_category ON papers(category);
CREATE INDEX IF NOT EXISTS idx_datasets_language ON datasets(language);
CREATE INDEX IF NOT EXISTS idx_sft_methods_resolution ON sft_methods(resolution_percent);
CREATE INDEX IF NOT EXISTS idx_rl_methods_resolution ON rl_methods(resolution_percent);
CREATE INDEX IF NOT EXISTS idx_foundation_models_resolution ON foundation_models(resolution_percent);

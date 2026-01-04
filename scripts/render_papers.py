#!/usr/bin/env python3
"""
自动从 YAML 数据文件渲染论文列表到 Markdown 文档。
使用原网站的格式：简单列表 + shields.io 风格图片徽章。

用法:
    python scripts/render_papers.py
"""
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"

# shields.io 徽章 URL
ARXIV_BADGE = "https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white"
GITHUB_BADGE = "https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white"
HF_BADGE = "https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white"

# 正则匹配 <!-- START PAPERS:xxx --> ... <!-- END PAPERS:xxx -->
BLOCK_RE = re.compile(
    r"<!-- START PAPERS:(\w+) -->(.*?)<!-- END PAPERS:\1 -->",
    re.DOTALL
)


def badge_arxiv(url: str) -> str:
    """生成 arXiv 图片徽章。"""
    if not url:
        return ""
    return f'[![arXiv]({ARXIV_BADGE})]({url}){{: target="_blank" }}'


def badge_github(url: str) -> str:
    """生成 GitHub 图片徽章。"""
    if not url:
        return ""
    return f'[![GitHub]({GITHUB_BADGE})]({url}){{: target="_blank" }}'


def badge_huggingface(url: str) -> str:
    """生成 HuggingFace 图片徽章。"""
    if not url:
        return ""
    return f'[![HuggingFace]({HF_BADGE})]({url}){{: target="_blank" }}'


def load_yaml(path: Path) -> list:
    """加载 YAML 文件并返回条目列表。"""
    if not path.exists():
        print(f"[WARN] {path} 不存在，跳过。", file=sys.stderr)
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        return data
    except Exception as ex:
        print(f"[ERR] 加载 {path} 失败: {ex}", file=sys.stderr)
        return []


def render_paper_item(entry: dict) -> str:
    """渲染单个论文为列表项 - 原网站格式。"""
    short_name = entry.get("short_name", "").strip()
    full_title = entry.get("title", "").strip()
    year = entry.get("year", "").strip()
    links = entry.get("links", {}) or {}
    
    arxiv = links.get("arxiv", "")
    github = links.get("github", "")
    huggingface = links.get("huggingface", "")
    
    # 如果简短名称和完整标题相同，只显示一次
    if short_name == full_title:
        if year:
            item = f"* **{short_name}** ({year})"
        else:
            item = f"* **{short_name}**"
    else:
        # 简短名称 + 完整标题
        if year:
            item = f"* **{short_name}**: {full_title} ({year})"
        else:
            item = f"* **{short_name}**: {full_title}"
    
    # 添加徽章
    badges = []
    if arxiv:
        badges.append(badge_arxiv(arxiv))
    if github:
        badges.append(badge_github(github))
    if huggingface:
        badges.append(badge_huggingface(huggingface))
    
    if badges:
        item += " " + " ".join(badges)
    
    return item


def render_section(section_id: str) -> str:
    """从 YAML 文件渲染所有论文为 Markdown 列表。"""
    yaml_file = f"papers_{section_id}.yaml"
    path = DATA_DIR / yaml_file
    entries = load_yaml(path)
    
    if not entries:
        return f"\n<!-- 没有找到 {yaml_file} 中的论文 -->\n"
    
    items = [render_paper_item(e) for e in entries]
    content = "\n".join(items)
    
    return f"\n{content}\n"


def update_markdown_file(filepath: Path) -> int:
    """更新 Markdown 文件中的论文列表。返回更新的块数量。"""
    if not filepath.exists():
        print(f"[WARN] {filepath} 不存在，跳过。", file=sys.stderr)
        return 0
    
    content = filepath.read_text(encoding="utf-8")
    
    def replace_block(match):
        section_id = match.group(1)
        md = render_section(section_id)
        entries = load_yaml(DATA_DIR / f"papers_{section_id}.yaml")
        print(f"  [OK] {section_id}: {len(entries)} 篇论文")
        return f"<!-- START PAPERS:{section_id} -->{md}<!-- END PAPERS:{section_id} -->"
    
    new_content, count = BLOCK_RE.subn(replace_block, content)
    
    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
    
    return count


def main():
    """主函数：更新所有文档文件。"""
    print("=" * 60)
    print("自动更新论文列表（原网站样式 - 图片徽章）")
    print("=" * 60)
    
    doc_files = [
        DOCS_DIR / "index.md",
        DOCS_DIR / "methods.md",
        DOCS_DIR / "data.md",
        DOCS_DIR / "analysis.md",
    ]
    
    total_blocks = 0
    
    for doc_file in doc_files:
        if doc_file.exists():
            print(f"\n处理 {doc_file.name}:")
            count = update_markdown_file(doc_file)
            total_blocks += count
            if count == 0:
                print(f"  [INFO] 没有找到 <!-- START PAPERS:xxx --> 标记")
    
    print("\n" + "=" * 60)
    print(f"完成！共更新 {total_blocks} 个论文块。")
    print("=" * 60)


if __name__ == "__main__":
    main()

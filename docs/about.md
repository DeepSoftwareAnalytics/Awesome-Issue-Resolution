# About

## About This Project

Based on a systematic review of 188 papers and online resources, this project establishes a holistic theoretical framework for Issue Resolution in software engineering. This website is designed to facilitate efficient literature retrieval and exploration.


---

## Key Features

- **Comprehensive Coverage**: Covers three major sections - Data, Methods, and Analysis
- **Convenient Retrieval**: Supports full-text search and categorical browsing
- **Database-Driven**: All paper and table data is managed in a local SQLite database
- **Admin Interface**: Web-based admin panel at `/admin` for CRUD operations, arXiv auto-fill, and one-click site build
- **Two-Way Sync**: Data can be exported to YAML/CSV (`data/`) or re-imported from files at any time

---

### Common Operations

| Goal | Command / Action |
|------|-----------------|
| Full update + start server | `python start.py` (refreshes news, renders README/docs, builds site) |
| Re-import data then full update | `python start.py --init` |
| Start server without updates | `python start.py --no-update` |
| Refresh news section only | `python start.py --news` |
| Re-render README/docs from DB | `python start.py --render` or **Render from DB** in admin |
| Build static site only | `python start.py --build` or **Build Website** in admin |
| Export DB → YAML/CSV | **Sync to Data** in admin |
| Import YAML/CSV → DB | **Import from Data** in admin |

---

## Contribution Guide

We welcome Pull Requests to add new papers or fix errors!

1. Fork this repository
2. Add paper entries in the corresponding YAML file under `data/` directory (e.g., `papers_evaluation_datasets.yaml`, `papers_single_agent.yaml`, etc.)
3. Follow the existing format with fields: `short_name`, `title`, `authors`, `venue`, `month`, and `links` (arxiv, github, huggingface)
4. Run `python start.py --render` to regenerate the README and docs from the database
5. Submit a PR with your changes

---

## Acknowledgements

We would like to express our sincere gratitude to:

- The **authors of cited papers** who provided valuable feedback on how their work is presented in this survey, greatly improving its accuracy and comprehensiveness.

- All **contributors** who have helped improve this project through issues, pull requests, and discussions.

- The **open-source community** for developing the amazing tools and frameworks that made this project possible.

### Special Thanks

- **[@chao-peng](https://github.com/chao-peng){: target="_blank" }** ([Dr. Chao Peng](https://chao-peng.github.io){: target="_blank" }), ByteDance Software Engineering Lab, for providing valuable suggestions on the Challenges and Opportunities section of our survey.

- **[@EuniAI/awesome-code-agents](https://github.com/EuniAI/awesome-code-agents){: target="_blank" }** for providing an excellent reference on managing survey papers through documentation systems and inspiring our project structure.

---

## Interactive Exploration

<div align="center" markdown="1">

[![NotebookLM](https://img.shields.io/badge/🎧_NotebookLM-Listen_&_Explore-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://notebooklm.google.com/notebook/2b70100e-9d5a-46db-96f5-6ccb7b53890a){: target="_blank" }
[![Discord](https://img.shields.io/badge/💬_Discord-Join_Discussion-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/awBHrRJx){: target="_blank" }
[![Issues](https://img.shields.io/badge/💡_GitHub-Open_Issue-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/issues){: target="_blank" }

</div>

---

## Contact Us

If you have any questions or suggestions, please contact us through [GitHub Issues](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/issues) or email at [noranotdor4@gmail.com](mailto:noranotdor4@gmail.com).

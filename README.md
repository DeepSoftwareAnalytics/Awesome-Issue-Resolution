# ✨ Awesome Issue Resolution

<div align="center">

**Advances and Frontiers of LLM-based Issue Resolution in Software Engineering A Comprehensive Survey**

[![GitHub Stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&logo=github&color=4c1)](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution)
[![Forks](https://img.shields.io/github/forks/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&logo=github&color=blue)](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/fork)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Paper](https://img.shields.io/badge/PAPER-PDF-4285F4?style=for-the-badge&logo=googledocs&logoColor=white)](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/)
[![arXiv](https://img.shields.io/badge/arXiv-2501.XXXXX-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/XXXX.XXXXX)
[![Tables](https://img.shields.io/badge/TABLES-Statistics-blue?style=for-the-badge&logo=databricks)](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)
[![Contributors](https://img.shields.io/github/contributors/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&color=green&logo=github)](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/graphs/contributors)
![Papers Count](https://img.shields.io/badge/papers-135-green?style=for-the-badge&logo=googlescholar&logoColor=white)

[**📖 Documentation Website**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/) | [**📄 Full Paper**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/) | [**📋 Tables & Resources**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)

<img src="docs/images/awesome-issue-resolution.png" alt="Awesome Issue Resolution" width="60%">

</div>

---

## 📖 Abstract

Based on a systematic review of **135 papers and online resources**, this survey establishes a holistic theoretical framework for Issue Resolution in software engineering. We examine how **Large Language Models (LLMs)** are transforming the automation of GitHub issue resolution. Beyond the theoretical analysis, we have curated a comprehensive collection of datasets and model training resources, which are continuously synchronized with our GitHub repository and project documentation website. 

**🔍 Explore This Survey:**

- 📊 **[Data](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#data)**: Evaluation and training datasets, data collection and synthesis methods
- 🛠️ **[Methods](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#methods)**: Training-free (agent/workflow) and training-based (SFT/RL) approaches  
- 🔍 **[Analysis](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#analysis)**: Insights into both data characteristics and method performance
- 📋 **[Tables & Resources](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)**: Comprehensive statistical tables and resources
- 📄 **[Full Paper](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/)**: Read the complete survey paper

---

## 📊 Data

### Evaluation Datasets

We comprehensively survey evaluation benchmarks for issue resolution, categorizing them by programming language, multimodal support, and reproducible execution environments.

**Key Datasets:**
- **SWE-bench**: Python-based benchmark with 2,294 real-world issues from 12 repositories
- **SWE-bench Lite**: Curated subset of 300 high-quality instances
- **Multi-SWE-bench**: Multilingual extension covering 7+ programming languages
- **SWE-bench Multimodal**: Incorporates visual elements (JS, TS, HTML, CSS)
- **Visual SWE-bench**: Focus on vision-intensive issue resolution

[**→ Explore all evaluation datasets**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#evaluation-datasets)

### Training Datasets

We analyze trajectory datasets used for agent training, including both human-annotated and synthetically generated examples.

**Notable Resources:**
- **R2E-Gym**: 3,321 trajectories for reinforcement learning
- **SWE-Gym**: 491 expert trajectories for supervised fine-tuning
- **SWE-Fixer**: Large-scale dataset with 69,752 editing chains of thought

[**→ Explore training datasets**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#training-datasets)

---

## 🛠️ Methods

### Training-Free Approaches

#### Agent-Based Methods
Autonomous agents that leverage tool use, memory, and planning to resolve issues without task-specific training.

**Representative Works:**
- **OpenHands**: Multi-agent collaboration framework
- **Agentless**: Localization + repair pipeline without agent loops
- **AutoCodeRover**: Hierarchical search-based code navigation

#### Workflow-Based Methods
Structured pipelines optimizing specific stages of issue resolution.

**Key Innovations:**
- **Meta-RAG**: Code summarization for enhanced retrieval
- **TestAider**: Test-driven development integration
- **PatchPilot**: Automated patch validation and refinement

[**→ Explore training-free methods**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#training-free-approaches)

### Training-Based Approaches

#### Supervised Fine-Tuning (SFT)
Models trained on expert trajectories to internalize issue resolution patterns.

**Notable Models:**
- **Devstral (22B)**: 46.8% on SWE-bench Verified
- **Co-PatcheR (14B)**: Multi-stage training with code editing focus
- **SWE-Swiss (32B)**: Synthetic data augmentation for improved generalization

#### Reinforcement Learning (RL)
Models optimized through environmental feedback and reward signals.

**State-of-the-Art:**
- **OpenHands Critic (32B)**: 66.4% on SWE-bench Verified
- **Kimi-Dev (72B)**: 60.4% with outcome-based rewards
- **DeepSWE (32B)**: Trained from scratch using RL on code repositories

[**→ Explore training-based methods**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#training-based-approaches)

---

## 🔍 Analysis

### Data Analysis
- **Quality vs. Quantity**: Analysis of dataset characteristics and their impact on model performance
- **Contamination Detection**: Protocols for ensuring benchmark integrity
- **Difficulty Spectrum**: Stratification of issues by complexity

### Methods Analysis
- **Performance Trends**: Comparative evaluation across model families and sizes
- **Scaling Laws**: Analysis of parameter count vs. performance gains
- **Efficiency Metrics**: Cost-benefit analysis of different approaches

[**→ Explore detailed analysis**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#analysis)

---

## 🚀 Challenges and Opportunities

### 🔧 High computational overhead
The scalability of SWE agents is bottlenecked by the high costs of sandboxed environments and long-context inference. Optimization strategies are required to streamline these resource-intensive loops without sacrificing performance.

### 📉 Opacity in resource consumption
Benchmarks often overlook efficiency, masking the high costs of techniques like inference-time scaling. Standardized reporting of latency and token usage is crucial for guiding the development of cost-effective agents.

### 🖼️ Limited visually-grounded reasoning
Reliance on text proxies for UI interpretation limits effectiveness. Future research can adopt intrinsic multi-modal solutions, such as code-centric MLLMs, to better bridge the gap between visual rendering and underlying code logic.

### 🛡️ Safety risks in autonomous resolution
High autonomy carries risks of destructive actions, such as accidental code deletion. Future systems should integrate safeguards, such as Git-based version control, to ensure autonomous modifications remain secure and reversible.

### 🎯 Lack of fine-grained reward signals
Reinforcement learning is hindered by sparse, binary feedback. Integrating fine-grained signals from compiler diagnostics and execution traces is necessary to guide models through complex reasoning steps.

### 🔍 Data leakage and contamination
As benchmarks approach saturation, evaluation validity is compromised by data leakage. Future frameworks must strictly enforce decontamination protocols to ensure fairness and reliability.

### 🌐 Lack of universality across SE domains
While current issue resolution tasks mirror development workflows, they represent only a fraction of the full Software Development Life Cycle (SDLC). Future research should broaden the scope of issue resolution tasks to develop more versatile automated software generation methods.

---

## 📋 Tables & Resources

Visit our [**Tables & Resources**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/) page for comprehensive statistical tables including:

- 📊 **Evaluation Datasets Overview**: Detailed comparison of 30+ benchmarks
- 🎯 **Training Trajectory Datasets**: Analysis of 5 major trajectory datasets
- 🔧 **Supervised Fine-Tuning Models**: Performance metrics for 10+ SFT models
- 🤖 **Reinforcement Learning Models**: Comprehensive analysis of 30+ RL-trained models
- 🌟 **General Foundation Models**: Evaluation of 15+ general-purpose LLMs

---

## 🤝 Contributing

We welcome contributions to this survey! If you'd like to add new papers or fix errors:

1. Fork this repository
2. Add paper entries in the corresponding YAML file under `data/` directory (e.g., `papers_evaluation_datasets.yaml`, `papers_single_agent.yaml`, etc.)
3. Follow the existing format with fields: `short_name`, `title`, `authors`, `venue`, `year`, and `links` (arxiv, github, huggingface)
4. Run `python scripts/render_papers.py` to update the documentation
5. Submit a PR with your changes

---

## 📄 Citation

If you use this project or related survey in your research or system, please cite the following BibTeX:

```bibtex
@misc{li2025awesome_issue_resolution,
    title       = {Advances and Frontiers of LLM-based Issue Resolution in Software Engineering A Comprehensive Survey},
    author      = {Caihua Li and Lianghong Guo and Yanlin Wang and Wei Tao and Zhenyu Shan and Mingwei Liu and Jiachi Chen and Haoyu Song and Duyu Tang and Hongyu Zhang and Zibin Zheng},
    year        = {2025},
    howpublished = {\url{https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution}}
}
```

Once published on arXiv or at a conference, please replace the entry with the official citation information (authors, DOI/arXiv ID, conference name, etc.).

---

## 📬 Contact

If you have any questions or suggestions, please contact us through:

- 📧 **Email**: [noranotdor4@gmail.com](mailto:noranotdor4@gmail.com)
- 💬 **GitHub Issues**: [Open an issue](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/issues)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by the [DeepSoftwareAnalytics](https://github.com/DeepSoftwareAnalytics) team

[Documentation](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/) | [Paper](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/) | [Tables](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/) | [About](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/about/) | [Cite](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/cite/)

</div>


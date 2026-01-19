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
![Papers Count](https://img.shields.io/badge/papers-176-green?style=for-the-badge&logo=googlescholar&logoColor=white)

[**📖 Documentation Website**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/) | [**📄 Full Paper**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/) | [**📋 Tables & Resources**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)

<img src="docs/images/awesome-issue-resolution.png" alt="Awesome Issue Resolution" width="60%">

</div>

---

## 📖 Abstract

Based on a systematic review of **176 papers and online resources**, this survey establishes a holistic theoretical framework for Issue Resolution in software engineering. We examine how **Large Language Models (LLMs)** are transforming the automation of GitHub issue resolution. Beyond the theoretical analysis, we have curated a comprehensive collection of datasets and model training resources, which are continuously synchronized with our GitHub repository and project documentation website. 

<!-- START EXPLORE -->
**🔍 Explore This Survey:**

- 📊 **[Data](#-data)**: Evaluation and training datasets, data collection and synthesis methods
  - [📊 Evaluation Datasets](#-evaluation-datasets)
  - [🎯 Training Datasets](#-training-datasets)
  - [📥 Data Collection Methods](#-data-collection)
  - [🔬 Data Synthesis Methods](#-data-synthesis)
- 🛠️ **[Methods](#%EF%B8%8F-methods)**: Training-free (agent/workflow) and training-based (SFT/RL) approaches
  - **Training-free Methods**
    - [🤖 Single-Agent Systems](#-single-agent-systems)
    - [👥 Multi-Agent Systems](#-multi-agent-systems)
    - [🔄 Workflow-Based Methods](#-workflow-based-methods)
    - [🛠️ Tool-Augmented Methods](#%EF%B8%8F-tool-augmented-methods)
    - [🧠 Memory-Enhanced Methods](#-memory-enhanced-methods)
    - [⚡ Inference-Time Scaling](#-inference-time-scaling)
  - **Training-based Methods**
    - [📚 Supervised Fine-Tuning (SFT)](#-supervised-fine-tuning-sft)
    - [🎮 Reinforcement Learning (RL)](#-reinforcement-learning-rl)
- 🔍 **[Analysis](#-analysis)**: Insights into both data characteristics and method performance
  - [📈 Data Analysis](#-data-analysis)
  - [🔍 Methods Analysis](#-methods-analysis)
- 📋 **[Tables & Resources](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)**: Comprehensive statistical tables and resources
- 📄 **[Full Paper](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/)**: Read the complete survey paper
- 🤝 **[Contributing](#-contributing)**: How to contribute to this project
<!-- END EXPLORE -->

**🎙️ Interactive Exploration:**

<div align="center">

[![NotebookLM](https://img.shields.io/badge/🎧_NotebookLM-Listen_&_Explore-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://notebooklm.google.com/notebook/2b70100e-9d5a-46db-96f5-6ccb7b53890a)
[![Discord](https://img.shields.io/badge/💬_Discord-Join_Discussion-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/3nF2EYTD)
[![Issues](https://img.shields.io/badge/💡_GitHub-Open_Issue-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/issues)

</div>

---

<!-- START PAPERS -->
## 📚 Complete Paper List


> **Total: 176 works** across 14 categories


### 📊 Evaluation Datasets

*Benchmarks for evaluating issue resolution systems*

- **SWE-bench Lite**: SWE-bench: Can Language Models Resolve Real-world Github Issues? (2024)
- **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024)
- **SWE-bench-java**: SWE-bench-java: A GitHub Issue Resolving Benchmark for Java (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.14354)
- **Visual SWE-bench**: CodeV: Issue Resolving with Visual Data (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.18653/v1/2025.findings-acl.384)
- **SWE-Lancer**: SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World
                  Freelance Software Engineering? (2025)
- **FEA-Bench**: FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation
                  for Feature Implementation (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.acl-long.839/)
- **Multi-SWE-bench**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=MhBZzkz4h9)
- **SWE-PolyBench**: SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08703)
- **SWE-bench Multilingual**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=63iVrXc8cC)
- **SwingArena**: SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23932)
- **SWE-bench Multimodal**: SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=riTiq3i21b)
- **OmniGIRL**: Omnigirl: A multilingual and multimodal benchmark for github issue resolution (2025)
- **SWE-bench-Live**: SWE-bench Goes Live! (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=OGWkr7gXka)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059)
- **SWE-Perf**: SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories? (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=KxFaKvtBiG)
- **SWE-Bench Pro**: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16941)
- **SWE-InfraBench**: SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=XX0ciUwfXa)
- **SWE-Sharp-Bench**: SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02352)
- **SWE-fficiency**: SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.06090)
- **SWE-Compass**: SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.05459)
- **SWE-EVO**: SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18470)

### 🎯 Training Datasets

*Datasets for training issue resolution agents*

- **SWE-bench-extra**: SWE-bench: Can Language Models Resolve Real-world Github Issues? (2024)
- **Multi-SWE-RL**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=MhBZzkz4h9)
- **R2E-Gym**: R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=7evvwwdo3z)
- **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757)
- **LocAgent**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=LyUfPOvM6I)
- **SWE-Smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=63iVrXc8cC)
- **SWE-Fixer**: SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution
- **SWELoc**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849)
- **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym
- **SWE-Flow**: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=P9DQ2IExgS)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **Skywork-SWE**: Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.19290)
- **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550)
- **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724)
- **SWE-Lego**: SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.01426)

### 🤖 Single-Agent Systems

*Individual autonomous agents for issue resolution*

- **SWE-agent**: Swe-agent: Agent-computer interfaces enable automated software engineering (2024)
- **Aider** (2026) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://aider.chat/)
- **Devin**: SWE-bench technical report (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://cognition.ai/blog/swe-bench-technical-report)
- **PatchPilot**: PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=ybODpT8ydV)
- **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120)
- **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954)
- **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370)
- **Live-SWE-agent**: SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=isATAFP71B)
- **Lita**: Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25873)
- **TOM-SWE**: TOM-SWE: User Mental Modeling For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.21903)
- **Confucius Code Agent**: Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.10398)

### 👥 Multi-Agent Systems

*Collaborative multi-agent frameworks*

- **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=qevq3FZ63J)
- **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384)
- **CodeR**: CodeR: Issue Resolving with Multi-Agent and Task Graphs (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.01304)
- **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=OJd3ayDDoF)
- **AgentScope**: SWE-Bench - AgentScope (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://doc.agentscope.io/v0/en/tutorial/swe.html)
- **OrcaLora**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=LyUfPOvM6I)
- **DEI**: Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=cKlzKs3Nnb)
- **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899)
- **Lingxi**: Lingxi/docs/Lingxi Technical Report 2505.pdf at master · lingxi-agent/Lingxi (2026) [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/lingxi-agent/Lingxi/blob/master/docs/Lingxi%20Technical%20Report%202505.pdf)
- **Devlo**: Achieving SOTA on SWE-bench (2026) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://devlo.ai/blog/devlo-swe-bench-sota/)
- **Refact.ai Agent**: AI Coding Agent for Software Development - Refact.ai (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://refact.ai/blog/2025/open-source-sota-on-swe-bench-verified-refact-ai/)
- **HyperAgent**: HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.16299)
- **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=G7sIFXugTX)
- **CodeCoR**: CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.07811)
- **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229)
- **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2026)
- **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361)
- **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611)

### 🔄 Workflow-Based Methods

*Structured pipeline approaches*

- **Agentless**: Demystifying LLM-Based Software Engineering Agents (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://api.semanticscholar.org/CorpusID:277850376)
- **Conversational Pipeline**: Exploring the Potential of Conversational Test Suite Based Program Repair on SWE-bench (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.04485)
- **SynFix**: SynFix: Dependency-Aware Program Repair via RelationGraph Analysis (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.findings-acl.252/) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.18653/v1/2025.findings-acl.252)
- **CodeV**: CodeV: Issue Resolving with Visual Data (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.18653/v1/2025.findings-acl.384)
- **GUIRepair**: Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visual Software Issue Fixing (2025)

### 🛠️ Tool-Augmented Methods

*Methods leveraging external tools*

- **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=qevq3FZ63J)
- **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384)
- **SWE-agent**: Swe-agent: Agent-computer interfaces enable automated software engineering (2024)
- **Alibaba LingmaAgent**: Alibaba LingmaAgent: Improving Automated Issue Resolution via Comprehensive Repository Exploration (2025) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.1145/3696630.3728549)
- **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=OJd3ayDDoF)
- **SpecRover**: SpecRover: Code Intent Extraction via LLMs (2025)
- **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899)
- **RepoGraph**: RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph
- **SuperCoder2.0**: SuperCoder2.0: Technical Report on Exploring the feasibility of LLMs as Autonomous Programmer (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.11190)
- **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941)
- **AEGIS**: AEGIS: An Agent-based Framework for General Bug Reproduction from Issue Descriptions (2025)
- **CoRNStack**: CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=iyJOUELYir)
- **OrcaLoca**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=LyUfPOvM6I)
- **DARS**: DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.14269)
- **Otter**: Otter: Generating Tests from Issues to Validate SWE Patches (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=b0jYs6JOZu)
- **Quadropic Insiders**: Quadropic Insiders : Syntheo Tops Swelite Feb (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://insiders.quadropic.com/insiders/syntheo-tops-swelite-feb)
- **Issue2Test**: Issue2Test: Generating Reproducing Test Cases from Issue Reports (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.16320)
- **KGCompass**: Enhancing repository-level software repair via repository-aware knowledge graphs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.21710)
- **CoSIL**: Issue Localization via LLM-Driven Iterative Code Graph Searching (2025)
- **InfantAgent-Next**: InfantAgent-Next: A Multimodal Generalist Agent for Automated Computer Interaction (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.10887)
- **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955)
- **SWERank**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849)
- **Nemotron-CORTEXA**: Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=k6p8UKRdH7)
- **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120)
- **SACL**: SACL: Understanding and Combating Textual Bias in Code Retrieval with Semantic-Augmented Reranking and Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.20081)
- **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2026)
- **OpenHands-Versa**: Coding Agents with Multimodal Browsing are Generalist Problem Solvers
- **SemAgent**: SemAgent: A Semantics Aware Program Repair Agent (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.16650)
- **Repeton**: Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.08173)
- **cAST**: cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.15655)
- **Prometheus**: Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.19942)
- **Git Context Controller**: Git Context Controller: Manage the Context of LLM-based Agents like Git (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00031)
- **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370)
- **BugPilot**: BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.19898)
- **TestPrune**: When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18270)
- **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611)
- **InfCode**: InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.16004)
- **GraphLocator**: GraphLocator: Graph-guided Causal Reasoning for Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.22469)

### 🧠 Memory-Enhanced Methods

*Systems with memory mechanisms*

- **Infant Agent**: Infant Agent: A Tool-Integrated, Logic-Driven Agent with Cost-Effective API Usage (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.01114)
- **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941)
- **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY)
- **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954)
- **ExpeRepair**: EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10484)
- **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229)
- **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361)
- **RepoMem**: Improving Code Localization with Repository Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01003)
- **AgentDiet**: Improving the Efficiency of LLM Agent Systems through Trajectory Reduction (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23586)
- **ReasoningBank**: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25140)
- **MemGovern**: MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.06789)

### 📚 Supervised Fine-Tuning (SFT)

*Models trained via supervised learning*

- **Lingma SWE-GPT**: SWE-GPT: A Process-Centric Language Model for Automated Software Improvement (2025)
- **ReSAT**: Repository Structure-Aware Training Makes SLMs Better Issue Resolver (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.19031)
- **Scaling data collection**: Scaling Data Collection for Training SWE Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://nebius.com/blog/posts/scaling-data-collection-for-training-swe-agents)
- **CodeXEmbed**: CodeXEmbed: A Generalist Embedding Model Family for Multilingual and Multi-task Code Retrieval (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=z3lG70Azbg)
- **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym
- **Thinking Longer**: Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.23803)
- **Search for training**: Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.13652)
- **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955)
- **MCTS-Refined CoT**: MCTS-Refined CoT: High-Quality Fine-Tuning Data for LLM-Based Repository Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.12728)
- **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://www.notion.so/SWE-Swiss-A-Multi-Task-Fine-Tuning-and-RL-Recipe-for-High-Performance-Issue-Resolution-21e174dedd4880ea829ed4c861c44f88)
- **Devstral**: Devstral: Fine-tuning Language Models for Coding Agent Applications (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25193)
- **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045)
- **SWE-Compressor**: Context as a Tool: Context Management for Long-Horizon SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.22087)
- **SWE-Lego**: SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.01426)
- **Agentic Rubrics**: Agentic Rubrics as Contextual Verifiers for SWE Agents (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.04171)

### 🎮 Reinforcement Learning (RL)

*Models trained via reinforcement learning*

- **SWE-RL**: SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=ULblO61XZ0)
- **SoRFT**: SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.acl-long.559/)
- **SEAlign**: SEAlign: Alignment Training for Software Engineering Agent (2026)
- **SWE-Dev1**: SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.16975)
- **Satori-SWE**: Satori-SWE: Evolutionary Test-Time Scaling for Sample-Efficient Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23604)
- **Agent-RLVR**: Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.11425)
- **DeepSWE**: DeepSWE: Training a State-of-the-Art Coding Agent from Scratch by Scaling RL (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://pretty-radio-b75.notion.site/DeepSWE-Training-a-Fully-Open-sourced-State-of-the-Art-Coding-Agent-by-Scaling-RL-22281902c1468193aabbe9a8c59bbe33)
- **SWE-Dev2**: SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.07636)
- **Tool-integrated RL**: Tool-integrated Reinforcement Learning for Repo Deep Search (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03012)
- **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://www.notion.so/SWE-Swiss-A-Multi-Task-Fine-Tuning-and-RL-Recipe-for-High-Performance-Issue-Resolution-21e174dedd4880ea829ed4c861c44f88)
- **SeamlessFlow**: SeamlessFlow: A Trainer Agent Isolation RL Framework Achieving Bubble-Free Pipelines via Tag Scheduling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.11553)
- **DAPO**: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03501)
- **CoreThink**: CoreThink: A Symbolic Reasoning Layer to reason over Long Horizon Tasks with LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.00971)
- **CWM**: CWM: An Open-Weights LLM for Research on Code Generation with World Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.02387)
- **EntroPO**: Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.12434)
- **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045)
- **FoldGRPO**: Scaling Long-Horizon LLM Agent via Context-Folding (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.11967)
- **GRPO-based Method**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=yPWJG9wgll)
- **TSP**: Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.emnlp-industry.109/) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.18653/v1/2025.emnlp-industry.109)
- **Self-play SWE-RL**: Toward Training Superintelligent Software Agents through Self-Play SWE-RL (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18552)
- **SWE-Playground**: Training Versatile Coding Agents in Synthetic Environments (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.12216)
- **Supervised RL**: Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.25992)
- **OSCA**: Scaling LLM Inference Efficiently with Optimized Sample Compute Allocation (2025) [![ACL](https://img.shields.io/badge/ACL-paper-0077B5?logo=googlescholar&logoColor=white)](https://aclanthology.org/2025.naacl-long.404/) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.18653/v1/2025.naacl-long.404)
- **SWE-RM**: SWE-RM: Execution-free Feedback For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.21919)
- **One Tool Is Enough**: One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.20957)
- **Let It Flow**: Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.24873)
- **KAT-Coder**: KAT-Coder Technical Report (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18779)
- **Seed1.5-Thinking**: Seed1.5-Thinking: Advancing Superb Reasoning Models with Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.13914)
- **Deepseek V3.2**: DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.02556)
- **Kimi-K2-Instruct**: Kimi K2: Open Agentic Intelligence (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.20534)
- **GLM-4.6**: gpt-oss-120b & gpt-oss-20b model card (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.10925)
- **Qwen3-Coder**: Qwen3 Technical Report (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.09388)
- **GLM-4.6**: Glm-4.5: Agentic, reasoning, and coding (arc) foundation models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.06471)
- **Minimax M2**: MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.13585)
- **LongCat-Flash-Think**: Introducing LongCat-Flash-Thinking: A Technical Report (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.18883)
- **MiMo-V2-Flash**: MiMo-V2-Flash Technical Report (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.02780)

### ⚡ Inference-Time Scaling

*Methods for scaling at inference time*

- **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=G7sIFXugTX)
- **ReasoningBank**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723)
- **SWE-PRM**: When Agents go Astray: Course-Correcting SWE Agents with PRMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.02360)
- **SIADAFIX**: SIADAFIX: issue description response for adaptive program repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.16059)

### 📥 Data Collection Methods

*Techniques for collecting training data*

- **SWE-rebench**: SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=nMpJoVmRy1)
- **RepoLaunch**: SWE-bench Goes Live! (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=OGWkr7gXka)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059)
- **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550)
- **Multi-Docker-Eval**: Multi-Docker-Eval: A `Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.06915)

### 🔬 Data Synthesis Methods

*Approaches for synthetic data generation*

- **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY)
- **R2E-Gym**: R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=7evvwwdo3z)
- **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757)
- **SWE-smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=63iVrXc8cC)
- **SWE-Flow**: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![OpenReview](https://img.shields.io/badge/OpenReview-paper-8C1B13?logo=openreview&logoColor=white)](https://openreview.net/forum?id=P9DQ2IExgS)
- **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724)

### 📈 Data Analysis

*Analysis of datasets and benchmarks*

- **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024)
- **Patch Correctness**: Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.15223)
- **UTBoost**: UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09289)
- **Trustworthiness**: Is Your Automated Software Engineer Trustworthy? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17812)
- **Rigorous agentic benchmarks**: Establishing Best Practices for Building Rigorous Agentic Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02825)
- **The SWE-Bench Illusion**: The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.12286)
- **Revisiting SWE-Bench**: Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Based Code Models (2025) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.1109/ICSE-Companion66252.2025.00075)
- **SPICE**: SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity,
               Test Coverage, and Effort Estimation (2025)
- **Data contamination**: Does SWE-Bench-Verified Test Agent Ability or Model Memory? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.10218)

### 🔍 Methods Analysis

*Comparative analysis of different methods*

- **Context Retrieval**: On The Importance of Reasoning for Context Retrieval in Repository-Level Code Editing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.04464)
- **Evaluating software development agents**: Evaluating Software Development Agents: Patch Patterns, Code Quality, and Issue Complexity in Real-World GitHub Scenarios (2025) [![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)](http://dx.doi.org/10.1109/SANER64311.2025.00068)
- **Overthinking**: The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.08235)
- **Beyond final code**: Beyond Final Code: A Process-Oriented Error Analysis of Software Development Agents in Real-World GitHub Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.12374)
- **GSO**: GSO: Challenging Software Optimization Tasks for Evaluating SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23671)
- **Dissecting the SWE-Bench Leaderboards**: Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17208)
- **Security analysis**: How Safe Are AI-Generated Patches? A Large-scale Study on Security Risks in LLM and Agentic Automated Program Repair on SWE-bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02976)
- **Failures analysis**: An Empirical Study on Failures in Automated Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.13941)
- **SeaView**: SeaView: Software Engineering Agent Visual Interface for Enhanced Workflow (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08696)
- **SWEnergy**: SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs (2026)
- **Strong-Weak Model Collaboration**: An Empirical Study on Strong-Weak Model Collaboration for Repo-level Code Generation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.20182)
- **Agents in the Wild** (2025) [![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)](https://insights.logicstar.ai/)
<!-- END PAPERS -->

---

<!-- START TABLES -->
## 📋 Statistical Tables

Comprehensive tables and statistics about issue resolution datasets, methods, and benchmarks.


### Evaluation & Training Datasets

_A comprehensive survey and statistical overview of issue resolution datasets. We categorize these datasets based on programming language, modality support, source repositories, data scale (Amount), and the availability of reproducible execution environments._

| **Dataset** | **Language** | **Multimodal** | **Repos** | **Amount** | **Environment** | **Link** |
|---|---|---|---|---|---|---|
| **Single-PL Datasets** |  |  |  |  |  |  |
| SWE-Fixer | Python | ❌ | 856 | 115,406 | ❌ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/InternLM/SWE-Fixer) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/internlm/SWE-Fixer-Train-110K) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/internlm/SWE-Fixer-Eval) |
| SWE-smith | Python | ❌ | 128 | 50k | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-smith) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench/SWE-smith) |
| SWE-Lego | Python | ❌ | 3,251 | 32,119 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Lego/SWE-Lego) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Lego/datasets) |
| SWE-rebench | Python | ❌ | 3,468 | 21,336 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-rebench/SWE-bench-fork) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/nebius/SWE-rebench) |
| SWE-bench-train | Python | ❌ | 37 | 19k | ❌ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/princeton-nlp/SWE-bench/viewer/default/train) |
| SWE-Flow | Python | ❌ | 74 | 18,081 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/Hambaobao/SWE-Flow) |
| Skywork-SWE | Python | ❌ | 2,531 | 10,169 | ✅ | - |
| R2E-Gym | Python | ❌ | 10 | 8,135 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/R2E-Gym/R2E-Gym) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/R2E-Gym/datasets) |
| RepoForge | Python | ❌ | - | 7.3k | ✅ | - |
| SWE-bench-extra | Python | ❌ | 2k | 6.38k | ✅ | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/nebius/SWE-bench-extra) |
| SWE-Gym | Python | ❌ | 11 | 2,438 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Gym/SWE-Gym) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Gym/datasets) |
| SWE-bench | Python | ❌ | 12 | 2,294 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/princeton-nlp/SWE-bench) |
| SWE-bench-java | Java | ❌ | 19 | 1,797 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/multi-swe-bench/multi-swe-bench-env) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Daoguang/Multi-SWE-bench) |
| FEA-bench | Python | ❌ | 83 | 1,401 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/microsoft/FEA-Bench/) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/microsoft/FEA-Bench) |
| SWE-bench-Live | Python | ❌ | 164 | 1,565 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/microsoft/SWE-bench-Live) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live) |
| Loc-Bench | Python | ❌ | - | 560 | ❌ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/gersteinlab/LocAgent) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/czlll/Loc-Bench_V1) |
| SWE-bench Verified | Python | ❌ | - | 500 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified) |
| SWE-bench Lite | Python | ❌ | 12 | 300 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite) |
| SWE-MERA | Python | ❌ | 200 | 300 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/MERA-Evaluation/SWE-MERA-submissions) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/MERA-evaluation/SWE-MERA) |
| SWE-Bench-CL | Python | ❌ | 8 | 273 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/thomasjoshi/agents-never-forget) |
| SWE-Sharp-Bench | C# | ❌ | 17 | 150 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/microsoft/prose/tree/main/misc/SWE-Sharp-Bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/microsoft/SWE-Sharp-Bench) |
| SWE-Perf | Python | ❌ | 12 | 140 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Perf/swe-perf) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-Perf/SWE-Perf) |
| Visual SWE-bench | Python | ✅ | 11 | 133 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/luolin101/CodeV) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/luolin101/Visual-SWE-bench) |
| SWE-EVO | Python | ❌ | 7 | 48 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/bdqnghi/SWE-EVO) |
| **Multi-PL Datasets** |  |  |  |  |  |  |
| SWE-Mirror | Python, Rust, Go | ❌ | 40 | 60k | ✅ | - |
| Multi-SWE-bench | Java, JS, TS, Go, Rust, C, C++ | ❌ | 76 | 4,723 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/multi-swe-bench/multi-swe-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/ByteDance-Seed/Multi-SWE-bench) |
| Swing-Bench | Python, Go, C++, Rust | ❌ | 400 | 2300 | ✅ | - |
| SWE-PolyBench | Python, Java, JS, TS | ❌ | 21 | 2,110 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/amazon-science/SWE-PolyBench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/AmazonScience/SWE-PolyBench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Sellopale/SWE-PolyBench_500) |
| SWE-Compass | Python, JS, TS, Java, C, C++, Go, Rust, Kotlin, C# | ❌ | - | 2,000 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/kwaipilot/SWE-Compass/) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Kwaipilot/SWE-Compass) |
| SWE-Bench Pro | Python, Go, TS | ❌ | 41 | 1,865 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/scaleapi/SWE-bench_Pro-os) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) |
| SWE-bench++ | Python, Go, TS, JS, Ruby, PHP, Java, Rust, C++, C#, C | ❌ | 3,971 | 1,782 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/TuringEnterprises/SWE-Bench-plus-plus) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/TuringEnterprises/SWE-Bench-plus-plus) |
| SWE-Lancer | JS, TS | ❌ | - | 1,488 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/openai/frontier-evals) |
| OmniGIRL | Python, TS, Java, JS | ✅ | 15 | 959 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/deepsoftwareanalytics/omnigirl) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Deep-Software-Analytics/OmniGIRL) |
| SWE-bench Multimodal | JS, TS, HTML, CSS | ✅ | 17 | 619 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal) |
| SWE-fficiency | Python, Cython | ❌ | 9 | 498 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/swefficiency/swefficiency-site) |
| SWE-Factory | Python, Java, JS, TS | ❌ | 12 | 430 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/DeepSoftwareAnalytics/swe-factory) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Factory) |
| SWE-bench-Live-MultiLang \& Windows | Python, JS, TS, C, C++, C#, Java, Go, Rust | ❌ | 238 | 418 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/microsoft/SWE-bench-Live) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench-Live/MultiLang) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench-Live/Windows) |
| SWE-bench Multilingual | C, C++, Go, Java, JS, TS, Rust, Python, Ruby, PHP | ❌ | 42 | 300 | ✅ | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-bench/SWE-bench) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual) |
| SWE-InfraBench | Python, TS | ❌ | - | 100 | ✅ | - |

---

### Training Trajectory Datasets

_A survey of trajectory datasets used for agent training or analysis. We list the programming language, number of source repositories, and total trajectories for each dataset._

| **Dataset** | **Language** | **Repos** | **Amount** | **Link** |
|---|---|---|---|---|
| SWE-Fixer | Python | 856 | 69,752 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/InternLM/SWE-Fixer) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/internlm/SWE-Fixer-Train-Editing-CoT-70K) |
| SWE-rebench | Python | 1,823 | 67,074 | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) |
| R2E-Gym | Python | 10 | 3,321 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/R2E-Gym/R2E-Gym) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/R2E-Gym/R2EGym-SFT-Trajectories) |
| SWE-Synth | Python | 11 | 3,018 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/FSoft-AI4Code/SWE-Synth) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/swesynth/SWE-Synth_Moatless-SFT-Trajectories) |
| SWE-Factory | Python | 10 | 2,809 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/DeepSoftwareAnalytics/swe-factory) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-Factory/DeepSWE-Agent-Kimi-K2-Trajectories-2.8K) |
| SWE-Gym | Python | 11 | 491 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Gym/SWE-Gym) [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/SWE-Gym/OpenHands-SFT-Trajectories) |
| SWE-Lego | Python | 3251 | 14.6k | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Lego/SWE-Lego) |

---

### SFT-based Methods

_Overview of SFT-based methods for issue resolution. This table categorizes models by their base architecture and training scaffold (Sorted by Performance)._

| **Model Name** | **Base Model** | **Size** | **Arch.** | **Training Scaffold** | **Res.(%)** | **Code** | **Data** | **Model** |
|---|---|---|---|---|---|---|---|---|
| SWE-rebench-openhands-Qwen3-235B-A22B | Qwen3-235B-A22B | 235B-A22B | MoE | OpenHands | 59.9 | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-235B-A22B) |
| SWE-Lego-Qwen3-32B | Qwen3-32B | 32B | Dense | OpenHands | 57.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Lego/SWE-Lego) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Lego/datasets) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Lego/SWE-Lego-Qwen3-32B) |
| SWE-rebench-openhands-Qwen3-30B-A3B | Qwen3-30B-A3B | 30B-A3B | MoE | OpenHands | 49.7 | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-30B-A3B) |
| Devstral | Mistral Small 3 | 22B | Dense | OpenHands | 46.8 | - | [![Website](https://img.shields.io/badge/Website-blog-5B9BD5?logo=googlechrome&logoColor=white)](https://mistral.ai/news/devstral) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/mistralai/Devstral-Small-2507) |
| Co-PatcheR | Qwen2.5-Coder-14B | 3×14B | Dense | PatchPilot-mini | 46.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/ucsb-mlsec/Co-PatcheR) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/collections/UCSB-SURFI/co-patcher) |
| SWE-Swiss-32B | Qwen2.5-32B-Instruct | 32B | Dense | Agentless | 45.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/zhenyuhe00/SWE-Swiss) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Swiss/datasets) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Swiss/models) |
| SWE-Lego-Qwen3-8B | Qwen3-8B | 8B | Dense | OpenHands | 44.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Lego/SWE-Lego) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Lego/datasets) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Lego/SWE-Lego-Qwen3-8B) |
| Lingma SWE-GPT | Qwen2.5-72B-Instruct | 72B | Dense | SWESynInfer | 30.2 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/LingmaTongyi/Lingma-SWE-GPT) | - | - |
| SWE-Gym-Qwen-32B | Qwen2.5-Coder-32B | 32B | Dense | OpenHands, MoatlessTools | 20.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Gym/SWE-Gym) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Gym) |
| Lingma SWE-GPT | Qwen2.5-Coder-7B | 7B | Dense | SWESynInfer | 18.2 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/LingmaTongyi/Lingma-SWE-GPT) | - | - |
| SWE-Gym-Qwen-14B | Qwen2.5-Coder-14B | 14B | Dense | OpenHands, MoatlessTools | 16.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Gym/SWE-Gym) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Gym) |
| SWE-Gym-Qwen-7B | Qwen2.5-Coder-7B | 7B | Dense | OpenHands, MoatlessTools | 10.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/SWE-Gym/SWE-Gym) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Gym) |

---

### RL-based Methods

_A comprehensive overview of specialized models for issue resolution, categorized by parameter size. The table details each model's base architecture, the training scaffold used for rollout, the type of reward signal employed (Outcome vs. Process), and their performance results (Res. %) on issue resolution benchmarks._

| **Model Name** | **Base Model** | **Size** | **Arch.** | **Train. Scaffold** | **Reward** | **Res.(%)** | **Code** | **Data** | **Model** |
|---|---|---|---|---|---|---|---|---|---|
| **560B Models (MoE)** |  |  |  |  |  |  |  |  |  |
| LongCat-Flash-Think | LongCatFlash-Base | 560B-A27B | MoE | R2E-Gym | Outcome | 60.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/meituan-longcat/LongCat-Flash-Thinking) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/meituan-longcat/LongCat-Flash-Thinking) |
| **72B Models** |  |  |  |  |  |  |  |  |  |
| Kimi-Dev | Qwen 2.5-72B-Base | 72B | Dense | BugFixer + TestWriter | Outcome | 60.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/MoonshotAI/Kimi-Dev) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/moonshotai/Kimi-Dev-72B) |
| SWE-RL | Llama-3.3-70B-Instruct | 70B | Dense | Agentless-mini | Outcome | 41.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/facebookresearch/swe-rl) | - | - |
| Multi-turn RL(Nebius) | Qwen2.5-72B-Instruct | 72B | Dense | SWE-agent | Outcome | 39.0 | - | - | - |
| Agent-RLVR-RM-72B | Qwen2.5-Coder-72B | 72B | Dense | Localization + Repair | Outcome | 27.8 | - | - | - |
| Agent-RLVR-72B | Qwen2.5-Coder-72B | 72B | Dense | Localization + Repair | Outcome | 22.4 | - | - | - |
| **32B Models** |  |  |  |  |  |  |  |  |  |
| OpenHands Critic | Qwen2.5-Coder-32B | 32B | Dense | SWE-Gym | - | 66.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/All-Hands-AI/OpenHands) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/OpenHands/openhands-critic-32b-exp-20250417) |
| KAT-Dev-32B | Qwen3-32B | 32B | Dense | - | - | 62.4 | - | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/Kwaipilot/KAT-Dev) |
| SWE-Swiss-32B | Qwen2.5-32B-Instruct | 32B | Dense | - | Outcome | 60.2 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/zhenyuhe00/SWE-Swiss) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Swiss/datasets) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/SWE-Swiss/models) |
| FoldAgent | Seed-OSS-36B-Instruct | 36B | Dense | FoldAgent | Process | 58.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/sunnweiwei/FoldAgent) | [![Website](https://img.shields.io/badge/Website-data-5B9BD5?logo=googlechrome&logoColor=white)](https://drive.google.com/file/u/0/d/1aX5xXAN5R-gLKd8A0AY-troxXJRawyAM/view?usp=sharing\&pli=1) | - |
| SeamlessFlow-32B | Qwen3-32B | 32B | Dense | SWE-agent | Outcome | 45.8 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/Chojikun/seamlessflow) | - | - |
| DeepSWE | Qwen3-32B | 32B | Dense | R2E-Gym | Outcome | 42.2 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/agentica-project/rllm) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/R2E-Gym/R2E-Gym-Subset) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/agentica-org/DeepSWE-Preview) |
| SA-SWE-32B | - | 32B | Dense | SkyRL-Agent | - | 39.4 | - | - | - |
| OpenHands LM v0.1 | Qwen2.5-Coder-32B | 32B | Dense | SWE-Gym | - | 37.2 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/All-Hands-AI/OpenHands) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/OpenHands/openhands-lm-32b-v0.1) |
| SWE-Dev-32B | Qwen2.5-Coder-32B | 32B | Dense | OpenHands | Outcome | 36.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/THUDM/SWE-Dev) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/zai-org/SWE-Dev-32B) |
| Satori-SWE | Qwen2.5-Coder-32B | 32B | Dense | Retriever + Code editor | Outcome | 35.8 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/satori-reasoning/Satori-SWE) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/Satori-reasoning) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/Satori-reasoning) |
| SoRFT-32B | Qwen2.5-Coder-32B | 32B | Dense | Agentless | Outcome | 30.8 | - | - | - |
| Agent-RLVR-32B | Qwen2.5-Coder-32B | 32B | Dense | Localization + Repair | Outcome | 21.6 | - | - | - |
| **14B Models** |  |  |  |  |  |  |  |  |  |
| Agent-RLVR-14B | Qwen2.5-Coder-14B | 14B | Dense | Localization + Repair | Outcome | 18.0 | - | - | - |
| SEAlign-14B | Qwen2.5-Coder-14B | 14B | Dense | OpenHands | Process | 17.7 | - | - | - |
| **7-8B Models** |  |  |  |  |  |  |  |  |  |
| SeamlessFlow-8B | Qwen3-8B | 8B | Dense | SWE-agent | Outcome | 27.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/Chojikun/seamlessflow) | - | - |
| SWE-Dev-7B | Qwen2.5-Coder-7B | 7B | Dense | OpenHands | Outcome | 23.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/THUDM/SWE-Dev) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/zai-org/SWE-Dev-7B) |
| SoRFT-7B | Qwen2.5-Coder-7B | 7B | Dense | Agentless | Outcome | 21.4 | - | - | - |
| SWE-Dev-8B | Llama-3.1-8B | 8B | Dense | OpenHands | Outcome | 18.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/THUDM/SWE-Dev) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/zai-org/SWE-Dev-8B) |
| SEAlign-7B | Qwen2.5-Coder-7B | 7B | Dense | OpenHands | Process | 15.0 | - | - | - |
| SWE-Dev-9B | GLM-4-9B | 9B | Dense | OpenHands | Outcome | 13.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/THUDM/SWE-Dev) | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/zai-org/SWE-Dev-9B) |

---

### General Foundation Models

_Overview of general foundation models evaluated on issue resolution. The table details the specific inference scaffolds (e.g., OpenHands, Agentless) employed during the evaluation process to achieve the reported results._

| **Model Name** | **Size** | **Arch.** | **Inf. Scaffold** | **Reward** | **Res.(%)** | **Code** | **Model** |
|---|---|---|---|---|---|---|---|
| MiMo-V2-Flash | 309B-A15B | MoE | Agentless | Outcome | 73.4 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/XiaomiMiMo/MiMo-V2-Flash) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash) |
| KAT-Coder | - | - | Claude Code | Outcome | 73.4 | - | [![Website](https://img.shields.io/badge/Website-model-5B9BD5?logo=googlechrome&logoColor=white)](https://www.modelscope.cn/models/Kwaipilot/KAT-Dev-72B-Exp) |
| Deepseek V3.2 | 671B-A37B | MoE | Claude Code, RooCode | - | 73.1 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale) |
| Kimi-K2-Instruct | 1T | MoE | Agentless | Outcome | 71.6 | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/moonshotai/Kimi-K2-Instruct) |
| Qwen3-Coder | 480B-A35B | MoE | OpenHands | Outcome | 69.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/QwenLM/Qwen3-Coder) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/collections/Qwen/qwen3-coder) |
| GLM-4.6 | 355B-A32B | MoE | OpenHands | Outcome | 68.0 | - | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/zai-org/GLM-4.6) |
| gpt-oss-120b | 116.8B-A5.1B | MoE | Internal tool | Outcome | 62.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/openai/gpt-oss) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/openai/gpt-oss-120b) |
| Minimax M2 | 230B-10B | MoE | R2E-Gym | Outcome | 61.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/MiniMax-AI/MiniMax-M2) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/MiniMaxAI/MiniMax-M2) |
| gpt-oss-20b | 20.9B-A3.6B | MoE | Internal tool | Outcome | 60.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/openai/gpt-oss) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/openai/gpt-oss-20b) |
| GLM-4.5-Air | 106B-A12B | MoE | OpenHands | Outcome | 57.6 | - | - |
| Minimax M1-80k | 456B-A45.9B | MoE | Agentless | Outcome | 56.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/MiniMax-AI/MiniMax-M1) | [![Website](https://img.shields.io/badge/Website-model-5B9BD5?logo=googlechrome&logoColor=white)](https://www.modelscope.cn/models/MiniMax/MiniMax-M1-80k) |
| Minimax M1-40k | 456B-A45.9B | MoE | Agentless | Outcome | 55.6 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/MiniMax-AI/MiniMax-M1) | [![Website](https://img.shields.io/badge/Website-model-5B9BD5?logo=googlechrome&logoColor=white)](https://www.modelscope.cn/models/MiniMax/MiniMax-M1-40k/summary) |
| Seed1.5-Thinking | 200B-A20B | MoE | - | Outcome | 47.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5) | - |
| Llama 4 Maverick | 400B-A17B | MoE | mini-SWE-agent | Outcome | 21.0 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/meta-llama/llama-models/tree/main/models/llama4) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) |
| Llama 4 Scout | 109B-17B | MoE | mini-SWE-agent | Outcome | 9.1 | [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/meta-llama/llama-models/tree/main/models/llama4) | [![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) |

---

<!-- END TABLES -->

---

<!-- START USAGE -->
## 🚀 Quick Start


**Windows:**
```cmd
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Options:**
- `[1]` Add Paper - Interactive paper entry with duplicate check
- `[2]` Add Table - Update statistical tables
- `[3]` Batch Import - Import papers from CSV template
- `[4]` Sync & Build - Render website and sync README

**Manual operations:**
```bash
# Local preview
mkdocs serve

# Deploy (or push to GitHub for auto-deploy via Actions)
mkdocs gh-deploy
```

---
<!-- END USAGE -->

---

## 🤝 Contributing

We welcome contributions! To add new papers or tables:

1. Fork this repository
2. Run `run.bat` (Windows) or `run.sh` (Linux/Mac)
3. Or manually edit YAML/CSV files in `data/` directory
4. Submit a PR with your changes

---

## 🌟 Related Work

### Code Generation

The application of LLMs in the programming domain has witnessed explosive growth. Early research focused primarily on function-level code generation, with benchmarks such as [HumanEval](https://arxiv.org/abs/2107.03374) serving as standard metrics. However, generic benchmarks often fail to capture the nuances of real-world development. To bridge this gap, recent initiatives have attempted to extend evaluation tasks to align more closely with realistic software development scenarios, revealing the limitations of general models in specialized domains. Concurrently, methods are also evolving to capture these broader contexts. While foundational approaches primarily relied on SFT or standard retrieval-augmented generation, RL-based methods emerged as a pivotal direction for handling complex coding tasks.

**Related:**
- **HumanEval**: [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)
- **Program Synthesis**: [Program Synthesis with Large Language Models](https://arxiv.org/abs/2108.07732)
- **Repository-Level Code Completion**: [RLCoder: Reinforcement Learning for Repository-Level Code Completion](https://doi.org/10.1109/ICSE55347.2025.00014)
- **Domain-Specific Benchmarks**: [Top General Performance = Top Domain Performance? DomainCodeBench](https://arxiv.org/abs/2412.18573)
- **Long-Context Code Models**: [Long Code Arena](https://arxiv.org/abs/2406.11612)
- **Multitask Fine-Tuning**: [MFTCoder: Boosting Code LLMs with Multitask Fine-Tuning](https://doi.org/10.1145/3637528.3671609)
- **RAG for Code**: [RAG or Fine-tuning? A Comparative Study on LCMs-based Code Completion in Industry](https://doi.org/10.1145/3696630.3728549), [Repoformer: Selective Retrieval for Repository-Level Code Completion](https://openreview.net/forum?id=ZUnIGtP0Nf), [CodeRAG-Bench](https://aclanthology.org/2025.findings-naacl.176/)
- **Code Generation Survey**: [A Survey on Large Language Models for Code Generation](https://doi.org/10.1145/3747588)

### Automated Software Generation

The primary goal of this task is to autonomously construct complete and executable software systems starting from high-level natural language requirements. Unlike code completion, it necessitates covering the Software Development Life Cycle (SDLC), including requirement analysis, system design, coding, and testing. To address the complexity and potential logic inconsistencies in this process, state-of-the-art frameworks leverage multi-agent collaboration, simulating human development teams to decompose complex tasks into streamlined and verifiable workflows.

**Related:**
- **ChatDev**: [Communicative Agents for Software Development](https://doi.org/10.18653/v1/2024.acl-long.810)
- **MetaGPT**: [Meta Programming for Multi-Agent Collaborative Framework](https://openreview.net/forum?id=VtmBAGCN7o)
- **RPG**: [Repository Planning Graph for Unified and Scalable Codebase Generation](https://arxiv.org/abs/2509.16198)

### Automated Software Maintenance

Issue resolution is intrinsically linked to the broader domain of automated software maintenance. Methodologies established in this field are frequently encapsulated as callable tools to augment the capabilities of LLMs in software development tasks.

**Related:**

- **Bug Reproduction**: [AssertFlip](https://arxiv.org/abs/2507.17542), [Automated Generation of Issue-Reproducing Tests](https://arxiv.org/abs/2509.01616)
- **Fault Localization**: 
  - [A Survey on Software Fault Localization](https://doi.org/10.1109/TSE.2016.2521368)
  - [Where should the bugs be fixed?](https://doi.org/10.1145/2393596.2393616)
  - [DreamLoc](https://doi.org/10.1109/TR.2021.3104728)
  - [Effective Bug Triage](https://doi.org/10.1109/ISSRE.2014.17)
  - [BLAZE](https://doi.org/10.1109/TSE.2025.3579574)
  - [Bridging Bug Localization and Issue Fixing](https://arxiv.org/abs/2502.15292)
  - [Hierarchical Reward Modeling](https://aclanthology.org/2025.findings-emnlp.966/)
- **Code Search**: [A Benchmark for Localizing Code and Non-Code Issues](https://arxiv.org/abs/2509.25242)
- **Test Generation**: 
  - [TDD-Bench Verified](https://arxiv.org/abs/2412.02883)
  - [SWT-Bench](https://proceedings.neurips.cc/paper_files/paper/2024/file/94f093b41fc2666376fb1f667fe282f3-Paper-Conference.pdf)
  - [TDFlow](https://arxiv.org/abs/2510.23761)
- **Security**: [Is Vibe Coding Safe?](https://arxiv.org/abs/2512.03262)
- **Survey Papers**:
  - [A Survey on Automated Program Repair Techniques](https://arxiv.org/abs/2303.18184)
  - [A Survey of Learning-based Automated Program Repair](https://doi.org/10.1145/3631974)

### Automated Environment Setup

Recent initiatives focus on automating the configuration of runtime environments for entire repositories. This capability develops in parallel with data construction for issue resolution.

**Related:**
- **EnvBench**: [A Benchmark for Automated Environment Setup](https://openreview.net/forum?id=izy1oaAOeX)
- **PIPer**: [On-Device Environment Setup via Online Reinforcement Learning](https://arxiv.org/abs/2509.25455)
- **Automated Benchmark Generation**: [Automated Benchmark Generation for Repository-Level Coding Tasks](https://openreview.net/forum?id=BQA7dkV3iZ)

### Related Surveys

Existing surveys primarily focus on code generation or other tasks within the software engineering domain. This paper bridges this gap by offering the first systematic survey dedicated to the entire spectrum of issue resolution, ranging from non-agent approaches to the latest agentic advancements.

**Related:**
- [A Survey on Large Language Models for Code Generation](https://doi.org/10.1145/3747588)
- [Agents in software engineering: survey, landscape, and vision](https://doi.org/10.1007/s10515-025-00544-2)
- [A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System](https://arxiv.org/abs/2510.09721)

> **Note:** The BibTeX sources and automated scripts for managing these references are maintained in the `bib2data/` directory for internal use. These resources are not required for general users contributing papers to this project.

---

## 📄 Citation

If you use this project or related survey in your research or system, please cite the following:

**Li, Caihua, Guo, Lianghong, Wang, Yanlin, et al.** (2026). *Advances, Frontiers, and Future of Issue Resolution in Software Engineering: A Comprehensive Survey*. TechRxiv.  DOI: [10.36227/techrxiv.176779734.47868328/v2](https://doi.org/10.36227/techrxiv.176779734.47868328/v2)

**BibTeX:**

```bibtex
@article{li2026advances,
  title={Advances, Frontiers, and Future of Issue Resolution in Software Engineering: A Comprehensive Survey},
  author={Li, Caihua and Guo, Lianghong and Wang, Yanlin and Guo, Daya and Tao, Wei and Shan, Zhenyu and Liu, Mingwei and Chen, Jiachi and Liu, Runze and Song, Haoyu and Tang, Duyu and Zhang, Hongyu and Zheng, Zibin},
  journal={TechRxiv},
  year={2026},
  page={1375056},
  dor={10.36227/techrxiv.176779734.47868328/v2},
  publisher={IEEE}
}
```

Once published on arXiv or at a conference, please replace the entry with the official citation information (authors, DOI/arXiv ID, conference name, etc.).
---

## 🙏 Acknowledgements

We would like to express our sincere gratitude to:

- **[@chao-peng](https://github.com/chao-peng)** ([Dr. Chao Peng](https://chao-peng.github.io)), ByteDance Software Engineering Lab, for providing valuable suggestions on the Challenges and Opportunities section of our survey.

- **[@EuniAI/awesome-code-agents](https://github.com/EuniAI/awesome-code-agents)** for providing an excellent reference on managing survey papers through documentation systems and inspiring our project structure.

- All **contributors** who have helped improve this project through issues, pull requests, and discussions.

- The **open-source community** for developing the amazing tools and frameworks that made this project possible.

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


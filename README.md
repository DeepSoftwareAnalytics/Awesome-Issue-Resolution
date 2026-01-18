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
![Papers Count](https://img.shields.io/badge/papers-175-green?style=for-the-badge&logo=googlescholar&logoColor=white)

[**📖 Documentation Website**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/) | [**📄 Full Paper**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/) | [**📋 Tables & Resources**](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)

<img src="docs/images/awesome-issue-resolution.png" alt="Awesome Issue Resolution" width="60%">

</div>

---

## 📖 Abstract

Based on a systematic review of **175 papers and online resources**, this survey establishes a holistic theoretical framework for Issue Resolution in software engineering. We examine how **Large Language Models (LLMs)** are transforming the automation of GitHub issue resolution. Beyond the theoretical analysis, we have curated a comprehensive collection of datasets and model training resources, which are continuously synchronized with our GitHub repository and project documentation website. 

**🔍 Explore This Survey:**

- 📊 **[Data](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#data)**: Evaluation and training datasets, data collection and synthesis methods
- 🛠️ **[Methods](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#methods)**: Training-free (agent/workflow) and training-based (SFT/RL) approaches  
- 🔍 **[Analysis](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/#analysis)**: Insights into both data characteristics and method performance
- 📋 **[Tables & Resources](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/tables/)**: Comprehensive statistical tables and resources
- 📄 **[Full Paper](https://deepsoftwareanalytics.github.io/Awesome-Issue-Resolution/paper/)**: Read the complete survey paper

---

<!-- START PAPERS -->
## 📚 Complete Paper List


> **Total: 170 papers** across 14 categories


### 📊 Evaluation Datasets

*Benchmarks for evaluating issue resolution systems*

- **SWE-bench**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770)
- **SWE-bench Lite**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770)
- **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openai.com/index/introducing-swe-bench-verified/)
- **SWE-bench-java**: SWE-bench-java: A GitHub Issue Resolving Benchmark for Java (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.14354)
- **Visual SWE-bench**: CodeV: Issue Resolving with Visual Data (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/)
- **SWE-Lancer**: SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12115)
- **Multi-SWE-bench**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.02605)
- **SWE-PolyBench**: SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08703)
- **SWE-bench Multilingual**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798)
- **SwingArena**: SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23932)
- **SWE-bench Multimodal**: SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.03859)
- **OmniGIRL**: OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3728871)
- **SWE-bench-Live**: SWE-bench Goes Live! (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23419)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059)
- **SWE-Perf**: SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.12415)
- **SWE-Bench Pro**: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16941)
- **SWE-InfraBench**: SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=XX0ciUwfXa)
- **SWE-Sharp-Bench**: SWE-Sharp-Bench: A Reproducible Benchmark for C\# Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02352)
- **SWE-fficiency**: SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.06090)
- **SWE-Compass**: SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.05459)
- **SWE-Bench++**: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.17419)
- **SWE-EVO**: SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18470)
- **SWE-Lego**: SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving (2026) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.01426)

### 🎯 Training Datasets

*Datasets for training issue resolution agents*

- **SWE-bench-train**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770)
- **SWE-bench-extra**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770)
- **Multi-SWE-RL**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.02605)
- **R2E-Gym**: R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.07164)
- **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757)
- **LocAgent**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350)
- **SWE-Smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798)
- **SWE-Fixer**: SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.05040)
- **SWELoc**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849)
- **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.21139)
- **SWE-Flow**: SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09003)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **Skywork-SWE**: Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.19290)
- **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550)
- **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724)
- **SWE-Bench++**: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.17419)

### 🤖 Single-Agent Systems

*Individual autonomous agents for issue resolution*

- **SWE-agent**: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15793)
- **PatchPilot**: PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.02747)
- **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120)
- **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954)
- **SE-Agent**: SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02085)
- **TOM-SWE**: TOM-SWE: User Mental Modeling For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.21903)
- **Live-SWE-agent**: SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02085)

### 👥 Multi-Agent Systems

*Collaborative multi-agent frameworks*

- **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.17927)
- **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384)
- **CodeR**: CodeR: Issue Resolving with Multi-Agent and Task Graphs (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.01304)
- **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.16741)
- **OrcaLora**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350)
- **DEI**: Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.07060)
- **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899)
- **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.20285)
- **CodeCoR**: CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.07811)
- **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229)
- **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23348)
- **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361)
- **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370)
- **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611)

### 🔄 Workflow-Based Methods

*Structured pipeline approaches*

- **Agentless**: Agentless: Demystifying LLM-based Software Engineering Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.01489)
- **Conversational Pipeline**: Exploring the Potential of Conversational Test Suite Based Program Repair on SWE-bench (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.04485)
- **SynFix**: SynFix: Dependency-Aware Program Repair via RelationGraph Analysis (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.252/)
- **CodeV**: CodeV: Issue Resolving with Visual Data (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/)
- **GUIRepair**: Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visual Software Issue Fixing (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.16136)

### 🛠️ Tool-Augmented Methods

*Methods leveraging external tools*

- **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.17927)
- **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384)
- **SWE-agent**: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15793)
- **Alibaba LingmaAgent**: Alibaba LingmaAgent: Improving Automated Issue Resolution via Comprehensive Repository Exploration (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3696630.3728549)
- **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.16741)
- **SpecRover**: SpecRover: Code Intent Extraction via LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1109/ICSE55347.2025.00080)
- **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899)
- **RepoGraph**: RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.14684)
- **SuperCoder2.0**: SuperCoder2.0: Technical Report on Exploring the feasibility of LLMs as Autonomous Programmer (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.11190)
- **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941)
- **AEGIS**: AEGIS: An Agent-based Framework for General Bug Reproduction from Issue Descriptions (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.18015)
- **OrcaLoca**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350)
- **Otter**: Otter: Generating Tests from Issues to Validate SWE Patches (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.05368)
- **CoRNStack**: CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=iyJOUELYir)
- **Issue2Test**: Issue2Test: Generating Reproducing Test Cases from Issue Reports (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.16320)
- **KGCompass**: Enhancing repository-level software repair via repository-aware knowledge graphs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.21710)
- **CoSIL**: Issue Localization via LLM-Driven Iterative Code Graph Searching (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.22424)
- **InfantAgent-Next**: InfantAgent-Next: A Multimodal Generalist Agent for Automated Computer Interaction (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.10887)
- **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955)
- **SWERank**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849)
- **Nemotron-CORTEXA**: Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=k6p8UKRdH7)
- **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120)
- **SACL**: SACL: Understanding and Combating Textual Bias in Code Retrieval with Semantic-Augmented Reranking and Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.20081)
- **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23348)
- **OpenHands-Versa**: Coding Agents with Multimodal Browsing are Generalist Problem Solvers (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.03011)
- **Repeton**: Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.08173)
- **cAST**: cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.15655)
- **Prometheus**: Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.19942)
- **Git Context Controller**: Git Context Controller: Manage the Context of LLM-based Agents like Git (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00031)
- **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370)
- **TestPrune**: When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18270)
- **e-Otter++**: Execution-Feedback Driven Test Generation from SWE Issues (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.06365)
- **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611)

### 🧠 Memory-Enhanced Methods

*Systems with memory mechanisms*

- **Infant Agent**: Infant Agent: A Tool-Integrated, Logic-Driven Agent with Cost-Effective API Usage (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.01114)
- **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941)
- **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY)
- **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954)
- **ExpeRepair**: EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10484)
- **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229)
- **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361)
- **RepoMem**: Improving Code Localization with Repository Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01003)
- **ReasoningBank**: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25140)

### 📚 Supervised Fine-Tuning (SFT)

*Models trained via supervised learning*

- **Lingma SWE-GPT**: Lingma SWE-GPT: An Open Development-Process-Centric Language Model for Automated Software Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.00622)
- **Scaling data collection**: Scaling Data Collection for Training SWE Agents (2024)
- **CodeXEmbed**: CodeXEmbed: A Generalist Embedding Model Family for Multilingual and Multi-task Code Retrieval (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=z3lG70Azbg)
- **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.21139)
- **TSP**: Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.emnlp-industry.109/) [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/Gengar0215/TSP-framework)
- **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955)
- **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025)
- **Devstral**: Devstral: Fine-tuning Language Models for Coding Agent Applications (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25193)
- **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045)
- **SWE-Compressor**: Context as a Tool: Context Management for Long-Horizon SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.22087)

### 🎮 Reinforcement Learning (RL)

*Models trained via reinforcement learning*

- **SWE-RL**: SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.18449)
- **SoRFT**: SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.20127)
- **SEAlign**: SEAlign: Alignment Training for Software Engineering Agent (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.18455)
- **SWE-Dev<sub>1</sub>**: SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.16975)
- **Satori-SWE**: Satori-SWE: Evolutionary Test-Time Scaling for Sample-Efficient Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23604)
- **Agent-RLVR**: Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.11425)
- **DeepSWE**: DeepSWE: Training a State-of-the-Art Coding Agent from Scratch by Scaling RL (2025)
- **SWE-Dev<sub>2</sub>**: SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.07636)
- **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025)
- **SeamlessFlow**: SeamlessFlow: A Trainer Agent Isolation RL Framework Achieving Bubble-Free Pipelines via Tag Scheduling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.11553)
- **DAPO**: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03501)
- **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045)
- **FoldGRPO**: Scaling Long-Horizon LLM Agent via Context-Folding (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.11967)
- **GRPO-based Method**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01132)
- **Self-play SWE-RL**: Toward Training Superintelligent Software Agents through Self-Play SWE-RL (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18552)
- **SWE-RM**: SWE-RM: Execution-free Feedback For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.21919)

### ⚡ Inference-Time Scaling

*Methods for scaling at inference time*

- **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.20285)
- **CodeMonkeys**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723)
- **SWE-PRM**: When Agents go Astray: Course-Correcting SWE Agents with PRMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.02360)
- **ReasoningBank**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723)

### 📥 Data Collection Methods

*Techniques for collecting training data*

- **SWE-rebench**: SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.20411)
- **RepoLaunch**: SWE-bench Goes Live! (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23419)
- **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954)
- **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059)
- **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550)
- **Multi-Docker-Eval**: Multi-Docker-Eval: A `Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.06915)

### 🔬 Data Synthesis Methods

*Approaches for synthetic data generation*

- **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY)
- **R2E-Gym**: R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.07164)
- **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757)
- **SWE-smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798)
- **SWE-Flow**: SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09003)
- **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724)

### 📈 Data Analysis

*Analysis of datasets and benchmarks*

- **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openai.com/index/introducing-swe-bench-verified/)
- **SWE-Bench+**: SWE-Bench+: Enhanced Coding Benchmark for LLMs (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.06992)
- **Patch Correctness**: Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://arxiv.org/abs/2503.15223)
- **UTBoost**: UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09289)
- **Trustworthiness**: Is Your Automated Software Engineer Trustworthy? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17812)
- **Rigorous agentic benchmarks**: Establishing Best Practices for Building Rigorous Agentic Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02825)
- **The SWE-Bench Illusion**: The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.12286)
- **Revisiting SWE-Bench**: Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Based Code Models (2025)
- **SPICE**: SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.09108)
- **Data contamination**: Does SWE-Bench-Verified Test Agent Ability or Model Memory? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.10218)

### 🔍 Methods Analysis

*Comparative analysis of different methods*

- **Context Retrieval**: On The Importance of Reasoning for Context Retrieval in Repository-Level Code Editing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.04464)
- **Evaluating software development agents**: Evaluating Software Development Agents: Patch Patterns, Code Quality, and Issue Complexity in Real-World GitHub Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1109/SANER64311.2025.00068)
- **Overthinking**: The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.08235)
- **Beyond final code**: Beyond Final Code: A Process-Oriented Error Analysis of Software Development Agents in Real-World GitHub Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.12374)
- **GSO**: GSO: Challenging Software Optimization Tasks for Evaluating SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23671)
- **Dissecting the SWE-Bench Leaderboards**: Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17208)
- **Security analysis**: Are AI-Generated Fixes Secure? Analyzing LLM and Agent Patches on SWE-bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02976)
- **Failures analysis**: An Empirical Study on Failures in Automated Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.13941)
- **SeaView**: SeaView: Software Engineering Agent Visual Interface for Enhanced Workflow (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08696)
- **SWEnergy**: SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.09543)
<!-- END PAPERS -->

---

## 🤝 Contributing

We welcome contributions to this survey! If you'd like to add new papers or fix errors:

### 🚀 Quick Add (Recommended)

Use our interactive scripts to add papers easily:

**Windows:**
```cmd
add_paper.bat
```

**Linux/Mac:**
```bash
chmod +x add_paper.sh
./add_paper.sh
```

**Or use Python directly (cross-platform):**
```bash
python scripts/add_paper.py
```

The script will guide you through:
1. Selecting a category
2. Entering paper information (title, authors, links, etc.)
3. Automatically saving to the correct YAML file

### 📝 Manual Process

1. Fork this repository
2. Add paper entries in the corresponding YAML file under `data/` directory (e.g., `papers_evaluation_datasets.yaml`, `papers_single_agent.yaml`, etc.)
3. Follow the existing format with fields: `short_name`, `title`, `authors`, `venue`, `year`, and `links` (arxiv, github, huggingface)
4. Run `python scripts/sync_readme.py` to update the README.md
5. Run `python scripts/render_papers.py` to update the documentation website
6. Submit a PR with your changes

📖 **Detailed instructions:** See [scripts/README_ADD_PAPER.md](scripts/README_ADD_PAPER.md) or [QUICK_START.md](QUICK_START.md)

---

## 📄 Citation

If you use this project or related survey in your research or system, please cite the following BibTeX:

```bibtex
@misc{li2025awesome_issue_resolution,
    title       = {Advances and Frontiers of LLM-based Issue Resolution in Software Engineering A Comprehensive Survey},
    author      = {Caihua Li and Lianghong Guo and Yanlin Wang and Daya Guo and Wei Tao and Zhenyu Shan and Mingwei Liu and Jiachi Chen and Haoyu Song and Duyu Tang and Hongyu Zhang and Zibin Zheng},
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


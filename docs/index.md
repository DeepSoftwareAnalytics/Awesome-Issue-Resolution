# ✨ Awesome Issue Resolution

<div class="hero-section">
    <h1 class="hero-title">✨ Awesome Issue Resolution</h1>
    <p class="hero-subtitle">Advances, Frontiers, and Future of Issue Resolution in Software Engineering: A Comprehensive Survey</p>
    
    <!-- Dynamic Badges -->
    <div class="hero-badges-dynamic">
        <a href="https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution" target="_blank">
            <img src="https://img.shields.io/github/stars/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&logo=github&color=4c1" alt="GitHub Stars">
        </a>
        <a href="https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/fork" target="_blank">
            <img src="https://img.shields.io/github/forks/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&logo=github&color=blue" alt="Forks">
        </a>
        <a href="https://github.com/sindresorhus/awesome" target="_blank">
            <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome" style="height: 28px;">
        </a>
        <a href="paper/" target="_blank">
            <img src="https://img.shields.io/badge/PAPER-PDF-4285F4?style=for-the-badge&logo=googledocs&logoColor=white" alt="Paper">
        </a>
        <a href="https://arxiv.org/abs/XXXX.XXXXX" target="_blank">
            <img src="https://img.shields.io/badge/arXiv-2501.XXXXX-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv">
        </a>
        <a href="tables/" target="_blank">
            <img src="https://img.shields.io/badge/TABLES-Statistics-blue?style=for-the-badge&logo=databricks" alt="Tables">
        </a>
        <a href="https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/graphs/contributors" target="_blank">
            <img src="https://img.shields.io/github/contributors/DeepSoftwareAnalytics/Awesome-Issue-Resolution?style=for-the-badge&color=green&logo=github" alt="Contributors">
        </a>
        <img src="https://img.shields.io/badge/papers-135-green?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Papers Count">
    </div>
    
    <div class="hero-image">
        <img src="images/awesome-issue-resolution.png" alt="Awesome Issue Resolution" loading="lazy">
    </div>
</div>

---

## 📖 Abstract

<div class="abstract-content" markdown="1">

Based on a systematic review of 135 publications, this survey establishes a holistic theoretical framework for Issue Resolution in software engineering. We examine how Large Language Models (LLMs) are transforming the automation of GitHub issue resolution. Beyond the theoretical analysis, we have curated a comprehensive collection of datasets and model training resources, which are continuously synchronized with our [GitHub repository](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution) and project documentation website. 

**🔍 Explore This Survey:**

- 📊 **[Data](#data)**: Evaluation and training datasets, data collection and synthesis methods
- 🛠️ **[Methods](#methods)**: Training-free (agent/workflow) and training-based (SFT/RL) approaches  
- 🔍 **[Analysis](#analysis)**: Insights into both data characteristics and method performance
- 📋 **[Tables & Resources](tables/)**: Comprehensive statistical tables and resources
- 📄 **[Full Paper](paper/)**: Read the complete survey paper

<figure class="framework-figure">
    <img src="images/framework.png" alt="Overview of the Issue Resolution taxonomy" loading="lazy">
    <figcaption>Figure: Overview of the Issue Resolution framework.</figcaption>
</figure>

</div>

---

## 📊 Data

This section covers the datasets used for evaluation and training, as well as methods for data construction.

### Evaluation Datasets

<!-- START PAPERS:evaluation_datasets -->
* **SWE-bench**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770){: target="_blank" }
* **SWE-bench Lite**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770){: target="_blank" }
* **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openai.com/index/introducing-swe-bench-verified/){: target="_blank" }
* **SWE-bench-java**: SWE-bench-java: A GitHub Issue Resolving Benchmark for Java (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.14354){: target="_blank" }
* **Visual SWE-bench**: CodeV: Issue Resolving with Visual Data (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/){: target="_blank" }
* **SWE-Lancer**: SWE-Lancer: Can Frontier LLMs Earn \1 Million from Real-World Freelance Software Engineering? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12115){: target="_blank" }
* **Multi-SWE-bench**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.02605){: target="_blank" }
* **SWE-PolyBench**: SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08703){: target="_blank" }
* **SWE-bench Multilingual**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798){: target="_blank" }
* **SwingArena**: SwingArena: Competitive Programming Arena for Long-context GitHub Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23932){: target="_blank" }
* **SWE-bench Multimodal**: SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.03859){: target="_blank" }
* **OmniGIRL**: OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3728871){: target="_blank" }
* **SWE-bench-Live**: SWE-bench Goes Live! (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23419){: target="_blank" }
* **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954){: target="_blank" }
* **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059){: target="_blank" }
* **SWE-Perf**: SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.12415){: target="_blank" }
* **SWE-Bench Pro**: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16941){: target="_blank" }
* **SWE-InfraBench**: SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=XX0ciUwfXa){: target="_blank" }
* **SWE-Sharp-Bench**: SWE-Sharp-Bench: A Reproducible Benchmark for C\# Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02352){: target="_blank" }
* **SWE-fficiency**: SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.06090){: target="_blank" }
* **SWE-Compass**: SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.05459){: target="_blank" }
* **SWE-Bench++**: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.17419){: target="_blank" }
* **SWE-EVO**: SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18470){: target="_blank" }
<!-- END PAPERS:evaluation_datasets -->

### Training Datasets

<!-- START PAPERS:training_datasets -->
* **SWE-bench-train**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770){: target="_blank" }
* **SWE-bench-extra**: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770){: target="_blank" }
* **Multi-SWE-RL**: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.02605){: target="_blank" }
* **R2E-Gym**: R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.07164){: target="_blank" }
* **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757){: target="_blank" }
* **LocAgent**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350){: target="_blank" }
* **SWE-Smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798){: target="_blank" }
* **SWE-Fixer**: SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.05040){: target="_blank" }
* **SWELoc**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849){: target="_blank" }
* **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.21139){: target="_blank" }
* **SWE-Flow**: SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09003){: target="_blank" }
* **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954){: target="_blank" }
* **Skywork-SWE**: Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.19290){: target="_blank" }
* **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550){: target="_blank" }
* **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724){: target="_blank" }
* **SWE-Bench++**: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.17419){: target="_blank" }
<!-- END PAPERS:training_datasets -->

### Data Collection

<!-- START PAPERS:data_collection -->
* **SWE-rebench**: SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.20411){: target="_blank" }
* **RepoLaunch**: SWE-bench Goes Live! (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23419){: target="_blank" }
* **SWE-Factory**: SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10954){: target="_blank" }
* **SWE-MERA**: SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059){: target="_blank" }
* **RepoForge**: RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550){: target="_blank" }
* **Multi-Docker-Eval**: Multi-Docker-Eval: A `Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.06915){: target="_blank" }
<!-- END PAPERS:data_collection -->

### Data Synthesis

<!-- START PAPERS:data_synthesis -->
* **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY){: target="_blank" }
* **R2E-Gym**: R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.07164){: target="_blank" }
* **SWE-Synth**: SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Language Models in Resolving Real-World Bugs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.14757){: target="_blank" }
* **SWE-smith**: SWE-smith: Scaling Data for Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.21798){: target="_blank" }
* **SWE-Flow**: SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09003){: target="_blank" }
* **SWE-Mirror**: SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724){: target="_blank" }
<!-- END PAPERS:data_synthesis -->

---

## 🛠️ Methods

This section covers both training-free and training-based methods for issue resolution.

### 🧑‍💻 Training-free Methods

#### Single-Agent

<!-- START PAPERS:single_agent -->
* **SWE-agent**: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15793){: target="_blank" }
* **PatchPilot**: PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.02747){: target="_blank" }
* **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120){: target="_blank" }
* **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954){: target="_blank" }
* **SE-Agent**: SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02085){: target="_blank" }
* **TOM-SWE**: TOM-SWE: User Mental Modeling For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.21903){: target="_blank" }
* **Live-SWE-agent**: SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02085){: target="_blank" }
<!-- END PAPERS:single_agent -->

#### Multi-Agent

<!-- START PAPERS:multi_agent -->
* **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.17927){: target="_blank" }
* **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384){: target="_blank" }
* **CodeR**: CodeR: Issue Resolving with Multi-Agent and Task Graphs (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.01304){: target="_blank" }
* **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.16741){: target="_blank" }
* **OrcaLora**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350){: target="_blank" }
* **DEI**: Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.07060){: target="_blank" }
* **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899){: target="_blank" }
* **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.20285){: target="_blank" }
* **CodeCoR**: CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.07811){: target="_blank" }
* **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229){: target="_blank" }
* **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23348){: target="_blank" }
* **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361){: target="_blank" }
* **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370){: target="_blank" }
* **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611){: target="_blank" }
<!-- END PAPERS:multi_agent -->

#### Workflow

<!-- START PAPERS:workflow -->
* **Agentless**: Agentless: Demystifying LLM-based Software Engineering Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.01489){: target="_blank" }
* **Conversational Pipeline**: Exploring the Potential of Conversational Test Suite Based Program Repair on SWE-bench (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.04485){: target="_blank" }
* **SynFix**: SynFix: Dependency-Aware Program Repair via RelationGraph Analysis (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.252/){: target="_blank" }
* **CodeV**: CodeV: Issue Resolving with Visual Data (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/){: target="_blank" }
* **GUIRepair**: Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visual Software Issue Fixing (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.16136){: target="_blank" }
<!-- END PAPERS:workflow -->

#### Tool

<!-- START PAPERS:tool -->
* **MAGIS**: MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.17927){: target="_blank" }
* **AutoCodeRover**: AutoCodeRover: Autonomous Program Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3650212.3680384){: target="_blank" }
* **SWE-agent**: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15793){: target="_blank" }
* **Alibaba LingmaAgent**: Alibaba LingmaAgent: Improving Automated Issue Resolution via Comprehensive Repository Exploration (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1145/3696630.3728549){: target="_blank" }
* **OpenHands**: OpenHands: An Open Platform for AI Software Developers as Generalist Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.16741){: target="_blank" }
* **SpecRover**: SpecRover: Code Intent Extraction via LLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1109/ICSE55347.2025.00080){: target="_blank" }
* **MarsCode Agent**: MarsCode Agent: AI-native Automated Bug Fixing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.00899){: target="_blank" }
* **RepoGraph**: RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.14684){: target="_blank" }
* **SuperCoder2.0**: SuperCoder2.0: Technical Report on Exploring the feasibility of LLMs as Autonomous Programmer (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.11190){: target="_blank" }
* **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941){: target="_blank" }
* **AEGIS**: AEGIS: An Agent-based Framework for General Bug Reproduction from Issue Descriptions (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.18015){: target="_blank" }
* **OrcaLoca**: OrcaLoca: An LLM Agent Framework for Software Issue Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.00350){: target="_blank" }
* **Otter**: Otter: Generating Tests from Issues to Validate SWE Patches (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.05368){: target="_blank" }
* **CoRNStack**: CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=iyJOUELYir){: target="_blank" }
* **Issue2Test**: Issue2Test: Generating Reproducing Test Cases from Issue Reports (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.16320){: target="_blank" }
* **KGCompass**: Enhancing repository-level software repair via repository-aware knowledge graphs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.21710){: target="_blank" }
* **CoSIL**: Issue Localization via LLM-Driven Iterative Code Graph Searching (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.22424){: target="_blank" }
* **InfantAgent-Next**: InfantAgent-Next: A Multimodal Generalist Agent for Automated Computer Interaction (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.10887){: target="_blank" }
* **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955){: target="_blank" }
* **SWERank**: SweRank: Software Issue Localization with Code Ranking (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.07849){: target="_blank" }
* **Nemotron-CORTEXA**: Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=k6p8UKRdH7){: target="_blank" }
* **LCLM**: Putting It All into Context: Simplifying Agents with LCLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.08120){: target="_blank" }
* **SACL**: SACL: Understanding and Combating Textual Bias in Code Retrieval with Semantic-Augmented Reranking and Localization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.20081){: target="_blank" }
* **SWE-Debate**: SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23348){: target="_blank" }
* **OpenHands-Versa**: Coding Agents with Multimodal Browsing are Generalist Problem Solvers (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.03011){: target="_blank" }
* **Repeton**: Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.08173){: target="_blank" }
* **cAST**: cAST: Enhancing Code Retrieval-Augmented Generation with Structural Chunking via Abstract Syntax Tree (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.15655){: target="_blank" }
* **Prometheus**: Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.19942){: target="_blank" }
* **Git Context Controller**: Git Context Controller: Manage the Context of LLM-based Agents like Git (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00031){: target="_blank" }
* **Trae Agent**: Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370){: target="_blank" }
* **TestPrune**: When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18270){: target="_blank" }
* **e-Otter++**: Execution-Feedback Driven Test Generation from SWE Issues (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.06365){: target="_blank" }
* **Meta-RAG**: Meta-RAG on Large Codebases Using Code Summarization (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02611){: target="_blank" }
<!-- END PAPERS:tool -->

#### Memory

<!-- START PAPERS:memory -->
* **Infant Agent**: Infant Agent: A Tool-Integrated, Logic-Driven Agent with Cost-Effective API Usage (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.01114){: target="_blank" }
* **EvoCoder**: LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.13941){: target="_blank" }
* **Learn-by-interact**: Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=3UKOzGWCVY){: target="_blank" }
* **DGM**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.22954){: target="_blank" }
* **ExpeRepair**: EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.10484){: target="_blank" }
* **Agent KB**: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.06229){: target="_blank" }
* **SWE-Exp**: SWE-Exp: Experience-Driven Software Issue Resolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361){: target="_blank" }
* **RepoMem**: Improving Code Localization with Repository Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01003){: target="_blank" }
* **ReasoningBank**: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25140){: target="_blank" }
<!-- END PAPERS:memory -->

#### Inference-time Scaling

<!-- START PAPERS:inference_scaling -->
* **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.20285){: target="_blank" }
* **CodeMonkeys**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723){: target="_blank" }
* **SWE-PRM**: When Agents go Astray: Course-Correcting SWE Agents with PRMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.02360){: target="_blank" }
* **ReasoningBank**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723){: target="_blank" }
<!-- END PAPERS:inference_scaling -->

### 🧠 Training-based Methods

#### SFT-based Methods

<!-- START PAPERS:sft -->
* **Lingma SWE-GPT**: Lingma SWE-GPT: An Open Development-Process-Centric Language Model for Automated Software Improvement (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2411.00622){: target="_blank" }
* **Scaling data collection**: Scaling Data Collection for Training SWE Agents (2024)
* **CodeXEmbed**: CodeXEmbed: A Generalist Embedding Model Family for Multilingual and Multi-task Code Retrieval (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openreview.net/forum?id=z3lG70Azbg){: target="_blank" }
* **SWE-Gym**: Training Software Engineering Agents and Verifiers with SWE-Gym (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.21139){: target="_blank" }
* **TSP**: Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.emnlp-industry.109/){: target="_blank" } [![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)](https://github.com/Gengar0215/TSP-framework){: target="_blank" }
* **Co-PatcheR**: Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.18955){: target="_blank" }
* **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025)
* **Devstral**: Devstral: Fine-tuning Language Models for Coding Agent Applications (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25193){: target="_blank" }
* **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045){: target="_blank" }
* **SWE-Compressor**: Context as a Tool: Context Management for Long-Horizon SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.22087){: target="_blank" }
<!-- END PAPERS:sft -->

#### RL-based Methods

<!-- START PAPERS:rl -->
* **SWE-RL**: SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.18449){: target="_blank" }
* **SoRFT**: SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.20127){: target="_blank" }
* **SEAlign**: SEAlign: Alignment Training for Software Engineering Agent (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.18455){: target="_blank" }
* **SWE-Dev<sub>1</sub>**: SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.16975){: target="_blank" }
* **Satori-SWE**: Satori-SWE: Evolutionary Test-Time Scaling for Sample-Efficient Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23604){: target="_blank" }
* **Agent-RLVR**: Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.11425){: target="_blank" }
* **DeepSWE**: DeepSWE: Training a State-of-the-Art Coding Agent from Scratch by Scaling RL (2025)
* **SWE-Dev<sub>2</sub>**: SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.07636){: target="_blank" }
* **SWE-Swiss**: SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution (2025)
* **SeamlessFlow**: SeamlessFlow: A Trainer Agent Isolation RL Framework Achieving Bubble-Free Pipelines via Tag Scheduling (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.11553){: target="_blank" }
* **DAPO**: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03501){: target="_blank" }
* **Kimi-Dev**: Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045){: target="_blank" }
* **FoldGRPO**: Scaling Long-Horizon LLM Agent via Context-Folding (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.11967){: target="_blank" }
* **GRPO-based Method**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01132){: target="_blank" }
* **Self-play SWE-RL**: Toward Training Superintelligent Software Agents through Self-Play SWE-RL (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18552){: target="_blank" }
* **SWE-RM**: SWE-RM: Execution-free Feedback For Software Engineering Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.21919){: target="_blank" }
<!-- END PAPERS:rl -->

---

## 🔍 Analysis

This section includes research works that provide in-depth analysis and discussion of data, methods, and related phenomena in issue resolution.

### Data Analysis

<!-- START PAPERS:data_analysis -->
* **SWE-bench Verified**: Introducing SWE-bench Verified | OpenAI (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://openai.com/index/introducing-swe-bench-verified/){: target="_blank" }
* **SWE-Bench+**: SWE-Bench+: Enhanced Coding Benchmark for LLMs (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.06992){: target="_blank" }
* **Patch Correctness**: Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://arxiv.org/abs/2503.15223){: target="_blank" }
* **UTBoost**: UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.09289){: target="_blank" }
* **Trustworthiness**: Is Your Automated Software Engineer Trustworthy? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17812){: target="_blank" }
* **Rigorous agentic benchmarks**: Establishing Best Practices for Building Rigorous Agentic Benchmarks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02825){: target="_blank" }
* **The SWE-Bench Illusion**: The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.12286){: target="_blank" }
* **Revisiting SWE-Bench**: Revisiting SWE-Bench: On the Importance of Data Quality for LLM-Based Code Models (2025)
* **SPICE**: SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.09108){: target="_blank" }
* **Data contamination**: Does SWE-Bench-Verified Test Agent Ability or Model Memory? (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.10218){: target="_blank" }
<!-- END PAPERS:data_analysis -->

### Methods Analysis

<!-- START PAPERS:methods_analysis -->
* **Context Retrieval**: On The Importance of Reasoning for Context Retrieval in Repository-Level Code Editing (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2406.04464){: target="_blank" }
* **Evaluating software development agents**: Evaluating Software Development Agents: Patch Patterns, Code Quality, and Issue Complexity in Real-World GitHub Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](http://dx.doi.org/10.1109/SANER64311.2025.00068){: target="_blank" }
* **Overthinking**: The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.08235){: target="_blank" }
* **Beyond final code**: Beyond Final Code: A Process-Oriented Error Analysis of Software Development Agents in Real-World GitHub Scenarios (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.12374){: target="_blank" }
* **GSO**: GSO: Challenging Software Optimization Tasks for Evaluating SWE-Agents (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23671){: target="_blank" }
* **Dissecting the SWE-Bench Leaderboards**: Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.17208){: target="_blank" }
* **Security analysis**: Are AI-Generated Fixes Secure? Analyzing LLM and Agent Patches on SWE-bench (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.02976){: target="_blank" }
* **Failures analysis**: An Empirical Study on Failures in Automated Issue Solving (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.13941){: target="_blank" }
* **SeaView**: SeaView: Software Engineering Agent Visual Interface for Enhanced Workflow (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.08696){: target="_blank" }
* **SWEnergy**: SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.09543){: target="_blank" }
<!-- END PAPERS:methods_analysis -->

---

## 🚀 Challenges and Opportunities

<div class="challenges-content" markdown="1">

### High computational overhead

The scalability of SWE agents is bottlenecked by the high costs of sandboxed environments and long-context inference. Optimization strategies are required to streamline these resource-intensive loops without sacrificing performance.

### Opacity in resource consumption

Benchmarks often overlook efficiency, masking the high costs of techniques like inference-time scaling. Standardized reporting of latency and token usage is crucial for guiding the development of cost-effective agents.

### Limited visually-grounded reasoning

Reliance on text proxies for UI interpretation limits effectiveness. Future research can adopt intrinsic multi-modal solutions, such as code-centric MLLMs, to better bridge the gap between visual rendering and underlying code logic.

### Safety risks in autonomous resolution

High autonomy carries risks of destructive actions, such as accidental code deletion. Future systems should integrate safeguards, such as Git-based version control, to ensure autonomous modifications remain secure and reversible.

### Lack of fine-grained reward signals

Reinforcement learning is hindered by sparse, binary feedback. Integrating fine-grained signals from compiler diagnostics and execution traces is necessary to guide models through complex reasoning steps.

### Data leakage and contamination

As benchmarks approach saturation, evaluation validity is compromised by data leakage. Future frameworks must strictly enforce decontamination protocols to ensure fairness and reliability.

### Lack of universality across SE domains

While current issue resolution tasks mirror development workflows, they represent only a fraction of the full Software Development Life Cycle (SDLC). Future research should broaden the scope of issue resolution tasks to develop more versatile automated software generation methods.

</div>

---

## 📚 More to read

<div class="resources-content" markdown="1">

- 📂 **GitHub Repository**: [DeepSoftwareAnalytics/Awesome-Issue-Resolution](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution)
- 📄 **Paper PDF**: [PDF](paper.md)
- 📧 **Contact**: [GitHub Issues](https://github.com/DeepSoftwareAnalytics/Awesome-Issue-Resolution/issues)

</div>

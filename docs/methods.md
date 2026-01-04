---
title: Methods
---

# 🛠️ Methods

This section highlights the different techniques and frameworks proposed for resolving SWE tasks, categorized into **Training-free Methods** and **Training-based Methods**.

---

## 🧑‍💻 Training-free Methods

These approaches generally focus on designing effective **Agent Frameworks** or **Modules** (such as tools and memory) to maximize the LLM's reasoning capability without extensive model fine-tuning.

### Frameworks

Frameworks typically define the overall structure for how agents interact with the environment and execute tasks.

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

---

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

---

#### Workflow

<!-- START PAPERS:workflow -->
* **Agentless**: Agentless: Demystifying LLM-based Software Engineering Agents (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.01489){: target="_blank" }
* **Conversational Pipeline**: Exploring the Potential of Conversational Test Suite Based Program Repair on SWE-bench (2024) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.04485){: target="_blank" }
* **SynFix**: SynFix: Dependency-Aware Program Repair via RelationGraph Analysis (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.252/){: target="_blank" }
* **CodeV**: CodeV: Issue Resolving with Visual Data (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://aclanthology.org/2025.findings-acl.384/){: target="_blank" }
* **GUIRepair**: Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visual Software Issue Fixing (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.16136){: target="_blank" }
<!-- END PAPERS:workflow -->

---

### Modules

Core components used to enhance the capabilities of agents within a framework.

#### Tool

Tools for code analysis, testing, localization and other utilities.

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

---

#### Memory

Experience replay, knowledge storage, and learning from history.

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

---

#### Inference-time Scaling

Test-time compute optimization and search strategies.

<!-- START PAPERS:inference_scaling -->
* **SWE-Search**: SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.20285){: target="_blank" }
* **CodeMonkeys**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723){: target="_blank" }
* **SWE-PRM**: When Agents go Astray: Course-Correcting SWE Agents with PRMs (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.02360){: target="_blank" }
* **ReasoningBank**: CodeMonkeys: Scaling Test-Time Compute for Software Engineering (2025) [![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.14723){: target="_blank" }
<!-- END PAPERS:inference_scaling -->

---

## 🧠 Training-based Methods

Focuses on adapting LLMs to SWE tasks through model training and fine-tuning on specific datasets.

### SFT-based Methods (Supervised Fine-Tuning)

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

---

### RL-based Methods (Reinforcement Learning)

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

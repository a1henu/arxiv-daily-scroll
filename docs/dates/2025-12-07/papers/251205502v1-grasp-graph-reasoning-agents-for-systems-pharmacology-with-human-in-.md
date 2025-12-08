---
layout: default
title: GRASP: Graph Reasoning Agents for Systems Pharmacology with Human-in-the-Loop
---

# GRASP: Graph Reasoning Agents for Systems Pharmacology with Human-in-the-Loop
**arXiv**：[2512.05502v1](https://arxiv.org/abs/2512.05502) · [PDF](https://arxiv.org/pdf/2512.05502.pdf)  
**作者**：Omid Bazgir, Vineeth Manthapuri, Ilia Rattsev, Mohammad Jafarnejad  

**一句话要点**：提出GRASP框架，通过图推理代理和人在环界面，提升定量系统药理学模型开发的可访问性和严谨性。

**关键词**：定量系统药理学, 图推理代理, 人在环界面, 知识图谱, 模型编译, 参数对齐

## 3 点简述
- 核心问题：定量系统药理学建模耗时，限制专家吞吐量，需平衡自然语言交互与生物医学保真度。
- 方法要点：将模型编码为类型化知识图，编译为可执行代码，采用两阶段工作流和广度优先参数对齐。
- 实验或效果：在LLM评估中，GRASP在生物合理性、数学正确性等方面优于基线，依赖发现F1达0.95。

## 摘要（原文）

> Quantitative Systems Pharmacology (QSP) modeling is essential for drug development but it requires significant time investment that limits the throughput of domain experts. We present \textbf{GRASP} -- a multi-agent, graph-reasoning framework with a human-in-the-loop conversational interface -- that encodes QSP models as typed biological knowledge graphs and compiles them to executable MATLAB/SimBiology code while preserving units, mass balance, and physiological constraints. A two-phase workflow -- \textsc{Understanding} (graph reconstruction of legacy code) and \textsc{Action} (constraint-checked, language-driven modification) -- is orchestrated by a state machine with iterative validation. GRASP performs breadth-first parameter-alignment around new entities to surface dependent quantities and propose biologically plausible defaults, and it runs automatic execution/diagnostics until convergence. In head-to-head evaluations using LLM-as-judge, GRASP outperforms SME-guided CoT and ToT baselines across biological plausibility, mathematical correctness, structural fidelity, and code quality (\(\approx\)9--10/10 vs.\ 5--7/10). BFS alignment achieves F1 = 0.95 for dependency discovery, units, and range. These results demonstrate that graph-structured, agentic workflows can make QSP model development both accessible and rigorous, enabling domain experts to specify mechanisms in natural language without sacrificing biomedical fidelity.


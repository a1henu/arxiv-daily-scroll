---
layout: default
title: Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back
---

# Explainable Innovation Engine: Dual-Tree Agent-RAG with Methods-as-Nodes and Verifiable Write-Back
**arXiv**：[2603.09192v1](https://arxiv.org/abs/2603.09192) · [PDF](https://arxiv.org/pdf/2603.09192.pdf)  
**作者**：Renwei Meng  

**一句话要点**：提出双树代理RAG系统，以方法为节点实现可解释和可验证的创新生成

**关键词**：检索增强生成, 可解释人工智能, 方法节点, 双树结构, 代理系统, 可验证创新

## 3 点简述
- 核心问题：传统RAG系统依赖扁平文本块检索，在多步合成中控制性和可解释性有限
- 方法要点：引入方法节点作为知识单元，构建加权溯源树和层次聚类抽象树，代理选择合成算子并记录轨迹
- 实验或效果：在六个领域评估显示优于基线，尤其在推导密集型任务中提升显著，溯源回溯和剪枝起互补作用

## 摘要（原文）

> Retrieval-augmented generation (RAG) improves factual grounding, yet most systems rely on flat chunk retrieval and provide limited control over multi-step synthesis. We propose an Explainable Innovation Engine that upgrades the knowledge unit from text chunks to methods-as-nodes. The engine maintains a weighted method provenance tree for traceable derivations and a hierarchical clustering abstraction tree for efficient top-down navigation. At inference time, a strategy agent selects explicit synthesis operators (e.g., induction, deduction, analogy), composes new method nodes, and records an auditable trajectory. A verifier-scorer layer then prunes low-quality candidates and writes validated nodes back to support continual growth. Expert evaluation across six domains and multiple backbones shows consistent gains over a vanilla baseline, with the largest improvements on derivation-heavy settings, and ablations confirm the complementary roles of provenance backtracking and pruning. These results suggest a practical path toward controllable, explainable, and verifiable innovation in agentic RAG systems. Code is available at the project GitHub repository https://github.com/xiaolu-666113/Dual-Tree-Agent-RAG.


---
layout: default
title: ModelWisdom: An Integrated Toolkit for TLA+ Model Visualization, Digest and Repair
---

# ModelWisdom: An Integrated Toolkit for TLA+ Model Visualization, Digest and Repair
**arXiv**：[2602.12058v1](https://arxiv.org/abs/2602.12058) · [PDF](https://arxiv.org/pdf/2602.12058.pdf)  
**作者**：Zhiyong Chen, Jialun Cao, Chang Xu, Shing-Chi Cheung  

**一句话要点**：提出ModelWisdom集成工具包，通过可视化与LLM增强TLA+模型检查的可解释性与可操作性

**关键词**：TLA+模型检查, 可视化工具, 大语言模型应用, 模型修复, 交互式调试

## 3 点简述
- 核心问题：TLA+模型检查中反例解释困难、状态图理解复杂、模型修复手动成本高。
- 方法要点：提供交互式可视化、图优化、模型摘要与LLM解释、模型修复支持。
- 实验或效果：将原始输出转化为可解释工作流，提升理解并减少调试工作量。

## 摘要（原文）

> Model checking in TLA+ provides strong correctness guarantees, yet practitioners continue to face significant challenges in interpreting counterexamples, understanding large state-transition graphs, and repairing faulty models. These difficulties stem from the limited explainability of raw model-checker output and the substantial manual effort required to trace violations back to source specifications. Although the TLA+ Toolbox includes a state diagram viewer, it offers only a static, fully expanded graph without folding, color highlighting, or semantic explanations, which limits its scalability and interpretability. We present ModelWisdom, an interactive environment that uses visualization and large language models to make TLA+ model checking more interpretable and actionable. ModelWisdom offers: (i) Model Visualization, with colorized violation highlighting, click-through links from transitions to TLA+ code, and mapping between violating states and broken properties; (ii) Graph Optimization, including tree-based structuring and node/edge folding to manage large models; (iii) Model Digest, which summarizes and explains subgraphs via large language models (LLMs) and performs preprocessing and partial explanations; and (iv) Model Repair, which extracts error information and supports iterative debugging. Together, these capabilities turn raw model-checker output into an interactive, explainable workflow, improving understanding and reducing debugging effort for nontrivial TLA+ specifications. The website to ModelWisdom is available: https://model-wisdom.pages.dev. A demonstrative video can be found at https://www.youtube.com/watch?v=plyZo30VShA.


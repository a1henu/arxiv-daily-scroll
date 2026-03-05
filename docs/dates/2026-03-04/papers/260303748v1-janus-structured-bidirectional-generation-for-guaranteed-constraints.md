---
layout: default
title: JANUS: Structured Bidirectional Generation for Guaranteed Constraints and Analytical Uncertainty
---

# JANUS: Structured Bidirectional Generation for Guaranteed Constraints and Analytical Uncertainty
**arXiv**：[2603.03748v1](https://arxiv.org/abs/2603.03748) · [PDF](https://arxiv.org/pdf/2603.03748.pdf)  
**作者**：Taha Racicot  

**一句话要点**：提出JANUS框架以解决高风险合成数据生成中的四难问题，实现约束保证与快速不确定性估计。

**关键词**：合成数据生成, 约束满足, 不确定性估计, 贝叶斯决策树, 反向拓扑回填, 高维保真度

## 3 点简述
- 核心问题：高维保真度、复杂逻辑约束、可靠不确定性估计和计算效率难以同时满足。
- 方法要点：基于贝叶斯决策树DAG，采用反向拓扑回填算法实现100%约束满足，无需拒绝采样。
- 实验或效果：在15个数据集上实现最优保真度，消除模式崩溃，并快速处理复杂列间约束。

## 摘要（原文）

> High-stakes synthetic data generation faces a fundamental Quadrilemma: achieving Fidelity to the original distribution, Control over complex logical constraints, Reliability in uncertainty estimation, and Efficiency in computational cost -- simultaneously. State-of-the-art Deep Generative Models (CTGAN, TabDDPM) excel at fidelity but rely on inefficient rejection sampling for continuous range constraints. Conversely, Structural Causal Models offer logical control but struggle with high-dimensional fidelity and complex noise inversion. We introduce JANUS (Joint Ancestral Network for Uncertainty and Synthesis), a framework that unifies these capabilities using a DAG of Bayesian Decision Trees. Our key innovation is Reverse-Topological Back-filling, an algorithm that propagates constraints backwards through the causal graph, achieving 100% constraint satisfaction on feasible constraint sets without rejection sampling. This is paired with an Analytical Uncertainty Decomposition derived from Dirichlet priors, enabling 128x faster uncertainty estimation than Monte Carlo methods. Across 15 datasets and 523 constrained scenarios, JANUS achieves state-of-the-art fidelity (Detection Score 0.497), eliminates mode collapse on imbalanced data, and provides exact handling of complex inter-column constraints (e.g., Salary_offered >= Salary_requested) where baselines fail entirely.


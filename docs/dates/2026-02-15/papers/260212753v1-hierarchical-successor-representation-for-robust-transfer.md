---
layout: default
title: Hierarchical Successor Representation for Robust Transfer
---

# Hierarchical Successor Representation for Robust Transfer
**arXiv**：[2602.12753v1](https://arxiv.org/abs/2602.12753) · [PDF](https://arxiv.org/pdf/2602.12753.pdf)  
**作者**：Changmin Yu, Máté Lengyel  

**一句话要点**：提出分层后继表示以解决策略依赖和谱扩散问题，实现鲁棒任务迁移。

**关键词**：后继表示, 分层表示, 任务迁移, 非负矩阵分解, 策略无关表示, 探索效率

## 3 点简述
- 核心问题：经典后继表示因策略依赖和谱扩散，在复杂环境中预测表示不稳定且可扩展性差。
- 方法要点：引入时间抽象构建分层后继表示，结合非负矩阵分解获得稀疏低秩状态表示。
- 实验或效果：在分区环境中实现高效样本迁移，发现可解释拓扑结构，支持探索和可扩展性。

## 摘要（原文）

> The successor representation (SR) provides a powerful framework for decoupling predictive dynamics from rewards, enabling rapid generalisation across reward configurations. However, the classical SR is limited by its inherent policy dependence: policies change due to ongoing learning, environmental non-stationarities, and changes in task demands, making established predictive representations obsolete. Furthermore, in topologically complex environments, SRs suffer from spectral diffusion, leading to dense and overlapping features that scale poorly. Here we propose the Hierarchical Successor Representation (HSR) for overcoming these limitations. By incorporating temporal abstractions into the construction of predictive representations, HSR learns stable state features which are robust to task-induced policy changes. Applying non-negative matrix factorisation (NMF) to the HSR yields a sparse, low-rank state representation that facilitates highly sample-efficient transfer to novel tasks in multi-compartmental environments. Further analysis reveals that HSR-NMF discovers interpretable topological structures, providing a policy-agnostic hierarchical map that effectively bridges model-free optimality and model-based flexibility. Beyond providing a useful basis for task-transfer, we show that HSR's temporally extended predictive structure can also be leveraged to drive efficient exploration, effectively scaling to large, procedurally generated environments.


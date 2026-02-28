---
layout: default
title: Relatron: Automating Relational Machine Learning over Relational Databases
---

# Relatron: Automating Relational Machine Learning over Relational Databases
**arXiv**：[2602.22552v1](https://arxiv.org/abs/2602.22552) · [PDF](https://arxiv.org/pdf/2602.22552.pdf)  
**作者**：Zhikai Chen, Han Xie, Jian Zhang, Jiliang Tang, Xiang Song, Huzefa Rangwala  

**一句话要点**：提出Relatron以自动化关系数据库上的机器学习模型选择与优化

**关键词**：关系机器学习, 模型选择, 任务嵌入, 损失景观优化, 自动化特征工程

## 3 点简述
- 核心问题：关系深度学习与深度特征合成方法性能对比不明确，缺乏任务感知的架构选择原则
- 方法要点：统一设计空间分析，引入任务信号指导模型选择，结合轻量级损失景观指标优化
- 实验或效果：在联合超参数-架构优化中，性能提升达18.5%，成本降低10倍

## 摘要（原文）

> Predictive modeling over relational databases (RDBs) powers applications, yet remains challenging due to capturing both cross-table dependencies and complex feature interactions. Relational Deep Learning (RDL) methods automate feature engineering via message passing, while classical approaches like Deep Feature Synthesis (DFS) rely on predefined non-parametric aggregators. Despite performance gains, the comparative advantages of RDL over DFS and the design principles for selecting effective architectures remain poorly understood. We present a comprehensive study that unifies RDL and DFS in a shared design space and conducts architecture-centric searches across diverse RDB tasks. Our analysis yields three key findings: (1) RDL does not consistently outperform DFS, with performance being highly task-dependent; (2) no single architecture dominates across tasks, underscoring the need for task-aware model selection; and (3) validation accuracy is an unreliable guide for architecture choice. This search yields a model performance bank that links architecture configurations to their performance; leveraging this bank, we analyze the drivers of the RDL-DFS performance gap and introduce two task signals -- RDB task homophily and an affinity embedding that captures size, path, feature, and temporal structure -- whose correlation with the gap enables principled routing. Guided by these signals, we propose Relatron, a task embedding-based meta-selector that chooses between RDL and DFS and prunes the within-family search. Lightweight loss-landscape metrics further guard against brittle checkpoints by preferring flatter optima. In experiments, Relatron resolves the "more tuning, worse performance" effect and, in joint hyperparameter-architecture optimization, achieves up to 18.5% improvement over strong baselines with 10x lower cost than Fisher information-based alternatives.


---
layout: default
title: A Unified Hierarchical Multi-Task Multi-Fidelity Framework for Data-Efficient Surrogate Modeling in Manufacturing
---

# A Unified Hierarchical Multi-Task Multi-Fidelity Framework for Data-Efficient Surrogate Modeling in Manufacturing
**arXiv**：[2603.09842v1](https://arxiv.org/abs/2603.09842) · [PDF](https://arxiv.org/pdf/2603.09842.pdf)  
**作者**：Manan Mehta, Zhiqiao Dong, Yuhang Yang, Chenhui Shao  

**一句话要点**：提出分层多任务多保真度框架，以解决制造中数据高效代理建模的挑战。

**关键词**：代理建模, 多任务学习, 多保真度建模, 高斯过程, 分层贝叶斯, 制造系统

## 3 点简述
- 核心问题：代理建模面临数据需求大和异构保真度数据整合的挑战。
- 方法要点：基于高斯过程，通过分层贝叶斯公式联合学习任务特定趋势和跨任务残差。
- 实验或效果：在合成和真实案例中，预测精度提升最高达23%。

## 摘要（原文）

> Surrogate modeling is an essential data-driven technique for quantifying relationships between input variables and system responses in manufacturing and engineering systems. Two major challenges limit its effectiveness: (1) large data requirements for learning complex nonlinear relationships, and (2) heterogeneous data collected from sources with varying fidelity levels. Multi-task learning (MTL) addresses the first challenge by enabling information sharing across related processes, while multi-fidelity modeling addresses the second by accounting for fidelity-dependent uncertainty. However, existing approaches typically address these challenges separately, and no unified framework simultaneously leverages inter-task similarity and fidelity-dependent data characteristics. This paper develops a novel hierarchical multi-task multi-fidelity (H-MT-MF) framework for Gaussian process-based surrogate modeling. The proposed framework decomposes each task's response into a task-specific global trend and a residual local variability component that is jointly learned across tasks using a hierarchical Bayesian formulation. The framework accommodates an arbitrary number of tasks, design points, and fidelity levels while providing predictive uncertainty quantification. We demonstrate the effectiveness of the proposed method using a 1D synthetic example and a real-world engine surface shape prediction case study. Compared to (1) a state-of-the-art MTL model that does not account for fidelity information and (2) a stochastic kriging model that learns tasks independently, the proposed approach improves prediction accuracy by up to 19% and 23%, respectively. The H-MT-MF framework provides a general and extensible solution for surrogate modeling in manufacturing systems characterized by heterogeneous data sources.


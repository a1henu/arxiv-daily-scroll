---
layout: default
title: Feature-Based Semantics-Aware Scheduling for Energy-Harvesting Federated Learning
---

# Feature-Based Semantics-Aware Scheduling for Energy-Harvesting Federated Learning
**arXiv**：[2512.01983v1](https://arxiv.org/abs/2512.01983) · [PDF](https://arxiv.org/pdf/2512.01983.pdf)  
**作者**：Eunjeong Jeong, Giovanni Perin, Howard H. Yang, Nikolaos Pappas  

**一句话要点**：提出基于特征的语义感知调度框架，以解决能量收集联邦学习中训练能耗主导的问题。

**关键词**：联邦学习, 能量收集, 语义感知调度, 版本信息年龄, 特征提取, 非独立同分布数据

## 3 点简述
- 核心问题：联邦学习中训练能耗常高于通信成本，现有能量收集策略忽略此点，导致冗余计算浪费能量。
- 方法要点：引入基于特征的代理，通过单次前向传播提取中间层特征，估计模型冗余，降低版本信息年龄的计算复杂度。
- 实验或效果：在极端非独立同分布数据和能量稀缺条件下，相比基线策略，实现学习性能提升和能量减少。

## 摘要（原文）

> Federated Learning (FL) on resource-constrained edge devices faces a critical challenge: The computational energy required for training Deep Neural Networks (DNNs) often dominates communication costs. However, most existing Energy-Harvesting FL (EHFL) strategies fail to account for this reality, resulting in wasted energy due to redundant local computations. For efficient and proactive resource management, algorithms that predict local update contributions must be devised. We propose a lightweight client scheduling framework using the Version Age of Information (VAoI), a semantics-aware metric that quantifies update timeliness and significance. Crucially, we overcome VAoI's typical prohibitive computational cost, which requires statistical distance over the entire parameter space, by introducing a feature-based proxy. This proxy estimates model redundancy using intermediate-layer extraction from a single forward pass, dramatically reducing computational complexity. Experiments conducted under extreme non-IID data distributions and scarce energy availability demonstrate superior learning performance while achieving energy reduction compared to existing baseline selection policies. Our framework establishes semantics-aware scheduling as a practical and vital solution for EHFL in realistic scenarios where training costs dominate transmission costs.


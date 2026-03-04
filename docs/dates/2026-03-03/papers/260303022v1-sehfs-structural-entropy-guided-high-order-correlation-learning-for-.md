---
layout: default
title: SEHFS: Structural Entropy-Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection
---

# SEHFS: Structural Entropy-Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection
**arXiv**：[2603.03022v1](https://arxiv.org/abs/2603.03022) · [PDF](https://arxiv.org/pdf/2603.03022.pdf)  
**作者**：Cheng Peng, Yonghao Li, Wanfu Gao, Jie Wen, Weiping Ding  

**一句话要点**：提出SEHFS方法，通过结构熵引导高阶相关性学习，解决多视图多标签特征选择中的高阶依赖和局部最优问题。

**关键词**：多视图多标签学习, 特征选择, 结构熵, 高阶相关性学习, 信息论方法, 矩阵融合

## 3 点简述
- 核心问题：现有信息论方法难以学习特征的高阶结构相关性，且易陷入局部最优。
- 方法要点：将特征图转换为结构熵最小化编码树，量化高阶依赖信息成本，并融合信息论与矩阵方法优化全局和局部。
- 实验或效果：在八个数据集上验证，SEHFS在特征选择中表现优异，并通过消融研究支持其有效性。

## 摘要（原文）

> In recent years, multi-view multi-label learning (MVML) has attracted extensive attention due to its close alignment to real-world scenarios. Information-theoretic methods have gained prominence for learning nonlinear correlations. However, two key challenges persist: first, features in real-world data commonly exhibit high-order structural correlations, but existing information-theoretic methods struggle to learn such correlations; second, commonly relying on heuristic optimization, information-theoretic methods are prone to converging to local optima. To address these two challenges, we propose a novel method called Structural Entropy Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection (SEHFS). The core idea of SEHFS is to convert the feature graph into a structural-entropy-minimizing encoding tree, quantifying the information cost of high-order dependencies and thus learning high-order feature correlations beyond pairwise correlations. Specifically, features exhibiting strong high-order redundancy are grouped into a single cluster within the encoding tree, while inter-cluster feaeture correlations are minimized, thereby eliminating redundancy both within and across clusters. Furthermore, a new framework based on the fusion of information theory and matrix methods is adopted, which learns a shared semantic matrix and view-specific contribution matrices to reconstruct a global view matrix, thereby enhancing the information-theoretic method and balancing the global and local optimization. The ability of structural entropy to learn high-order correlations is theoretically established, and and both experiments on eight datasets from various domains and ablation studies demonstrate that SEHFS achieves superior performance in feature selection.


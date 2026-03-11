---
layout: default
title: Transductive Generalization via Optimal Transport and Its Application to Graph Node Classification
---

# Transductive Generalization via Optimal Transport and Its Application to Graph Node Classification
**arXiv**：[2603.09257v1](https://arxiv.org/abs/2603.09257) · [PDF](https://arxiv.org/pdf/2603.09257.pdf)  
**作者**：MoonJeong Park, Seungbeom Lee, Kyungmin Kim, Jaeseung Heo, Seunghyuk Cho, Shouheng Li, Sangdon Park, Dongwoo Kim  

**一句话要点**：提出基于最优传输的转导泛化界，应用于图节点分类，改进经典复杂度度量。

**关键词**：转导学习, 最优传输, 图神经网络, 泛化界, 节点分类, Wasserstein距离

## 3 点简述
- 核心问题：现有转导泛化界依赖计算难且与经验行为不符的经典复杂度度量。
- 方法要点：在分布无关转导设置中，通过最优传输推导基于表示的泛化界，使用Wasserstein距离度量特征分布。
- 实验或效果：在图上验证界可高效计算且与经验泛化强相关，揭示GNN聚合过程对表示分布的影响。

## 摘要（原文）

> Many existing transductive bounds rely on classical complexity measures that are computationally intractable and often misaligned with empirical behavior. In this work, we establish new representation-based generalization bounds in a distribution-free transductive setting, where learned representations are dependent, and test features are accessible during training. We derive global and class-wise bounds via optimal transport, expressed in terms of Wasserstein distances between encoded feature distributions. We demonstrate that our bounds are efficiently computable and strongly correlate with empirical generalization in graph node classification, improving upon classical complexity measures. Additionally, our analysis reveals how the GNN aggregation process transforms the representation distributions, inducing a trade-off between intra-class concentration and inter-class separation. This yields depth-dependent characterizations that capture the non-monotonic relationship between depth and generalization error observed in practice. The code is available at https://github.com/ml-postech/Transductive-OT-Gen-Bound.


---
layout: default
title: Mitigating Homophily Disparity in Graph Anomaly Detection: A Scalable and Adaptive Approach
---

# Mitigating Homophily Disparity in Graph Anomaly Detection: A Scalable and Adaptive Approach
**arXiv**：[2603.08137v1](https://arxiv.org/abs/2603.08137) · [PDF](https://arxiv.org/pdf/2603.08137.pdf)  
**作者**：Yunhui Liu, Qizhuo Xie, Yinfeng Chen, Xudong Jin, Tao Zheng, Bin Chong, Tieke He  

**一句话要点**：提出SAGAD框架以解决图异常检测中的同质性差异与可扩展性问题

**关键词**：图异常检测, 同质性差异, 可扩展框架, 切比雪夫滤波器, 自适应融合, 频率偏好损失

## 3 点简述
- 核心问题：图异常检测面临节点和类级别同质性差异及大规模图可扩展性挑战
- 方法要点：使用重参数化切比雪夫滤波器提取多频信息，并通过异常上下文感知自适应融合与频率偏好指导损失缓解差异
- 实验或效果：在10个基准测试中验证了SAGAD在准确性和可扩展性上的优越性，支持小批量训练并降低内存使用

## 摘要（原文）

> Graph anomaly detection (GAD) aims to identify nodes that deviate from normal patterns in structure or features. While recent GNN-based approaches have advanced this task, they struggle with two major challenges: 1) homophily disparity, where nodes exhibit varying homophily at both class and node levels; and 2) limited scalability, as many methods rely on costly whole-graph operations. To address them, we propose SAGAD, a Scalable and Adaptive framework for GAD. SAGAD precomputes multi-hop embeddings and applies reparameterized Chebyshev filters to extract low- and high-frequency information, enabling efficient training and capturing both homophilic and heterophilic patterns. To mitigate node-level homophily disparity, we introduce an Anomaly Context-Aware Adaptive Fusion, which adaptively fuses low- and high-pass embeddings using fusion coefficients conditioned on Rayleigh Quotient-guided anomalous subgraph structures for each node. To alleviate class-level disparity, we design a Frequency Preference Guidance Loss, which encourages anomalies to preserve more high-frequency information than normal nodes. SAGAD supports mini-batch training, achieves linear time and space complexity, and drastically reduces memory usage on large-scale graphs. Theoretically, SAGAD ensures asymptotic linear separability between normal and abnormal nodes under mild conditions. Extensive experiments on 10 benchmarks confirm SAGAD's superior accuracy and scalability over state-of-the-art methods.


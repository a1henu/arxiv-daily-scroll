---
layout: default
title: A Graph Meta-Network for Learning on Kolmogorov-Arnold Networks
---

# A Graph Meta-Network for Learning on Kolmogorov-Arnold Networks
**arXiv**：[2602.16316v1](https://arxiv.org/abs/2602.16316) · [PDF](https://arxiv.org/pdf/2602.16316.pdf)  
**作者**：Guy Bar-Shalom, Ami Tavory, Itay Evron, Maya Bechler-Speicher, Ido Guy, Haggai Maron  

**一句话要点**：提出WS-KAN以解决KAN权重空间学习问题，基于图表示和对称性设计。

**关键词**：权重空间学习, Kolmogorov-Arnold网络, 图表示, 置换对称性, 神经网络架构, 元网络

## 3 点简述
- 核心问题：现有权重空间模型对Kolmogorov-Arnold Networks（KANs）缺乏有效架构，无法利用其对称性。
- 方法要点：分析KANs的置换对称性，提出KAN-graph图表示，并开发首个针对KANs的权重空间架构WS-KAN。
- 实验或效果：在多样化任务构建的KANs基准上，WS-KAN显著优于结构无关基线，验证其有效性。

## 摘要（原文）

> Weight-space models learn directly from the parameters of neural networks, enabling tasks such as predicting their accuracy on new datasets. Naive methods -- like applying MLPs to flattened parameters -- perform poorly, making the design of better weight-space architectures a central challenge. While prior work leveraged permutation symmetries in standard networks to guide such designs, no analogous analysis or tailored architecture yet exists for Kolmogorov-Arnold Networks (KANs). In this work, we show that KANs share the same permutation symmetries as MLPs, and propose the KAN-graph, a graph representation of their computation. Building on this, we develop WS-KAN, the first weight-space architecture that learns on KANs, which naturally accounts for their symmetry. We analyze WS-KAN's expressive power, showing it can replicate an input KAN's forward pass - a standard approach for assessing expressiveness in weight-space architectures. We construct a comprehensive ``zoo'' of trained KANs spanning diverse tasks, which we use as benchmarks to empirically evaluate WS-KAN. Across all tasks, WS-KAN consistently outperforms structure-agnostic baselines, often by a substantial margin. Our code is available at https://github.com/BarSGuy/KAN-Graph-Metanetwork.


---
layout: default
title: Learning Compact Boolean Networks
---

# Learning Compact Boolean Networks
**arXiv**：[2602.05830v1](https://arxiv.org/abs/2602.05830) · [PDF](https://arxiv.org/pdf/2602.05830.pdf)  
**作者**：Shengpu Wang, Yuhao Mao, Yani Zhang, Martin Vechev  

**一句话要点**：提出学习紧凑布尔网络的方法，以在资源受限场景中提升效率与准确性

**关键词**：布尔网络, 紧凑模型, 自适应离散化, 卷积架构, 资源受限计算, 视觉基准

## 3 点简述
- 核心问题：布尔网络因组合性质难以学习紧凑且准确的模型，导致推理成本高
- 方法要点：通过无参连接学习、紧凑卷积架构和自适应离散化策略优化布尔网络
- 实验或效果：在标准视觉基准上，准确性与计算量的帕累托前沿显著优于现有方法，布尔操作减少达37倍

## 摘要（原文）

> Floating-point neural networks dominate modern machine learning but incur substantial inference cost, motivating interest in Boolean networks for resource-constrained settings. However, learning compact and accurate Boolean networks is challenging due to their combinatorial nature. In this work, we address this challenge from three different angles: learned connections, compact convolutions and adaptive discretization. First, we propose a novel strategy to learn efficient connections with no additional parameters and negligible computational overhead. Second, we introduce a novel convolutional Boolean architecture that exploits the locality with reduced number of Boolean operations than existing methods. Third, we propose an adaptive discretization strategy to reduce the accuracy drop when converting a continuous-valued network into a Boolean one. Extensive results on standard vision benchmarks demonstrate that the Pareto front of accuracy vs. computation of our method significantly outperforms prior state-of-the-art, achieving better accuracy with up to 37x fewer Boolean operations.


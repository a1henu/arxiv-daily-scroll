---
layout: default
title: SAL: Selective Adaptive Learning for Backpropagation-Free Training with Sparsification
---

# SAL: Selective Adaptive Learning for Backpropagation-Free Training with Sparsification
**arXiv**：[2601.21561v1](https://arxiv.org/abs/2601.21561) · [PDF](https://arxiv.org/pdf/2601.21561.pdf)  
**作者**：Fanping Liu, Hua Yang, Jiasi Zou  

**一句话要点**：提出选择性自适应学习以解决反向传播的梯度干扰和权重对称性问题

**关键词**：反向传播替代训练, 梯度干扰缓解, 参数空间分解, 选择性学习, 大规模神经网络训练

## 3 点简述
- 核心问题：反向传播存在梯度干扰和生物不可信的权重对称性约束
- 方法要点：通过选择性参数激活和自适应区域划分分解参数空间
- 实验或效果：在10个基准测试中提升分类性能，支持深度和大规模模型

## 摘要（原文）

> Standard deep learning relies on Backpropagation (BP), which is constrained by biologically implausible weight symmetry and suffers from significant gradient interference within dense representations. To mitigate these bottlenecks, we propose Selective Adaptive Learning (SAL), a training method that combines selective parameter activation with adaptive area partitioning. Specifically, SAL decomposes the parameter space into mutually exclusive, sample-dependent regions. This decoupling mitigates gradient interference across divergent semantic patterns and addresses explicit weight symmetry requirements through our refined feedback alignment. Empirically, SAL demonstrates competitive convergence rates, leading to improved classification performance across 10 standard benchmarks. Additionally, SAL achieves numerical consistency and competitive accuracy even in deep regimes (up to 128 layers) and large-scale models (up to 1B parameters). Our approach is loosely inspired by biological learning mechanisms, offering a plausible alternative that contributes to the study of scalable neural network training.


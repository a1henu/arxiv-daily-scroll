---
layout: default
title: IDAP++: Advancing Divergence-Based Pruning via Filter-Level and Layer-Level Optimization
---

# IDAP++: Advancing Divergence-Based Pruning via Filter-Level and Layer-Level Optimization
**arXiv**：[2511.20141v1](https://arxiv.org/abs/2511.20141) · [PDF](https://arxiv.org/pdf/2511.20141.pdf)  
**作者**：Aleksei Samarin, Artem Nazarenko, Egor Kotenko, Valentin Malykh, Alexander Savelev, Aleksei Toropov  

**一句话要点**：提出基于信息流张量散度的滤波器与层级优化方法，实现神经网络压缩。

**关键词**：神经网络压缩, 信息流分析, 滤波器剪枝, 层级优化, 张量散度, 模型部署

## 3 点简述
- 核心问题：神经网络在滤波器和架构层面存在冗余，影响部署效率。
- 方法要点：使用张量流散度分析信息流，分阶段剪枝冗余滤波器和层。
- 实验效果：在多种架构上实现高压缩率，保持准确性，优于现有方法。

## 摘要（原文）

> This paper presents a novel approach to neural network compression that addresses redundancy at both the filter and architectural levels through a unified framework grounded in information flow analysis. Building on the concept of tensor flow divergence, which quantifies how information is transformed across network layers, we develop a two-stage optimization process. The first stage employs iterative divergence-aware pruning to identify and remove redundant filters while preserving critical information pathways. The second stage extends this principle to higher-level architecture optimization by analyzing layer-wise contributions to information propagation and selectively eliminating entire layers that demonstrate minimal impact on network performance. The proposed method naturally adapts to diverse architectures, including convolutional networks, transformers, and hybrid designs, providing a consistent metric for comparing the structural importance across different layer types. Experimental validation across multiple modern architectures and datasets reveals that this combined approach achieves substantial model compression while maintaining competitive accuracy. The presented approach achieves parameter reduction results that are globally comparable to those of state-of-the-art solutions and outperforms them across a wide range of modern neural network architectures, from convolutional models to transformers. The results demonstrate how flow divergence serves as an effective guiding principle for both filter-level and layer-level optimization, offering practical benefits for deployment in resource-constrained environments.


---
layout: default
title: Dynamic Graph Structure Learning via Resistance Curvature Flow
---

# Dynamic Graph Structure Learning via Resistance Curvature Flow
**arXiv**：[2601.08149v1](https://arxiv.org/abs/2601.08149) · [PDF](https://arxiv.org/pdf/2601.08149.pdf)  
**作者**：Chaoqun Fei, Huanjiang Liu, Tinglve Zhou, Yangyang Li, Tianyong Hao  

**一句话要点**：提出基于电阻曲率流的动态图结构学习框架，以高效优化数据流形拓扑。

**关键词**：几何表示学习, 动态图结构学习, 电阻曲率流, 流形优化, 计算加速, 深度学习兼容性

## 3 点简述
- 传统静态图构建方法难以捕捉数据流形的内在曲率特征，且Ollivier-Ricci曲率流计算复杂度高。
- 利用电路物理中的有效电阻概念，将曲率优化转化为高效矩阵运算，实现百倍加速。
- 实验表明DGSL-RCF算法在深度度量学习等任务中显著提升表示质量和下游性能。

## 摘要（原文）

> Geometric Representation Learning (GRL) aims to approximate the non-Euclidean topology of high-dimensional data through discrete graph structures, grounded in the manifold hypothesis. However, traditional static graph construction methods based on Euclidean distance often fail to capture the intrinsic curvature characteristics of the data manifold. Although Ollivier-Ricci Curvature Flow (OCF) has proven to be a powerful tool for dynamic topological optimization, its core reliance on Optimal Transport (Wasserstein distance) leads to prohibitive computational complexity, severely limiting its application in large-scale datasets and deep learning frameworks. To break this bottleneck, this paper proposes a novel geometric evolution framework: Resistance Curvature Flow (RCF). Leveraging the concept of effective resistance from circuit physics, RCF transforms expensive curvature optimization into efficient matrix operations. This approach achieves over 100x computational acceleration while maintaining geometric optimization capabilities comparable to OCF. We provide an in-depth exploration of the theoretical foundations and dynamical principles of RCF, elucidating how it guides the redistribution of edge weights via curvature gradients to eliminate topological noise and strengthen local cluster structures. Furthermore, we provide a mechanistic explanation of RCF's role in manifold enhancement and noise suppression, as well as its compatibility with deep learning models. We design a graph optimization algorithm, DGSL-RCF, based on this framework. Experimental results across deep metric learning, manifold learning, and graph structure learning demonstrate that DGSL-RCF significantly improves representation quality and downstream task performance.


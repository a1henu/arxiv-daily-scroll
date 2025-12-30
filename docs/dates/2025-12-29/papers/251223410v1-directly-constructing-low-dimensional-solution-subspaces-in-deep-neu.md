---
layout: default
title: Directly Constructing Low-Dimensional Solution Subspaces in Deep Neural Networks
---

# Directly Constructing Low-Dimensional Solution Subspaces in Deep Neural Networks
**arXiv**：[2512.23410v1](https://arxiv.org/abs/2512.23410) · [PDF](https://arxiv.org/pdf/2512.23410.pdf)  
**作者**：Yusuf Kalyoncuoglu  

**一句话要点**：提出直接构建低维解子空间方法，以绕过深度网络优化瓶颈，实现高效压缩。

**关键词**：低维解子空间, 优化瓶颈, 网络压缩, 蒸馏训练, 本征维度

## 3 点简述
- 核心问题：深度网络权重和特征流形具有低本征维度，但现有模型依赖高维宽度以解决非凸优化搜索问题。
- 方法要点：通过解耦解几何与搜索空间，直接构建低维解子空间，用于压缩分类头。
- 实验或效果：在ResNet-50、ViT和BERT上，分类头可压缩高达16倍，性能损失可忽略。

## 摘要（原文）

> While it is well-established that the weight matrices and feature manifolds of deep neural networks exhibit a low Intrinsic Dimension (ID), current state-of-the-art models still rely on massive high-dimensional widths. This redundancy is not required for representation, but is strictly necessary to solve the non-convex optimization search problem-finding a global minimum, which remains intractable for compact networks. In this work, we propose a constructive approach to bypass this optimization bottleneck. By decoupling the solution geometry from the ambient search space, we empirically demonstrate across ResNet-50, ViT, and BERT that the classification head can be compressed by even huge factors of 16 with negligible performance degradation. This motivates Subspace-Native Distillation as a novel paradigm: by defining the target directly in this constructed subspace, we provide a stable geometric coordinate system for student models, potentially allowing them to circumvent the high-dimensional search problem entirely and realize the vision of Train Big, Deploy Small.


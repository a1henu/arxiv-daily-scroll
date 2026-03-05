---
layout: default
title: On the Learnability of Offline Model-Based Optimization: A Ranking Perspective
---

# On the Learnability of Offline Model-Based Optimization: A Ranking Perspective
**arXiv**：[2603.04000v1](https://arxiv.org/abs/2603.04000) · [PDF](https://arxiv.org/pdf/2603.04000.pdf)  
**作者**：Shen-Huan Lyu, Rong-Xi Tan, Ke Xue, Yi-Xiao He, Yu Huang, Qingfu Zhang, Chao Qian  

**一句话要点**：提出基于排序的离线模型优化方法，以解决分布不匹配导致的过乐观外推问题。

**关键词**：离线模型优化, 排序学习, 分布不匹配, 理论框架, 过乐观外推

## 3 点简述
- 核心问题：离线模型优化中，回归方法假设预测准确度等同于优化性能，但实际是排序高质量设计的问题。
- 方法要点：引入基于排序的优化风险理论框架，设计分布感知排序方法以减少训练数据与近优设计间的分布不匹配。
- 实验或效果：在多种任务上超越二十种现有方法，验证理论优势并揭示离线优化的内在局限性。

## 摘要（原文）

> Offline model-based optimization (MBO) seeks to discover high-performing designs using only a fixed dataset of past evaluations. Most existing methods rely on learning a surrogate model via regression and implicitly assume that good predictive accuracy leads to good optimization performance. In this work, we challenge this assumption and study offline MBO from a learnability perspective. We argue that offline optimization is fundamentally a problem of ranking high-quality designs rather than accurate value prediction. Specifically, we introduce an optimization-oriented risk based on ranking between near-optimal and suboptimal designs, and develop a unified theoretical framework that connects surrogate learning to final optimization. We prove the theoretical advantages of ranking over regression, and identify distributional mismatch between the training data and near-optimal designs as the dominant error. Inspired by this, we design a distribution-aware ranking method to reduce this mismatch. Empirical results across various tasks show that our approach outperforms twenty existing methods, validating our theoretical findings. Additionally, both theoretical and empirical results reveal intrinsic limitations in offline MBO, showing a regime in which no offline method can avoid over-optimistic extrapolation.


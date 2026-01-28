---
layout: default
title: Scale-Consistent State-Space Dynamics via Fractal of Stationary Transformations
---

# Scale-Consistent State-Space Dynamics via Fractal of Stationary Transformations
**arXiv**：[2601.19551v1](https://arxiv.org/abs/2601.19551) · [PDF](https://arxiv.org/pdf/2601.19551.pdf)  
**作者**：Geunhyeok Yu, Hyoseok Hwang  

**一句话要点**：提出FROST方法以解决深度模型中间表示缺乏结构保证的问题，实现尺度一致的状态空间动态。

**关键词**：状态空间模型, 尺度一致性, 分形归纳偏置, 自适应计算, 表示学习, 几何分析

## 3 点简述
- 核心问题：深度模型依赖深度但中间表示缺乏结构保证，导致早期停止和自适应计算难以定义。
- 方法要点：通过分形归纳偏置强制自相似表示流形，确保状态空间模型在迭代细化中具有尺度一致的潜在动态。
- 实验或效果：在ImageNet-100上验证尺度一致行为，自适应效率源于对齐的潜在几何结构。

## 摘要（原文）

> Recent deep learning models increasingly rely on depth without structural guarantees on the validity of intermediate representations, rendering early stopping and adaptive computation ill-posed. We address this limitation by formulating a structural requirement for state-space model's scale-consistent latent dynamics across iterative refinement, and derive Fractal of Stationary Transformations (FROST), which enforces a self-similar representation manifold through a fractal inductive bias. Under this geometry, intermediate states correspond to different resolutions of a shared representation, and we provide a geometric analysis establishing contraction and stable convergence across iterations. As a consequence of this scale-consistent structure, halting naturally admits a ranking-based formulation driven by intrinsic feature quality rather than extrinsic objectives. Controlled experiments on ImageNet-100 empirically verify the predicted scale-consistent behavior, showing that adaptive efficiency emerges from the aligned latent geometry.


---
layout: default
title: On the Structural Failure of Chamfer Distance in 3D Shape Optimization
---

# On the Structural Failure of Chamfer Distance in 3D Shape Optimization
**arXiv**：[2603.09925v1](https://arxiv.org/abs/2603.09925) · [PDF](https://arxiv.org/pdf/2603.09925.pdf)  
**作者**：Chang-Yong Song, David Hyde  

**一句话要点**：揭示Chamfer距离在3D形状优化中的梯度结构失效，提出非局部耦合作为抑制崩溃的必要条件

**关键词**：Chamfer距离, 3D形状优化, 梯度结构失效, 非局部耦合, 点云重建

## 3 点简述
- Chamfer距离直接优化可能导致比不优化更差的结果，源于梯度结构引起的多对一崩溃
- 崩溃是前向项的独特吸引子，局部正则化无法解决，需非局部耦合传播
- 在3D形状变形中，可微分MPM先验实现非局部耦合，显著减少Chamfer差距

## 摘要（原文）

> Chamfer distance is the standard training loss for point cloud reconstruction, completion, and generation, yet directly optimizing it can produce worse Chamfer values than not optimizing it at all. We show that this paradoxical failure is gradient-structural. The per-point Chamfer gradient creates a many-to-one collapse that is the unique attractor of the forward term and cannot be resolved by any local regularizer, including repulsion, smoothness, and density-aware re-weighting. We derive a necessary condition for collapse suppression: coupling must propagate beyond local neighborhoods. In a controlled 2D setting, shared-basis deformation suppresses collapse by providing global coupling; in 3D shape morphing, a differentiable MPM prior instantiates the same principle, consistently reducing the Chamfer gap across 20 directed pairs with a 2.5$\times$ improvement on the topologically complex dragon. The presence or absence of non-local coupling determines whether Chamfer optimization succeeds or collapses. This provides a practical design criterion for any pipeline that optimizes point-level distance metrics.


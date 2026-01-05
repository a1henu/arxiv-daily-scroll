---
layout: default
title: Unified Primitive Proxies for Structured Shape Completion
---

# Unified Primitive Proxies for Structured Shape Completion
**arXiv**：[2601.00759v1](https://arxiv.org/abs/2601.00759) · [PDF](https://arxiv.org/pdf/2601.00759.pdf)  
**作者**：Zhaiyu Chen, Yuqing Wang, Xiao Xiang Zhu  

**一句话要点**：提出UniCo方法，通过统一基元代理实现结构化形状补全，从残缺数据中恢复完整几何结构。

**关键词**：结构化形状补全, 基元代理, 三维理解, 几何重建, 在线目标更新

## 3 点简述
- 核心问题：结构化形状补全需将缺失几何恢复为基元而非无结构点，以支持基于基元的表面重建。
- 方法要点：设计专用解码路径，利用基元代理作为可学习查询，在单次前向传递中预测完整几何、语义和内点成员关系。
- 实验或效果：在合成和真实基准测试中，Chamfer距离降低达50%，法线一致性提升达7%，优于现有基线。

## 摘要（原文）

> Structured shape completion recovers missing geometry as primitives rather than as unstructured points, which enables primitive-based surface reconstruction. Instead of following the prevailing cascade, we rethink how primitives and points should interact, and find it more effective to decode primitives in a dedicated pathway that attends to shared shape features. Following this principle, we present UniCo, which in a single feed-forward pass predicts a set of primitives with complete geometry, semantics, and inlier membership. To drive this unified representation, we introduce primitive proxies, learnable queries that are contextualized to produce assembly-ready outputs. To ensure consistent optimization, our training strategy couples primitives and points with online target updates. Across synthetic and real-world benchmarks with four independent assembly solvers, UniCo consistently outperforms recent baselines, lowering Chamfer distance by up to 50% and improving normal consistency by up to 7%. These results establish an attractive recipe for structured 3D understanding from incomplete data. Project page: https://unico-completion.github.io.


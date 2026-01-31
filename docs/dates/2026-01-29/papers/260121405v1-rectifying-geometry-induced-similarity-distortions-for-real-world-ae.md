---
layout: default
title: Rectifying Geometry-Induced Similarity Distortions for Real-World Aerial-Ground Person Re-Identification
---

# Rectifying Geometry-Induced Similarity Distortions for Real-World Aerial-Ground Person Re-Identification
**arXiv**：[2601.21405v1](https://arxiv.org/abs/2601.21405) · [PDF](https://arxiv.org/pdf/2601.21405.pdf)  
**作者**：Kailash A. Hambarde, Hugo Proença  

**一句话要点**：提出几何诱导查询-键变换以解决航拍-地面行人重识别中的几何失真问题

**关键词**：航拍-地面行人重识别, 几何失真, 相似性空间, 查询-键变换, 低秩模块, 注意力机制

## 3 点简述
- 核心问题：极端视角和距离差异导致几何失真，破坏跨视图相似性空间假设
- 方法要点：引入轻量级低秩模块，基于相机几何调整查询-键相似性计算以补偿失真
- 实验或效果：在四个基准测试中提升鲁棒性，计算开销小

## 摘要（原文）

> Aerial-ground person re-identification (AG-ReID) is fundamentally challenged by extreme viewpoint and distance discrepancies between aerial and ground cameras, which induce severe geometric distortions and invalidate the assumption of a shared similarity space across views. Existing methods primarily rely on geometry-aware feature learning or appearance-conditioned prompting, while implicitly assuming that the geometry-invariant dot-product similarity used in attention mechanisms remains reliable under large viewpoint and scale variations. We argue that this assumption does not hold. Extreme camera geometry systematically distorts the query-key similarity space and degrades attention-based matching, even when feature representations are partially aligned.
>   To address this issue, we introduce Geometry-Induced Query-Key Transformation (GIQT), a lightweight low-rank module that explicitly rectifies the similarity space by conditioning query-key interactions on camera geometry. Rather than modifying feature representations or the attention formulation itself, GIQT adapts the similarity computation to compensate for dominant geometry-induced anisotropic distortions. Building on this local similarity rectification, we further incorporate a geometry-conditioned prompt generation mechanism that provides global, view-adaptive representation priors derived directly from camera geometry.
>   Experiments on four aerial-ground person re-identification benchmarks demonstrate that the proposed framework consistently improves robustness under extreme and previously unseen geometric conditions, while introducing minimal computational overhead compared to state-of-the-art methods.


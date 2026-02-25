---
layout: default
title: Path-Decoupled Hyperbolic Flow Matching for Few-Shot Adaptation
---

# Path-Decoupled Hyperbolic Flow Matching for Few-Shot Adaptation
**arXiv**：[2602.20479v1](https://arxiv.org/abs/2602.20479) · [PDF](https://arxiv.org/pdf/2602.20479.pdf)  
**作者**：Lin Li, Ziqi Jiang, Gefan Ye, Zhenqi He, Jiahui Li, Jun Xiao, Kwang-Ting Cheng, Long Chen  

**一句话要点**：提出路径解耦双曲流匹配以解决少样本适应中的路径纠缠问题

**关键词**：少样本适应, 流匹配, 双曲几何, 视觉-语义对齐, 轨迹解耦

## 3 点简述
- 核心问题：欧几里得流匹配因平坦几何限制导致特征分布适应不足和路径纠缠
- 方法要点：利用洛伦兹流形的指数扩展实现轨迹解耦，包括向心双曲对齐和路径解耦目标
- 实验或效果：在11个基准测试中实现新最优性能，优于欧几里得方法

## 摘要（原文）

> Recent advances in cross-modal few-shot adaptation treat visual-semantic alignment as a continuous feature transport problem via Flow Matching (FM). However, we argue that Euclidean-based FM overlooks fundamental limitations of flat geometry, where polynomial volume growth fails to accommodate diverse feature distributions, leading to severe path entanglement. To this end, we propose path-decoupled Hyperbolic Flow Matching (HFM), leveraging the Lorentz manifold's exponential expansion for trajectory decoupling. HFM structures the transport via two key designs: 1) Centripetal hyperbolic alignment: It constructs a centripetal hierarchy by anchoring textual roots, which pushes visual leaves to the boundary to initialize orderly flows. 2) Path-decoupled objective: It acts as a ``semantic guardrail'' rigidly confining trajectories within isolated class-specific geodesic corridors via step-wise supervision. Furthermore, we devise an adaptive diameter-based stopping to prevent over-transportation into the crowded origin based on the intrinsic semantic scale. Extensive ablations on 11 benchmarks have shown that HFM establishes a new state-of-the-art, consistently outperforming its Euclidean counterparts. Our codes and models will be released.


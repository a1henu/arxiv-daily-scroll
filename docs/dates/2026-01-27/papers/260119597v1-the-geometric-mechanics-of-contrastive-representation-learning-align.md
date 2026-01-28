---
layout: default
title: The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-Modal Divergence
---

# The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-Modal Divergence
**arXiv**：[2601.19597v1](https://arxiv.org/abs/2601.19597) · [PDF](https://arxiv.org/pdf/2601.19597.pdf)  
**作者**：Yichao Cai, Zhen Zhang, Yuhang Liu, Javen Qinfeng Shi  

**一句话要点**：提出测度理论框架以揭示对比表示学习的几何机制，区分单模态与多模态场景的能量景观。

**关键词**：对比学习, 几何力学, 测度理论, 能量景观, 多模态表示, 分布对齐

## 3 点简述
- 核心问题：InfoNCE对比学习的几何机制在经典对齐-均匀分解之外缺乏深入刻画。
- 方法要点：建立大批次极限下的值和梯度一致性，将随机目标桥接至确定性能量景观。
- 实验或效果：揭示单模态场景的严格凸景观与多模态场景的负对称散度诱导的屏障驱动共适应。

## 摘要（原文）

> While InfoNCE powers modern contrastive learning, its geometric mechanisms remain under-characterized beyond the canonical alignment--uniformity decomposition. We present a measure-theoretic framework that models learning as the evolution of representation measures on a fixed embedding manifold. By establishing value and gradient consistency in the large-batch limit, we bridge the stochastic objective to explicit deterministic energy landscapes, uncovering a fundamental geometric bifurcation between the unimodal and multimodal regimes. In the unimodal setting, the intrinsic landscape is strictly convex with a unique Gibbs equilibrium; here, entropy acts merely as a tie-breaker, clarifying "uniformity" as a constrained expansion within the alignment basin. In contrast, the symmetric multimodal objective contains a persistent negative symmetric divergence term that remains even after kernel sharpening. We show that this term induces barrier-driven co-adaptation, enforcing a population-level modality gap as a structural geometric necessity rather than an initialization artifact. Our results shift the analytical lens from pointwise discrimination to population geometry, offering a principled basis for diagnosing and controlling distributional misalignment.


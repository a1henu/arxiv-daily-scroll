---
layout: default
title: Infinite dimensional generative sensing
---

# Infinite dimensional generative sensing
**arXiv**：[2603.03196v1](https://arxiv.org/abs/2603.03196) · [PDF](https://arxiv.org/pdf/2603.03196.pdf)  
**作者**：Paolo Angella, Vito Paolo Pastore, Matteo Santacesaria  

**一句话要点**：提出无限维生成压缩感知框架，解决希尔伯特空间中逆问题的理论缺口。

**关键词**：生成压缩感知, 希尔伯特空间, 无限维理论, 逆问题, 局部相干性, 达西流方程

## 3 点简述
- 核心问题：现有生成模型理论局限于有限维空间，与物理信号在希尔伯特空间建模不匹配。
- 方法要点：扩展局部相干性概念，推导分辨率无关的最优采样分布，基于广义限制等距性证明稳定恢复。
- 实验或效果：在达西流方程上验证理论，显示低分辨率生成器在欠采样时作为隐式正则化器提升重建稳定性。

## 摘要（原文）

> Deep generative models have become a standard for modeling priors for inverse problems, going beyond classical sparsity-based methods. However, existing theoretical guarantees are mostly confined to finite-dimensional vector spaces, creating a gap when the physical signals are modeled as functions in Hilbert spaces. This work presents a rigorous framework for generative compressed sensing in Hilbert spaces. We extend the notion of local coherence in an infinite-dimensional setting, to derive optimal, resolution-independent sampling distributions. Thanks to a generalization of the Restricted Isometry Property, we show that stable recovery holds when the number of measurements is proportional to the prior's intrinsic dimension (up to logarithmic factors), independent of the ambient dimension. Finally, numerical experiments on the Darcy flow equation validate our theoretical findings and demonstrate that in severely undersampled regimes, employing lower-resolution generators acts as an implicit regularizer, improving reconstruction stability.


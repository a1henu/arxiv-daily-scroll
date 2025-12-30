---
layout: default
title: Dynamic Subspace Composition: Efficient Adaptation via Contractive Basis Expansion
---

# Dynamic Subspace Composition: Efficient Adaptation via Contractive Basis Expansion
**arXiv**：[2512.23448v1](https://arxiv.org/abs/2512.23448) · [PDF](https://arxiv.org/pdf/2512.23448.pdf)  
**作者**：Vladimer Khasia  

**一句话要点**：提出动态子空间组合以高效适应混合专家模型中的表示崩溃和梯度不稳定问题

**关键词**：混合专家模型, 动态子空间组合, 参数高效适应, 表示崩溃, 梯度不稳定, 基库扩展

## 3 点简述
- 核心问题：混合专家模型存在表示崩溃和梯度不稳定，影响扩展能力
- 方法要点：通过状态依赖的稀疏扩展共享基库，构建星形域内的残差轨迹，降低参数复杂度
- 实验或效果：减少参数复杂度至O(M d)，内存流量至O(Kd)，并提供动态更新的最坏情况界限

## 摘要（原文）

> Mixture of Experts (MoE) models scale capacity but often suffer from representation collapse and gradient instability. We propose Dynamic Subspace Composition (DSC), a framework that approximates context-dependent weights via a state-dependent, sparse expansion of a shared basis bank. Formally, DSC models the weight update as a residual trajectory within a Star- Shaped Domain, employing a Magnitude-Gated Simplex Interpolation to ensure continuity at the identity. Unlike standard Mixture-of-LoRAs, which incurs O(M rd) parameter complexity by retrieving independent rank-r matrices, DSC constructs a compositional rank-K approximation from decoupled unit-norm basis vectors. This reduces parameter complexity to O(M d) and memory traffic to O(Kd), while Frame-Theoretic regularization and spectral constraints provide rigorous worst-case bounds on the dynamic update. The code is available at https://github. com/VladimerKhasia/DSC


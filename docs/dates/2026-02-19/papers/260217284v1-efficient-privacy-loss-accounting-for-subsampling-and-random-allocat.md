---
layout: default
title: Efficient privacy loss accounting for subsampling and random allocation
---

# Efficient privacy loss accounting for subsampling and random allocation
**arXiv**：[2602.17284v1](https://arxiv.org/abs/2602.17284) · [PDF](https://arxiv.org/pdf/2602.17284.pdf)  
**作者**：Vitaly Feldman, Moshe Shenfeld  

**一句话要点**：提出高效隐私损失分布计算以改进随机分配采样的隐私放大分析

**关键词**：差分隐私, 隐私放大, 随机分配采样, 隐私损失分布, 高斯机制, DP-SGD

## 3 点简述
- 核心问题：随机分配采样隐私分析存在近似误差和隐私参数不紧致问题
- 方法要点：基于隐私损失分布实现概念，开发通用隐私损失核算新工具
- 实验或效果：应用于高斯机制，隐私-效用权衡至少与泊松采样相当

## 摘要（原文）

> We consider the privacy amplification properties of a sampling scheme in which a user's data is used in $k$ steps chosen randomly and uniformly from a sequence (or set) of $t$ steps. This sampling scheme has been recently applied in the context of differentially private optimization (Chua et al., 2024a; Choquette-Choo et al., 2025) and communication-efficient high-dimensional private aggregation (Asi et al., 2025), where it was shown to have utility advantages over the standard Poisson sampling. Theoretical analyses of this sampling scheme (Feldman & Shenfeld, 2025; Dong et al., 2025) lead to bounds that are close to those of Poisson sampling, yet still have two significant shortcomings. First, in many practical settings, the resulting privacy parameters are not tight due to the approximation steps in the analysis. Second, the computed parameters are either the hockey stick or Renyi divergence, both of which introduce overheads when used in privacy loss accounting.
>   In this work, we demonstrate that the privacy loss distribution (PLD) of random allocation applied to any differentially private algorithm can be computed efficiently. When applied to the Gaussian mechanism, our results demonstrate that the privacy-utility trade-off for random allocation is at least as good as that of Poisson subsampling. In particular, random allocation is better suited for training via DP-SGD. To support these computations, our work develops new tools for general privacy loss accounting based on a notion of PLD realization. This notion allows us to extend accurate privacy loss accounting to subsampling which previously required manual noise-mechanism-specific analysis.


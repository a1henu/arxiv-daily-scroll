---
layout: default
title: Improved Regret Guarantees for Online Mirror Descent using a Portfolio of Mirror Maps
---

# Improved Regret Guarantees for Online Mirror Descent using a Portfolio of Mirror Maps
**arXiv**：[2602.13177v1](https://arxiv.org/abs/2602.13177) · [PDF](https://arxiv.org/pdf/2602.13177.pdf)  
**作者**：Swati Gupta, Jai Moondra, Mohit Singh  

**一句话要点**：提出基于块范数的镜像映射组合，以提升在线凸优化中稀疏损失函数的遗憾保证。

**关键词**：在线凸优化, 镜像映射, 稀疏损失, 块范数, 遗憾保证, 自适应算法

## 3 点简述
- 核心问题：在线镜像下降中，如何选择镜像映射以优化稀疏损失函数的遗憾性能。
- 方法要点：使用块范数构建镜像映射组合，并设计元算法动态选择映射以适应未知稀疏度。
- 实验或效果：证明块范数映射在稀疏损失上比传统L1和L2映射有多项式级遗憾改进。

## 摘要（原文）

> OMD and its variants give a flexible framework for OCO where the performance depends crucially on the choice of the mirror map. While the geometries underlying OPGD and OEG, both special cases of OMD, are well understood, it remains a challenging open question on how to construct an optimal mirror map for any given constrained set and a general family of loss functions, e.g., sparse losses. Motivated by parameterizing a near-optimal set of mirror maps, we consider a simpler question: is it even possible to obtain polynomial gains in regret by using mirror maps for geometries that interpolate between $L_1$ and $L_2$, which may not be possible by restricting to only OEG ($L_1$) or OPGD ($L_2$).
>   Our main result answers this question positively. We show that mirror maps based on block norms adapt better to the sparsity of loss functions, compared to previous $L_p$ (for $p \in [1, 2]$) interpolations. In particular, we construct a family of online convex optimization instances in $\mathbb{R}^d$, where block norm-based mirror maps achieve a provable polynomial (in $d$) improvement in regret over OEG and OPGD for sparse loss functions. We then turn to the setting in which the sparsity level of the loss functions is unknown. In this case, the choice of geometry itself becomes an online decision problem. We first show that naively switching between OEG and OPGD can incur linear regret, highlighting the intrinsic difficulty of geometry selection. To overcome this issue, we propose a meta-algorithm based on multiplicative weights that dynamically selects among a family of uniform block norms. We show that this approach effectively tunes OMD to the sparsity of the losses, yielding adaptive regret guarantees. Overall, our results demonstrate that online mirror-map selection can significantly enhance the ability of OMD to exploit sparsity in online convex optimization.


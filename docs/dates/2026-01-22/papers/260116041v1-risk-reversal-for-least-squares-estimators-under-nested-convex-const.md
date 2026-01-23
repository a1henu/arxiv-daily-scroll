---
layout: default
title: Risk reversal for least squares estimators under nested convex constraints
---

# Risk reversal for least squares estimators under nested convex constraints
**arXiv**：[2601.16041v1](https://arxiv.org/abs/2601.16041) · [PDF](https://arxiv.org/pdf/2601.16041.pdf)  
**作者**：Omar Al-Ghattas  

**一句话要点**：揭示嵌套凸约束下最小二乘估计器的风险反转现象

**关键词**：约束优化, 最小二乘估计, 风险分析, 高斯序列模型, 凸集投影

## 3 点简述
- 在约束随机优化中，更严格的可行集可能增加投影估计器的统计风险
- 通过高斯序列模型构造显式例子，展示噪声较大时风险反转
- 对比噪声机制：小噪声下风险由局部几何决定，大噪声下由全局几何交互主导

## 摘要（原文）

> In constrained stochastic optimization, one naturally expects that imposing a stricter feasible set does not increase the statistical risk of an estimator defined by projection onto that set. In this paper, we show that this intuition can fail even in canonical settings.
>   We study the Gaussian sequence model, a deliberately austere test best, where for a compact, convex set $Θ\subset \mathbb{R}^d$ one observes \[ Y = θ^\star + σZ, \qquad Z \sim N(0, I_d), \] and seeks to estimate an unknown parameter $θ^\star \in Θ$. The natural estimator is the least squares estimator (LSE), which coincides with the Euclidean projection of $Y$ onto $Θ$. We construct an explicit example exhibiting \emph{risk reversal}: for sufficiently large noise, there exist nested compact convex sets $Θ_S \subset Θ_L$ and a parameter $θ^\star \in Θ_S$ such that the LSE constrained to $Θ_S$ has strictly larger risk than the LSE constrained to $Θ_L$. We further show that this phenomenon can persist at the level of worst-case risk, with the supremum risk over the smaller constraint set exceeding that over the larger one.
>   We clarify this behavior by contrasting noise regimes. In the vanishing-noise limit, the risk admits a first-order expansion governed by the statistical dimension of the tangent cone at $θ^\star$, and tighter constraints uniformly reduce risk. In contrast, in the diverging-noise regime, the risk is determined by global geometric interactions between the constraint set and random noise directions. Here, the embedding of $Θ_S$ within $Θ_L$ can reverse the risk ordering.
>   These results reveal a previously unrecognized failure mode of projection-based estimators: in sufficiently noisy settings, tightening a constraint can paradoxically degrade statistical performance.


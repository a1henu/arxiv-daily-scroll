---
layout: default
title: Risk reversal for least squares estimators under nested convex constraints
---

# Risk reversal for least squares estimators under nested convex constraints
**arXiv**：[2601.16041v1](https://arxiv.org/abs/2601.16041) · [PDF](https://arxiv.org/pdf/2601.16041.pdf)  
**作者**：Omar Al-Ghattas  

**一句话要点**：提出风险反转现象，揭示在噪声较大时，更紧约束可能增加最小二乘估计器风险

**关键词**：约束随机优化, 最小二乘估计器, 风险反转, 高斯序列模型, 凸约束

## 3 点简述
- 核心问题：约束随机优化中，更紧可行集是否总能降低估计器风险？
- 方法要点：在高斯序列模型中，构造嵌套凸集示例展示风险反转现象
- 实验或效果：在噪声较大时，较小约束集的最坏情况风险可能超过较大集

## 摘要（原文）

> In constrained stochastic optimization, one naturally expects that imposing a stricter feasible set does not increase the statistical risk of an estimator defined by projection onto that set. In this paper, we show that this intuition can fail even in canonical settings.
>   We study the Gaussian sequence model, a deliberately austere test best, where for a compact, convex set $Θ\subset \mathbb{R}^d$ one observes \[ Y = θ^\star + σZ, \qquad Z \sim N(0, I_d), \] and seeks to estimate an unknown parameter $θ^\star \in Θ$. The natural estimator is the least squares estimator (LSE), which coincides with the Euclidean projection of $Y$ onto $Θ$. We construct an explicit example exhibiting \emph{risk reversal}: for sufficiently large noise, there exist nested compact convex sets $Θ_S \subset Θ_L$ and a parameter $θ^\star \in Θ_S$ such that the LSE constrained to $Θ_S$ has strictly larger risk than the LSE constrained to $Θ_L$. We further show that this phenomenon can persist at the level of worst-case risk, with the supremum risk over the smaller constraint set exceeding that over the larger one.
>   We clarify this behavior by contrasting noise regimes. In the vanishing-noise limit, the risk admits a first-order expansion governed by the statistical dimension of the tangent cone at $θ^\star$, and tighter constraints uniformly reduce risk. In contrast, in the diverging-noise regime, the risk is determined by global geometric interactions between the constraint set and random noise directions. Here, the embedding of $Θ_S$ within $Θ_L$ can reverse the risk ordering.
>   These results reveal a previously unrecognized failure mode of projection-based estimators: in sufficiently noisy settings, tightening a constraint can paradoxically degrade statistical performance.


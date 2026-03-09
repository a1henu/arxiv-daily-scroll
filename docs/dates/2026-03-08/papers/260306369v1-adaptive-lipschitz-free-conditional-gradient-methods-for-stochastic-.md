---
layout: default
title: Adaptive Lipschitz-Free Conditional Gradient Methods for Stochastic Composite Nonconvex Optimization
---

# Adaptive Lipschitz-Free Conditional Gradient Methods for Stochastic Composite Nonconvex Optimization
**arXiv**：[2603.06369v1](https://arxiv.org/abs/2603.06369) · [PDF](https://arxiv.org/pdf/2603.06369.pdf)  
**作者**：Ganzhao Yuan  

**一句话要点**：提出自适应Lipschitz-Free条件梯度方法，用于随机复合非凸优化，无需全局平滑常数或线搜索。

**关键词**：随机优化, 条件梯度方法, 非凸优化, 自适应算法, 方差缩减, 投影自由

## 3 点简述
- 核心问题：传统条件梯度方法依赖全局平滑常数或线搜索，在随机复合非凸优化中效率受限。
- 方法要点：ALFCG通过历史迭代差的自归一化累加器估计局部平滑度，每步最小化二次代理模型，实现自适应几何适应。
- 实验或效果：在核范数球和ℓ_p球上的多类分类实验中，ALFCG通常优于最先进的条件梯度基线。

## 摘要（原文）

> We propose ALFCG (Adaptive Lipschitz-Free Conditional Gradient), the first \textit{adaptive} projection-free framework for stochastic composite nonconvex minimization that \textit{requires neither global smoothness constants nor line search}. Unlike prior conditional gradient methods that use openloop diminishing stepsizes, conservative Lipschitz constants, or costly backtracking, ALFCG maintains a self-normalized accumulator of historical iterate differences to estimate local smoothness and minimize a quadratic surrogate model at each step. This retains the simplicity of Frank-Wolfe while adapting to unknown geometry. We study three variants. ALFCG-FS addresses finite-sum problems with a SPIDER estimator. ALFCG-MVR1 and ALFCG-MVR2 handle stochastic expectation problems by using momentum-based variance reduction with single-batch and two-batch updates, and operate under average and individual smoothness, respectively. To reach an $ε$-stationary point, ALFCG-FS attains $\mathcal{O}(N+\sqrt{N}ε^{-2})$ iteration complexity, while ALFCG-MVR1 and ALFCG-MVR2 achieve $\tilde{\mathcal{O}}(σ^2ε^{-4}+ε^{-2})$ and $\tilde{\mathcal{O}}(σε^{-3}+ε^{-2})$, where $N$ is the number of components and $σ$ is the noise level. In contrast to typical $\mathcal{O}(ε^{-4})$ or $\mathcal{O}(ε^{-3})$ rates, our bounds reduce to the optimal rate up to logarithmic factors $\tilde{\mathcal{O}}(ε^{-2})$ as the noise level $σ\to 0$. Extensive experiments on multiclass classification over nuclear norm balls and $\ell_p$ balls show that ALFCG generally outperforms state-of-the-art conditional gradient baselines.


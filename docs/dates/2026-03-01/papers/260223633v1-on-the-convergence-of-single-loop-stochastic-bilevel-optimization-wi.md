---
layout: default
title: On the Convergence of Single-Loop Stochastic Bilevel Optimization with Approximate Implicit Differentiation
---

# On the Convergence of Single-Loop Stochastic Bilevel Optimization with Approximate Implicit Differentiation
**arXiv**：[2602.23633v1](https://arxiv.org/abs/2602.23633) · [PDF](https://arxiv.org/pdf/2602.23633.pdf)  
**作者**：Yubo Zhou, Luo Luo, Guang Dai, Haishan Ye  

**一句话要点**：提出SSAID算法，实现单环随机双层优化收敛，匹配多环方法最优速率。

**关键词**：随机双层优化, 单环算法, 近似隐式微分, 收敛分析, 元学习, 超参数优化

## 3 点简述
- 针对单环随机双层优化理论分析不足，收敛率次优且κ依赖不明确的问题。
- 通过精化收敛分析，证明SSAID达到ε-稳定点的复杂度为O(κ^7 ε^{-2})。
- 结果匹配多环方法最优O(ε^{-2})速率，首次显式刻画随机AID单环方法的κ依赖。

## 摘要（原文）

> Stochastic Bilevel Optimization has emerged as a fundamental framework for meta-learning and hyperparameter optimization. Despite the practical prevalence of single-loop algorithms--which update lower and upper variables concurrently--their theoretical understanding, particularly in the stochastic regime, remains significantly underdeveloped compared to their multi-loop counterparts. Existing analyses often yield suboptimal convergence rates or obscure the critical dependence on the lower-level condition number $κ$, frequently burying it within generic Lipschitz constants. In this paper, we bridge this gap by providing a refined convergence analysis of the Single-loop Stochastic Approximate Implicit Differentiation (SSAID) algorithm. We prove that SSAID achieves an $ε$-stationary point with an oracle complexity of $\mathcal{O}(κ^7 ε^{-2})$. Our result is noteworthy in two aspects: (i) it matches the optimal $\mathcal{O}(ε^{-2})$ rate of state-of-the-art multi-loop methods (e.g., stocBiO) while maintaining the computational efficiency of a single-loop update; and (ii) it provides the first explicit, fine-grained characterization of the $κ$-dependence for stochastic AID-based single-loop methods. This work demonstrates that SSAID is not merely a heuristic approach, but admits a rigorous theoretical foundation with convergence guarantees competitive with mainstream multi-loop frameworks.


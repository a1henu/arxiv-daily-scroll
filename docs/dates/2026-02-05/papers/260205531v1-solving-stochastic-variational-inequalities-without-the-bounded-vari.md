---
layout: default
title: Solving Stochastic Variational Inequalities without the Bounded Variance Assumption
---

# Solving Stochastic Variational Inequalities without the Bounded Variance Assumption
**arXiv**：[2602.05531v1](https://arxiv.org/abs/2602.05531) · [PDF](https://arxiv.org/pdf/2602.05531.pdf)  
**作者**：Ahmet Alacaoglu, Jun-Hyun Kim  

**一句话要点**：提出无界方差假设下求解随机变分不等式的方法，优化min-max问题复杂度

**关键词**：随机变分不等式, min-max优化, 无界方差, 复杂度分析, 非凸非凹优化

## 3 点简述
- 核心问题：解决随机变分不等式时无需有界方差或域假设，适用于无界约束集min-max优化
- 方法要点：针对单调和结构化非单调变分不等式，基于弱Minty VI假设，实现最优复杂度
- 实验或效果：在方差随变量平方增长下，达到预期残差范数小于ε的复杂度为O(ε^{-4})

## 摘要（原文）

> We analyze algorithms for solving stochastic variational inequalities (VI) without the bounded variance or bounded domain assumptions, where our main focus is min-max optimization with possibly unbounded constraint sets. We focus on two classes of problems: monotone VIs; and structured nonmonotone VIs that admit a solution to the weak Minty VI. The latter assumption allows us to solve structured nonconvex-nonconcave min-max problems. For both classes of VIs, to make the expected residual norm less than $\varepsilon$, we show an oracle complexity of $\widetilde{O}(\varepsilon^{-4})$, which is the best-known for constrained VIs. In our setting, this complexity had been obtained with the bounded variance assumption in the literature, which is not even satisfied for bilinear min-max problems with an unbounded domain. We obtain this complexity for stochastic oracles whose variance can grow as fast as the squared norm of the optimization variable.


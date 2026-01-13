---
layout: default
title: Optimal Transport under Group Fairness Constraints
---

# Optimal Transport under Group Fairness Constraints
**arXiv**：[2601.07144v1](https://arxiv.org/abs/2601.07144) · [PDF](https://arxiv.org/pdf/2601.07144.pdf)  
**作者**：Linus Bleistein, Mathieu Dagréou, Francisco Andrade, Thomas Boudou, Aurélien Bellet  

**一句话要点**：提出公平约束下的最优传输方法，以解决资源分配中的群体公平性问题。

**关键词**：最优传输, 群体公平性, Sinkhorn算法, 惩罚优化, 双层优化, 资源分配

## 3 点简述
- 核心问题：最优传输匹配中群体公平性不足，需满足预定义目标概率。
- 方法要点：开发FairSinkhorn算法计算公平传输，并引入惩罚和双层优化松弛策略。
- 实验或效果：实证展示公平与性能的权衡，提供理论保证如样本复杂度和泛化界。

## 摘要（原文）

> Ensuring fairness in matching algorithms is a key challenge in allocating scarce resources and positions. Focusing on Optimal Transport (OT), we introduce a novel notion of group fairness requiring that the probability of matching two individuals from any two given groups in the OT plan satisfies a predefined target. We first propose \texttt{FairSinkhorn}, a modified Sinkhorn algorithm to compute perfectly fair transport plans efficiently. Since exact fairness can significantly degrade matching quality in practice, we then develop two relaxation strategies. The first one involves solving a penalised OT problem, for which we derive novel finite-sample complexity guarantees. This result is of independent interest as it can be generalized to arbitrary convex penalties. Our second strategy leverages bilevel optimization to learn a ground cost that induces a fair OT solution, and we establish a bound guaranteeing that the learned cost yields fair matchings on unseen data. Finally, we present empirical results that illustrate the trade-offs between fairness and performance.


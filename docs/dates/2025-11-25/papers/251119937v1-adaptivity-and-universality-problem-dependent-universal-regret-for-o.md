---
layout: default
title: Adaptivity and Universality: Problem-dependent Universal Regret for Online Convex Optimization
---

# Adaptivity and Universality: Problem-dependent Universal Regret for Online Convex Optimization
**arXiv**：[2511.19937v1](https://arxiv.org/abs/2511.19937) · [PDF](https://arxiv.org/pdf/2511.19937.pdf)  
**作者**：Peng Zhao, Yu-Hu Yan, Hang Yu, Zhi-Hua Zhou  

**一句话要点**：提出UniGrad方法实现通用在线优化，兼具自适应性和低计算成本。

**关键词**：在线凸优化, 通用遗憾界, 梯度变化自适应, 元算法, 计算效率优化

## 3 点简述
- 现有通用在线学习方法缺乏对梯度变化的自适应，无法实现问题依赖的遗憾界。
- UniGrad方法通过元算法设计，自适应梯度变化，获得强凸和指数凹函数的对数遗憾界。
- UniGrad++在保持遗憾界的同时，将每轮梯度查询降至1次，提升计算效率。

## 摘要（原文）

> Universal online learning aims to achieve optimal regret guarantees without requiring prior knowledge of the curvature of online functions. Existing methods have established minimax-optimal regret bounds for universal online learning, where a single algorithm can simultaneously attain $\mathcal{O}(\sqrt{T})$ regret for convex functions, $\mathcal{O}(d \log T)$ for exp-concave functions, and $\mathcal{O}(\log T)$ for strongly convex functions, where $T$ is the number of rounds and $d$ is the dimension of the feasible domain. However, these methods still lack problem-dependent adaptivity. In particular, no universal method provides regret bounds that scale with the gradient variation $V_T$, a key quantity that plays a crucial role in applications such as stochastic optimization and fast-rate convergence in games. In this work, we introduce UniGrad, a novel approach that achieves both universality and adaptivity, with two distinct realizations: UniGrad.Correct and UniGrad.Bregman. Both methods achieve universal regret guarantees that adapt to gradient variation, simultaneously attaining $\mathcal{O}(\log V_T)$ regret for strongly convex functions and $\mathcal{O}(d \log V_T)$ regret for exp-concave functions. For convex functions, the regret bounds differ: UniGrad.Correct achieves an $\mathcal{O}(\sqrt{V_T \log V_T})$ bound while preserving the RVU property that is crucial for fast convergence in online games, whereas UniGrad.Bregman achieves the optimal $\mathcal{O}(\sqrt{V_T})$ regret bound through a novel design. Both methods employ a meta algorithm with $\mathcal{O}(\log T)$ base learners, which naturally requires $\mathcal{O}(\log T)$ gradient queries per round. To enhance computational efficiency, we introduce UniGrad++, which retains the regret while reducing the gradient query to just $1$ per round via surrogate optimization. We further provide various implications.


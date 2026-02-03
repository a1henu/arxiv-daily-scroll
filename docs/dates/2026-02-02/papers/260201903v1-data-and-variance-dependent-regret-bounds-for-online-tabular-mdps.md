---
layout: default
title: Data- and Variance-dependent Regret Bounds for Online Tabular MDPs
---

# Data- and Variance-dependent Regret Bounds for Online Tabular MDPs
**arXiv**：[2602.01903v1](https://arxiv.org/abs/2602.01903) · [PDF](https://arxiv.org/pdf/2602.01903.pdf)  
**作者**：Mingyi Li, Taira Tsuchiya, Kenji Yamanishi  

**一句话要点**：提出基于全局优化和策略优化的算法，在已知转移的在线表格MDP中实现数据和方差依赖的遗憾界。

**关键词**：在线强化学习, 表格MDP, 遗憾界分析, 对抗环境, 随机环境, 复杂度度量

## 3 点简述
- 研究在线表格MDP，已知转移，在对抗和随机环境中实现数据和方差依赖的遗憾界。
- 开发基于乐观跟随正则化领导者的算法，引入一阶、二阶、路径长度和方差依赖的复杂度度量。
- 全局优化算法在对抗环境中实现多类遗憾界，在随机环境中实现方差感知的遗憾界，接近最优。

## 摘要（原文）

> This work studies online episodic tabular Markov decision processes (MDPs) with known transitions and develops best-of-both-worlds algorithms that achieve refined data-dependent regret bounds in the adversarial regime and variance-dependent regret bounds in the stochastic regime. We quantify MDP complexity using a first-order quantity and several new data-dependent measures for the adversarial regime, including a second-order quantity and a path-length measure, as well as variance-based measures for the stochastic regime. To adapt to these measures, we develop algorithms based on global optimization and policy optimization, both built on optimistic follow-the-regularized-leader with log-barrier regularization. For global optimization, our algorithms achieve first-order, second-order, and path-length regret bounds in the adversarial regime, and in the stochastic regime, they achieve a variance-aware gap-independent bound and a variance-aware gap-dependent bound that is polylogarithmic in the number of episodes. For policy optimization, our algorithms achieve the same data- and variance-dependent adaptivity, up to a factor of the episode horizon, by exploiting a new optimistic $Q$-function estimator. Finally, we establish regret lower bounds in terms of data-dependent complexity measures for the adversarial regime and a variance measure for the stochastic regime, implying that the regret upper bounds achieved by the global-optimization approach are nearly optimal.


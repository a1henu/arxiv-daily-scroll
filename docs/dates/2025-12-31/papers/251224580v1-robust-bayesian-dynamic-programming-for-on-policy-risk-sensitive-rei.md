---
layout: default
title: Robust Bayesian Dynamic Programming for On-policy Risk-sensitive Reinforcement Learning
---

# Robust Bayesian Dynamic Programming for On-policy Risk-sensitive Reinforcement Learning
**arXiv**：[2512.24580v1](https://arxiv.org/abs/2512.24580) · [PDF](https://arxiv.org/pdf/2512.24580.pdf)  
**作者**：Shanyu Han, Yangbo He, Yang Liu  

**一句话要点**：提出鲁棒贝叶斯动态规划框架，用于策略内风险敏感强化学习，以应对转移不确定性。

**关键词**：风险敏感强化学习, 鲁棒马尔可夫决策过程, 贝叶斯动态规划, 转移不确定性, CVaR风险度量, 期权对冲

## 3 点简述
- 核心问题：在强化学习中结合风险敏感性和转移动态不确定性，统一现有框架。
- 方法要点：定义内外风险度量，构建RSRMDP，开发贝叶斯DP算法，结合蒙特卡洛采样与凸优化。
- 实验或效果：通过数值实验验证收敛性和优势，应用于期权对冲展示实用性。

## 摘要（原文）

> We propose a novel framework for risk-sensitive reinforcement learning (RSRL) that incorporates robustness against transition uncertainty. We define two distinct yet coupled risk measures: an inner risk measure addressing state and cost randomness and an outer risk measure capturing transition dynamics uncertainty. Our framework unifies and generalizes most existing RL frameworks by permitting general coherent risk measures for both inner and outer risk measures. Within this framework, we construct a risk-sensitive robust Markov decision process (RSRMDP), derive its Bellman equation, and provide error analysis under a given posterior distribution. We further develop a Bayesian Dynamic Programming (Bayesian DP) algorithm that alternates between posterior updates and value iteration. The approach employs an estimator for the risk-based Bellman operator that combines Monte Carlo sampling with convex optimization, for which we prove strong consistency guarantees. Furthermore, we demonstrate that the algorithm converges to a near-optimal policy in the training environment and analyze both the sample complexity and the computational complexity under the Dirichlet posterior and CVaR. Finally, we validate our approach through two numerical experiments. The results exhibit excellent convergence properties while providing intuitive demonstrations of its advantages in both risk-sensitivity and robustness. Empirically, we further demonstrate the advantages of the proposed algorithm through an application on option hedging.


---
layout: default
title: EUBRL: Epistemic Uncertainty Directed Bayesian Reinforcement Learning
---

# EUBRL: Epistemic Uncertainty Directed Bayesian Reinforcement Learning
**arXiv**：[2512.15405v1](https://arxiv.org/abs/2512.15405) · [PDF](https://arxiv.org/pdf/2512.15405.pdf)  
**作者**：Jianfei Ma, Wee Sun Lee  

**一句话要点**：提出EUBRL算法，利用认知不确定性指导贝叶斯强化学习以实现原则性探索。

**关键词**：贝叶斯强化学习, 认知不确定性, 原则性探索, 样本效率, 无限时域MDP, 稀疏奖励

## 3 点简述
- 核心问题：智能体在已知与未知边界面临探索与利用的困境，认知不确定性反映知识有限导致的系统不确定性。
- 方法要点：通过认知不确定性指导自适应减少估计误差带来的每步遗憾，为无限时域折扣MDP中一类充分表达先验提供理论保证。
- 实验或效果：在稀疏奖励、长时域和随机性任务中评估，EUBRL展现出优越的样本效率、可扩展性和一致性。

## 摘要（原文）

> At the boundary between the known and the unknown, an agent inevitably confronts the dilemma of whether to explore or to exploit. Epistemic uncertainty reflects such boundaries, representing systematic uncertainty due to limited knowledge. In this paper, we propose a Bayesian reinforcement learning (RL) algorithm, $\texttt{EUBRL}$, which leverages epistemic guidance to achieve principled exploration. This guidance adaptively reduces per-step regret arising from estimation errors. We establish nearly minimax-optimal regret and sample complexity guarantees for a class of sufficiently expressive priors in infinite-horizon discounted MDPs. Empirically, we evaluate $\texttt{EUBRL}$ on tasks characterized by sparse rewards, long horizons, and stochasticity. Results demonstrate that $\texttt{EUBRL}$ achieves superior sample efficiency, scalability, and consistency.


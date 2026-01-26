---
layout: default
title: A Regularized Actor-Critic Algorithm for Bi-Level Reinforcement Learning
---

# A Regularized Actor-Critic Algorithm for Bi-Level Reinforcement Learning
**arXiv**：[2601.16399v1](https://arxiv.org/abs/2601.16399) · [PDF](https://arxiv.org/pdf/2601.16399.pdf)  
**作者**：Sihan Zeng, Sujay Bhatt, Sumitra Ganesh, Alec Koppel  

**一句话要点**：提出正则化演员-评论家算法，通过惩罚重构和熵正则化解决双层强化学习优化问题。

**关键词**：双层优化, 强化学习, 演员-评论家算法, 熵正则化, 超梯度估计, 收敛分析

## 3 点简述
- 研究双层优化问题，上层目标为平滑函数，下层为MDP策略优化，上层变量参数化下层奖励。
- 提出单循环一阶演员-评论家算法，引入衰减熵正则化实现无偏超梯度估计，无需精确求解下层问题。
- 在GridWorld和RLHF实验中验证算法性能，通过残差分析证明收敛到原问题平稳点。

## 摘要（原文）

> We study a structured bi-level optimization problem where the upper-level objective is a smooth function and the lower-level problem is policy optimization in a Markov decision process (MDP). The upper-level decision variable parameterizes the reward of the lower-level MDP, and the upper-level objective depends on the optimal induced policy. Existing methods for bi-level optimization and RL often require second-order information, impose strong regularization at the lower level, or inefficiently use samples through nested-loop procedures. In this work, we propose a single-loop, first-order actor-critic algorithm that optimizes the bi-level objective via a penalty-based reformulation. We introduce into the lower-level RL objective an attenuating entropy regularization, which enables asymptotically unbiased upper-level hyper-gradient estimation without solving the unregularized RL problem exactly. We establish the finite-time and finite-sample convergence of the proposed algorithm to a stationary point of the original, unregularized bi-level optimization problem through a novel lower-level residual analysis under a special type of Polyak-Lojasiewicz condition. We validate the performance of our method through experiments on a GridWorld goal position problem and on happy tweet generation through reinforcement learning from human feedback (RLHF).


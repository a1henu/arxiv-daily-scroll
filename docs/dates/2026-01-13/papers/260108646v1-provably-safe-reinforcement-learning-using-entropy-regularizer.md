---
layout: default
title: Provably Safe Reinforcement Learning using Entropy Regularizer
---

# Provably Safe Reinforcement Learning using Entropy Regularizer
**arXiv**：[2601.08646v1](https://arxiv.org/abs/2601.08646) · [PDF](https://arxiv.org/pdf/2601.08646.pdf)  
**作者**：Abhijit Mazumdar, Rafal Wisniewski, Manuela L. Bujorianu  

**一句话要点**：提出基于熵正则化的安全强化学习算法，以解决马尔可夫决策过程中的安全约束问题。

**关键词**：安全强化学习, 熵正则化, 马尔可夫决策过程, 乐观面对不确定性, 遗憾界, 变异性控制

## 3 点简述
- 核心问题：在马尔可夫决策过程中学习最优策略，同时确保学习阶段的安全约束以高概率满足。
- 方法要点：基于乐观面对不确定性原则设计算法，并引入熵正则化以改进遗憾和控制变异性。
- 实验或效果：进行有限样本分析，推导遗憾界，展示熵正则化提升性能并减少变异性。

## 摘要（原文）

> We consider the problem of learning the optimal policy for Markov decision processes with safety constraints. We formulate the problem in a reach-avoid setup. Our goal is to design online reinforcement learning algorithms that ensure safety constraints with arbitrarily high probability during the learning phase. To this end, we first propose an algorithm based on the optimism in the face of uncertainty (OFU) principle. Based on the first algorithm, we propose our main algorithm, which utilizes entropy regularization. We investigate the finite-sample analysis of both algorithms and derive their regret bounds. We demonstrate that the inclusion of entropy regularization improves the regret and drastically controls the episode-to-episode variability that is inherent in OFU-based safe RL algorithms.


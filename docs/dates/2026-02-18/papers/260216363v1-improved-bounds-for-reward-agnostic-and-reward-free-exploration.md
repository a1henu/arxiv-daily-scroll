---
layout: default
title: Improved Bounds for Reward-Agnostic and Reward-Free Exploration
---

# Improved Bounds for Reward-Agnostic and Reward-Free Exploration
**arXiv**：[2602.16363v1](https://arxiv.org/abs/2602.16363) · [PDF](https://arxiv.org/pdf/2602.16363.pdf)  
**作者**：Oran Ridel, Alon Cohen  

**一句话要点**：提出新算法以放宽奖励无关探索中对精度参数ε的限制要求

**关键词**：奖励无关探索, 马尔可夫决策过程, 在线学习, 样本复杂度, 最优策略

## 3 点简述
- 研究无奖励和奖励无关探索，目标是在未知MDP中实现ε最优策略
- 算法采用在线学习过程，设计奖励构建探索策略以收集数据
- 建立奖励无关探索的紧下界，缩小了已知上下界之间的差距

## 摘要（原文）

> We study reward-free and reward-agnostic exploration in episodic finite-horizon Markov decision processes (MDPs), where an agent explores an unknown environment without observing external rewards. Reward-free exploration aims to enable $ε$-optimal policies for any reward revealed after exploration, while reward-agnostic exploration targets $ε$-optimality for rewards drawn from a small finite class. In the reward-agnostic setting, Li, Yan, Chen, and Fan achieve minimax sample complexity, but only for restrictively small accuracy parameter $ε$. We propose a new algorithm that significantly relaxes the requirement on $ε$. Our approach is novel and of technical interest by itself. Our algorithm employs an online learning procedure with carefully designed rewards to construct an exploration policy, which is used to gather data sufficient for accurate dynamics estimation and subsequent computation of an $ε$-optimal policy once the reward is revealed. Finally, we establish a tight lower bound for reward-free exploration, closing the gap between known upper and lower bounds.


---
layout: default
title: Learning Distributed Equilibria in Linear-Quadratic Stochastic Differential Games: An $α$-Potential Approach
---

# Learning Distributed Equilibria in Linear-Quadratic Stochastic Differential Games: An $α$-Potential Approach
**arXiv**：[2602.16555v1](https://arxiv.org/abs/2602.16555) · [PDF](https://arxiv.org/pdf/2602.16555.pdf)  
**作者**：Philipp Plank, Yufei Zhang  

**一句话要点**：提出α-势能方法以分析线性-二次随机微分博弈中独立策略梯度学习的全局收敛性

**关键词**：随机微分博弈, 策略梯度学习, 分布式均衡, α-势能, 线性-二次控制, 收敛分析

## 3 点简述
- 研究N玩家线性-二次随机微分博弈中独立策略梯度学习的收敛问题
- 利用α-势能结构证明全局线性收敛，对称交互下构建分布式均衡
- 数值实验验证理论结果，收敛复杂度随玩家数线性增长

## 摘要（原文）

> We analyze independent policy-gradient (PG) learning in $N$-player linear-quadratic (LQ) stochastic differential games. Each player employs a distributed policy that depends only on its own state and updates the policy independently using the gradient of its own objective. We establish global linear convergence of these methods to an equilibrium by showing that the LQ game admits an $α$-potential structure, with $α$ determined by the degree of pairwise interaction asymmetry. For pairwise-symmetric interactions, we construct an affine distributed equilibrium by minimizing the potential function and show that independent PG methods converge globally to this equilibrium, with complexity scaling linearly in the population size and logarithmically in the desired accuracy. For asymmetric interactions, we prove that independent projected PG algorithms converge linearly to an approximate equilibrium, with suboptimality proportional to the degree of asymmetry. Numerical experiments confirm the theoretical results across both symmetric and asymmetric interaction networks.


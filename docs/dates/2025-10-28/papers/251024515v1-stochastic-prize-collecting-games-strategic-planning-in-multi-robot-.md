---
layout: default
title: Stochastic Prize-Collecting Games: Strategic Planning in Multi-Robot Systems
---

# Stochastic Prize-Collecting Games: Strategic Planning in Multi-Robot Systems
**arXiv**：[2510.24515v1](https://arxiv.org/abs/2510.24515) · [PDF](https://arxiv.org/pdf/2510.24515.pdf)  
**作者**：Malintha Fernando, Petter Ögren, Silun Zhang  

**一句话要点**：提出随机奖品收集游戏以解决多机器人系统中自利机器人在随机环境下的规划问题

**关键词**：多机器人系统, 随机规划, 纳什均衡, 团队定向问题, 强化学习, 竞争环境

## 3 点简述
- 核心问题：多机器人系统在奖励稀缺环境中竞争，传统团队定向问题假设合作，不适用于自利机器人。
- 方法要点：提出SPCG扩展TOP，引入序数秩搜索和虚构序数响应学习算法，计算均衡策略。
- 实验效果：在道路网络和合成图上评估，学习策略在团队规模扩展和奖励分布泛化方面优于基线。

## 摘要（原文）

> The Team Orienteering Problem (TOP) generalizes many real-world multi-robot
> scheduling and routing tasks that occur in autonomous mobility, aerial
> logistics, and surveillance applications. While many flavors of the TOP exist
> for planning in multi-robot systems, they assume that all the robots cooperate
> toward a single objective; thus, they do not extend to settings where the
> robots compete in reward-scarce environments. We propose Stochastic
> Prize-Collecting Games (SPCG) as an extension of the TOP to plan in the
> presence of self-interested robots operating on a graph, under energy
> constraints and stochastic transitions. A theoretical study on complete and
> star graphs establishes that there is a unique pure Nash equilibrium in SPCGs
> that coincides with the optimal routing solution of an equivalent TOP given a
> rank-based conflict resolution rule. This work proposes two algorithms: Ordinal
> Rank Search (ORS) to obtain the ''ordinal rank'' --one's effective rank in
> temporarily-formed local neighborhoods during the games' stages, and Fictitious
> Ordinal Response Learning (FORL) to obtain best-response policies against one's
> senior-rank opponents. Empirical evaluations conducted on road networks and
> synthetic graphs under both dynamic and stationary prize distributions show
> that 1) the state-aliasing induced by OR-conditioning enables learning policies
> that scale more efficiently to large team sizes than those trained with the
> global index, and 2) Policies trained with FORL generalize better to imbalanced
> prize distributions than those with other multi-agent training methods.
> Finally, the learned policies in the SPCG achieved between 87% and 95%
> optimality compared to an equivalent TOP solution obtained by mixed-integer
> linear programming.


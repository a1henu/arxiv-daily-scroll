---
layout: default
title: QuayPoints: A Reasoning Framework to Bridge the Information Gap Between Global and Local Planning in Autonomous Racing
---

# QuayPoints: A Reasoning Framework to Bridge the Information Gap Between Global and Local Planning in Autonomous Racing
**arXiv**：[2510.10886v1](https://arxiv.org/abs/2510.10886) · [PDF](https://arxiv.org/pdf/2510.10886.pdf)  
**作者**：Yashom Dighe, Youngjin Kim, Karthik Dantu  

**一句话要点**：提出QuayPoints框架以在自动驾驶赛车中传递全局最优性信息到局部规划器

**关键词**：自动驾驶赛车, 全局规划, 局部规划, 最优性传递, 决策框架, 路径规划

## 3 点简述
- 核心问题：标准自动驾驶管道中全局规划器的最优性信息在传递到局部规划器时丢失，导致决策受限
- 方法要点：引入QuayPoints区域，将时间最优性信息从全局规划器传递到局部规划器，辅助偏离最优路径时的决策
- 实验或效果：集成QuayPoints后，在四个赛道中能稳定超越速度达自车75%的对手

## 摘要（原文）

> Autonomous racing requires tight integration between perception, planning and
> control to minimize latency as well as timely decision making. A standard
> autonomy pipeline comprising a global planner, local planner, and controller
> loses information as the higher-level racing context is sequentially propagated
> downstream into specific task-oriented context. In particular, the global
> planner's understanding of optimality is typically reduced to a sparse set of
> waypoints, leaving the local planner to make reactive decisions with limited
> context. This paper investigates whether additional global insights,
> specifically time-optimality information, can be meaningfully passed to the
> local planner to improve downstream decisions. We introduce a framework that
> preserves essential global knowledge and conveys it to the local planner
> through QuayPoints regions where deviations from the optimal raceline result in
> significant compromises to optimality. QuayPoints enable local planners to make
> more informed global decisions when deviating from the raceline, such as during
> strategic overtaking. To demonstrate this, we integrate QuayPoints into an
> existing planner and show that it consistently overtakes opponents traveling at
> up to 75% of the ego vehicle's speed across four distinct race tracks.


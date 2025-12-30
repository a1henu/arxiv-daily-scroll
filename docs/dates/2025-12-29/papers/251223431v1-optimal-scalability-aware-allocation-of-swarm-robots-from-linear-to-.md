---
layout: default
title: Optimal Scalability-Aware Allocation of Swarm Robots: From Linear to Retrograde Performance via Marginal Gains
---

# Optimal Scalability-Aware Allocation of Swarm Robots: From Linear to Retrograde Performance via Marginal Gains
**arXiv**：[2512.23431v1](https://arxiv.org/abs/2512.23431) · [PDF](https://arxiv.org/pdf/2512.23431.pdf)  
**作者**：Simay Atasoy Bingöl, Tobias Töpfer, Sven Kosub, Heiko Hamann, Andreagiovanni Reina  

**一句话要点**：提出基于边际增益的算法，以优化群体机器人在任务间的分配，最大化集体性能。

**关键词**：群体机器人分配, 边际增益算法, 非线性性能缩放, 集体决策任务, 可扩展性函数

## 3 点简述
- 核心问题：在集体系统中，如何高效分配有限代理到多个任务，以应对不同任务性能随代理数变化的非线性缩放。
- 方法要点：基于边际性能增益，设计计算高效算法，适用于凹可扩展性函数，包括线性、饱和和倒退缩放。
- 实验或效果：通过模拟机器人群体在集体决策任务中的分配测试，算法能有效处理饱和和倒退缩放场景，提升部署实用性。

## 摘要（原文）

> In collective systems, the available agents are a limited resource that must be allocated among tasks to maximize collective performance. Computing the optimal allocation of several agents to numerous tasks through a brute-force approach can be infeasible, especially when each task's performance scales differently with the increase of agents. For example, difficult tasks may require more agents to achieve similar performances compared to simpler tasks, but performance may saturate nonlinearly as the number of allocated agents increases. We propose a computationally efficient algorithm, based on marginal performance gains, for optimally allocating agents to tasks with concave scalability functions, including linear, saturating, and retrograde scaling, to achieve maximum collective performance. We test the algorithm by allocating a simulated robot swarm among collective decision-making tasks, where embodied agents sample their environment and exchange information to reach a consensus on spatially distributed environmental features. We vary task difficulties by different geometrical arrangements of environmental features in space (patchiness). In this scenario, decision performance in each task scales either as a saturating curve (following the Condorcet's Jury Theorem in an interference-free setup) or as a retrograde curve (when physical interference among robots restricts their movement). Using simple robot simulations, we show that our algorithm can be useful in allocating robots among tasks. Our approach aims to advance the deployment of future real-world multi-robot systems.


---
layout: default
title: CASSR: Continuous A-Star Search through Reachability for real time footstep planning
---

# CASSR: Continuous A-Star Search through Reachability for real time footstep planning
**arXiv**：[2603.02989v1](https://arxiv.org/abs/2603.02989) · [PDF](https://arxiv.org/pdf/2603.02989.pdf)  
**作者**：Jiayi Wang, Steve Tonneau  

**一句话要点**：提出CASSR框架，通过连续可达性A*搜索实现实时足部步态规划

**关键词**：足部步态规划, A*搜索, 连续可达性, 运动学约束, 实时规划, 双足机器人

## 3 点简述
- 核心问题：足部步态规划涉及组合搜索，传统A*需离散化可达约束，MIP连续但计算复杂。
- 方法要点：CASSR在A*搜索中递归传播机器人运动学约束的连续凸公式，结合基于EPA算法的启发式成本。
- 实验或效果：在双足运动任务中，CASSR比传统离散A*快达100倍，超越商业MIP求解器，125毫秒内规划30步。

## 摘要（原文）

> Footstep planning involves a challenging combinatorial search. Traditional A* approaches require discretising reachability constraints, while Mixed-Integer Programming (MIP) supports continuous formulations but quickly becomes intractable, especially when rotations are included. We present CASSR, a novel framework that recursively propagates convex, continuous formulations of a robot's kinematic constraints within an A* search. Combined with a new cost-to-go heuristic based on the EPA algorithm, CASSR efficiently plans contact sequences of up to 30 footsteps in under 125 ms. Experiments on biped locomotion tasks demonstrate that CASSR outperforms traditional discretised A* by up to a factor of 100, while also surpassing a commercial MIP solver. These results show that CASSR enables fast, reliable, and real-time footstep planning for biped robots.


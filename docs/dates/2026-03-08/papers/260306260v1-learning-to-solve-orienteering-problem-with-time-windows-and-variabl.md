---
layout: default
title: Learning to Solve Orienteering Problem with Time Windows and Variable Profits
---

# Learning to Solve Orienteering Problem with Time Windows and Variable Profits
**arXiv**：[2603.06260v1](https://arxiv.org/abs/2603.06260) · [PDF](https://arxiv.org/pdf/2603.06260.pdf)  
**作者**：Songqun Gao, Zanxi Ruan, Patrick Floor, Marco Roveri, Luigi Palopoli, Daniele Fontanelli  

**一句话要点**：提出DeCoST方法以解决带时间窗和可变收益定向问题中的离散-连续变量耦合优化

**关键词**：定向问题, 离散-连续优化, 学习型求解器, 两阶段解耦, 线性规划优化, 服务时间分配

## 3 点简述
- 核心问题：OPTWVP涉及离散和连续变量，现有方法难以高效求解。
- 方法要点：采用两阶段解耦优化，第一阶段预测路径和初始服务时间，第二阶段通过线性规划优化服务时间。
- 实验或效果：在OPTWVP实例上优于现有求解器，推理速度提升最高达6.6倍。

## 摘要（原文）

> The orienteering problem with time windows and variable profits (OPTWVP) is common in many real-world applications and involves continuous time variables. Current approaches fail to develop an efficient solver for this orienteering problem variant with discrete and continuous variables. In this paper, we propose a learning-based two-stage DEcoupled discrete-Continuous optimization with Service-time-guided Trajectory (DeCoST), which aims to effectively decouple the discrete and continuous decision variables in the OPTWVP problem, while enabling efficient and learnable coordination between them. In the first stage, a parallel decoding structure is employed to predict the path and the initial service time allocation. The second stage optimizes the service times through a linear programming (LP) formulation and provides a long-horizon learning of structure estimation. We rigorously prove the global optimality of the second-stage solution. Experiments on OPTWVP instances demonstrate that DeCoST outperforms both state-of-the-art constructive solvers and the latest meta-heuristic algorithms in terms of solution quality and computational efficiency, achieving up to 6.6x inference speedup on instances with fewer than 500 nodes. Moreover, the proposed framework is compatible with various constructive solvers and consistently enhances the solution quality for OPTWVP.


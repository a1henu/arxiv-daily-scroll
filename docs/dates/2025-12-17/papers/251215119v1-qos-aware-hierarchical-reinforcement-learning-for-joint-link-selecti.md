---
layout: default
title: QoS-Aware Hierarchical Reinforcement Learning for Joint Link Selection and Trajectory Optimization in SAGIN-Supported UAV Mobility Management
---

# QoS-Aware Hierarchical Reinforcement Learning for Joint Link Selection and Trajectory Optimization in SAGIN-Supported UAV Mobility Management
**arXiv**：[2512.15119v1](https://arxiv.org/abs/2512.15119) · [PDF](https://arxiv.org/pdf/2512.15119.pdf)  
**作者**：Jiayang Wan, Ke He, Yafei Wang, Fan Liu, Wenjin Wang, Shi Jin  

**一句话要点**：提出分层强化学习框架以解决SAGIN中无人机移动管理的联合链路选择与轨迹优化问题

**关键词**：无人机移动管理, 空天地一体化网络, 分层强化学习, 联合优化, 服务质量约束, 多智能体系统

## 3 点简述
- 核心问题：异构网络覆盖差异导致无人机移动时难以保障连续可靠的三维连接
- 方法要点：采用双层多智能体架构，上层DDQN处理离散链路选择，下层CSAC处理连续轨迹优化
- 实验效果：仿真显示在吞吐量、链路切换频率和QoS满足度方面显著优于现有基准

## 摘要（原文）

> Due to the significant variations in unmanned aerial vehicle (UAV) altitude and horizontal mobility, it becomes difficult for any single network to ensure continuous and reliable threedimensional coverage. Towards that end, the space-air-ground integrated network (SAGIN) has emerged as an essential architecture for enabling ubiquitous UAV connectivity. To address the pronounced disparities in coverage and signal characteristics across heterogeneous networks, this paper formulates UAV mobility management in SAGIN as a constrained multi-objective joint optimization problem. The formulation couples discrete link selection with continuous trajectory optimization. Building on this, we propose a two-level multi-agent hierarchical deep reinforcement learning (HDRL) framework that decomposes the problem into two alternately solvable subproblems. To map complex link selection decisions into a compact discrete action space, we conceive a double deep Q-network (DDQN) algorithm in the top-level, which achieves stable and high-quality policy learning through double Q-value estimation. To handle the continuous trajectory action space while satisfying quality of service (QoS) constraints, we integrate the maximum-entropy mechanism of the soft actor-critic (SAC) and employ a Lagrangian-based constrained SAC (CSAC) algorithm in the lower-level that dynamically adjusts the Lagrange multipliers to balance constraint satisfaction and policy optimization. Moreover, the proposed algorithm can be extended to multi-UAV scenarios under the centralized training and decentralized execution (CTDE) paradigm, which enables more generalizable policies. Simulation results demonstrate that the proposed scheme substantially outperforms existing benchmarks in throughput, link switching frequency and QoS satisfaction.


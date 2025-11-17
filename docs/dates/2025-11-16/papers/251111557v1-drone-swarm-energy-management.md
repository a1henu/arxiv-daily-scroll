---
layout: default
title: Drone Swarm Energy Management
---

# Drone Swarm Energy Management
**arXiv**：[2511.11557v1](https://arxiv.org/abs/2511.11557) · [PDF](https://arxiv.org/pdf/2511.11557.pdf)  
**作者**：Michael Z. Zgurovsky, Pavlo O. Kasyanov, Liliia S. Paliichuk  

**一句话要点**：提出POMDP-DDPG框架以解决无人机群在不确定环境中的能量管理与控制问题

**关键词**：无人机群控制, 部分可观测马尔可夫决策过程, 深度确定性策略梯度, 能量管理, 多智能体强化学习, 认知AI平台

## 3 点简述
- 核心问题：无人机群在部分可观测环境下的能量管理与自适应控制决策
- 方法要点：结合POMDP与DDPG强化学习，引入贝叶斯滤波信念状态表示
- 实验或效果：仿真显示模型显著提升任务成功率和能量效率，优于基线方法

## 摘要（原文）

> This note presents an analytical framework for decision-making in drone swarm systems operating under uncertainty, based on the integration of Partially Observable Markov Decision Processes (POMDP) with Deep Deterministic Policy Gradient (DDPG) reinforcement learning. The proposed approach enables adaptive control and cooperative behavior of unmanned aerial vehicles (UAVs) within a cognitive AI platform, where each agent learns optimal energy management and navigation policies from dynamic environmental states. We extend the standard DDPG architecture with a belief-state representation derived from Bayesian filtering, allowing for robust decision-making in partially observable environments. In this paper, for the Gaussian case, we numerically compare the performance of policies derived from DDPG to optimal policies for discretized versions of the original continuous problem. Simulation results demonstrate that the POMDP-DDPG-based swarm control model significantly improves mission success rates and energy efficiency compared to baseline methods. The developed framework supports distributed learning and decision coordination across multiple agents, providing a foundation for scalable cognitive swarm autonomy. The outcomes of this research contribute to the advancement of energy-aware control algorithms for intelligent multi-agent systems and can be applied in security, environmental monitoring, and infrastructure inspection scenarios.


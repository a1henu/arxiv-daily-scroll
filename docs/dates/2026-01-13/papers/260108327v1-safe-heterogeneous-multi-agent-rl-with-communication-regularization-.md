---
layout: default
title: Safe Heterogeneous Multi-Agent RL with Communication Regularization for Coordinated Target Acquisition
---

# Safe Heterogeneous Multi-Agent RL with Communication Regularization for Coordinated Target Acquisition
**arXiv**：[2601.08327v1](https://arxiv.org/abs/2601.08327) · [PDF](https://arxiv.org/pdf/2601.08327.pdf)  
**作者**：Gabriele Calzolari, Vidya Sumathy, Christoforos Kanellakis, George Nikolakopoulos  

**一句话要点**：提出基于通信正则化的异构多智能体强化学习框架，用于安全协调目标获取

**关键词**：多智能体强化学习, 异构智能体, 通信正则化, 图注意力网络, 安全过滤器, 目标获取

## 3 点简述
- 核心问题：异构多智能体在部分可观测、通信受限环境中协同发现和获取随机目标。
- 方法要点：采用MAPPO算法和图注意力网络，结合安全过滤器实现基于图的通信和轨迹安全。
- 实验或效果：通过消融研究验证奖励函数有效性，仿真显示安全稳定的任务执行。

## 摘要（原文）

> This paper introduces a decentralized multi-agent reinforcement learning framework enabling structurally heterogeneous teams of agents to jointly discover and acquire randomly located targets in environments characterized by partial observability, communication constraints, and dynamic interactions. Each agent's policy is trained with the Multi-Agent Proximal Policy Optimization algorithm and employs a Graph Attention Network encoder that integrates simulated range-sensing data with communication embeddings exchanged among neighboring agents, enabling context-aware decision-making from both local sensing and relational information. In particular, this work introduces a unified framework that integrates graph-based communication and trajectory-aware safety through safety filters. The architecture is supported by a structured reward formulation designed to encourage effective target discovery and acquisition, collision avoidance, and de-correlation between the agents' communication vectors by promoting informational orthogonality. The effectiveness of the proposed reward function is demonstrated through a comprehensive ablation study. Moreover, simulation results demonstrate safe and stable task execution, confirming the framework's effectiveness.


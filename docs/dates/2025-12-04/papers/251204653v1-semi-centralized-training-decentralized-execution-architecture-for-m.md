---
layout: default
title: Semi Centralized Training Decentralized Execution Architecture for Multi Agent Deep Reinforcement Learning in Traffic Signal Control
---

# Semi Centralized Training Decentralized Execution Architecture for Multi Agent Deep Reinforcement Learning in Traffic Signal Control
**arXiv**：[2512.04653v1](https://arxiv.org/abs/2512.04653) · [PDF](https://arxiv.org/pdf/2512.04653.pdf)  
**作者**：Pouria Yazdani, Arash Rezaali, Monireh Abdoos  

**一句话要点**：提出半集中训练去中心化执行架构以解决多智能体强化学习在交通信号控制中的协调与可扩展性问题

**关键词**：多智能体强化学习, 交通信号控制, 半集中训练, 去中心化执行, 区域划分, 参数共享

## 3 点简述
- 现有方法存在维度灾难或部分可观测性限制，导致性能次优
- 基于区域划分，采用集中训练与参数共享，结合局部和区域信息的状态奖励设计
- 实验表明该架构在多种交通密度下性能优越，且可迁移至不同策略骨干

## 摘要（原文）

> Multi-agent reinforcement learning (MARL) has emerged as a promising paradigm for adaptive traffic signal control (ATSC) of multiple intersections. Existing approaches typically follow either a fully centralized or a fully decentralized design. Fully centralized approaches suffer from the curse of dimensionality, and reliance on a single learning server, whereas purely decentralized approaches operate under severe partial observability and lack explicit coordination resulting in suboptimal performance. These limitations motivate region-based MARL, where the network is partitioned into smaller, tightly coupled intersections that form regions, and training is organized around these regions. This paper introduces a Semi-Centralized Training, Decentralized Execution (SEMI-CTDE) architecture for multi intersection ATSC. Within each region, SEMI-CTDE performs centralized training with regional parameter sharing and employs composite state and reward formulations that jointly encode local and regional information. The architecture is highly transferable across different policy backbones and state-reward instantiations. Building on this architecture, we implement two models with distinct design objectives. A multi-perspective experimental analysis of the two implemented SEMI-CTDE-based models covering ablations of the architecture's core elements including rule based and fully decentralized baselines shows that they achieve consistently superior performance and remain effective across a wide range of traffic densities and distributions.


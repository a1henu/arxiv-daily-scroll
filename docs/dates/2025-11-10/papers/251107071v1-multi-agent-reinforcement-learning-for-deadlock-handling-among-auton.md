---
layout: default
title: Multi-Agent Reinforcement Learning for Deadlock Handling among Autonomous Mobile Robots
---

# Multi-Agent Reinforcement Learning for Deadlock Handling among Autonomous Mobile Robots
**arXiv**：[2511.07071v1](https://arxiv.org/abs/2511.07071) · [PDF](https://arxiv.org/pdf/2511.07071.pdf)  
**作者**：Marcel Müller  

**一句话要点**：提出多智能体强化学习方法以解决自主移动机器人在物流系统中的死锁问题

**关键词**：多智能体强化学习, 自主移动机器人, 死锁处理, 物流系统, 路径规划

## 3 点简述
- 核心问题：自主移动机器人系统易发死锁，降低吞吐量和可靠性
- 方法要点：集成MARL于物流规划，使用PPO和IMPALA算法进行训练
- 实验或效果：MARL策略在复杂环境中优于规则方法，需根据场景定制

## 摘要（原文）

> This dissertation explores the application of multi-agent reinforcement
> learning (MARL) for handling deadlocks in intralogistics systems that rely on
> autonomous mobile robots (AMRs). AMRs enhance operational flexibility but also
> increase the risk of deadlocks, which degrade system throughput and
> reliability. Existing approaches often neglect deadlock handling in the
> planning phase and rely on rigid control rules that cannot adapt to dynamic
> operational conditions.
>   To address these shortcomings, this work develops a structured methodology
> for integrating MARL into logistics planning and operational control. It
> introduces reference models that explicitly consider deadlock-capable
> multi-agent pathfinding (MAPF) problems, enabling systematic evaluation of MARL
> strategies. Using grid-based environments and an external simulation software,
> the study compares traditional deadlock handling strategies with MARL-based
> solutions, focusing on PPO and IMPALA algorithms under different training and
> execution modes.
>   Findings reveal that MARL-based strategies, particularly when combined with
> centralized training and decentralized execution (CTDE), outperform rule-based
> methods in complex, congested environments. In simpler environments or those
> with ample spatial freedom, rule-based methods remain competitive due to their
> lower computational demands. These results highlight that MARL provides a
> flexible and scalable solution for deadlock handling in dynamic intralogistics
> scenarios, but requires careful tailoring to the operational context.


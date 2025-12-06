---
layout: default
title: Multi-Agent Reinforcement Learning for Intraday Operating Rooms Scheduling under Uncertainty
---

# Multi-Agent Reinforcement Learning for Intraday Operating Rooms Scheduling under Uncertainty
**arXiv**：[2512.04918v1](https://arxiv.org/abs/2512.04918) · [PDF](https://arxiv.org/pdf/2512.04918.pdf)  
**作者**：Kailiang Liu, Ying Chen, Ralf Borndörfer, Thorsten Koch  

**一句话要点**：提出多智能体强化学习框架以解决不确定环境下手术室日内调度问题

**关键词**：多智能体强化学习, 手术室调度, 不确定性优化, 马尔可夫博弈, PPO算法, 实时决策

## 3 点简述
- 核心问题：手术室日内调度是多目标决策问题，需平衡择期手术吞吐量、紧急需求、延迟、序列依赖设置和加班。
- 方法要点：将问题建模为合作马尔可夫博弈，采用集中训练分散执行的多智能体强化学习，使用PPO训练共享策略。
- 实验或效果：在模拟医院环境中，学习策略优于六种基于规则的启发式方法，并通过与事后MIP预言机比较量化最优性差距。

## 摘要（原文）

> Intraday surgical scheduling is a multi-objective decision problem under uncertainty-balancing elective throughput, urgent and emergency demand, delays, sequence-dependent setups, and overtime. We formulate the problem as a cooperative Markov game and propose a multi-agent reinforcement learning (MARL) framework in which each operating room (OR) is an agent trained with centralized training and decentralized execution. All agents share a policy trained via Proximal Policy Optimization (PPO), which maps rich system states to actions, while a within-epoch sequential assignment protocol constructs conflict-free joint schedules across ORs. A mixed-integer pre-schedule provides reference starting times for electives; we impose type-specific quadratic delay penalties relative to these references and a terminal overtime penalty, yielding a single reward that captures throughput, timeliness, and staff workload. In simulations reflecting a realistic hospital mix (six ORs, eight surgery types, random urgent and emergency arrivals), the learned policy outperforms six rule-based heuristics across seven metrics and three evaluation subsets, and, relative to an ex post MIP oracle, quantifies optimality gaps. Policy analytics reveal interpretable behavior-prioritizing emergencies, batching similar cases to reduce setups, and deferring lower-value electives. We also derive a suboptimality bound for the sequential decomposition under simplifying assumptions. We discuss limitations-including OR homogeneity and the omission of explicit staffing constraints-and outline extensions. Overall, the approach offers a practical, interpretable, and tunable data-driven complement to optimization for real-time OR scheduling.


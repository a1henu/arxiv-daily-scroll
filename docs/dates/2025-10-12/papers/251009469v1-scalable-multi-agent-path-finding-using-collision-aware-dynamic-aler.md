---
layout: default
title: Scalable Multi-Agent Path Finding using Collision-Aware Dynamic Alert Mask and a Hybrid Execution Strategy
---

# Scalable Multi-Agent Path Finding using Collision-Aware Dynamic Alert Mask and a Hybrid Execution Strategy
**arXiv**：[2510.09469v1](https://arxiv.org/abs/2510.09469) · [PDF](https://arxiv.org/pdf/2510.09469.pdf)  
**作者**：Bharath Muppasani, Ritirupa Dey, Biplav Srivastava, Vignesh Narayanan  

**一句话要点**：提出混合框架结合去中心化路径规划与轻量级中央协调器，以解决大规模多智能体路径规划问题。

**关键词**：多智能体路径规划, 强化学习, 混合框架, 冲突解决, 可扩展性

## 3 点简述
- 多智能体路径规划在机器人中需高效导航并避免冲突，传统方法计算昂贵，分布式方法牺牲质量。
- 方法结合强化学习去中心化规划与动态警报共享，减少信息交换，确保无碰撞解决方案。
- 实验验证在大规模场景中可行，减少冲突并保持高可扩展性。

## 摘要（原文）

> Multi-agent pathfinding (MAPF) remains a critical problem in robotics and
> autonomous systems, where agents must navigate shared spaces efficiently while
> avoiding conflicts. Traditional centralized algorithms that have global
> information, such as Conflict-Based Search (CBS), provide high-quality
> solutions but become computationally expensive in large-scale scenarios due to
> the combinatorial explosion of conflicts that need resolution. Conversely,
> distributed approaches that have local information, particularly learning-based
> methods, offer better scalability by operating with relaxed information
> availability, yet often at the cost of solution quality. To address these
> limitations, we propose a hybrid framework that combines decentralized path
> planning with a lightweight centralized coordinator. Our framework leverages
> reinforcement learning (RL) for decentralized planning, enabling agents to
> adapt their planning based on minimal, targeted alerts--such as static
> conflict-cell flags or brief conflict tracks--that are dynamically shared
> information from the central coordinator for effective conflict resolution. We
> empirically study the effect of the information available to an agent on its
> planning performance. Our approach reduces the inter-agent information sharing
> compared to fully centralized and distributed methods, while still consistently
> finding feasible, collision-free solutions--even in large-scale scenarios
> having higher agent counts.


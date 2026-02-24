---
layout: default
title: CACTO-BIC: Scalable Actor-Critic Learning via Biased Sampling and GPU-Accelerated Trajectory Optimization
---

# CACTO-BIC: Scalable Actor-Critic Learning via Biased Sampling and GPU-Accelerated Trajectory Optimization
**arXiv**：[2602.19699v1](https://arxiv.org/abs/2602.19699) · [PDF](https://arxiv.org/pdf/2602.19699.pdf)  
**作者**：Elisa Alboni, Pietro Noah Crestaz, Elias Fontanari, Andrea Del Prete  

**一句话要点**：提出CACTO-BIC以提升轨迹优化与强化学习结合方法的可扩展性

**关键词**：轨迹优化, 强化学习, GPU加速, 样本效率, 高维系统控制

## 3 点简述
- 核心问题：轨迹优化与强化学习结合方法在系统复杂度增加时计算成本高，可扩展性受限
- 方法要点：通过价值函数特性偏置初始状态采样提升数据效率，并利用GPU加速减少计算时间
- 实验或效果：实验显示相比CACTO改进样本效率和计算速度，在四足机器人上验证高维系统适用性

## 摘要（原文）

> Trajectory Optimization (TO) and Reinforcement Learning (RL) offer complementary strengths for solving optimal control problems. TO efficiently computes locally optimal solutions but can struggle with non-convexity, while RL is more robust to non-convexity at the cost of significantly higher computational demands. CACTO (Continuous Actor-Critic with Trajectory Optimization) was introduced to combine these advantages by learning a warm-start policy that guides the TO solver towards low-cost trajectories. However, scalability remains a key limitation, as increasing system complexity significantly raises the computational cost of TO. This work introduces CACTO-BIC to address these challenges. CACTO-BIC improves data efficiency by biasing initial-state sampling leveraging a property of the value function associated with locally optimal policies; moreover, it reduces computation time by exploiting GPU acceleration. Empirical evaluations show improved sample efficiency and faster computation compared to CACTO. Comparisons with PPO demonstrate that our approach can achieve similar solutions in less time. Finally, experiments on the AlienGO quadruped robot demonstrate that CACTO-BIC can scale to high-dimensional systems and is suitable for real-time applications.


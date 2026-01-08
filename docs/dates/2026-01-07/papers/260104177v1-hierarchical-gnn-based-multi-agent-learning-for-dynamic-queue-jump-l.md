---
layout: default
title: Hierarchical GNN-Based Multi-Agent Learning for Dynamic Queue-Jump Lane and Emergency Vehicle Corridor Formation
---

# Hierarchical GNN-Based Multi-Agent Learning for Dynamic Queue-Jump Lane and Emergency Vehicle Corridor Formation
**arXiv**：[2601.04177v1](https://arxiv.org/abs/2601.04177) · [PDF](https://arxiv.org/pdf/2601.04177.pdf)  
**作者**：Haoran Su  

**一句话要点**：提出基于分层图神经网络的多智能体强化学习框架，以协调联网车辆形成应急走廊，解决拥堵交通中应急车辆快速通行问题。

**关键词**：应急车辆走廊, 分层图神经网络, 多智能体强化学习, 交通协调, 图注意力网络, 智能交通系统

## 3 点简述
- 核心问题：现有策略无法适应动态交通条件，应急车辆在拥堵中通行困难。
- 方法要点：采用分层GNN框架，高层规划器制定全局策略，低层控制器执行轨迹，利用图注意力网络适应可变智能体数量。
- 实验或效果：在模拟中，相比基线减少应急车辆旅行时间28.3%，碰撞率接近零（0.3%），保持81%背景交通效率。

## 摘要（原文）

> Emergency vehicles require rapid passage through congested traffic, yet existing strategies fail to adapt to dynamic conditions. We propose a novel hierarchical graph neural network (GNN)-based multi-agent reinforcement learning framework to coordinate connected vehicles for emergency corridor formation. Our approach uses a high-level planner for global strategy and low-level controllers for trajectory execution, utilizing graph attention networks to scale with variable agent counts. Trained via Multi-Agent Proximal Policy Optimization (MAPPO), the system reduces emergency vehicle travel time by 28.3% compared to baselines and 44.6% compared to uncoordinated traffic in simulations. The design achieves near-zero collision rates (0.3%) while maintaining 81% of background traffic efficiency. Ablation and generalization studies confirm the framework's robustness across diverse scenarios. These results demonstrate the effectiveness of combining GNNs with hierarchical learning for intelligent transportation systems.


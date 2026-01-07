---
layout: default
title: Effective Online 3D Bin Packing with Lookahead Parcels Using Monte Carlo Tree Search
---

# Effective Online 3D Bin Packing with Lookahead Parcels Using Monte Carlo Tree Search
**arXiv**：[2601.02649v1](https://arxiv.org/abs/2601.02649) · [PDF](https://arxiv.org/pdf/2601.02649.pdf)  
**作者**：Jiangyi Fang, Bowen Zhou, Haotian Wang, Xin Zhu, Leye Wang  

**一句话要点**：提出基于蒙特卡洛树搜索的在线三维装箱方法，利用前瞻包裹信息应对物流中的分布偏移问题。

**关键词**：在线三维装箱, 蒙特卡洛树搜索, 模型预测控制, 分布偏移, 前瞻信息, 物流优化

## 3 点简述
- 核心问题：在线三维装箱在物流中面临短期分布偏移，导致深度强化学习性能下降。
- 方法要点：将问题建模为模型预测控制，采用蒙特卡洛树搜索框架，结合动态探索先验平衡学习策略与随机策略。
- 实验或效果：在真实数据集上优于基线，分布偏移下提升超10%，在线部署平均提升4%。

## 摘要（原文）

> Online 3D Bin Packing (3D-BP) with robotic arms is crucial for reducing transportation and labor costs in modern logistics. While Deep Reinforcement Learning (DRL) has shown strong performance, it often fails to adapt to real-world short-term distribution shifts, which arise as different batches of goods arrive sequentially, causing performance drops. We argue that the short-term lookahead information available in modern logistics systems is key to mitigating this issue, especially during distribution shifts. We formulate online 3D-BP with lookahead parcels as a Model Predictive Control (MPC) problem and adapt the Monte Carlo Tree Search (MCTS) framework to solve it. Our framework employs a dynamic exploration prior that automatically balances a learned RL policy and a robust random policy based on the lookahead characteristics. Additionally, we design an auxiliary reward to penalize long-term spatial waste from individual placements. Extensive experiments on real-world datasets show that our method consistently outperforms state-of-the-art baselines, achieving over 10\% gains under distributional shifts, 4\% average improvement in online deployment, and up to more than 8\% in the best case--demonstrating the effectiveness of our framework.


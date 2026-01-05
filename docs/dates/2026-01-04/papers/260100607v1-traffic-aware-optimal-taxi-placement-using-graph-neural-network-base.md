---
layout: default
title: Traffic-Aware Optimal Taxi Placement Using Graph Neural Network-Based Reinforcement Learning
---

# Traffic-Aware Optimal Taxi Placement Using Graph Neural Network-Based Reinforcement Learning
**arXiv**：[2601.00607v1](https://arxiv.org/abs/2601.00607) · [PDF](https://arxiv.org/pdf/2601.00607.pdf)  
**作者**：Sonia Khetarpaul, P Y Sharan  

**一句话要点**：提出基于图神经网络强化学习的交通感知出租车最优放置框架，以优化智能城市交通匹配。

**关键词**：图神经网络, 强化学习, 交通感知优化, 出租车放置, 智能城市交通

## 3 点简述
- 核心问题：传统出租车热点预测忽略交通拥堵等动态因素，导致供需匹配效率低。
- 方法要点：将城市路网建模为图，利用GNN编码时空依赖，通过Q学习推荐最优出租车放置点。
- 实验或效果：在模拟德里数据集上，乘客等待时间减少约56%，行驶距离减少38%。

## 摘要（原文）

> In the context of smart city transportation, efficient matching of taxi supply with passenger demand requires real-time integration of urban traffic network data and mobility patterns. Conventional taxi hotspot prediction models often rely solely on historical demand, overlooking dynamic influences such as traffic congestion, road incidents, and public events. This paper presents a traffic-aware, graph-based reinforcement learning (RL) framework for optimal taxi placement in metropolitan environments. The urban road network is modeled as a graph where intersections represent nodes, road segments serve as edges, and node attributes capture historical demand, event proximity, and real-time congestion scores obtained from live traffic APIs. Graph Neural Network (GNN) embeddings are employed to encode spatial-temporal dependencies within the traffic network, which are then used by a Q-learning agent to recommend optimal taxi hotspots. The reward mechanism jointly optimizes passenger waiting time, driver travel distance, and congestion avoidance. Experiments on a simulated Delhi taxi dataset, generated using real geospatial boundaries and historic ride-hailing request patterns, demonstrate that the proposed model reduced passenger waiting time by about 56% and reduced travel distance by 38% compared to baseline stochastic selection. The proposed approach is adaptable to multi-modal transport systems and can be integrated into smart city platforms for real-time urban mobility optimization.


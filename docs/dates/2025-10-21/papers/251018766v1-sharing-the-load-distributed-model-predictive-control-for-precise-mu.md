---
layout: default
title: Sharing the Load: Distributed Model-Predictive Control for Precise Multi-Rover Cargo Transport
---

# Sharing the Load: Distributed Model-Predictive Control for Precise Multi-Rover Cargo Transport
**arXiv**：[2510.18766v1](https://arxiv.org/abs/2510.18766) · [PDF](https://arxiv.org/pdf/2510.18766.pdf)  
**作者**：Alexander Krawciw, Sven Lilge, Luka Antonyshyn, Timothy D. Barfoot  

**一句话要点**：提出分布式模型预测控制以实现多车精确货物运输

**关键词**：分布式模型预测控制, 多车货物运输, 路径跟踪, 共享地图定位, 实时控制

## 3 点简述
- 核心问题：多车货物运输中需精确控制车辆间距和路径跟踪
- 方法要点：基于共享地图定位，无需GNSS或直接观测
- 实验或效果：分布式MPC性能与集中式相当，实时保持间距误差小于20cm

## 摘要（原文）

> For autonomous cargo transportation, teams of mobile robots can provide more
> operational flexibility than a single large robot. In these scenarios,
> precision in both inter-vehicle distance and path tracking is key. With this
> motivation, we develop a distributed model-predictive controller (MPC) for
> multi-vehicle cargo operations that builds on the precise path-tracking of
> lidar teach and repeat. To carry cargo, a following vehicle must maintain a
> Euclidean distance offset from a lead vehicle regardless of the path curvature.
> Our approach uses a shared map to localize the robots relative to each other
> without GNSS or direct observations. We compare our approach to a centralized
> MPC and a baseline approach that directly measures the inter-vehicle distance.
> The distributed MPC shows equivalent nominal performance to the more complex
> centralized MPC. Using a direct measurement of the relative distance between
> the leader and follower shows improved tracking performance in close-range
> scenarios but struggles with long-range offsets. The operational flexibility
> provided by distributing the computation makes it well suited for real
> deployments. We evaluate four types of convoyed path trackers with over 10 km
> of driving in a coupled convoy. With convoys of two and three rovers, the
> proposed distributed MPC method works in real-time to allow map-based convoying
> to maintain maximum spacing within 20 cm of the target in various conditions.


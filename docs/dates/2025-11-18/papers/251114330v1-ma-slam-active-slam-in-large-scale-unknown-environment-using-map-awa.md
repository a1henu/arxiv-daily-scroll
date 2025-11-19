---
layout: default
title: MA-SLAM: Active SLAM in Large-Scale Unknown Environment using Map Aware Deep Reinforcement Learning
---

# MA-SLAM: Active SLAM in Large-Scale Unknown Environment using Map Aware Deep Reinforcement Learning
**arXiv**：[2511.14330v1](https://arxiv.org/abs/2511.14330) · [PDF](https://arxiv.org/pdf/2511.14330.pdf)  
**作者**：Yizhen Yin, Yuhua Qi, Dapeng Feng, Hongbo Chen, Hongjun Ma, Jin Wu, Yi Jiang  

**一句话要点**：提出MA-SLAM系统，基于地图感知深度强化学习解决大规模未知环境高效探索问题

**关键词**：主动SLAM, 深度强化学习, 地图表示, 全局规划, 机器人探索

## 3 点简述
- 核心问题：现有主动SLAM方法在大规模多样环境中探索时间长、路径不优
- 方法要点：使用结构化地图表示和全局规划器优化探索路径
- 实验或效果：在仿真和真实UGV中显著减少探索时间和距离

## 摘要（原文）

> Active Simultaneous Localization and Mapping (Active SLAM) involves the strategic planning and precise control of a robotic system's movement in order to construct a highly accurate and comprehensive representation of its surrounding environment, which has garnered significant attention within the research community. While the current methods demonstrate efficacy in small and controlled settings, they face challenges when applied to large-scale and diverse environments, marked by extended periods of exploration and suboptimal paths of discovery. In this paper, we propose MA-SLAM, a Map-Aware Active SLAM system based on Deep Reinforcement Learning (DRL), designed to address the challenge of efficient exploration in large-scale environments. In pursuit of this objective, we put forward a novel structured map representation. By discretizing the spatial data and integrating the boundary points and the historical trajectory, the structured map succinctly and effectively encapsulates the visited regions, thereby serving as input for the deep reinforcement learning based decision module. Instead of sequentially predicting the next action step within the decision module, we have implemented an advanced global planner to optimize the exploration path by leveraging long-range target points. We conducted experiments in three simulation environments and deployed in a real unmanned ground vehicle (UGV), the results demonstrate that our approach significantly reduces both the duration and distance of exploration compared with state-of-the-art methods.


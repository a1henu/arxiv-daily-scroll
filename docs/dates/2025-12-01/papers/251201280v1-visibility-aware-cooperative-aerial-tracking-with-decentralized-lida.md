---
layout: default
title: Visibility-aware Cooperative Aerial Tracking with Decentralized LiDAR-based Swarms
---

# Visibility-aware Cooperative Aerial Tracking with Decentralized LiDAR-based Swarms
**arXiv**：[2512.01280v1](https://arxiv.org/abs/2512.01280) · [PDF](https://arxiv.org/pdf/2512.01280.pdf)  
**作者**：Longji Yin, Yunfan Ren, Fangcheng Zhu, Liuyu Shi, Fanze Kong, Benxu Tang, Wenyi Liu, Ximin Lyu, Fu Zhang  

**一句话要点**：提出基于LiDAR的分散式无人机群可见性感知协同跟踪框架，用于复杂环境中的目标追踪。

**关键词**：无人机群跟踪, 可见性感知, LiDAR感知, 分散式规划, 协同控制, 环境遮挡建模

## 3 点简述
- 核心问题：无人机群目标跟踪在分布式感知和可见性方面研究不足，需处理环境遮挡和异构配置。
- 方法要点：引入球形有符号距离场表示遮挡，结合层次规划器生成无碰撞、可见性优化的轨迹。
- 实验或效果：在杂乱户外环境中验证，系统能稳健协同跟踪敏捷目标，并保持优越可见性。

## 摘要（原文）

> Autonomous aerial tracking with drones offers vast potential for surveillance, cinematography, and industrial inspection applications. While single-drone tracking systems have been extensively studied, swarm-based target tracking remains underexplored, despite its unique advantages of distributed perception, fault-tolerant redundancy, and multidirectional target coverage. To bridge this gap, we propose a novel decentralized LiDAR-based swarm tracking framework that enables visibility-aware, cooperative target tracking in complex environments, while fully harnessing the unique capabilities of swarm systems. To address visibility, we introduce a novel Spherical Signed Distance Field (SSDF)-based metric for 3-D environmental occlusion representation, coupled with an efficient algorithm that enables real-time onboard SSDF updating. A general Field-of-View (FOV) alignment cost supporting heterogeneous LiDAR configurations is proposed for consistent target observation. Swarm coordination is enhanced through cooperative costs that enforce inter-robot safe clearance, prevent mutual occlusions, and notably facilitate 3-D multidirectional target encirclement via a novel electrostatic-potential-inspired distribution metric. These innovations are integrated into a hierarchical planner, combining a kinodynamic front-end searcher with a spatiotemporal $SE(3)$ back-end optimizer to generate collision-free, visibility-optimized trajectories.Deployed on heterogeneous LiDAR swarms, our fully decentralized implementation features collaborative perception, distributed planning, and dynamic swarm reconfigurability. Validated through rigorous real-world experiments in cluttered outdoor environments, the proposed system demonstrates robust cooperative tracking of agile targets (drones, humans) while achieving superior visibility maintenance.


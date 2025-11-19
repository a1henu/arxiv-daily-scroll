---
layout: default
title: BIM-Discrepancy-Driven Active Sensing for Risk-Aware UAV-UGV Navigation
---

# BIM-Discrepancy-Driven Active Sensing for Risk-Aware UAV-UGV Navigation
**arXiv**：[2511.14037v1](https://arxiv.org/abs/2511.14037) · [PDF](https://arxiv.org/pdf/2511.14037.pdf)  
**作者**：Hesam Mojtahedi, Reza Akhavian  

**一句话要点**：提出BIM差异驱动主动感知框架以解决动态建筑环境中无人机-地面车协同导航风险问题

**关键词**：无人机-地面车协同导航, BIM差异驱动感知, 风险感知规划, LiDAR数据融合, 动态建筑环境, 不确定性降低

## 3 点简述
- 传统导航依赖静态BIM或有限感知，无法适应动态环境变化
- 融合实时LiDAR与BIM先验，量化风险并触发无人机重扫描以降低不确定性
- 仿真验证风险触发重扫描使平均走廊风险降低58%，地图熵减少43%

## 摘要（原文）

> This paper presents a BIM-discrepancy-driven active sensing framework for cooperative navigation between unmanned aerial vehicles (UAVs) and unmanned ground vehicles (UGVs) in dynamic construction environments. Traditional navigation approaches rely on static Building Information Modeling (BIM) priors or limited onboard perception. In contrast, our framework continuously fuses real-time LiDAR data from aerial and ground robots with BIM priors to maintain an evolving 2D occupancy map. We quantify navigation safety through a unified corridor-risk metric integrating occupancy uncertainty, BIM-map discrepancy, and clearance. When risk exceeds safety thresholds, the UAV autonomously re-scans affected regions to reduce uncertainty and enable safe replanning. Validation in PX4-Gazebo simulation with Robotec GPU LiDAR demonstrates that risk-triggered re-scanning reduces mean corridor risk by 58% and map entropy by 43% compared to static BIM navigation, while maintaining clearance margins above 0.4 m. Compared to frontier-based exploration, our approach achieves similar uncertainty reduction in half the mission time. These results demonstrate that integrating BIM priors with risk-adaptive aerial sensing enables scalable, uncertainty-aware autonomy for construction robotics.


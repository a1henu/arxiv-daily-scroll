---
layout: default
title: Occlusion-Aware Ground Target Search by a UAV in an Urban Environment
---

# Occlusion-Aware Ground Target Search by a UAV in an Urban Environment
**arXiv**：[2511.07822v1](https://arxiv.org/abs/2511.07822) · [PDF](https://arxiv.org/pdf/2511.07822.pdf)  
**作者**：Collin Hague, Artur Wolek  

**一句话要点**：提出基于概率可见性体积的无人机路径规划方法，以解决城市环境中遮挡下的地面目标搜索问题。

**关键词**：无人机路径规划, 概率可见性体积, 迭代加深A*, 城市环境搜索, 遮挡感知

## 3 点简述
- 核心问题：无人机在城市道路网络中搜索移动兴趣点，传感器视线可能被遮挡。
- 方法要点：使用概率可见性体积和迭代加深A*规划路径，优化目标发现概率。
- 实验或效果：蒙特卡洛模拟显示，在高误报概率的杂乱环境中优于基线方法。

## 摘要（原文）

> This paper considers the problem of searching for a point of interest (POI) moving along an urban road network with an uncrewed aerial vehicle (UAV). The UAV is modeled as a variable-speed Dubins vehicle with a line-of-sight sensor in an urban environment that may occlude the sensor's view of the POI. A search strategy is proposed that exploits a probabilistic visibility volume (VV) to plan its future motion with iterative deepening $A^\ast$. The probabilistic VV is a time-varying three-dimensional representation of the sensing constraints for a particular distribution of the POI's state. To find the path most likely to view the POI, the planner uses a heuristic to optimistically estimate the probability of viewing the POI over a time horizon. The probabilistic VV is max-pooled to create a variable-timestep planner that reduces the search space and balances long-term and short-term planning. The proposed path planning method is compared to prior work with a Monte-Carlo simulation and is shown to outperform the baseline methods in cluttered environments when the UAV's sensor has a higher false alarm probability.


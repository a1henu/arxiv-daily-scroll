---
layout: default
title: TRAKNN: Efficient Trajectory Aware Spatiotemporal kNN for Rare Meteorological Trajectory Detection
---

# TRAKNN: Efficient Trajectory Aware Spatiotemporal kNN for Rare Meteorological Trajectory Detection
**arXiv**：[2603.02059v1](https://arxiv.org/abs/2603.02059) · [PDF](https://arxiv.org/pdf/2603.02059.pdf)  
**作者**：Guillaume Coulaud, Davide Faranda  

**一句话要点**：提出TRAKNN框架以高效检测气象轨迹中的罕见模式

**关键词**：时空数据挖掘, 轨迹检测, k近邻算法, 气象学应用, 高效计算

## 3 点简述
- 核心问题：传统方法难以高效处理多年代、大尺度时空数据中的轨迹相似性搜索
- 方法要点：基于递归算法解耦计算复杂度与轨迹长度，支持CPU/GPU批量操作
- 实验或效果：在75年欧洲海平面压力数据中验证，罕见轨迹与物理异常和极端事件数据库一致

## 摘要（原文）

> Extreme weather events, such as windstorms and heatwaves, are driven by persistent atmospheric circulation patterns that evolve over several consecutive days. While traditional circulation-based studies often focus on instantaneous atmospheric states, capturing the temporal evolution, or trajectory, of these spatial fields is essential for characterizing rare and potentially impactful atmospheric behavior. However, performing an exhaustive similarity search on multi-decadal, continental-scale gridded datasets presents significant computational and memory challenges. In this paper, we propose TRAKNN (TRajectory Aware KNN), a fully unsupervised and data-agnostic framework for detecting geometrically rare short trajectories in spatio-temporal data with an exact kNN approach. TRAKNN leverages a recurrence-based algorithm that decouples computational complexity from trajectory length and efficient batch operations, maximizing computational intensity. These optimizations enable exhaustive analysis on standard workstations, either on CPU or on GPU. We evaluate our approach on 75 years of daily European sea-level pressure data. Our results illustrate that rare trajectories identified by TRAKNN correspond to physically coherent atmospheric anomalies and align with independent extreme-event databases.


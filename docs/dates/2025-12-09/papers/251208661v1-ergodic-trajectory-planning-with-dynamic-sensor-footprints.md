---
layout: default
title: Ergodic Trajectory Planning with Dynamic Sensor Footprints
---

# Ergodic Trajectory Planning with Dynamic Sensor Footprints
**arXiv**：[2512.08661v1](https://arxiv.org/abs/2512.08661) · [PDF](https://arxiv.org/pdf/2512.08661.pdf)  
**作者**：Ziyue Zheng, Yongce Liu, Hesheng Wang, Zhongqiang Ren  

**一句话要点**：提出动态传感器足迹的遍历轨迹规划方法，以优化信息采集任务

**关键词**：遍历规划, 动态传感器足迹, 轨迹优化, 信息采集, 多无人机系统, 3D覆盖

## 3 点简述
- 核心问题：现有遍历规划假设传感器足迹固定，忽略动态变化如无人机相机视角随姿态和高度变化
- 方法要点：引入新度量考虑动态足迹，分析局部最优条件，开发数值轨迹优化算法
- 实验或效果：实验显示方法能同时优化轨迹和足迹，遍历性比传统方法提升一个数量级，并应用于多无人机3D物体覆盖

## 摘要（原文）

> This paper addresses the problem of trajectory planning for information gathering with a dynamic and resolution-varying sensor footprint. Ergodic planning offers a principled framework that balances exploration (visiting all areas) and exploitation (focusing on high-information regions) by planning trajectories such that the time spent in a region is proportional to the amount of information in that region. Existing ergodic planning often oversimplifies the sensing model by assuming a point sensor or a footprint with constant shape and resolution. In practice, the sensor footprint can drastically change over time as the robot moves, such as aerial robots equipped with downward-facing cameras, whose field of view depends on the orientation and altitude. To overcome this limitation, we propose a new metric that accounts for dynamic sensor footprints, analyze the theoretic local optimality conditions, and propose numerical trajectory optimization algorithms. Experimental results show that the proposed approach can simultaneously optimize both the trajectories and sensor footprints, with up to an order of magnitude better ergodicity than conventional methods. We also deploy our approach in a multi-drone system to ergodically cover an object in 3D space.


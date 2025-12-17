---
layout: default
title: Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments
---

# Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments
**arXiv**：[2512.14340v1](https://arxiv.org/abs/2512.14340) · [PDF](https://arxiv.org/pdf/2512.14340.pdf)  
**作者**：Aleksi Karhunen, Teemu Hakala, Väinö Karjalainen, Eija Honkavaara  

**一句话要点**：提出基于轻量激光雷达的无人机导航系统，在稠密北方森林环境中进行现场评估与优化。

**关键词**：无人机导航, 激光雷达, 森林环境, 自主飞行, SLAM算法, 路径规划

## 3 点简述
- 核心问题：无人机在森林冠层下自主导航困难，现有实验缺乏严谨性，如森林密度和飞行成功率报告不足。
- 方法要点：基于开源算法实现轻量激光雷达四旋翼无人机，使用IPC路径规划器和LTA-OM SLAM算法，并进行系统优化。
- 实验或效果：在93次飞行测试中，优化系统在1 m/s速度下中密度和稠密森林成功率分别为12/15和15/15，并提出了标准化测试框架。

## 摘要（原文）

> The interest in the usage of uncrewed aerial vehicles (UAVs) for forest applications has increased in recent years. While above-canopy flight has reached a high level of autonomy, navigating under-canopy remains a significant challenge. The use of autonomous UAVs could reduce the burden of data collection, which has motivated the development of numerous solutions for under-canopy autonomous flight. However, the experiments conducted in the literature and their reporting lack rigor. Very rarely, the density and the difficulty of the test forests are reported, or multiple flights are flown, and the success rate of those flights is reported. The aim of this study was to implement an autonomously flying quadrotor based on a lightweight lidar using openly available algorithms and test its behavior in real forest environments. A set of rigorous experiments was conducted with a quadrotor prototype utilizing the IPC path planner and LTA-OM SLAM algorithm. Based on the results of the first 33 flights, the original system was further enhanced. With the optimized system, 60 flights were performed, resulting in a total of 93 test flights. The optimized system performed significantly better in terms of reliability and flight mission completion times, achieving success rates of 12/15 in a medium-density forest and 15/15 in a dense forest, at a target flight velocity of 1 m/s. At a target flight velocity of 2 m/s, it had a success rate of 12/15 and 5/15, respectively. Furthermore, a standardized testing setup and evaluation criteria were proposed, enabling consistent performance comparisons of autonomous under-canopy UAV systems, enhancing reproducibility, guiding system improvements, and accelerating progress in forest robotics.


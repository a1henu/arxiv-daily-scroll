---
layout: default
title: ViSE: A Systematic Approach to Vision-Only Street-View Extrapolation
---

# ViSE: A Systematic Approach to Vision-Only Street-View Extrapolation
**arXiv**：[2510.18341v1](https://arxiv.org/abs/2510.18341) · [PDF](https://arxiv.org/pdf/2510.18341.pdf)  
**作者**：Kaiyuan Tan, Yingying Shen, Haiyang Sun, Bing Wang, Guang Chen, Hangjun Ye  

**一句话要点**：提出ViSE四阶段流程以解决自动驾驶街景外推中的失真问题

**关键词**：街景外推, 新视角合成, 几何先验, 伪LiDAR, 数据驱动适应, 自动驾驶仿真

## 3 点简述
- 核心问题：现有NVS方法在街景外推时易产生扭曲和不一致图像
- 方法要点：采用伪LiDAR初始化、2D-SDF几何先验、生成先验伪真值和数据驱动适应网络
- 实验或效果：在RealADSim-NVS基准上以0.441分排名第一

## 摘要（原文）

> Realistic view extrapolation is critical for closed-loop simulation in
> autonomous driving, yet it remains a significant challenge for current Novel
> View Synthesis (NVS) methods, which often produce distorted and inconsistent
> images beyond the original trajectory. This report presents our winning
> solution which ctook first place in the RealADSim Workshop NVS track at ICCV
> 2025. To address the core challenges of street view extrapolation, we introduce
> a comprehensive four-stage pipeline. First, we employ a data-driven
> initialization strategy to generate a robust pseudo-LiDAR point cloud, avoiding
> local minima. Second, we inject strong geometric priors by modeling the road
> surface with a novel dimension-reduced SDF termed 2D-SDF. Third, we leverage a
> generative prior to create pseudo ground truth for extrapolated viewpoints,
> providing auxilary supervision. Finally, a data-driven adaptation network
> removes time-specific artifacts. On the RealADSim-NVS benchmark, our method
> achieves a final score of 0.441, ranking first among all participants.


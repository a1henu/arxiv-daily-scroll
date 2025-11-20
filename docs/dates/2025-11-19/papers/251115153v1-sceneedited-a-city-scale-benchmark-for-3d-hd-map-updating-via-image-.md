---
layout: default
title: SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection
---

# SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection
**arXiv**：[2511.15153v1](https://arxiv.org/abs/2511.15153) · [PDF](https://arxiv.org/pdf/2511.15153.pdf)  
**作者**：Chun-Jung Lin, Tat-Jun Chin, Sourav Garg, Feras Dayoub  

**一句话要点**：提出SceneEdited数据集以解决城市规模3D高清地图通过图像引导变化检测更新的问题

**关键词**：3D高清地图更新, 图像引导变化检测, 城市规模数据集, 点云更新, 自动驾驶导航

## 3 点简述
- 核心问题：高清地图易过时，现有方法难以从2D变化检测更新3D地图
- 方法要点：提供城市规模数据集，包含合成变化、图像和LiDAR数据，支持3D点云更新
- 实验或效果：包含800+场景、73公里驾驶数据，提供基线方法和工具包用于评估

## 摘要（原文）

> Accurate, up-to-date High-Definition (HD) maps are critical for urban planning, infrastructure monitoring, and autonomous navigation. However, these maps quickly become outdated as environments evolve, creating a need for robust methods that not only detect changes but also incorporate them into updated 3D representations. While change detection techniques have advanced significantly, there remains a clear gap between detecting changes and actually updating 3D maps, particularly when relying on 2D image-based change detection. To address this gap, we introduce SceneEdited, the first city-scale dataset explicitly designed to support research on HD map maintenance through 3D point cloud updating. SceneEdited contains over 800 up-to-date scenes covering 73 km of driving and approximate 3 $\text{km}^2$ of urban area, with more than 23,000 synthesized object changes created both manually and automatically across 2000+ out-of-date versions, simulating realistic urban modifications such as missing roadside infrastructure, buildings, overpasses, and utility poles. Each scene includes calibrated RGB images, LiDAR scans, and detailed change masks for training and evaluation. We also provide baseline methods using a foundational image-based structure-from-motion pipeline for updating outdated scenes, as well as a comprehensive toolkit supporting scalability, trackability, and portability for future dataset expansion and unification of out-of-date object annotations. Both the dataset and the toolkit are publicly available at https://github.com/ChadLin9596/ScenePoint-ETK, establising a standardized benchmark for 3D map updating research.


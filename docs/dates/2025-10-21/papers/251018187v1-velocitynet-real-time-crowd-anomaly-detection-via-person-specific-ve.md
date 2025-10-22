---
layout: default
title: VelocityNet: Real-Time Crowd Anomaly Detection via Person-Specific Velocity Analysis
---

# VelocityNet: Real-Time Crowd Anomaly Detection via Person-Specific Velocity Analysis
**arXiv**：[2510.18187v1](https://arxiv.org/abs/2510.18187) · [PDF](https://arxiv.org/pdf/2510.18187.pdf)  
**作者**：Fatima AlGhamdi, Omar Alharbi, Abdullah Aldwyish, Raied Aljadaany, Muhammad Kamran J Khan, Huda Alamri  

**一句话要点**：提出VelocityNet以实时检测密集人群中的异常运动模式

**关键词**：人群异常检测, 实时检测, 个体速度分析, 光学流, 聚类分类, 异常评分

## 3 点简述
- 核心问题：密集场景中人际遮挡和动态运动模式导致异常检测困难
- 方法要点：结合头部检测和光流提取个体速度，聚类分类并基于百分位评分异常
- 实验或效果：在密集拥挤环境中有效实时检测多种异常运动模式

## 摘要（原文）

> Detecting anomalies in crowded scenes is challenging due to severe
> inter-person occlusions and highly dynamic, context-dependent motion patterns.
> Existing approaches often struggle to adapt to varying crowd densities and lack
> interpretable anomaly indicators. To address these limitations, we introduce
> VelocityNet, a dual-pipeline framework that combines head detection and dense
> optical flow to extract person-specific velocities. Hierarchical clustering
> categorizes these velocities into semantic motion classes (halt, slow, normal,
> and fast), and a percentile-based anomaly scoring system measures deviations
> from learned normal patterns. Experiments demonstrate the effectiveness of our
> framework in real-time detection of diverse anomalous motion patterns within
> densely crowded environments.


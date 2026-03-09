---
layout: default
title: CFEAR-Teach-and-Repeat: Fast and Accurate Radar-only Localization
---

# CFEAR-Teach-and-Repeat: Fast and Accurate Radar-only Localization
**arXiv**：[2603.06501v1](https://arxiv.org/abs/2603.06501) · [PDF](https://arxiv.org/pdf/2603.06501.pdf)  
**作者**：Maximilian Hilger, Daniel Adolfsson, Ralf Becker, Henrik Andreasson, Achim J. Lilienthal  

**一句话要点**：提出CFEAR-TR雷达定位方法，用于恶劣天气下的自主导航，实现高精度与鲁棒性。

**关键词**：雷达定位, 恶劣天气导航, 位姿图, 稀疏点云, 多传感器融合, 实时系统

## 3 点简述
- 核心问题：恶劣天气下光学传感器失效，需可靠雷达定位方法。
- 方法要点：联合对齐实时扫描与存储扫描及滑动窗口，使用稀疏定向表面点表示雷达数据。
- 实验或效果：在Boreas数据集上达到0.117米和0.096°精度，运行频率29Hz，提升63%。

## 摘要（原文）

> Reliable localization in prior maps is essential for autonomous navigation, particularly under adverse weather, where optical sensors may fail. We present CFEAR-TR, a teach-and-repeat localization pipeline using a single spinning radar, which is designed for easily deployable, lightweight, and robust navigation in adverse conditions. Our method localizes by jointly aligning live scans to both stored scans from the teach mapping pass, and to a sliding window of recent live keyframes. This ensures accurate and robust pose estimation across different seasons and weather phenomena. Radar scans are represented using a sparse set of oriented surface points, computed from Doppler-compensated measurements. The map is stored in a pose graph that is traversed during localization. Experiments on the held-out test sequences from the Boreas dataset show that CFEAR-TR can localize with an accuracy as low as 0.117 m and 0.096°, corresponding to improvements of up to 63% over the previous state of the art, while running efficiently at 29 Hz. These results substantially narrow the gap to lidar-level localization, particularly in heading estimation. We make the C++ implementation of our work available to the community.


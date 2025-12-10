---
layout: default
title: RAVES-Calib: Robust, Accurate and Versatile Extrinsic Self Calibration Using Optimal Geometric Features
---

# RAVES-Calib: Robust, Accurate and Versatile Extrinsic Self Calibration Using Optimal Geometric Features
**arXiv**：[2512.08170v1](https://arxiv.org/abs/2512.08170) · [PDF](https://arxiv.org/pdf/2512.08170.pdf)  
**作者**：Haoxin Zhang, Shuaixin Li, Xiaozhou Zhu, Hongbo Chen, Wen Yao  

**一句话要点**：提出RAVES-Calib方法，用于无目标环境下鲁棒、精确的LiDAR-相机外参自校准。

**关键词**：LiDAR-相机校准, 外参自校准, 特征对应, 自适应加权, 无目标环境, 多传感器兼容

## 3 点简述
- 核心问题：无需初始变换，在单对激光点与图像下实现多传感器兼容的外参校准。
- 方法要点：利用Gluestick建立2D-3D特征对应，基于特征分布自适应加权优化参数。
- 实验或效果：在室内外多传感器实验中，相比SOTA技术展现更优的鲁棒性和精度。

## 摘要（原文）

> In this paper, we present a user-friendly LiDAR-camera calibration toolkit that is compatible with various LiDAR and camera sensors and requires only a single pair of laser points and a camera image in targetless environments. Our approach eliminates the need for an initial transform and remains robust even with large positional and rotational LiDAR-camera extrinsic parameters. We employ the Gluestick pipeline to establish 2D-3D point and line feature correspondences for a robust and automatic initial guess. To enhance accuracy, we quantitatively analyze the impact of feature distribution on calibration results and adaptively weight the cost of each feature based on these metrics. As a result, extrinsic parameters are optimized by filtering out the adverse effects of inferior features. We validated our method through extensive experiments across various LiDAR-camera sensors in both indoor and outdoor settings. The results demonstrate that our method provides superior robustness and accuracy compared to SOTA techniques. Our code is open-sourced on GitHub to benefit the community.


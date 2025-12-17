---
layout: default
title: Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination
---

# Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination
**arXiv**：[2512.14200v1](https://arxiv.org/abs/2512.14200) · [PDF](https://arxiv.org/pdf/2512.14200.pdf)  
**作者**：Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  

**一句话要点**：提出SkyLume数据集以解决无人机多时相数据中光照不一致对城市三维重建的影响

**关键词**：无人机数据集, 光照鲁棒三维重建, 多时相采集, 反渲染, 城市场景建模, TCC指标

## 3 点简述
- 核心问题：无人机多时相采集导致光照不一致，引发颜色伪影和几何误差，缺乏相关数据集。
- 方法要点：收集10个城市区域超10万张高分辨率图像，每个区域在三个时段捕获，提供LiDAR扫描和三维真值。
- 实验或效果：引入TCC指标评估反渲染中光照与材质的解耦稳定性，支持几何和外观的精确评估。

## 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.


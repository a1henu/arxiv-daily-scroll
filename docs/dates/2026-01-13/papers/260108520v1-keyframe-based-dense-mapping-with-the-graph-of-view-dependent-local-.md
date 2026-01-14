---
layout: default
title: Keyframe-based Dense Mapping with the Graph of View-Dependent Local Maps
---

# Keyframe-based Dense Mapping with the Graph of View-Dependent Local Maps
**arXiv**：[2601.08520v1](https://arxiv.org/abs/2601.08520) · [PDF](https://arxiv.org/pdf/2601.08520.pdf)  
**作者**：Krzysztof Zielinski, Dominik Belter  

**一句话要点**：提出基于关键帧的密集建图系统，利用视图依赖局部地图优化RGB-D建图精度与全局一致性。

**关键词**：密集建图, 关键帧建图, NDT地图, 视图依赖表示, 位姿图优化, RGB-D传感器

## 3 点简述
- 核心问题：RGB-D建图中如何高效处理传感器不确定性并提升地图精度与全局一致性。
- 方法要点：使用视图依赖NDT局部地图，通过位姿图整合与闭环检测优化全局地图。
- 实验或效果：与Octomap和NDT-OM对比，展示建图性能提升及实际应用示例。

## 摘要（原文）

> In this article, we propose a new keyframe-based mapping system. The proposed method updates local Normal Distribution Transform maps (NDT) using data from an RGB-D sensor. The cells of the NDT are stored in 2D view-dependent structures to better utilize the properties and uncertainty model of RGB-D cameras. This method naturally represents an object closer to the camera origin with higher precision. The local maps are stored in the pose graph which allows correcting global map after loop closure detection. We also propose a procedure that allows merging and filtering local maps to obtain a global map of the environment. Finally, we compare our method with Octomap and NDT-OM and provide example applications of the proposed mapping method.


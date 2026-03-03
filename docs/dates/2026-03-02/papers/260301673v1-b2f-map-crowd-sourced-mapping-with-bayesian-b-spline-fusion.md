---
layout: default
title: B$^2$F-Map: Crowd-sourced Mapping with Bayesian B-spline Fusion
---

# B$^2$F-Map: Crowd-sourced Mapping with Bayesian B-spline Fusion
**arXiv**：[2603.01673v1](https://arxiv.org/abs/2603.01673) · [PDF](https://arxiv.org/pdf/2603.01673.pdf)  
**作者**：Yiping Xie, Yuxuan Xia, Erik Stenborg, Junsheng Fu, Axel Beauvisage, Gabriel E. Garcia, Tianyu Wu, Gustaf Hendeby  

**一句话要点**：提出B$^2$F-Map方法，通过贝叶斯B样条融合生成高精地图，解决众包建图中不确定性处理问题。

**关键词**：众包建图, 贝叶斯融合, B样条表示, 高精地图生成, 不确定性处理, 车载传感器

## 3 点简述
- 核心问题：现有众包建图方法依赖先验高精地图或忽略融合不确定性。
- 方法要点：使用单目相机、消费级GNSS和IMU，结合云端定位、车载映射和贝叶斯B样条融合。
- 实验或效果：在多样驾驶条件下的大规模真实数据集上验证，能生成几何一致的车道级地图。

## 摘要（原文）

> Crowd-sourced mapping offers a scalable alternative to creating maps using traditional survey vehicles. Yet, existing methods either rely on prior high-definition (HD) maps or neglect uncertainties in the map fusion. In this work, we present a complete pipeline for HD map generation using production vehicles equipped only with a monocular camera, consumer-grade GNSS, and IMU. Our approach includes on-cloud localization using lightweight standard-definition maps, on-vehicle mapping via an extended object trajectory (EOT) Poisson multi-Bernoulli (PMB) filter with Gibbs sampling, and on-cloud multi-drive optimization and Bayesian map fusion. We represent the lane lines using B-splines, where each B-spline is parameterized by a sequence of Gaussian distributed control points, and propose a novel Bayesian fusion framework for B-spline trajectories with differing density representation, enabling principled handling of uncertainties. We evaluate our proposed approach, B$^2$F-Map, on large-scale real-world datasets collected across diverse driving conditions and demonstrate that our method is able to produce geometrically consistent lane-level maps.


---
layout: default
title: IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes
---

# IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes
**arXiv**：[2511.19235v1](https://arxiv.org/abs/2511.19235) · [PDF](https://arxiv.org/pdf/2511.19235.pdf)  
**作者**：Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  

**一句话要点**：提出IDSplat以自监督重建动态驾驶场景，实现实例分解与运动轨迹学习

**关键词**：3D高斯泼溅, 实例分解, 自监督学习, 动态场景重建, 自动驾驶仿真, 运动轨迹优化

## 3 点简述
- 核心问题：动态驾驶场景重建中，静态与动态元素交织，依赖人工标注或缺乏实例分解
- 方法要点：使用零-shot语言跟踪与激光雷达锚定，建模动态对象为刚性变换实例
- 实验或效果：在Waymo数据集上实现竞争性重建质量，无需重训练泛化多序列

## 摘要（原文）

> Reconstructing dynamic driving scenes is essential for developing autonomous systems through sensor-realistic simulation. Although recent methods achieve high-fidelity reconstructions, they either rely on costly human annotations for object trajectories or use time-varying representations without explicit object-level decomposition, leading to intertwined static and dynamic elements that hinder scene separation. We present IDSplat, a self-supervised 3D Gaussian Splatting framework that reconstructs dynamic scenes with explicit instance decomposition and learnable motion trajectories, without requiring human annotations. Our key insight is to model dynamic objects as coherent instances undergoing rigid transformations, rather than unstructured time-varying primitives. For instance decomposition, we employ zero-shot, language-grounded video tracking anchored to 3D using lidar, and estimate consistent poses via feature correspondences. We introduce a coordinated-turn smoothing scheme to obtain temporally and physically consistent motion trajectories, mitigating pose misalignments and tracking failures, followed by joint optimization of object poses and Gaussian parameters. Experiments on the Waymo Open Dataset demonstrate that our method achieves competitive reconstruction quality while maintaining instance-level decomposition and generalizes across diverse sequences and view densities without retraining, making it practical for large-scale autonomous driving applications. Code will be released.


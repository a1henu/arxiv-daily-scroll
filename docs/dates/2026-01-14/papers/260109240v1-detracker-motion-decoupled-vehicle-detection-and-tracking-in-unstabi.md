---
layout: default
title: DeTracker: Motion-decoupled Vehicle Detection and Tracking in Unstabilized Satellite Videos
---

# DeTracker: Motion-decoupled Vehicle Detection and Tracking in Unstabilized Satellite Videos
**arXiv**：[2601.09240v1](https://arxiv.org/abs/2601.09240) · [PDF](https://arxiv.org/pdf/2601.09240.pdf)  
**作者**：Jiajun Chen, Jing Xiao, Shaohan Cao, Yuming Zhu, Liang Liao, Jun Pan, Mi Wang  

**一句话要点**：提出DeTracker框架，通过运动解耦和时序特征融合解决非稳定卫星视频中的车辆检测与跟踪问题。

**关键词**：卫星视频分析, 多目标跟踪, 运动解耦, 时序特征融合, 微小物体检测, 非稳定视频处理

## 3 点简述
- 核心问题：非稳定卫星视频中平台抖动和微小物体弱外观导致多目标跟踪性能下降。
- 方法要点：引入全局-局部运动解耦模块分离平台与物体运动，开发时序依赖特征金字塔增强特征连续性。
- 实验或效果：在模拟和真实数据集上显著优于现有方法，MOTA分别达61.1%和47.3%。

## 摘要（原文）

> Satellite videos provide continuous observations of surface dynamics but pose significant challenges for multi-object tracking (MOT), especially under unstabilized conditions where platform jitter and the weak appearance of tiny objects jointly degrade tracking performance. To address this problem, we propose DeTracker, a joint detection-and-tracking framework tailored for unstabilized satellite videos. DeTracker introduces a Global--Local Motion Decoupling (GLMD) module that explicitly separates satellite platform motion from true object motion through global alignment and local refinement, leading to improved trajectory stability and motion estimation accuracy. In addition, a Temporal Dependency Feature Pyramid (TDFP) module is developed to perform cross-frame temporal feature fusion, enhancing the continuity and discriminability of tiny-object representations. We further construct a new benchmark dataset, SDM-Car-SU, which simulates multi-directional and multi-speed platform motions to enable systematic evaluation of tracking robustness under varying motion perturbations. Extensive experiments on both simulated and real unstabilized satellite videos demonstrate that DeTracker significantly outperforms existing methods, achieving 61.1% MOTA on SDM-Car-SU and 47.3% MOTA on real satellite video data.


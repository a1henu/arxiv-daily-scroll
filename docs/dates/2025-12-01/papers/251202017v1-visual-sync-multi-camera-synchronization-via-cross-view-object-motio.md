---
layout: default
title: Visual Sync: Multi-Camera Synchronization via Cross-View Object Motion
---

# Visual Sync: Multi-Camera Synchronization via Cross-View Object Motion
**arXiv**：[2512.02017v1](https://arxiv.org/abs/2512.02017) · [PDF](https://arxiv.org/pdf/2512.02017.pdf)  
**作者**：Shaowei Liu, David Yifan Yao, Saurabh Gupta, Shenlong Wang  

**一句话要点**：提出VisualSync框架，通过多视角动态优化对齐未标定、未同步的多相机视频流

**关键词**：多相机同步, 视频对齐, 极线约束, 3D重建, 时间偏移估计

## 3 点简述
- 核心问题：多消费相机视频流同步困难，现有方法依赖控制设置、特定目标或昂贵硬件
- 方法要点：利用3D重建、特征匹配和密集跟踪提取轨迹，基于极线约束联合最小化误差估计时间偏移
- 实验或效果：在四个数据集上优于基线方法，中位同步误差低于50毫秒

## 摘要（原文）

> Today, people can easily record memorable moments, ranging from concerts, sports events, lectures, family gatherings, and birthday parties with multiple consumer cameras. However, synchronizing these cross-camera streams remains challenging. Existing methods assume controlled settings, specific targets, manual correction, or costly hardware. We present VisualSync, an optimization framework based on multi-view dynamics that aligns unposed, unsynchronized videos at millisecond accuracy. Our key insight is that any moving 3D point, when co-visible in two cameras, obeys epipolar constraints once properly synchronized. To exploit this, VisualSync leverages off-the-shelf 3D reconstruction, feature matching, and dense tracking to extract tracklets, relative poses, and cross-view correspondences. It then jointly minimizes the epipolar error to estimate each camera's time offset. Experiments on four diverse, challenging datasets show that VisualSync outperforms baseline methods, achieving an median synchronization error below 50 ms.


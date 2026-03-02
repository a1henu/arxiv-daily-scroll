---
layout: default
title: FocusTrack: One-Stage Focus-and-Suppress Framework for 3D Point Cloud Object Tracking
---

# FocusTrack: One-Stage Focus-and-Suppress Framework for 3D Point Cloud Object Tracking
**arXiv**：[2602.24133v1](https://arxiv.org/abs/2602.24133) · [PDF](https://arxiv.org/pdf/2602.24133.pdf)  
**作者**：Sifan Zhou, Jiahao Nie, Ziyu Zhao, Yichao Cao, Xiaobo Lu  

**一句话要点**：提出FocusTrack以解决3D点云目标跟踪中两阶段运动方法的误差累积与计算瓶颈问题。

**关键词**：3D点云目标跟踪, 运动建模, 注意力机制, 一阶段框架, 实时跟踪

## 3 点简述
- 核心问题：现有两阶段运动方法存在误差累积和计算瓶颈，源于解耦优化和顺序处理。
- 方法要点：通过帧间运动建模和聚焦-抑制注意力，实现运动-语义协同建模的一阶段框架。
- 实验或效果：在KITTI、nuScenes和Waymo基准上达到SOTA性能，运行速度达105 FPS。

## 摘要（原文）

> In 3D point cloud object tracking, the motion-centric methods have emerged as a promising avenue due to its superior performance in modeling inter-frame motion. However, existing two-stage motion-based approaches suffer from fundamental limitations: (1) error accumulation due to decoupled optimization caused by explicit foreground segmentation prior to motion estimation, and (2) computational bottlenecks from sequential processing. To address these challenges, we propose FocusTrack, a novel one-stage paradigms tracking framework that unifies motion-semantics co-modeling through two core innovations: Inter-frame Motion Modeling (IMM) and Focus-and-Suppress Attention. The IMM module employs a temp-oral-difference siamese encoder to capture global motion patterns between adjacent frames. The Focus-and-Suppress attention that enhance the foreground semantics via motion-salient feature gating and suppress the background noise based on the temporal-aware motion context from IMM without explicit segmentation. Based on above two designs, FocusTrack enables end-to-end training with compact one-stage pipeline. Extensive experiments on prominent 3D tracking benchmarks, such as KITTI, nuScenes, and Waymo, demonstrate that the FocusTrack achieves new SOTA performance while running at a high speed with 105 FPS.


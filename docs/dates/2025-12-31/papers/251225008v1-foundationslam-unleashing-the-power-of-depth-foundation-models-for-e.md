---
layout: default
title: FoundationSLAM: Unleashing the Power of Depth Foundation Models for End-to-End Dense Visual SLAM
---

# FoundationSLAM: Unleashing the Power of Depth Foundation Models for End-to-End Dense Visual SLAM
**arXiv**：[2512.25008v1](https://arxiv.org/abs/2512.25008) · [PDF](https://arxiv.org/pdf/2512.25008.pdf)  
**作者**：Yuchen Wu, Jiahe Li, Fabio Tosi, Matteo Poggi, Jin Zheng, Xiao Bai  

**一句话要点**：提出FoundationSLAM，利用深度基础模型增强单目稠密SLAM的几何一致性

**关键词**：单目稠密SLAM, 深度基础模型, 几何一致性, 混合光流网络, 束调整, 实时系统

## 3 点简述
- 核心问题：基于光流的方法缺乏几何一致性，影响SLAM的跟踪与建图精度
- 方法要点：结合深度基础模型指导，设计混合光流网络和双向一致束调整层
- 实验或效果：在多个数据集上实现高精度轨迹和稠密重建，实时运行18 FPS

## 摘要（原文）

> We present FoundationSLAM, a learning-based monocular dense SLAM system that addresses the absence of geometric consistency in previous flow-based approaches for accurate and robust tracking and mapping. Our core idea is to bridge flow estimation with geometric reasoning by leveraging the guidance from foundation depth models. To this end, we first develop a Hybrid Flow Network that produces geometry-aware correspondences, enabling consistent depth and pose inference across diverse keyframes. To enforce global consistency, we propose a Bi-Consistent Bundle Adjustment Layer that jointly optimizes keyframe pose and depth under multi-view constraints. Furthermore, we introduce a Reliability-Aware Refinement mechanism that dynamically adapts the flow update process by distinguishing between reliable and uncertain regions, forming a closed feedback loop between matching and optimization. Extensive experiments demonstrate that FoundationSLAM achieves superior trajectory accuracy and dense reconstruction quality across multiple challenging datasets, while running in real-time at 18 FPS, demonstrating strong generalization to various scenarios and practical applicability of our method.


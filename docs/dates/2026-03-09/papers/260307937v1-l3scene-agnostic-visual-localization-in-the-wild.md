---
layout: default
title: $L^3$:Scene-agnostic Visual Localization in the Wild
---

# $L^3$:Scene-agnostic Visual Localization in the Wild
**arXiv**：[2603.07937v1](https://arxiv.org/abs/2603.07937) · [PDF](https://arxiv.org/pdf/2603.07937.pdf)  
**作者**：Yu Zhang, Muhua Zhu, Yifei Xue, Tie Ji, Yizhen Lao  

**一句话要点**：提出L^3框架，实现无需离线预处理的场景无关视觉定位

**关键词**：视觉定位, 在线3D重建, 场景无关, 度量尺度恢复, 位姿细化, 稀疏场景鲁棒性

## 3 点简述
- 核心问题：标准视觉定位方法依赖离线场景预处理，增加计算、时间和存储开销
- 方法要点：利用前馈3D重建网络在线推理，通过两阶段度量尺度恢复和位姿细化实现定位
- 实验或效果：在多个基准测试中性能媲美先进方法，在稀疏场景中表现出显著鲁棒性

## 摘要（原文）

> Standard visual localization methods typically require offline pre-processing of scenes to obtain 3D structural information for better performance. This inevitably introduces additional computational and time costs, as well as the overhead of storing scene representations. Can we visually localize in a wild scene without any off-line preprocessing step? In this paper, we leverage the online inference capabilities of feed-forward 3D reconstruction networks to propose a novel map-free visual localization framework $L^3$. Specifically, by performing direct online 3D reconstruction on RGB images, followed by two-stage metric scale recovery and pose refinement based on 2D-3D correspondences, $L^3$ achieves high accuracy without the need to pre-build or store any offline scene representations. Extensive experiments demonstrate $L^3$ not only that the performance is comparable to state-of-the-art solutions on various benchmarks, but also that it exhibits significantly superior robustness in sparse scenes (fewer reference images per scene).


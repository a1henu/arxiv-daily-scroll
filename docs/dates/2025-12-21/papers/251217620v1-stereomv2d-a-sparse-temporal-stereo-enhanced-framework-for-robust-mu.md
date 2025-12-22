---
layout: default
title: StereoMV2D: A Sparse Temporal Stereo-Enhanced Framework for Robust Multi-View 3D Object Detection
---

# StereoMV2D: A Sparse Temporal Stereo-Enhanced Framework for Robust Multi-View 3D Object Detection
**arXiv**：[2512.17620v1](https://arxiv.org/abs/2512.17620) · [PDF](https://arxiv.org/pdf/2512.17620.pdf)  
**作者**：Di Wu, Feng Yang, Wenhui Zhao, Jinwen Yu, Pan Liao, Benlian Xu, Dingwen Zhang  

**一句话要点**：提出StereoMV2D框架，通过时域立体建模增强多视图3D目标检测的深度感知

**关键词**：多视图3D目标检测, 时域立体建模, 稀疏查询检测, 自动驾驶感知, 深度估计优化

## 3 点简述
- 核心问题：单帧2D检测的深度模糊性限制多视图3D检测精度
- 方法要点：利用相邻帧的跨时域视差，在2D RoI内高效优化查询先验
- 实验或效果：在nuScenes和Argoverse 2数据集上实现高性能，计算开销低

## 摘要（原文）

> Multi-view 3D object detection is a fundamental task in autonomous driving perception, where achieving a balance between detection accuracy and computational efficiency remains crucial. Sparse query-based 3D detectors efficiently aggregate object-relevant features from multi-view images through a set of learnable queries, offering a concise and end-to-end detection paradigm. Building on this foundation, MV2D leverages 2D detection results to provide high-quality object priors for query initialization, enabling higher precision and recall. However, the inherent depth ambiguity in single-frame 2D detections still limits the accuracy of 3D query generation. To address this issue, we propose StereoMV2D, a unified framework that integrates temporal stereo modeling into the 2D detection-guided multi-view 3D detector. By exploiting cross-temporal disparities of the same object across adjacent frames, StereoMV2D enhances depth perception and refines the query priors, while performing all computations efficiently within 2D regions of interest (RoIs). Furthermore, a dynamic confidence gating mechanism adaptively evaluates the reliability of temporal stereo cues through learning statistical patterns derived from the inter-frame matching matrix together with appearance consistency, ensuring robust detection under object appearance and occlusion. Extensive experiments on the nuScenes and Argoverse 2 datasets demonstrate that StereoMV2D achieves superior detection performance without incurring significant computational overhead. Code will be available at https://github.com/Uddd821/StereoMV2D.


---
layout: default
title: AIM-SLAM: Dense Monocular SLAM via Adaptive and Informative Multi-View Keyframe Prioritization with Foundation Model
---

# AIM-SLAM: Dense Monocular SLAM via Adaptive and Informative Multi-View Keyframe Prioritization with Foundation Model
**arXiv**：[2603.05097v1](https://arxiv.org/abs/2603.05097) · [PDF](https://arxiv.org/pdf/2603.05097.pdf)  
**作者**：Jinwoo Jeon, Dong-Uk Seo, Eungchang Mason Lee, Hyun Myung  

**一句话要点**：提出AIM-SLAM框架，通过自适应多视图关键帧优先化解决单目SLAM中的密集重建问题。

**关键词**：单目SLAM, 密集重建, 多视图优化, 关键帧选择, 几何基础模型, ROS集成

## 3 点简述
- 核心问题：现有方法局限于双视图或固定输入，缺乏几何上下文考虑，影响密集重建效果。
- 方法要点：引入SIGMA模块，基于体素重叠和信息增益自适应选择关键帧，并联合多视图Sim(3)优化提升姿态估计精度。
- 实验或效果：在真实数据集上实现姿态估计和密集重建的先进性能，支持ROS集成。

## 摘要（原文）

> Recent advances in geometric foundation models have emerged as a promising alternative for addressing the challenge of dense reconstruction in monocular visual simultaneous localization and mapping (SLAM). Although geometric foundation models enable SLAM to leverage variable input views, the previous methods remain confined to two-view pairs or fixed-length inputs without sufficient deliberation of geometric context for view selection. To tackle this problem, we propose AIM-SLAM, a dense monocular SLAM framework that exploits an adaptive and informative multi-view keyframe prioritization with dense pointmap predictions from visual geometry grounded transformer (VGGT). Specifically, we introduce the selective information- and geometric-aware multi-view adaptation (SIGMA) module, which employs voxel overlap and information gain to retrieve a candidate set of keyframes and adaptively determine its size. Furthermore, we formulate a joint multi-view Sim(3) optimization that enforces consistent alignment across selected views, substantially improving pose estimation accuracy. The effectiveness of AIM-SLAM is demonstrated on real-world datasets, where it achieves state-of-the-art performance in both pose estimation and dense reconstruction. Our system supports ROS integration, with code is available at https://aimslam.github.io/.


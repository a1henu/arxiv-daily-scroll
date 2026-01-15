---
layout: default
title: SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings
---

# SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings
**arXiv**：[2601.09665v1](https://arxiv.org/abs/2601.09665) · [PDF](https://arxiv.org/pdf/2601.09665.pdf)  
**作者**：Yuchen Wu, Jiahe Li, Xiaohan Yu, Lina Yu, Jin Zheng, Xiao Bai  

**一句话要点**：提出SCE-SLAM，通过场景坐标嵌入解决单目SLAM中的尺度漂移问题。

**关键词**：单目SLAM, 尺度漂移, 场景坐标嵌入, 几何引导聚合, 束调整, 实时性能

## 3 点简述
- 核心问题：单目视觉SLAM在长序列中因缺乏全局约束而累积尺度漂移。
- 方法要点：使用场景坐标嵌入编码规范尺度下的3D几何关系，结合几何引导聚合和场景坐标束调整。
- 实验效果：在KITTI等数据集上显著降低轨迹误差，保持实时性能并实现尺度一致性。

## 摘要（原文）

> Monocular visual SLAM enables 3D reconstruction from internet video and autonomous navigation on resource-constrained platforms, yet suffers from scale drift, i.e., the gradual divergence of estimated scale over long sequences. Existing frame-to-frame methods achieve real-time performance through local optimization but accumulate scale drift due to the lack of global constraints among independent windows. To address this, we propose SCE-SLAM, an end-to-end SLAM system that maintains scale consistency through scene coordinate embeddings, which are learned patch-level representations encoding 3D geometric relationships under a canonical scale reference. The framework consists of two key modules: geometry-guided aggregation that leverages 3D spatial proximity to propagate scale information from historical observations through geometry-modulated attention, and scene coordinate bundle adjustment that anchors current estimates to the reference scale through explicit 3D coordinate constraints decoded from the scene coordinate embeddings. Experiments on KITTI, Waymo, and vKITTI demonstrate substantial improvements: our method reduces absolute trajectory error by 8.36m on KITTI compared to the best prior approach, while maintaining 36 FPS and achieving scale consistency across large-scale scenes.


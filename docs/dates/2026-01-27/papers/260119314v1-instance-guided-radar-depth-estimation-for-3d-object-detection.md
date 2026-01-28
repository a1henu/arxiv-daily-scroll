---
layout: default
title: Instance-Guided Radar Depth Estimation for 3D Object Detection
---

# Instance-Guided Radar Depth Estimation for 3D Object Detection
**arXiv**：[2601.19314v1](https://arxiv.org/abs/2601.19314) · [PDF](https://arxiv.org/pdf/2601.19314.pdf)  
**作者**：Chen-Chou Lo, Patrick Vandewalle  

**一句话要点**：提出InstaRadar与RCDPT集成框架，通过实例引导增强雷达深度估计以改进自动驾驶3D检测。

**关键词**：雷达深度估计, 3D物体检测, 实例分割引导, 雷达相机融合, 自动驾驶感知

## 3 点简述
- 核心问题：雷达稀疏性限制其在3D检测中的直接应用，需有效融合雷达与相机数据。
- 方法要点：InstaRadar利用实例分割增强雷达密度与语义对齐，RCDPT集成到BEVDepth框架替换深度模块。
- 实验或效果：InstaRadar在雷达引导深度估计中达到先进水平，集成后提升3D检测性能，但落后于直接BEV特征提取模型。

## 摘要（原文）

> Accurate depth estimation is fundamental to 3D perception in autonomous driving, supporting tasks such as detection, tracking, and motion planning. However, monocular camera-based 3D detection suffers from depth ambiguity and reduced robustness under challenging conditions. Radar provides complementary advantages such as resilience to poor lighting and adverse weather, but its sparsity and low resolution limit its direct use in detection frameworks. This motivates the need for effective Radar-camera fusion with improved preprocessing and depth estimation strategies. We propose an end-to-end framework that enhances monocular 3D object detection through two key components. First, we introduce InstaRadar, an instance segmentation-guided expansion method that leverages pre-trained segmentation masks to enhance Radar density and semantic alignment, producing a more structured representation. InstaRadar achieves state-of-the-art results in Radar-guided depth estimation, showing its effectiveness in generating high-quality depth features. Second, we integrate the pre-trained RCDPT into the BEVDepth framework as a replacement for its depth module. With InstaRadar-enhanced inputs, the RCDPT integration consistently improves 3D detection performance. Overall, these components yield steady gains over the baseline BEVDepth model, demonstrating the effectiveness of InstaRadar and the advantage of explicit depth supervision in 3D object detection. Although the framework lags behind Radar-camera fusion models that directly extract BEV features, since Radar serves only as guidance rather than an independent feature stream, this limitation highlights potential for improvement. Future work will extend InstaRadar to point cloud-like representations and integrate a dedicated Radar branch with temporal cues for enhanced BEV fusion.


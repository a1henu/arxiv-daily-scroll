---
layout: default
title: Systematic Evaluation of Depth Backbones and Semantic Cues for Monocular Pseudo-LiDAR 3D Detection
---

# Systematic Evaluation of Depth Backbones and Semantic Cues for Monocular Pseudo-LiDAR 3D Detection
**arXiv**：[2601.03617v1](https://arxiv.org/abs/2601.03617) · [PDF](https://arxiv.org/pdf/2601.03617.pdf)  
**作者**：Samson Oseiwe Ajadalu  

**一句话要点**：系统评估深度骨干网络与语义线索对单目伪激光雷达3D检测的影响

**关键词**：单目3D检测, 伪激光雷达, 深度估计, 点云增强, KITTI数据集, 几何保真度

## 3 点简述
- 核心问题：单目3D检测因深度估计困难而精度不足，需评估深度骨干和特征工程的作用。
- 方法要点：在KITTI验证集上，比较NeWCRFs与Depth Anything V2 Metric-Outdoor，并测试点云增强使用外观和语义线索。
- 实验或效果：NeWCRFs在3D检测中表现更优，语义线索仅带来边际增益，深度骨干和几何保真度主导性能。

## 摘要（原文）

> Monocular 3D object detection offers a low-cost alternative to LiDAR, yet remains less accurate due to the difficulty of estimating metric depth from a single image. We systematically evaluate how depth backbones and feature engineering affect a monocular Pseudo-LiDAR pipeline on the KITTI validation split. Specifically, we compare NeWCRFs (supervised metric depth) against Depth Anything V2 Metric-Outdoor (Base) under an identical pseudo-LiDAR generation and PointRCNN detection protocol. NeWCRFs yields stronger downstream 3D detection, achieving 10.50\% AP$_{3D}$ at IoU$=0.7$ on the Moderate split using grayscale intensity (Exp~2). We further test point-cloud augmentations using appearance cues (grayscale intensity) and semantic cues (instance segmentation confidence). Contrary to the expectation that semantics would substantially close the gap, these features provide only marginal gains, and mask-based sampling can degrade performance by removing contextual geometry. Finally, we report a depth-accuracy-versus-distance diagnostic using ground-truth 2D boxes (including Ped/Cyc), highlighting that coarse depth correctness does not fully predict strict 3D IoU. Overall, under an off-the-shelf LiDAR detector, depth-backbone choice and geometric fidelity dominate performance, outweighing secondary feature injection.


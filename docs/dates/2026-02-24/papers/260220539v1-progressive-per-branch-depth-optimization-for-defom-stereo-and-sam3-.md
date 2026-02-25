---
layout: default
title: Progressive Per-Branch Depth Optimization for DEFOM-Stereo and SAM3 Joint Analysis in UAV Forestry Applications
---

# Progressive Per-Branch Depth Optimization for DEFOM-Stereo and SAM3 Joint Analysis in UAV Forestry Applications
**arXiv**：[2602.20539v1](https://arxiv.org/abs/2602.20539) · [PDF](https://arxiv.org/pdf/2602.20539.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：提出渐进式深度优化流程，结合DEFOM-Stereo和SAM3，提升无人机林业中树枝3D重建精度。

**关键词**：无人机林业, 树枝3D重建, 渐进式深度优化, 立体匹配, 实例分割, 点云处理

## 3 点简述
- 核心问题：立体匹配的密集视差图在复杂树冠中噪声大，难以用于树枝级分析。
- 方法要点：通过形态学侵蚀、颜色验证和多阶段滤波，逐步优化深度噪声和分割误差。
- 实验或效果：在松树图像上测试，树枝深度标准差降低82%，保持边缘保真度。

## 摘要（原文）

> Accurate per-branch 3D reconstruction is a prerequisite for autonomous UAV-based tree pruning; however, dense disparity maps from modern stereo matchers often remain too noisy for individual branch analysis in complex forest canopies. This paper introduces a progressive pipeline integrating DEFOM-Stereo foundation-model disparity estimation, SAM3 instance segmentation, and multi-stage depth optimization to deliver robust per-branch point clouds. Starting from a naive baseline, we systematically identify and resolve three error families through successive refinements. Mask boundary contamination is first addressed through morphological erosion and subsequently refined via a skeleton-preserving variant to safeguard thin-branch topology. Segmentation inaccuracy is then mitigated using LAB-space Mahalanobis color validation coupled with cross-branch overlap arbitration. Finally, depth noise - the most persistent error source - is initially reduced by outlier removal and median filtering, before being superseded by a robust five-stage scheme comprising MAD global detection, spatial density consensus, local MAD filtering, RGB-guided filtering, and adaptive bilateral filtering. Evaluated on 1920x1080 stereo imagery of Radiata pine (Pinus radiata) acquired with a ZED Mini camera (63 mm baseline) from a UAV in Canterbury, New Zealand, the proposed pipeline reduces the average per-branch depth standard deviation by 82% while retaining edge fidelity. The result is geometrically coherent 3D point clouds suitable for autonomous pruning tool positioning. All code and processed data are publicly released to facilitate further UAV forestry research.


---
layout: default
title: Accurate Planar Tracking With Robust Re-Detection
---

# Accurate Planar Tracking With Robust Re-Detection
**arXiv**：[2602.19624v1](https://arxiv.org/abs/2602.19624) · [PDF](https://arxiv.org/pdf/2602.19624.pdf)  
**作者**：Jonas Serych, Jiri Matas  

**一句话要点**：提出SAM-H和WOFTSAM平面跟踪器，结合分割与位姿估计以提升鲁棒性。

**关键词**：平面跟踪, 单应性估计, 分割跟踪, 目标重检测, 基准评估

## 3 点简述
- 核心问题：平面跟踪中目标外观变化和丢失重检测的挑战。
- 方法要点：SAM-H利用分割轮廓估计单应性，WOFTSAM集成SAM-H改进WOFT的重检测能力。
- 实验或效果：在POT-210和PlanarTrack基准上实现最优性能，并改进PlanarTrack标注。

## 摘要（原文）

> We present SAM-H and WOFTSAM, novel planar trackers that combine robust long-term segmentation tracking provided by SAM 2 with 8 degrees-of-freedom homography pose estimation. SAM-H estimates homographies from segmentation mask contours and is thus highly robust to target appearance changes. WOFTSAM significantly improves the current state-of-the-art planar tracker WOFT by exploiting lost target re-detection provided by SAM-H. The proposed methods are evaluated on POT-210 and PlanarTrack tracking benchmarks, setting the new state-of-the-art performance on both. On the latter, they outperform the second best by a large margin, +12.4 and +15.2pp on the p@15 metric. We also present improved ground-truth annotations of initial PlanarTrack poses, enabling more accurate benchmarking in the high-precision p@5 metric. The code and the re-annotations are available at https://github.com/serycjon/WOFTSAM


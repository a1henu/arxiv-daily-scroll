---
layout: default
title: CoWTracker: Tracking by Warping instead of Correlation
---

# CoWTracker: Tracking by Warping instead of Correlation
**arXiv**：[2602.04877v1](https://arxiv.org/abs/2602.04877) · [PDF](https://arxiv.org/pdf/2602.04877.pdf)  
**作者**：Zihang Lai, Eldar Insafutdinov, Edgar Sucar, Andrea Vedaldi  

**一句话要点**：提出CoWTracker，通过特征扭曲而非相关性计算实现密集点跟踪，提升效率与性能。

**关键词**：密集点跟踪, 特征扭曲, Transformer, 光流估计, 视频分析

## 3 点简述
- 密集点跟踪依赖成本体积导致二次复杂度，限制可扩展性和效率。
- 采用基于光流的特征扭曲迭代优化跟踪估计，结合Transformer进行时空推理。
- 在TAP-Vid和Robo-TAP等基准上达到SOTA，并在光流任务中表现优异。

## 摘要（原文）

> Dense point tracking is a fundamental problem in computer vision, with applications ranging from video analysis to robotic manipulation. State-of-the-art trackers typically rely on cost volumes to match features across frames, but this approach incurs quadratic complexity in spatial resolution, limiting scalability and efficiency. In this paper, we propose \method, a novel dense point tracker that eschews cost volumes in favor of warping. Inspired by recent advances in optical flow, our approach iteratively refines track estimates by warping features from the target frame to the query frame based on the current estimate. Combined with a transformer architecture that performs joint spatiotemporal reasoning across all tracks, our design establishes long-range correspondences without computing feature correlations. Our model is simple and achieves state-of-the-art performance on standard dense point tracking benchmarks, including TAP-Vid-DAVIS, TAP-Vid-Kinetics, and Robo-TAP. Remarkably, the model also excels at optical flow, sometimes outperforming specialized methods on the Sintel, KITTI, and Spring benchmarks. These results suggest that warping-based architectures can unify dense point tracking and optical flow estimation.


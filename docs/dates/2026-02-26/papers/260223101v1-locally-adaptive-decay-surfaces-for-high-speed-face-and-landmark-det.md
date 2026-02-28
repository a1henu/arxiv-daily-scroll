---
layout: default
title: Locally Adaptive Decay Surfaces for High-Speed Face and Landmark Detection with Event Cameras
---

# Locally Adaptive Decay Surfaces for High-Speed Face and Landmark Detection with Event Cameras
**arXiv**：[2602.23101v1](https://arxiv.org/abs/2602.23101) · [PDF](https://arxiv.org/pdf/2602.23101.pdf)  
**作者**：Paul Kielty, Timothy Hanley, Peter Corcoran  

**一句话要点**：提出局部自适应衰减表面以解决事件相机中时空表示在高速人脸检测中的权衡问题

**关键词**：事件相机, 自适应表示, 人脸检测, 时空处理, 实时系统, 神经形态视觉

## 3 点简述
- 事件相机输出稀疏异步，传统全局衰减表示在静止与运动区域间存在时空结构保留与边缘锐度权衡
- 引入局部自适应衰减表面，基于事件率、拉普拉斯-高斯响应和高频谱能量调制各位置时间衰减
- 在公开数据集上，LADS在30Hz和240Hz下提升人脸检测和关键点精度，支持轻量网络并保持实时性能

## 摘要（原文）

> Event cameras record luminance changes with microsecond resolution, but converting their sparse, asynchronous output into dense tensors that neural networks can exploit remains a core challenge. Conventional histograms or globally-decayed time-surface representations apply fixed temporal parameters across the entire image plane, which in practice creates a trade-off between preserving spatial structure during still periods and retaining sharp edges during rapid motion. We introduce Locally Adaptive Decay Surfaces (LADS), a family of event representations in which the temporal decay at each location is modulated according to local signal dynamics. Three strategies are explored, based on event rate, Laplacian-of-Gaussian response, and high-frequency spectral energy. These adaptive schemes preserve detail in quiescent regions while reducing blur in regions of dense activity. Extensive experiments on the public data show that LADS consistently improves both face detection and facial landmark accuracy compared to standard non-adaptive representations. At 30 Hz, LADS achieves higher detection accuracy and lower landmark error than either baseline, and at 240 Hz it mitigates the accuracy decline typically observed at higher frequencies, sustaining 2.44 % normalized mean error for landmarks and 0.966 mAP50 in face detection. These high-frequency results even surpass the accuracy reported in prior works operating at 30 Hz, setting new benchmarks for event-based face analysis. Moreover, by preserving spatial structure at the representation stage, LADS supports the use of much lighter network architectures while still retaining real-time performance. These results highlight the importance of context-aware temporal integration for neuromorphic vision and point toward real-time, high-frequency human-computer interaction systems that exploit the unique advantages of event cameras.


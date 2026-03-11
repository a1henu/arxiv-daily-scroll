---
layout: default
title: RiO-DETR: DETR for Real-time Oriented Object Detection
---

# RiO-DETR: DETR for Real-time Oriented Object Detection
**arXiv**：[2603.09411v1](https://arxiv.org/abs/2603.09411) · [PDF](https://arxiv.org/pdf/2603.09411.pdf)  
**作者**：Zhangchi Hu, Yifan Zhao, Yansong Peng, Wenzhang Sun, Xiangchen Yin, Jie Chen, Peixi Wu, Hebei Li, Xinghao Wang, Dongsheng Jiang, Xiaoyan Sun  

**一句话要点**：提出RiO-DETR，首个实时定向目标检测的DETR模型，解决语义依赖、角度周期性和收敛慢问题。

**关键词**：定向目标检测, 实时检测, DETR模型, 角度估计, 收敛加速, Transformer

## 3 点简述
- 核心问题：DETR适配定向框时面临语义依赖、角度周期性和搜索空间扩大导致收敛慢的挑战。
- 方法要点：通过内容驱动角度估计、解耦周期细化和定向密集监督，提升角度估计稳定性和收敛速度。
- 实验或效果：在DOTA-1.0等数据集上实现实时检测，建立了新的速度-精度权衡。

## 摘要（原文）

> We present RiO-DETR: DETR for Real-time Oriented Object Detection, the first real-time oriented detection transformer to the best of our knowledge. Adapting DETR to oriented bounding boxes (OBBs) poses three challenges: semantics-dependent orientation, angle periodicity that breaks standard Euclidean refinement, and an enlarged search space that slows convergence. RiO-DETR resolves these issues with task-native designs while preserving real-time efficiency. First, we propose Content-Driven Angle Estimation by decoupling angle from positional queries, together with Rotation-Rectified Orthogonal Attention to capture complementary cues for reliable orientation. Second, Decoupled Periodic Refinement combines bounded coarse-to-fine updates with a Shortest-Path Periodic Loss for stable learning across angular seams. Third, Oriented Dense O2O injects angular diversity into dense supervision to speed up angle convergence at no extra cost. Extensive experiments on DOTA-1.0, DIOR-R, and FAIR-1M-2.0 demonstrate RiO-DETR establishes a new speed--accuracy trade-off for real-time oriented detection. Code will be made publicly available.


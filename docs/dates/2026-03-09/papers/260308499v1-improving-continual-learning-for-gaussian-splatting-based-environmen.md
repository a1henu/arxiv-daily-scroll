---
layout: default
title: Improving Continual Learning for Gaussian Splatting based Environments Reconstruction on Commercial Off-the-Shelf Edge Devices
---

# Improving Continual Learning for Gaussian Splatting based Environments Reconstruction on Commercial Off-the-Shelf Edge Devices
**arXiv**：[2603.08499v1](https://arxiv.org/abs/2603.08499) · [PDF](https://arxiv.org/pdf/2603.08499.pdf)  
**作者**：Ivan Zaino, Matteo Risso, Daniele Jahier Pagliari, Miguel de Prado, Toon Van de Maele, Alessio Burrello  

**一句话要点**：提出精度自适应优化框架，使变分贝叶斯高斯泼溅能在资源受限边缘设备上训练，用于连续环境重建。

**关键词**：连续学习, 高斯泼溅, 边缘计算, 混合精度优化, 新视角合成, 资源受限训练

## 3 点简述
- 核心问题：变分贝叶斯高斯泼溅的高精度计算和大中间张量导致边缘设备训练不可行。
- 方法要点：通过内存/延迟热点分析、内核融合和混合精度搜索，减少内存占用和训练时间。
- 实验或效果：在多个数据集上，内存从9.44 GB降至1.11 GB，训练时间从约234分钟减至约61分钟，并在Jetson Orin Nano上首次实现训练。

## 摘要（原文）

> Novel view synthesis (NVS) is increasingly relevant for edge robotics, where compact and incrementally updatable 3D scene models are needed for SLAM, navigation, and inspection under tight memory and latency budgets. Variational Bayesian Gaussian Splatting (VBGS) enables replay-free continual updates for the 3DGS algorithm by maintaining a probabilistic scene model, but its high-precision computations and large intermediate tensors make on-device training impractical. We present a precision-adaptive optimization framework that enables VBGS training on resource-constrained hardware without altering its variational formulation. We (i) profile VBGS to identify memory/latency hotspots, (ii) fuse memory-dominant kernels to reduce materialized intermediate tensors, and (iii) automatically assign operation-level precisions via a mixed-precision search with bounded relative error. Across the Blender, Habitat, and Replica datasets, our optimised pipeline reduces peak memory from 9.44 GB to 1.11 GB and training time from ~234 min to ~61 min on an A5000 GPU, while preserving (and in some cases improving) reconstruction quality of the state-of-the-art VBGS baseline. We also enable for the first time NVS training on a commercial embedded platform, the Jetson Orin Nano, reducing per-frame latency by 19x compared to 3DGS.


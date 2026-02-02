---
layout: default
title: GaussianOcc3D: A Gaussian-Based Adaptive Multi-modal 3D Occupancy Prediction
---

# GaussianOcc3D: A Gaussian-Based Adaptive Multi-modal 3D Occupancy Prediction
**arXiv**：[2601.22729v1](https://arxiv.org/abs/2601.22729) · [PDF](https://arxiv.org/pdf/2601.22729.pdf)  
**作者**：A. Enes Doruk, Hasan F. Ates  

**一句话要点**：提出GaussianOcc3D，基于高斯表示的多模态3D占据预测框架，以解决自动驾驶中模态异构与计算效率问题。

**关键词**：3D占据预测, 多模态融合, 高斯表示, 自动驾驶感知, 状态空间模型, 鲁棒性评估

## 3 点简述
- 核心问题：多模态3D占据预测面临模态异构、空间错位和表示危机（体素计算重、BEV有损）。
- 方法要点：采用连续3D高斯表示，结合LDFA、EBFS、ACLF和Gauss-Mamba Head模块，实现高效多模态融合与全局上下文建模。
- 实验或效果：在Occ3D、SurroundOcc和SemanticKITTI基准上达到SOTA，mIoU分别为49.4%、28.9%、25.2%，并在雨夜条件下展现强鲁棒性。

## 摘要（原文）

> 3D semantic occupancy prediction is a pivotal task in autonomous driving, providing a dense and fine-grained understanding of the surrounding environment, yet single-modality methods face trade-offs between camera semantics and LiDAR geometry. Existing multi-modal frameworks often struggle with modality heterogeneity, spatial misalignment, and the representation crisis--where voxels are computationally heavy and BEV alternatives are lossy. We present GaussianOcc3D, a multi-modal framework bridging camera and LiDAR through a memory-efficient, continuous 3D Gaussian representation. We introduce four modules: (1) LiDAR Depth Feature Aggregation (LDFA), using depth-wise deformable sampling to lift sparse signals onto Gaussian primitives; (2) Entropy-Based Feature Smoothing (EBFS) to mitigate domain noise; (3) Adaptive Camera-LiDAR Fusion (ACLF) with uncertainty-aware reweighting for sensor reliability; and (4) a Gauss-Mamba Head leveraging Selective State Space Models for global context with linear complexity. Evaluations on Occ3D, SurroundOcc, and SemanticKITTI benchmarks demonstrate state-of-the-art performance, achieving mIoU scores of 49.4%, 28.9%, and 25.2% respectively. GaussianOcc3D exhibits superior robustness across challenging rainy and nighttime conditions.


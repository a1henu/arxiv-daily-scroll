---
layout: default
title: HE-VPR: Height Estimation Enabled Aerial Visual Place Recognition Against Scale Variance
---

# HE-VPR: Height Estimation Enabled Aerial Visual Place Recognition Against Scale Variance
**arXiv**：[2603.04050v1](https://arxiv.org/abs/2603.04050) · [PDF](https://arxiv.org/pdf/2603.04050.pdf)  
**作者**：Mengfan He, Xingyu Shao, Chunyu Li, Chao Chen, Liangzheng Sun, Ziyang Meng, Yuanqing Wu  

**一句话要点**：提出HE-VPR框架，通过高度估计解决空中视觉地点识别中的尺度变化问题。

**关键词**：视觉地点识别, 高度估计, 尺度不变性, 轻量适配器, 空中图像, DINOv2

## 3 点简述
- 核心问题：空中视觉地点识别因高度变化导致尺度差异，影响识别精度。
- 方法要点：使用冻结DINOv2骨干，集成轻量适配器分支进行高度分区检索和子数据库VPR。
- 实验或效果：在自收集多高度数据集上，Recall@1提升6.1%，内存使用减少90%。

## 摘要（原文）

> In this work, we propose HE-VPR, a visual place recognition (VPR) framework that incorporates height estimation. Our system decouples height inference from place recognition, allowing both modules to share a frozen DINOv2 backbone. Two lightweight bypass adapter branches are integrated into our system. The first estimates the height partition of the query image via retrieval from a compact height database, and the second performs VPR within the corresponding height-specific sub-database. The adaptation design reduces training cost and significantly decreases the search space of the database. We also adopt a center-weighted masking strategy to further enhance the robustness against scale differences. Experiments on two self-collected challenging multi-altitude datasets demonstrate that HE-VPR achieves up to 6.1\% Recall@1 improvement over state-of-the-art ViT-based baselines and reduces memory usage by up to 90\%. These results indicate that HE-VPR offers a scalable and efficient solution for height-aware aerial VPR, enabling practical deployment in GNSS-denied environments. All the code and datasets for this work have been released on https://github.com/hmf21/HE-VPR.


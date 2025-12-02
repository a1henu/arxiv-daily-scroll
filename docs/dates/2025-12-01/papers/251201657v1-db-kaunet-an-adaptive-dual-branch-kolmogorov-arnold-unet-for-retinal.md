---
layout: default
title: DB-KAUNet: An Adaptive Dual Branch Kolmogorov-Arnold UNet for Retinal Vessel Segmentation
---

# DB-KAUNet: An Adaptive Dual Branch Kolmogorov-Arnold UNet for Retinal Vessel Segmentation
**arXiv**：[2512.01657v1](https://arxiv.org/abs/2512.01657) · [PDF](https://arxiv.org/pdf/2512.01657.pdf)  
**作者**：Hongyu Xu, Panpan Meng, Meng Wang, Dayu Hu, Liming Liang, Xiaoqi Sheng  

**一句话要点**：提出自适应双分支Kolmogorov-Arnold UNet以解决视网膜血管分割中长程依赖和非线性关系捕获不足的问题。

**关键词**：视网膜血管分割, 双分支网络, Kolmogorov-Arnold网络, Transformer, 自适应采样, 医学图像分析

## 3 点简述
- 传统CNN方法在视网膜血管分割中难以捕获长程依赖和复杂非线性关系。
- 设计异构双分支编码器，结合CNN、Transformer及KANConv/KAT块，并集成跨分支通道交互与空间特征增强模块。
- 在DRIVE等数据集上验证了领先的分割性能和鲁棒性。

## 摘要（原文）

> Accurate segmentation of retinal vessels is crucial for the clinical diagnosis of numerous ophthalmic and systemic diseases. However, traditional Convolutional Neural Network (CNN) methods exhibit inherent limitations, struggling to capture long-range dependencies and complex nonlinear relationships. To address the above limitations, an Adaptive Dual Branch Kolmogorov-Arnold UNet (DB-KAUNet) is proposed for retinal vessel segmentation. In DB-KAUNet, we design a Heterogeneous Dual-Branch Encoder (HDBE) that features parallel CNN and Transformer pathways. The HDBE strategically interleaves standard CNN and Transformer blocks with novel KANConv and KAT blocks, enabling the model to form a comprehensive feature representation. To optimize feature processing, we integrate several critical components into the HDBE. First, a Cross-Branch Channel Interaction (CCI) module is embedded to facilitate efficient interaction of channel features between the parallel pathways. Second, an attention-based Spatial Feature Enhancement (SFE) module is employed to enhance spatial features and fuse the outputs from both branches. Building upon the SFE module, an advanced Spatial Feature Enhancement with Geometrically Adaptive Fusion (SFE-GAF) module is subsequently developed. In the SFE-GAF module, adaptive sampling is utilized to focus on true vessel morphology precisely. The adaptive process strengthens salient vascular features while significantly reducing background noise and computational overhead. Extensive experiments on the DRIVE, STARE, and CHASE_DB1 datasets validate that DB-KAUNet achieves leading segmentation performance and demonstrates exceptional robustness.


---
layout: default
title: Real-Time LiDAR Super-Resolution via Frequency-Aware Multi-Scale Fusion
---

# Real-Time LiDAR Super-Resolution via Frequency-Aware Multi-Scale Fusion
**arXiv**：[2511.07377v1](https://arxiv.org/abs/2511.07377) · [PDF](https://arxiv.org/pdf/2511.07377.pdf)  
**作者**：June Moh Goo, Zichao Zeng, Jan Boehm  

**一句话要点**：提出FLASH框架以解决低成本LiDAR传感器实时超分辨率问题

**关键词**：LiDAR超分辨率, 双域处理, 频率感知注意力, 自适应多尺度融合, 实时3D感知, KITTI基准

## 3 点简述
- 核心问题：低成本LiDAR传感器分辨率低，限制高质量3D感知，现有方法如TULIP仅空间域处理，感受野受限。
- 方法要点：引入双域处理，结合频率感知窗口注意力和自适应多尺度融合，捕获几何细节和扫描模式。
- 实验或效果：在KITTI数据集上实现SOTA性能，超越不确定性增强基线，保持单次推理实时性。

## 摘要（原文）

> LiDAR super-resolution addresses the challenge of achieving high-quality 3D
> perception from cost-effective, low-resolution sensors. While recent
> transformer-based approaches like TULIP show promise, they remain limited to
> spatial-domain processing with restricted receptive fields. We introduce FLASH
> (Frequency-aware LiDAR Adaptive Super-resolution with Hierarchical fusion), a
> novel framework that overcomes these limitations through dual-domain
> processing. FLASH integrates two key innovations: (i) Frequency-Aware Window
> Attention that combines local spatial attention with global frequency-domain
> analysis via FFT, capturing both fine-grained geometry and periodic scanning
> patterns at log-linear complexity. (ii) Adaptive Multi-Scale Fusion that
> replaces conventional skip connections with learned position-specific feature
> aggregation, enhanced by CBAM attention for dynamic feature selection.
> Extensive experiments on KITTI demonstrate that FLASH achieves state-of-the-art
> performance across all evaluation metrics, surpassing even uncertainty-enhanced
> baselines that require multiple forward passes. Notably, FLASH outperforms
> TULIP with Monte Carlo Dropout while maintaining single-pass efficiency, which
> enables real-time deployment. The consistent superiority across all distance
> ranges validates that our dual-domain approach effectively handles uncertainty
> through architectural design rather than computationally expensive stochastic
> inference, making it practical for autonomous systems.


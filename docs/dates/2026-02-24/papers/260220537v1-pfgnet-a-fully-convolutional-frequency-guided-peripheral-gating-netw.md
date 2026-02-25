---
layout: default
title: PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning
---

# PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning
**arXiv**：[2602.20537v1](https://arxiv.org/abs/2602.20537) · [PDF](https://arxiv.org/pdf/2602.20537.pdf)  
**作者**：Xinyong Cai, Changbin Sun, Yong Wang, Hongyu Yang, Yuankai Wu  

**一句话要点**：提出PFGNet，一种全卷积频率引导外围门控网络，用于高效时空预测学习。

**关键词**：时空预测学习, 全卷积网络, 频率引导门控, 可分离卷积, 自适应感受野, 高效模型

## 3 点简述
- 核心问题：纯卷积模型固定感受野限制自适应捕获空间变化运动模式。
- 方法要点：通过像素级频率引导门控动态调制感受野，使用可分离卷积保持效率。
- 实验效果：在多个数据集上实现SOTA或近SOTA性能，参数和计算量显著减少。

## 摘要（原文）

> Spatiotemporal predictive learning (STPL) aims to forecast future frames from past observations and is essential across a wide range of applications. Compared with recurrent or hybrid architectures, pure convolutional models offer superior efficiency and full parallelism, yet their fixed receptive fields limit their ability to adaptively capture spatially varying motion patterns. Inspired by biological center-surround organization and frequency-selective signal processing, we propose PFGNet, a fully convolutional framework that dynamically modulates receptive fields through pixel-wise frequency-guided gating. The core Peripheral Frequency Gating (PFG) block extracts localized spectral cues and adaptively fuses multi-scale large-kernel peripheral responses with learnable center suppression, effectively forming spatially adaptive band-pass filters. To maintain efficiency, all large kernels are decomposed into separable 1D convolutions ($1 \times k$ followed by $k \times 1$), reducing per-channel computational cost from $O(k^2)$ to $O(2k)$. PFGNet enables structure-aware spatiotemporal modeling without recurrence or attention. Experiments on Moving MNIST, TaxiBJ, Human3.6M, and KTH show that PFGNet delivers SOTA or near-SOTA forecasting performance with substantially fewer parameters and FLOPs. Our code is available at https://github.com/fhjdqaq/PFGNet.


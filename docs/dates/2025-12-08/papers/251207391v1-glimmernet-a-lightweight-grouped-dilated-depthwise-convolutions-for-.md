---
layout: default
title: GlimmerNet: A Lightweight Grouped Dilated Depthwise Convolutions for UAV-Based Emergency Monitoring
---

# GlimmerNet: A Lightweight Grouped Dilated Depthwise Convolutions for UAV-Based Emergency Monitoring
**arXiv**：[2512.07391v1](https://arxiv.org/abs/2512.07391) · [PDF](https://arxiv.org/pdf/2512.07391.pdf)  
**作者**：Đorđe Nedeljković  

**一句话要点**：提出GlimmerNet，一种基于分组扩张深度卷积的轻量网络，用于无人机应急监测。

**关键词**：轻量卷积网络, 无人机监测, 分组扩张卷积, 多尺度特征提取, 实时计算优化

## 3 点简述
- 核心问题：现有视觉Transformer引入计算开销，难以在资源受限无人机上实现高效全局感知。
- 方法要点：设计分组扩张深度卷积块，分离感受野多样性与特征重组，以零参数成本提取多尺度特征。
- 实验或效果：在AIDERv2数据集上，仅31K参数，FLOPs减少29%，加权F1-score达0.966，创下新SOTA。

## 摘要（原文）

> Convolutional Neural Networks (CNNs) have proven highly effective for edge and mobile vision tasks due to their computational efficiency. While many recent works seek to enhance CNNs with global contextual understanding via self-attention-based Vision Transformers, these approaches often introduce significant computational overhead. In this work, we demonstrate that it is possible to retain strong global perception without relying on computationally expensive components. We present GlimmerNet, an ultra-lightweight convolutional network built on the principle of separating receptive field diversity from feature recombination. GlimmerNet introduces Grouped Dilated Depthwise Convolutions(GDBlocks), which partition channels into groups with distinct dilation rates, enabling multi-scale feature extraction at no additional parameter cost. To fuse these features efficiently, we design a novel Aggregator module that recombines cross-group representations using grouped pointwise convolution, significantly lowering parameter overhead. With just 31K parameters and 29% fewer FLOPs than the most recent baseline, GlimmerNet achieves a new state-of-the-art weighted F1-score of 0.966 on the UAV-focused AIDERv2 dataset. These results establish a new accuracy-efficiency trade-off frontier for real-time emergency monitoring on resource-constrained UAV platforms. Our implementation is publicly available at https://github.com/djordjened92/gdd-cnn.


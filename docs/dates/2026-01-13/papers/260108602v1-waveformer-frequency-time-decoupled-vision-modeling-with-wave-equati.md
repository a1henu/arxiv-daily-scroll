---
layout: default
title: WaveFormer: Frequency-Time Decoupled Vision Modeling with Wave Equation
---

# WaveFormer: Frequency-Time Decoupled Vision Modeling with Wave Equation
**arXiv**：[2601.08602v1](https://arxiv.org/abs/2601.08602) · [PDF](https://arxiv.org/pdf/2601.08602.pdf)  
**作者**：Zishan Shu, Juntong Wu, Wei Yan, Xudong Liu, Hongyu Zhang, Chang Liu, Youdong Mao, Jie Chen  

**一句话要点**：提出WaveFormer，基于波动方程解耦频率与时间，以高效建模视觉语义传播。

**关键词**：视觉建模, 波动方程, 频率时间解耦, 高效算子, 全局交互, 语义传播

## 3 点简述
- 核心问题：Transformer注意力机制缺乏对语义信息空间传播的原理性建模。
- 方法要点：将特征图视为空间信号，用欠阻尼波动方程控制频率与传播时间的交互。
- 实验或效果：在图像分类等任务中实现竞争性精度，吞吐量提升1.6倍，FLOPs减少30%。

## 摘要（原文）

> Vision modeling has advanced rapidly with Transformers, whose attention mechanisms capture visual dependencies but lack a principled account of how semantic information propagates spatially. We revisit this problem from a wave-based perspective: feature maps are treated as spatial signals whose evolution over an internal propagation time (aligned with network depth) is governed by an underdamped wave equation. In this formulation, spatial frequency-from low-frequency global layout to high-frequency edges and textures-is modeled explicitly, and its interaction with propagation time is controlled rather than implicitly fixed. We derive a closed-form, frequency-time decoupled solution and implement it as the Wave Propagation Operator (WPO), a lightweight module that models global interactions in O(N log N) time-far lower than attention. Building on WPO, we propose a family of WaveFormer models as drop-in replacements for standard ViTs and CNNs, achieving competitive accuracy across image classification, object detection, and semantic segmentation, while delivering up to 1.6x higher throughput and 30% fewer FLOPs than attention-based alternatives. Furthermore, our results demonstrate that wave propagation introduces a complementary modeling bias to heat-based methods, effectively capturing both global coherence and high-frequency details essential for rich visual semantics. Codes are available at: https://github.com/ZishanShu/WaveFormer.


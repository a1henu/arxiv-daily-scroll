---
layout: default
title: Partial Ring Scan: Revisiting Scan Order in Vision State Space Models
---

# Partial Ring Scan: Revisiting Scan Order in Vision State Space Models
**arXiv**：[2602.04170v1](https://arxiv.org/abs/2602.04170) · [PDF](https://arxiv.org/pdf/2602.04170.pdf)  
**作者**：Yi-Kuan Hsieh, Jun-Wei Hsieh, Xin li, Ming-Ching Chang, Yu-Chee Tseng  

**一句话要点**：提出PRISMamba以解决视觉状态空间模型中扫描顺序对性能和旋转鲁棒性的影响

**关键词**：视觉状态空间模型, 扫描顺序设计, 旋转鲁棒性, 部分通道过滤, 图像序列化, 高效计算

## 3 点简述
- 核心问题：视觉SSMs中图像序列化扫描顺序常被忽视，但影响空间邻接和对象连续性，导致旋转等几何变换下性能下降
- 方法要点：引入PRISMamba，采用同心环分区、环内顺序无关聚合和径向SSMs跨环传播，结合部分通道过滤提升效率
- 实验或效果：在ImageNet-1K上达到84.5% Top-1准确率，3.9G FLOPs，A100上3,054 img/s，优于VMamba，旋转下性能稳定

## 摘要（原文）

> State Space Models (SSMs) have emerged as efficient alternatives to attention for vision tasks, offering lineartime sequence processing with competitive accuracy. Vision SSMs, however, require serializing 2D images into 1D token sequences along a predefined scan order, a factor often overlooked. We show that scan order critically affects performance by altering spatial adjacency, fracturing object continuity, and amplifying degradation under geometric transformations such as rotation. We present Partial RIng Scan Mamba (PRISMamba), a rotation-robust traversal that partitions an image into concentric rings, performs order-agnostic aggregation within each ring, and propagates context across rings through a set of short radial SSMs. Efficiency is further improved via partial channel filtering, which routes only the most informative channels through the recurrent ring pathway while keeping the rest on a lightweight residual branch. On ImageNet-1K, PRISMamba achieves 84.5% Top-1 with 3.9G FLOPs and 3,054 img/s on A100, outperforming VMamba in both accuracy and throughput while requiring fewer FLOPs. It also maintains performance under rotation, whereas fixed-path scans drop by 1~2%. These results highlight scan-order design, together with channel filtering, as a crucial, underexplored factor for accuracy, efficiency, and rotation robustness in Vision SSMs. Code will be released upon acceptance.


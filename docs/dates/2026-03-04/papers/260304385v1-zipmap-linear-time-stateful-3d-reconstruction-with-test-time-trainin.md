---
layout: default
title: ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training
---

# ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training
**arXiv**：[2603.04385v1](https://arxiv.org/abs/2603.04385) · [PDF](https://arxiv.org/pdf/2603.04385.pdf)  
**作者**：Haian Jin, Rundi Wu, Tianyuan Zhang, Ruiqi Gao, Jonathan T. Barron, Noah Snavely, Aleksander Holynski  

**一句话要点**：提出ZipMap，通过测试时训练实现线性时间状态化3D重建，解决大规模图像集合计算成本高的问题。

**关键词**：3D重建, 线性时间算法, 状态化模型, 测试时训练, 大规模图像处理, 实时查询

## 3 点简述
- 核心问题：现有前馈变换器模型如VGGT和π³在3D重建中计算成本随输入图像数量二次增长，效率低下。
- 方法要点：ZipMap采用状态化前馈模型和测试时训练层，在单次前向传播中将图像集合压缩为紧凑隐藏场景状态，实现双向线性时间重建。
- 实验或效果：在单个H100 GPU上，ZipMap重建超过700帧图像用时不到10秒，比VGGT快20倍以上，且精度匹配或超越二次时间方法。

## 摘要（原文）

> Feed-forward transformer models have driven rapid progress in 3D vision, but state-of-the-art methods such as VGGT and $π^3$ have a computational cost that scales quadratically with the number of input images, making them inefficient when applied to large image collections. Sequential-reconstruction approaches reduce this cost but sacrifice reconstruction quality. We introduce ZipMap, a stateful feed-forward model that achieves linear-time, bidirectional 3D reconstruction while matching or surpassing the accuracy of quadratic-time methods. ZipMap employs test-time training layers to zip an entire image collection into a compact hidden scene state in a single forward pass, enabling reconstruction of over 700 frames in under 10 seconds on a single H100 GPU, more than $20\times$ faster than state-of-the-art methods such as VGGT. Moreover, we demonstrate the benefits of having a stateful representation in real-time scene-state querying and its extension to sequential streaming reconstruction.


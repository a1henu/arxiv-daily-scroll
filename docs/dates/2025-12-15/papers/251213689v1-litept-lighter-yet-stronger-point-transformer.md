---
layout: default
title: LitePT: Lighter Yet Stronger Point Transformer
---

# LitePT: Lighter Yet Stronger Point Transformer
**arXiv**：[2512.13689v1](https://arxiv.org/abs/2512.13689) · [PDF](https://arxiv.org/pdf/2512.13689.pdf)  
**作者**：Yuanwen Yue, Damien Robert, Jianyuan Wang, Sunghwan Hong, Jan Dirk Wegner, Christian Rupprecht, Konrad Schindler  

**一句话要点**：提出LitePT，通过早期卷积与深层注意力结合，优化3D点云网络架构。

**关键词**：3D点云处理, 卷积注意力结合, 位置编码, 网络架构优化, 轻量化模型

## 3 点简述
- 分析卷积与注意力在3D点云网络中的角色，发现早期卷积提取低层几何更高效，深层注意力捕获高层语义更优。
- 引入训练无关的3D位置编码PointROPE，以保留空间布局信息，避免冗余卷积层丢弃。
- LitePT相比Point Transformer V3参数减少3.6倍、速度提升2倍、内存使用减半，性能相当或更优。

## 摘要（原文）

> Modern neural architectures for 3D point cloud processing contain both convolutional layers and attention blocks, but the best way to assemble them remains unclear. We analyse the role of different computational blocks in 3D point cloud networks and find an intuitive behaviour: convolution is adequate to extract low-level geometry at high-resolution in early layers, where attention is expensive without bringing any benefits; attention captures high-level semantics and context in low-resolution, deep layers more efficiently. Guided by this design principle, we propose a new, improved 3D point cloud backbone that employs convolutions in early stages and switches to attention for deeper layers. To avoid the loss of spatial layout information when discarding redundant convolution layers, we introduce a novel, training-free 3D positional encoding, PointROPE. The resulting LitePT model has $3.6\times$ fewer parameters, runs $2\times$ faster, and uses $2\times$ less memory than the state-of-the-art Point Transformer V3, but nonetheless matches or even outperforms it on a range of tasks and datasets. Code and models are available at: https://github.com/prs-eth/LitePT.


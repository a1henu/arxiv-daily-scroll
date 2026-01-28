---
layout: default
title: SONIC: Spectral Oriented Neural Invariant Convolutions
---

# SONIC: Spectral Oriented Neural Invariant Convolutions
**arXiv**：[2601.19884v1](https://arxiv.org/abs/2601.19884) · [PDF](https://arxiv.org/pdf/2601.19884.pdf)  
**作者**：Gijs Joppe Moens, Regina Beets-Tan, Eduardo H. P. Pooch  

**一句话要点**：提出SONIC以解决CNN和ViT在全局上下文与空间归纳偏差上的局限性

**关键词**：光谱卷积, 全局感受野, 方向选择性, 分辨率自适应, 参数效率, 鲁棒性

## 3 点简述
- 核心问题：CNN依赖局部卷积核，难以捕获全局上下文；ViT缺乏空间归纳偏差，依赖显式位置编码。
- 方法要点：引入连续光谱参数化，使用少量共享、方向选择性组件建模卷积算子，实现全局感受野和分辨率自适应。
- 实验或效果：在合成基准、大规模图像分类和3D医学数据集上，SONIC展示了对几何变换、噪声和分辨率变化的鲁棒性，参数更少且性能匹配或超越现有方法。

## 摘要（原文）

> Convolutional Neural Networks (CNNs) rely on fixed-size kernels scanning local patches, which limits their ability to capture global context or long-range dependencies without very deep architectures. Vision Transformers (ViTs), in turn, provide global connectivity but lack spatial inductive bias, depend on explicit positional encodings, and remain tied to the initial patch size. Bridging these limitations requires a representation that is both structured and global. We introduce SONIC (Spectral Oriented Neural Invariant Convolutions), a continuous spectral parameterisation that models convolutional operators using a small set of shared, orientation-selective components. These components define smooth responses across the full frequency domain, yielding global receptive fields and filters that adapt naturally across resolutions. Across synthetic benchmarks, large-scale image classification, and 3D medical datasets, SONIC shows improved robustness to geometric transformations, noise, and resolution shifts, and matches or exceeds convolutional, attention-based, and prior spectral architectures with an order of magnitude fewer parameters. These results demonstrate that continuous, orientation-aware spectral parameterisations provide a principled and scalable alternative to conventional spatial and spectral operators.


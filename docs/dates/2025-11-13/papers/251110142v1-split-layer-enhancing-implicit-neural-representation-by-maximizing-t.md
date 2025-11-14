---
layout: default
title: Split-Layer: Enhancing Implicit Neural Representation by Maximizing the Dimensionality of Feature Space
---

# Split-Layer: Enhancing Implicit Neural Representation by Maximizing the Dimensionality of Feature Space
**arXiv**：[2511.10142v1](https://arxiv.org/abs/2511.10142) · [PDF](https://arxiv.org/pdf/2511.10142.pdf)  
**作者**：Zhicheng Cai, Hao Zhu, Linsen Chen, Qiu Shen, Xun Cao  

**一句话要点**：提出Split-Layer以增强隐式神经表示，通过扩展特征空间维度提升性能

**关键词**：隐式神经表示, 多层感知机, 特征空间扩展, Hadamard积, 多项式空间, 逆问题优化

## 3 点简述
- 隐式神经表示受限于传统MLP的低维特征空间，导致表示能力不足
- Split-Layer将MLP层分割为并行分支，通过Hadamard积构建高次多项式空间
- 实验显示在图像拟合、CT重建等任务中性能显著优于现有方法

## 摘要（原文）

> Implicit neural representation (INR) models signals as continuous functions using neural networks, offering efficient and differentiable optimization for inverse problems across diverse disciplines. However, the representational capacity of INR defined by the range of functions the neural network can characterize, is inherently limited by the low-dimensional feature space in conventional multilayer perceptron (MLP) architectures. While widening the MLP can linearly increase feature space dimensionality, it also leads to a quadratic growth in computational and memory costs. To address this limitation, we propose the split-layer, a novel reformulation of MLP construction. The split-layer divides each layer into multiple parallel branches and integrates their outputs via Hadamard product, effectively constructing a high-degree polynomial space. This approach significantly enhances INR's representational capacity by expanding the feature space dimensionality without incurring prohibitive computational overhead. Extensive experiments demonstrate that the split-layer substantially improves INR performance, surpassing existing methods across multiple tasks, including 2D image fitting, 2D CT reconstruction, 3D shape representation, and 5D novel view synthesis.


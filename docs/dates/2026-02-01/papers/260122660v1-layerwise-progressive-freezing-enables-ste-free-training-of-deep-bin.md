---
layout: default
title: Layerwise Progressive Freezing Enables STE-Free Training of Deep Binary Neural Networks
---

# Layerwise Progressive Freezing Enables STE-Free Training of Deep Binary Neural Networks
**arXiv**：[2601.22660v1](https://arxiv.org/abs/2601.22660) · [PDF](https://arxiv.org/pdf/2601.22660.pdf)  
**作者**：Evan Gibson Smith, Bashima Islam  

**一句话要点**：提出层渐进冻结方法StoMPP，以替代STE训练深度二值神经网络

**关键词**：二值神经网络, 渐进冻结, 随机掩码, 梯度估计, 深度网络训练, 图像分类

## 3 点简述
- 核心问题：全局渐进冻结在全二值神经网络中因激活梯度阻塞而失效
- 方法要点：使用层随机掩码渐进替换可微权重/激活为硬二值函数，避免STE
- 实验效果：在匹配训练条件下，StoMPP提升准确率，增益随深度增加

## 摘要（原文）

> We investigate progressive freezing as an alternative to straight-through estimators (STE) for training binary networks from scratch. Under controlled training conditions, we find that while global progressive freezing works for binary-weight networks, it fails for full binary neural networks due to activation-induced gradient blockades. We introduce StoMPP (Stochastic Masked Partial Progressive Binarization), which uses layerwise stochastic masking to progressively replace differentiable clipped weights/activations with hard binary step functions, while only backpropagating through the unfrozen (clipped) subset (i.e., no straight-through estimator). Under a matched minimal training recipe, StoMPP improves accuracy over a BinaryConnect-style STE baseline, with gains that increase with depth (e.g., for ResNet-50 BNN: +18.0 on CIFAR-10, +13.5 on CIFAR-100, and +3.8 on ImageNet; for ResNet-18: +3.1, +4.7, and +1.3). For binary-weight networks, StoMPP achieves 91.2\% accuracy on CIFAR-10 and 69.5\% on CIFAR-100 with ResNet-50. We analyze training dynamics under progressive freezing, revealing non-monotonic convergence and improved depth scaling under binarization constraints.


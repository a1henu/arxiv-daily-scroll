---
layout: default
title: Shift-Equivariant Complex-Valued Convolutional Neural Networks
---

# Shift-Equivariant Complex-Valued Convolutional Neural Networks
**arXiv**：[2511.21250v1](https://arxiv.org/abs/2511.21250) · [PDF](https://arxiv.org/pdf/2511.21250.pdf)  
**作者**：Quentin Gabot, Teck-Yian Lim, Jérémy Fix, Joana Frontera-Pons, Chengfang Ren, Jean-Philippe Ovarlez  

**一句话要点**：提出复数卷积神经网络扩展LPS方法，以在极化SAR图像任务中实现平移等变性。

**关键词**：复数卷积神经网络, 平移等变性, 自适应多相采样, 极化SAR图像, 语义分割, 图像重建

## 3 点简述
- 传统卷积网络因下采样/上采样破坏平移等变性和不变性。
- 扩展LPS到复数网络，添加复数到实数的投影层。
- 在分类、重建和语义分割任务中评估平移性质。

## 摘要（原文）

> Convolutional neural networks have shown remarkable performance in recent years on various computer vision problems. However, the traditional convolutional neural network architecture lacks a critical property: shift equivariance and invariance, broken by downsampling and upsampling operations. Although data augmentation techniques can help the model learn the latter property empirically, a consistent and systematic way to achieve this goal is by designing downsampling and upsampling layers that theoretically guarantee these properties by construction. Adaptive Polyphase Sampling (APS) introduced the cornerstone for shift invariance, later extended to shift equivariance with Learnable Polyphase up/downsampling (LPS) applied to real-valued neural networks. In this paper, we extend the work on LPS to complex-valued neural networks both from a theoretical perspective and with a novel building block of a projection layer from $\mathbb{C}$ to $\mathbb{R}$ before the Gumbel Softmax. We finally evaluate this extension on several computer vision problems, specifically for either the invariance property in classification tasks or the equivariance property in both reconstruction and semantic segmentation problems, using polarimetric Synthetic Aperture Radar images.


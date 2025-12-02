---
layout: default
title: Revisiting Direct Encoding: Learnable Temporal Dynamics for Static Image Spiking Neural Networks
---

# Revisiting Direct Encoding: Learnable Temporal Dynamics for Static Image Spiking Neural Networks
**arXiv**：[2512.01687v1](https://arxiv.org/abs/2512.01687) · [PDF](https://arxiv.org/pdf/2512.01687.pdf)  
**作者**：Huaxu He  

**一句话要点**：提出可学习时序编码以解决静态图像脉冲神经网络中时序建模不足的问题

**关键词**：脉冲神经网络, 静态图像处理, 时序编码, 可学习动态, 替代梯度, 卷积网络

## 3 点简述
- 核心问题：静态图像缺乏固有时序动态，导致直接训练脉冲神经网络时时序维度退化，无法有效建模
- 方法要点：引入最小可学习时序编码，通过自适应相位偏移从静态输入诱导有意义的时序变化
- 实验或效果：澄清直接编码与速率编码性能差距源于卷积可学习性和替代梯度，而非编码方案本身

## 摘要（原文）

> Handling static images that lack inherent temporal dynamics remains a fundamental challenge for spiking neural networks (SNNs). In directly trained SNNs, static inputs are typically repeated across time steps, causing the temporal dimension to collapse into a rate like representation and preventing meaningful temporal modeling. This work revisits the reported performance gap between direct and rate based encodings and shows that it primarily stems from convolutional learnability and surrogate gradient formulations rather than the encoding schemes themselves. To illustrate this mechanism level clarification, we introduce a minimal learnable temporal encoding that adds adaptive phase shifts to induce meaningful temporal variation from static inputs.


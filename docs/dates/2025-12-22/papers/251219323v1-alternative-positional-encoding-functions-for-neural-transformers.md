---
layout: default
title: Alternative positional encoding functions for neural transformers
---

# Alternative positional encoding functions for neural transformers
**arXiv**：[2512.19323v1](https://arxiv.org/abs/2512.19323) · [PDF](https://arxiv.org/pdf/2512.19323.pdf)  
**作者**：Ezequiel Lopez-Rubio, Macoris Decena-Gimenez, Rafael Marcos Luque-Baena  

**一句话要点**：提出替代性位置编码函数以改进神经Transformer架构的性能。

**关键词**：位置编码, Transformer架构, 周期函数, 神经网络, 深度学习

## 3 点简述
- 核心问题：Transformer架构中位置编码模块依赖正弦函数，可能限制性能。
- 方法要点：提出一组替代性周期函数，保留正弦函数关键特性但进行根本性改变。
- 实验或效果：初步实验显示替代函数显著优于原始正弦版本，暗示更广泛应用潜力。

## 摘要（原文）

> A key module in neural transformer-based deep architectures is positional encoding. This module enables a suitable way to encode positional information as input for transformer neural layers. This success has been rooted in the use of sinusoidal functions of various frequencies, in order to capture recurrent patterns of differing typical periods. In this work, an alternative set of periodic functions is proposed for positional encoding. These functions preserve some key properties of sinusoidal ones, while they depart from them in fundamental ways. Some tentative experiments are reported, where the original sinusoidal version is substantially outperformed. This strongly suggests that the alternative functions may have a wider use in other transformer architectures.


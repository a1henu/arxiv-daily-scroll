---
layout: default
title: Padé Neurons for Efficient Neural Models
---

# Padé Neurons for Efficient Neural Models
**arXiv**：[2601.04005v1](https://arxiv.org/abs/2601.04005) · [PDF](https://arxiv.org/pdf/2601.04005.pdf)  
**作者**：Onur Keleş, A. Murat Tekalp  

**一句话要点**：提出Padé神经元以增强神经网络非线性并减少层数

**关键词**：Padé神经元, 非线性神经元模型, 神经网络效率, 图像超分辨率, ResNet架构

## 3 点简述
- 核心问题：传统McCulloch-Pitts神经元模型依赖点状非线性激活，非线性能力有限。
- 方法要点：基于Padé近似设计Padé神经元，学习输入的不同非线性函数，提供更强非线性。
- 实验或效果：在图像超分辨率、压缩和分类任务中，Padé神经元以更少层数实现同等或更好性能。

## 摘要（原文）

> Neural networks commonly employ the McCulloch-Pitts neuron model, which is a linear model followed by a point-wise non-linear activation. Various researchers have already advanced inherently non-linear neuron models, such as quadratic neurons, generalized operational neurons, generative neurons, and super neurons, which offer stronger non-linearity compared to point-wise activation functions. In this paper, we introduce a novel and better non-linear neuron model called Padé neurons (Paons), inspired by Padé approximants. Paons offer several advantages, such as diversity of non-linearity, since each Paon learns a different non-linear function of its inputs, and layer efficiency, since Paons provide stronger non-linearity in much fewer layers compared to piecewise linear approximation. Furthermore, Paons include all previously proposed neuron models as special cases, thus any neuron model in any network can be replaced by Paons. We note that there has been a proposal to employ the Padé approximation as a generalized point-wise activation function, which is fundamentally different from our model. To validate the efficacy of Paons, in our experiments, we replace classic neurons in some well-known neural image super-resolution, compression, and classification models based on the ResNet architecture with Paons. Our comprehensive experimental results and analyses demonstrate that neural models built by Paons provide better or equal performance than their classic counterparts with a smaller number of layers. The PyTorch implementation code for Paon is open-sourced at https://github.com/onur-keles/Paon.


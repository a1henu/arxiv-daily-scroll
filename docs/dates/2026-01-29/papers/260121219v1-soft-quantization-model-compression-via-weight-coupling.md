---
layout: default
title: Soft Quantization: Model Compression Via Weight Coupling
---

# Soft Quantization: Model Compression Via Weight Coupling
**arXiv**：[2601.21219v1](https://arxiv.org/abs/2601.21219) · [PDF](https://arxiv.org/pdf/2601.21219.pdf)  
**作者**：Daniel T. Bernstein, Luca Di Carlo, David Schwab  

**一句话要点**：提出软量化方法，通过权重耦合实现神经网络模型压缩

**关键词**：模型压缩, 权重量化, 神经网络训练, 混合精度, 泛化能力, 损失景观

## 3 点简述
- 核心问题：模型量化中权重分布离散化困难，影响压缩效果与泛化能力
- 方法要点：训练时引入短程吸引耦合，诱导权重分布自动离散化，仅需两个超参数
- 实验或效果：在ResNet-20/CIFAR-10上优于直方图均衡后训练量化，提供灵活压缩新途径

## 摘要（原文）

> We show that introducing short-range attractive couplings between the weights of a neural network during training provides a novel avenue for model quantization. These couplings rapidly induce the discretization of a model's weight distribution, and they do so in a mixed-precision manner despite only relying on two additional hyperparameters. We demonstrate that, within an appropriate range of hyperparameters, our "soft quantization'' scheme outperforms histogram-equalized post-training quantization on ResNet-20/CIFAR-10. Soft quantization provides both a new pipeline for the flexible compression of machine learning models and a new tool for investigating the trade-off between compression and generalization in high-dimensional loss landscapes.


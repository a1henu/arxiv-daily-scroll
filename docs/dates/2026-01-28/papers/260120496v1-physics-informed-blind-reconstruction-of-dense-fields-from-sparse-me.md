---
layout: default
title: Physics-informed Blind Reconstruction of Dense Fields from Sparse Measurements using Neural Networks with a Differentiable Simulator
---

# Physics-informed Blind Reconstruction of Dense Fields from Sparse Measurements using Neural Networks with a Differentiable Simulator
**arXiv**：[2601.20496v1](https://arxiv.org/abs/2601.20496) · [PDF](https://arxiv.org/pdf/2601.20496.pdf)  
**作者**：Ofek Aloni, Barak Fishbain  

**一句话要点**：提出基于可微分模拟器的神经网络方法，从稀疏测量重建密集物理场

**关键词**：密集场重建, 稀疏测量, 可微分模拟器, 物理信息神经网络, 流体力学

## 3 点简述
- 核心问题：从稀疏测量生成密集物理场，无需先验统计或密集场示例
- 方法要点：引入可微分数值模拟器到训练阶段，结合物理信息
- 实验或效果：在流体力学标准问题上优于统计和神经网络方法

## 摘要（原文）

> Generating dense physical fields from sparse measurements is a fundamental question in sampling, signal processing, and many other applications. State-of-the-art methods either use spatial statistics or rely on examples of dense fields in the training phase, which often are not available, and thus rely on synthetic data. Here, we present a reconstruction method that generates dense fields from sparse measurements, without assuming availability of the spatial statistics, nor of examples of the dense fields. This is made possible through the introduction of an automatically differentiable numerical simulator into the training phase of the method. The method is shown to have superior results over statistical and neural network based methods on a set of three standard problems from fluid mechanics.


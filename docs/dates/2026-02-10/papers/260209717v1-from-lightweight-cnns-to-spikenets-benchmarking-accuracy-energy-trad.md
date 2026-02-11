---
layout: default
title: From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet
---

# From Lightweight CNNs to SpikeNets: Benchmarking Accuracy-Energy Tradeoffs with Pruned Spiking SqueezeNet
**arXiv**：[2602.09717v1](https://arxiv.org/abs/2602.09717) · [PDF](https://arxiv.org/pdf/2602.09717.pdf)  
**作者**：Radib Bin Kabir, Tawsif Tashwar Dipto, Mehedi Ahamed, Sabbir Ahmed, Md Hasanul Kabir  

**一句话要点**：提出轻量级脉冲神经网络基准与剪枝优化，实现边缘部署的高能效智能

**关键词**：脉冲神经网络, 轻量级模型, 能效优化, 结构化剪枝, 边缘计算, 基准测试

## 3 点简述
- 核心问题：轻量级CNN到SNN转换的设计与评估不足，缺乏系统基准。
- 方法要点：将紧凑CNN转换为基于LIF神经元的SNN，采用结构化剪枝去除冗余模块。
- 实验或效果：SNN-SqueezeNet-P在CIFAR-10上精度提升6%，能耗降低88.1%，接近CNN性能。

## 摘要（原文）

> Spiking Neural Networks (SNNs) are increasingly studied as energy-efficient alternatives to Convolutional Neural Networks (CNNs), particularly for edge intelligence. However, prior work has largely emphasized large-scale models, leaving the design and evaluation of lightweight CNN-to-SNN pipelines underexplored. In this paper, we present the first systematic benchmark of lightweight SNNs obtained by converting compact CNN architectures into spiking networks, where activations are modeled with Leaky-Integrate-and-Fire (LIF) neurons and trained using surrogate gradient descent under a unified setup. We construct spiking variants of ShuffleNet, SqueezeNet, MnasNet, and MixNet, and evaluate them on CIFAR-10, CIFAR-100, and TinyImageNet, measuring accuracy, F1-score, parameter count, computational complexity, and energy consumption. Our results show that SNNs can achieve up to 15.7x higher energy efficiency than their CNN counterparts while retaining competitive accuracy. Among these, the SNN variant of SqueezeNet consistently outperforms other lightweight SNNs. To further optimize this model, we apply a structured pruning strategy that removes entire redundant modules, yielding a pruned architecture, SNN-SqueezeNet-P. This pruned model improves CIFAR-10 accuracy by 6% and reduces parameters by 19% compared to the original SNN-SqueezeNet. Crucially, it narrows the gap with CNN-SqueezeNet, achieving nearly the same accuracy (only 1% lower) but with an 88.1% reduction in energy consumption due to sparse spike-driven computations. Together, these findings establish lightweight SNNs as practical, low-power alternatives for edge deployment, highlighting a viable path toward deploying high-performance, low-power intelligence on the edge.


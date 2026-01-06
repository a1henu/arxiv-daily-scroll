---
layout: default
title: LION-DG: Layer-Informed Initialization with Deep Gradient Protocols for Accelerated Neural Network Training
---

# LION-DG: Layer-Informed Initialization with Deep Gradient Protocols for Accelerated Neural Network Training
**arXiv**：[2601.02105v1](https://arxiv.org/abs/2601.02105) · [PDF](https://arxiv.org/pdf/2601.02105.pdf)  
**作者**：Hyunjun Kim  

**一句话要点**：提出LION-DG层感知初始化方法，以加速带辅助分类器的深度网络训练。

**关键词**：权重初始化, 深度监督网络, 梯度干扰, 辅助分类器, 训练加速, 无超参数优化

## 3 点简述
- 核心问题：现有权重初始化方法对层不敏感，辅助分类器在早期训练中可能因梯度干扰导致不稳定。
- 方法要点：零初始化辅助分类器头部，主干网络采用标准He初始化，实现无超参数的梯度唤醒机制。
- 实验效果：在CIFAR数据集上，DenseNet-DS收敛速度提升8.3%，结合LSUV达到81.92%准确率，ResNet-DS在CIFAR-100上加速11.3%。

## 摘要（原文）

> Weight initialization remains decisive for neural network optimization, yet existing methods are largely layer-agnostic. We study initialization for deeply-supervised architectures with auxiliary classifiers, where untrained auxiliary heads can destabilize early training through gradient interference.
>   We propose LION-DG, a layer-informed initialization that zero-initializes auxiliary classifier heads while applying standard He-initialization to the backbone. We prove that this implements Gradient Awakening: auxiliary gradients are exactly zero at initialization, then phase in naturally as weights grow -- providing an implicit warmup without hyperparameters.
>   Experiments on CIFAR-10 and CIFAR-100 with DenseNet-DS and ResNet-DS architectures demonstrate: (1) DenseNet-DS: +8.3% faster convergence on CIFAR-10 with comparable accuracy, (2) Hybrid approach: Combining LSUV with LION-DG achieves best accuracy (81.92% on CIFAR-10), (3) ResNet-DS: Positive speedup on CIFAR-100 (+11.3%) with side-tap auxiliary design.
>   We identify architecture-specific trade-offs and provide clear guidelines for practitioners. LION-DG is simple, requires zero hyperparameters, and adds no computational overhead.


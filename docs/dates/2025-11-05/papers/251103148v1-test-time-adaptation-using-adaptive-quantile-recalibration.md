---
layout: default
title: Test Time Adaptation Using Adaptive Quantile Recalibration
---

# Test Time Adaptation Using Adaptive Quantile Recalibration
**arXiv**：[2511.03148v1](https://arxiv.org/abs/2511.03148) · [PDF](https://arxiv.org/pdf/2511.03148.pdf)  
**作者**：Paria Mehrbod, Pedro Vianna, Geraldin Nanfack, Guy Wolf, Eugene Belilovsky  

**一句话要点**：提出自适应分位数重校准以解决测试时分布偏移问题

**关键词**：测试时适应, 分位数对齐, 分布校准, 无监督适应, 归一化层泛化

## 3 点简述
- 核心问题：测试分布与训练分布差异大，传统方法需目标域先验或重训练
- 方法要点：通过通道级分位数对齐调整预激活分布，支持多种归一化层
- 实验或效果：在CIFAR和ImageNet-C上优于基线，适应动态数据分布

## 摘要（原文）

> Domain adaptation is a key strategy for enhancing the generalizability of
> deep learning models in real-world scenarios, where test distributions often
> diverge significantly from the training domain. However, conventional
> approaches typically rely on prior knowledge of the target domain or require
> model retraining, limiting their practicality in dynamic or
> resource-constrained environments. Recent test-time adaptation methods based on
> batch normalization statistic updates allow for unsupervised adaptation, but
> they often fail to capture complex activation distributions and are constrained
> to specific normalization layers. We propose Adaptive Quantile Recalibration
> (AQR), a test-time adaptation technique that modifies pre-activation
> distributions by aligning quantiles on a channel-wise basis. AQR captures the
> full shape of activation distributions and generalizes across architectures
> employing BatchNorm, GroupNorm, or LayerNorm. To address the challenge of
> estimating distribution tails under varying batch sizes, AQR incorporates a
> robust tail calibration strategy that improves stability and precision. Our
> method leverages source-domain statistics computed at training time, enabling
> unsupervised adaptation without retraining models. Experiments on CIFAR-10-C,
> CIFAR-100-C, and ImageNet-C across multiple architectures demonstrate that AQR
> achieves robust adaptation across diverse settings, outperforming existing
> test-time adaptation baselines. These results highlight AQR's potential for
> deployment in real-world scenarios with dynamic and unpredictable data
> distributions.


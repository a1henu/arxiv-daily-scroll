---
layout: default
title: Dynamic Momentum Recalibration in Online Gradient Learning
---

# Dynamic Momentum Recalibration in Online Gradient Learning
**arXiv**：[2603.06120v1](https://arxiv.org/abs/2603.06120) · [PDF](https://arxiv.org/pdf/2603.06120.pdf)  
**作者**：Zhipeng Yao, Rui Yu, Guisong Chang, Ying Li, Yu Zhang, Dazhou Li  

**一句话要点**：提出SGDF优化器，通过在线时变增益动态调整梯度估计，以解决固定动量系数导致的偏差-方差失衡问题。

**关键词**：梯度优化, 动量方法, 在线学习, 信号处理, 深度学习优化

## 3 点简述
- 核心问题：固定动量系数在SGD及其变体中扭曲偏差与方差平衡，导致参数更新次优。
- 方法要点：基于最优线性滤波原理，SGDF计算在线时变增益，最小化均方误差以优化梯度估计。
- 实验或效果：在多种架构和基准测试中，SGDF超越传统动量方法，性能媲美或优于先进优化器。

## 摘要（原文）

> Stochastic Gradient Descent (SGD) and its momentum variants form the backbone of deep learning optimization, yet the underlying dynamics of their gradient behavior remain insufficiently understood. In this work, we reinterpret gradient updates through the lens of signal processing and reveal that fixed momentum coefficients inherently distort the balance between bias and variance, leading to skewed or suboptimal parameter updates. To address this, we propose SGDF (SGD with Filter), an optimizer inspired by the principles of Optimal Linear Filtering. SGDF computes an online, time-varying gain to dynamically refine gradient estimation by minimizing the mean-squared error, thereby achieving an optimal trade-off between noise suppression and signal preservation. Furthermore, our approach could extend to other optimizers, showcasing its broad applicability to optimization frameworks. Extensive experiments across diverse architectures and benchmarks demonstrate SGDF surpasses conventional momentum methods and achieves performance on par with or surpassing state-of-the-art optimizers.


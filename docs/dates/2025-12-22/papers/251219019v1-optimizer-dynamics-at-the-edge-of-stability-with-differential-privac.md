---
layout: default
title: Optimizer Dynamics at the Edge of Stability with Differential Privacy
---

# Optimizer Dynamics at the Edge of Stability with Differential Privacy
**arXiv**：[2512.19019v1](https://arxiv.org/abs/2512.19019) · [PDF](https://arxiv.org/pdf/2512.19019.pdf)  
**作者**：Ayana Hussain, Ricky Fang  

**一句话要点**：分析差分隐私下神经网络优化器的稳定性动态，揭示其在边缘稳定性区域的持续模式。

**关键词**：差分隐私, 优化器动态, 边缘稳定性, 神经网络训练, 梯度裁剪, 高斯噪声

## 3 点简述
- 核心问题：差分隐私通过梯度裁剪和高斯噪声改变优化动态，是否影响稳定性模式。
- 方法要点：比较梯度下降和Adam及其隐私保护变体，分析裁剪和噪声对锐度和损失演化的影响。
- 实验或效果：DP通常降低锐度，但边缘稳定性模式在最大学习率和隐私预算下仍存在或超过阈值。

## 摘要（原文）

> Deep learning models can reveal sensitive information about individual training examples, and while differential privacy (DP) provides guarantees restricting such leakage, it also alters optimization dynamics in poorly understood ways. We study the training dynamics of neural networks under DP by comparing Gradient Descent (GD), and Adam to their privacy-preserving variants. Prior work shows that these optimizers exhibit distinct stability dynamics: full-batch methods train at the Edge of Stability (EoS), while mini-batch and adaptive methods exhibit analogous edge-of-stability behavior. At these regimes, the training loss and the sharpness--the maximum eigenvalue of the training loss Hessian--exhibit certain characteristic behavior. In DP training, per-example gradient clipping and Gaussian noise modify the update rule, and it is unclear whether these stability patterns persist. We analyze how clipping and noise change sharpness and loss evolution and show that while DP generally reduces the sharpness and can prevent optimizers from fully reaching the classical stability thresholds, patterns from EoS and analogous adaptive methods stability regimes persist, with the largest learning rates and largest privacy budgets approaching, and sometimes exceeding, these thresholds. These findings highlight the unpredictability introduced by DP in neural network optimization.


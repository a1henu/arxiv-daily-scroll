---
layout: default
title: Gradient Regularized Natural Gradients
---

# Gradient Regularized Natural Gradients
**arXiv**：[2601.18420v1](https://arxiv.org/abs/2601.18420) · [PDF](https://arxiv.org/pdf/2601.18420.pdf)  
**作者**：Satya Prakash Dash, Hossein Abdi, Wei Pan, Samuel Kaski, Mingfei Sun  

**一句话要点**：提出梯度正则化自然梯度方法以提升大规模深度学习优化与泛化性能

**关键词**：梯度正则化, 自然梯度下降, 二阶优化, 深度学习优化, 泛化性能, 大规模训练

## 3 点简述
- 核心问题：二阶优化器训练动态如何从梯度正则化中受益，以加速优化并增强泛化
- 方法要点：结合梯度正则化与自然梯度更新，提供免Fisher信息矩阵显式求逆的频域和贝叶斯算法
- 实验或效果：在视觉和语言基准上优于一阶和二阶基线，提升优化速度和泛化能力

## 摘要（原文）

> Gradient regularization (GR) has been shown to improve the generalizability of trained models. While Natural Gradient Descent has been shown to accelerate optimization in the initial phase of training, little attention has been paid to how the training dynamics of second-order optimizers can benefit from GR. In this work, we propose Gradient-Regularized Natural Gradients (GRNG), a family of scalable second-order optimizers that integrate explicit gradient regularization with natural gradient updates. Our framework provides two complementary algorithms: a frequentist variant that avoids explicit inversion of the Fisher Information Matrix (FIM) via structured approximations, and a Bayesian variant based on a Regularized-Kalman formulation that eliminates the need for FIM inversion entirely. We establish convergence guarantees for GRNG, showing that gradient regularization improves stability and enables convergence to global minima. Empirically, we demonstrate that GRNG consistently enhances both optimization speed and generalization compared to first-order methods (SGD, AdamW) and second-order baselines (K-FAC, Sophia), with strong results on vision and language benchmarks. Our findings highlight gradient regularization as a principled and practical tool to unlock the robustness of natural gradient methods for large-scale deep learning.


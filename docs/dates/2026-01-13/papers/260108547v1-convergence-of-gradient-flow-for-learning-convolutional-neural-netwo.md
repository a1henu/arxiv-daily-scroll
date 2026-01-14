---
layout: default
title: Convergence of gradient flow for learning convolutional neural networks
---

# Convergence of gradient flow for learning convolutional neural networks
**arXiv**：[2601.08547v1](https://arxiv.org/abs/2601.08547) · [PDF](https://arxiv.org/pdf/2601.08547.pdf)  
**作者**：Jona-Maria Diederen, Holger Rauhut, Ulrich Terstiege  

**一句话要点**：证明线性卷积网络在梯度流下对平方损失等函数收敛到临界点

**关键词**：卷积神经网络, 梯度流, 优化收敛, 线性网络, 非凸优化, 训练数据条件

## 3 点简述
- 研究卷积神经网络训练中的非凸优化收敛问题
- 分析线性卷积网络在梯度流下的收敛性，作为梯度下降的抽象
- 在训练数据满足温和条件下，证明梯度流总收敛到临界点

## 摘要（原文）

> Convolutional neural networks are widely used in imaging and image recognition. Learning such networks from training data leads to the minimization of a non-convex function. This makes the analysis of standard optimization methods such as variants of (stochastic) gradient descent challenging. In this article we study the simplified setting of linear convolutional networks. We show that the gradient flow (to be interpreted as an abstraction of gradient descent) applied to the empirical risk defined via certain loss functions including the square loss always converges to a critical point, under a mild condition on the training data.


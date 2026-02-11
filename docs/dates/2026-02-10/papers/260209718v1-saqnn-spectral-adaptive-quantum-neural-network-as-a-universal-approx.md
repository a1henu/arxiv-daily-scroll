---
layout: default
title: SAQNN: Spectral Adaptive Quantum Neural Network as a Universal Approximator
---

# SAQNN: Spectral Adaptive Quantum Neural Network as a Universal Approximator
**arXiv**：[2602.09718v1](https://arxiv.org/abs/2602.09718) · [PDF](https://arxiv.org/pdf/2602.09718.pdf)  
**作者**：Jialiang Tang, Jialin Zhang, Xiaoming Sun  

**一句话要点**：提出谱自适应量子神经网络作为通用逼近器，以解决量子神经网络表达能力理论不完整的问题。

**关键词**：量子机器学习, 量子神经网络, 通用逼近性质, 谱自适应, 数值逼近, 参数复杂度

## 3 点简述
- 核心问题：量子神经网络表达能力理论不完整，限制量子机器学习发展。
- 方法要点：构建性模型支持切换函数基，适应数值逼近和机器学习场景。
- 实验或效果：在电路尺寸上优于经典前馈神经网络，逼近Sobolev函数时参数复杂度最优。

## 摘要（原文）

> Quantum machine learning (QML), as an interdisciplinary field bridging quantum computing and machine learning, has garnered significant attention in recent years. Currently, the field as a whole faces challenges due to incomplete theoretical foundations for the expressivity of quantum neural networks (QNNs). In this paper we propose a constructive QNN model and demonstrate that it possesses the universal approximation property (UAP), which means it can approximate any square-integrable function up to arbitrary accuracy. Furthermore, it supports switching function bases, thus adaptable to various scenarios in numerical approximation and machine learning. Our model has asymptotic advantages over the best classical feed-forward neural networks in terms of circuit size and achieves optimal parameter complexity when approximating Sobolev functions under $L_2$ norm.


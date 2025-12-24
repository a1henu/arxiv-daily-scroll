---
layout: default
title: Saddle-to-Saddle Dynamics Explains A Simplicity Bias Across Neural Network Architectures
---

# Saddle-to-Saddle Dynamics Explains A Simplicity Bias Across Neural Network Architectures
**arXiv**：[2512.20607v1](https://arxiv.org/abs/2512.20607) · [PDF](https://arxiv.org/pdf/2512.20607.pdf)  
**作者**：Yedi Zhang, Andrew Saxe, Peter E. Latham  

**一句话要点**：提出鞍点到鞍点动力学框架，解释神经网络梯度下降中的简单性偏置现象

**关键词**：简单性偏置, 鞍点动力学, 梯度下降, 神经网络架构, 不变流形, 学习复杂度

## 3 点简述
- 核心问题：神经网络训练中梯度下降为何普遍学习复杂度递增的解，缺乏统一理论解释
- 方法要点：分析鞍点、不变流形和梯度下降动力学，揭示鞍点到鞍点学习机制
- 实验或效果：理论框架适用于全连接、卷积和注意力网络，阐明数据分布和初始化对学习平台的影响

## 摘要（原文）

> Neural networks trained with gradient descent often learn solutions of increasing complexity over time, a phenomenon known as simplicity bias. Despite being widely observed across architectures, existing theoretical treatments lack a unifying framework. We present a theoretical framework that explains a simplicity bias arising from saddle-to-saddle learning dynamics for a general class of neural networks, incorporating fully-connected, convolutional, and attention-based architectures. Here, simple means expressible with few hidden units, i.e., hidden neurons, convolutional kernels, or attention heads. Specifically, we show that linear networks learn solutions of increasing rank, ReLU networks learn solutions with an increasing number of kinks, convolutional networks learn solutions with an increasing number of convolutional kernels, and self-attention models learn solutions with an increasing number of attention heads. By analyzing fixed points, invariant manifolds, and dynamics of gradient descent learning, we show that saddle-to-saddle dynamics operates by iteratively evolving near an invariant manifold, approaching a saddle, and switching to another invariant manifold. Our analysis also illuminates the effects of data distribution and weight initialization on the duration and number of plateaus in learning, dissociating previously confounding factors. Overall, our theory offers a framework for understanding when and why gradient descent progressively learns increasingly complex solutions.


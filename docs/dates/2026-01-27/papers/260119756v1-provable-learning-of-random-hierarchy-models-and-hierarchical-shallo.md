---
layout: default
title: Provable Learning of Random Hierarchy Models and Hierarchical Shallow-to-Deep Chaining
---

# Provable Learning of Random Hierarchy Models and Hierarchical Shallow-to-Deep Chaining
**arXiv**：[2601.19756v1](https://arxiv.org/abs/2601.19756) · [PDF](https://arxiv.org/pdf/2601.19756.pdf)  
**作者**：Yunwei Ren, Yatin Dandi, Florent Krzakala, Jason D. Lee  

**一句话要点**：提出基于层间信号传递的深度卷积网络训练方法，以高效学习随机层次模型。

**关键词**：深度网络理论, 层次学习, 随机层次模型, 卷积网络, 梯度训练, 层间训练

## 3 点简述
- 核心问题：深度网络能否通过梯度方法高效利用数据层次结构？
- 方法要点：在中间层接收清晰标签信号和特征弱可识别条件下，逐层训练可学习目标函数。
- 实验或效果：证明深度卷积网络在温和条件下能高效学习随机层次模型。

## 摘要（原文）

> The empirical success of deep learning is often attributed to deep networks' ability to exploit hierarchical structure in data, constructing increasingly complex features across layers. Yet despite substantial progress in deep learning theory, most optimization results sill focus on networks with only two or three layers, leaving the theoretical understanding of hierarchical learning in genuinely deep models limited. This leads to a natural question: can we prove that deep networks, trained by gradient-based methods, can efficiently exploit hierarchical structure?
>   In this work, we consider Random Hierarchy Models -- a hierarchical context-free grammar introduced by arXiv:2307.02129 and conjectured to separate deep and shallow networks. We prove that, under mild conditions, a deep convolutional network can be efficiently trained to learn this function class. Our proof builds on a general observation: if intermediate layers can receive clean signal from the labels and the relevant features are weakly identifiable, then layerwise training each individual layer suffices to hierarchically learn the target function.


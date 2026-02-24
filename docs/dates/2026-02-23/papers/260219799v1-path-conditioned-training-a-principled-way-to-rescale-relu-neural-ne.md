---
layout: default
title: Path-conditioned training: a principled way to rescale ReLU neural networks
---

# Path-conditioned training: a principled way to rescale ReLU neural networks
**arXiv**：[2602.19799v1](https://arxiv.org/abs/2602.19799) · [PDF](https://arxiv.org/pdf/2602.19799.pdf)  
**作者**：Arthur Lebeurrier, Titouan Vayer, Rémi Gribonval  

**一句话要点**：提出路径条件训练方法，以利用ReLU网络缩放对称性加速训练

**关键词**：ReLU神经网络, 参数缩放, 训练加速, 路径提升框架, 几何优化

## 3 点简述
- 核心问题：ReLU网络参数缩放对称性未在训练中被有效利用，导致动态差异
- 方法要点：基于路径提升框架，引入几何准则对齐核与参考，实现参数重缩放
- 实验或效果：数值实验显示该方法能加速训练，分析架构和初始化尺度影响

## 摘要（原文）

> Despite recent algorithmic advances, we still lack principled ways to leverage the well-documented rescaling symmetries in ReLU neural network parameters. While two properly rescaled weights implement the same function, the training dynamics can be dramatically different. To offer a fresh perspective on exploiting this phenomenon, we build on the recent path-lifting framework, which provides a compact factorization of ReLU networks. We introduce a geometrically motivated criterion to rescale neural network parameters which minimization leads to a conditioning strategy that aligns a kernel in the path-lifting space with a chosen reference. We derive an efficient algorithm to perform this alignment. In the context of random network initialization, we analyze how the architecture and the initialization scale jointly impact the output of the proposed method. Numerical experiments illustrate its potential to speed up training.


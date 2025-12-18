---
layout: default
title: SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs
---

# SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs
**arXiv**：[2512.15088v1](https://arxiv.org/abs/2512.15088) · [PDF](https://arxiv.org/pdf/2512.15088.pdf)  
**作者**：Xianglin Wu, Chiheb Ben Hammouda, Cornelis W. Oosterlee  

**一句话要点**：提出SigMA架构，结合路径签名与多头注意力，用于估计分数布朗运动驱动的随机微分方程参数。

**关键词**：分数布朗运动, 随机微分方程, 路径签名, 多头注意力, 参数估计, 深度学习

## 3 点简述
- 核心问题：分数布朗运动驱动的SDEs参数估计困难，传统方法因非马尔可夫性和计算复杂性受限。
- 方法要点：集成路径签名作为特征映射，通过卷积预处理、多头自注意力和多层感知机进行编码学习。
- 实验或效果：在合成和真实数据上优于CNN、LSTM等基线，在准确性、鲁棒性和模型紧凑性方面表现突出。

## 摘要（原文）

> Stochastic differential equations (SDEs) driven by fractional Brownian motion (fBm) are increasingly used to model systems with rough dynamics and long-range dependence, such as those arising in quantitative finance and reliability engineering. However, these processes are non-Markovian and lack a semimartingale structure, rendering many classical parameter estimation techniques inapplicable or computationally intractable beyond very specific cases. This work investigates two central questions: (i) whether integrating path signatures into deep learning architectures can improve the trade-off between estimation accuracy and model complexity, and (ii) what constitutes an effective architecture for leveraging signatures as feature maps. We introduce SigMA (Signature Multi-head Attention), a neural architecture that integrates path signatures with multi-head self-attention, supported by a convolutional preprocessing layer and a multilayer perceptron for effective feature encoding. SigMA learns model parameters from synthetically generated paths of fBm-driven SDEs, including fractional Brownian motion, fractional Ornstein-Uhlenbeck, and rough Heston models, with a particular focus on estimating the Hurst parameter and on joint multi-parameter inference, and it generalizes robustly to unseen trajectories. Extensive experiments on synthetic data and two real-world datasets (i.e., equity-index realized volatility and Li-ion battery degradation) show that SigMA consistently outperforms CNN, LSTM, vanilla Transformer, and Deep Signature baselines in accuracy, robustness, and model compactness. These results demonstrate that combining signature transforms with attention-based architectures provides an effective and scalable framework for parameter inference in stochastic systems with rough or persistent temporal structure.


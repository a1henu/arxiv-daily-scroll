---
layout: default
title: Provable FDR Control for Deep Feature Selection: Deep MLPs and Beyond
---

# Provable FDR Control for Deep Feature Selection: Deep MLPs and Beyond
**arXiv**：[2512.04696v1](https://arxiv.org/abs/2512.04696) · [PDF](https://arxiv.org/pdf/2512.04696.pdf)  
**作者**：Kazuma Sawaya  

**一句话要点**：提出基于深度神经网络的灵活特征选择框架，在广义深度学习设置中近似控制假发现率。

**关键词**：假发现率控制, 深度特征选择, 神经网络理论, 渐近分析, 多索引模型

## 3 点简述
- 核心问题：在深度学习中实现特征选择的理论假发现率控制，以衡量第一类错误。
- 方法要点：适用于首层全连接的网络，支持多种架构和训练过程，基于多索引数据生成模型和渐近分析。
- 实验或效果：数值实验验证理论发现，但假设设计矩阵的右正交不变性，讨论更广泛推广。

## 摘要（原文）

> We develop a flexible feature selection framework based on deep neural networks that approximately controls the false discovery rate (FDR), a measure of Type-I error. The method applies to architectures whose first layer is fully connected. From the second layer onward, it accommodates multilayer perceptrons (MLPs) of arbitrary width and depth, convolutional and recurrent networks, attention mechanisms, residual connections, and dropout. The procedure also accommodates stochastic gradient descent with data-independent initializations and learning rates. To the best of our knowledge, this is the first work to provide a theoretical guarantee of FDR control for feature selection within such a general deep learning setting.
>   Our analysis is built upon a multi-index data-generating model and an asymptotic regime in which the feature dimension $n$ diverges faster than the latent dimension $q^{*}$, while the sample size, the number of training iterations, the network depth, and hidden layer widths are left unrestricted. Under this setting, we show that each coordinate of the gradient-based feature-importance vector admits a marginal normal approximation, thereby supporting the validity of asymptotic FDR control. As a theoretical limitation, we assume $\mathbf{B}$-right orthogonal invariance of the design matrix, and we discuss broader generalizations. We also present numerical experiments that underscore the theoretical findings.


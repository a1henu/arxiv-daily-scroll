---
layout: default
title: How Controlling the Variance can Improve Training Stability of Sparsely Activated DNNs and CNNs
---

# How Controlling the Variance can Improve Training Stability of Sparsely Activated DNNs and CNNs
**arXiv**：[2602.05779v1](https://arxiv.org/abs/2602.05779) · [PDF](https://arxiv.org/pdf/2602.05779.pdf)  
**作者**：Emily Dent, Jared Tanner  

**一句话要点**：通过控制高斯过程方差提升稀疏激活深度网络训练稳定性

**关键词**：稀疏激活, 训练稳定性, 高斯过程, Edge-of-Chaos初始化, 能耗优化, 深度神经网络

## 3 点简述
- 核心问题：稀疏激活深度网络训练不稳定，影响表达能力和能耗优化
- 方法要点：利用高斯过程方差控制，结合Edge-of-Chaos初始化策略
- 实验或效果：在DNN和CNN中实现高达90%激活稀疏性，保持高精度

## 摘要（原文）

> The intermediate layers of deep networks can be characterised as a Gaussian process, in particular the Edge-of-Chaos (EoC) initialisation strategy prescribes the limiting covariance matrix of the Gaussian process. Here we show that the under-utilised chosen variance of the Gaussian process is important in the training of deep networks with sparsity inducing activation, such as a shifted and clipped ReLU, $\text{CReLU}_{τ,m}(x)=\min(\max(x-τ,0),m)$. Specifically, initialisations leading to larger fixed Gaussian process variances, allow for improved expressivity with activation sparsity as large as 90% in DNNs and CNNs, and generally improve the stability of the training process. Enabling full, or near full, accuracy at such high levels of sparsity in the hidden layers suggests a promising mechanism to reduce the energy consumption of machine learning models involving fully connected layers.


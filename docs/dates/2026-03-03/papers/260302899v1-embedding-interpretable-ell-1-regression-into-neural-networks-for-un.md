---
layout: default
title: Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging
---

# Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging
**arXiv**：[2603.02899v1](https://arxiv.org/abs/2603.02899) · [PDF](https://arxiv.org/pdf/2603.02899.pdf)  
**作者**：Fabian Kabus, Maren Hackenberg, Julia Hindel, Thibault Cholvin, Antje Kilias, Thomas Brox, Abhinav Valada, Marlene Bartos, Harald Binder  

**一句话要点**：提出嵌入可解释ℓ₁回归的卷积自编码器，以从细胞成像数据中提取稀疏时间结构

**关键词**：可解释机器学习, 稀疏回归, 卷积自编码器, 细胞成像分析, 时间序列建模, ℓ₁正则化

## 3 点简述
- 核心问题：神经网络在无监督学习中难以提供可解释的稀疏时间结构，而传统统计回归方法在可解释性上更优。
- 方法要点：将向量自回归模型嵌入卷积自编码器，通过ℓ₁正则化实现稀疏性，并利用跳跃连接处理非稀疏空间信息。
- 实验或效果：应用于双光子钙成像数据，提取稀疏自回归动态，并提供贡献图可视化空间区域对动态的驱动作用。

## 摘要（原文）

> While artificial neural networks excel in unsupervised learning of non-sparse structure, classical statistical regression techniques offer better interpretability, in particular when sparseness is enforced by $\ell_1$ regularization, enabling identification of which factors drive observed dynamics. We investigate how these two types of approaches can be optimally combined, exemplarily considering two-photon calcium imaging data where sparse autoregressive dynamics are to be extracted. We propose embedding a vector autoregressive (VAR) model as an interpretable regression technique into a convolutional autoencoder, which provides dimension reduction for tractable temporal modeling. A skip connection separately addresses non-sparse static spatial information, selectively channeling sparse structure into the $\ell_1$-regularized VAR. $\ell_1$-estimation of regression parameters is enabled by differentiating through the piecewise linear solution path. This is contrasted with approaches where the autoencoder does not adapt to the VAR model. Having an embedded statistical model also enables a testing approach for comparing temporal sequences from the same observational unit. Additionally, contribution maps visualize which spatial regions drive the learned dynamics.


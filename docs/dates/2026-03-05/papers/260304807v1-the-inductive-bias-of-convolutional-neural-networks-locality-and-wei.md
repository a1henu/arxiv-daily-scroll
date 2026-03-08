---
layout: default
title: The Inductive Bias of Convolutional Neural Networks: Locality and Weight Sharing Reshape Implicit Regularization
---

# The Inductive Bias of Convolutional Neural Networks: Locality and Weight Sharing Reshape Implicit Regularization
**arXiv**：[2603.04807v1](https://arxiv.org/abs/2603.04807) · [PDF](https://arxiv.org/pdf/2603.04807.pdf)  
**作者**：Tongtong Liang, Esha Singh, Rahul Parhi, Alexander Cloninger, Yu-Xiang Wang  

**一句话要点**：证明卷积网络的局部性与权重共享通过稳定机制提升球面数据泛化能力

**关键词**：卷积神经网络, 隐式正则化, 泛化理论, 权重共享, 局部性, 球面数据

## 3 点简述
- 研究架构归纳偏置如何重塑梯度下降边缘稳定性中的隐式正则化
- 证明卷积网络在接收域较小时能泛化球面数据，而全连接网络失败
- 分析自然图像块几何，解释卷积网络优于全连接基线的泛化原因

## 摘要（原文）

> We study how architectural inductive bias reshapes the implicit regularization induced by the edge-of-stability phenomenon in gradient descent. Prior work has established that for fully connected networks, the strength of this regularization is governed solely by the global input geometry; consequently, it is insufficient to prevent overfitting on difficult distributions such as the high-dimensional sphere. In this paper, we show that locality and weight sharing fundamentally change this picture. Specifically, we prove that provided the receptive field size $m$ remains small relative to the ambient dimension $d$, these networks generalize on spherical data with a rate of $n^{-\frac{1}{6} +O(m/d)}$, a regime where fully connected networks provably fail. This theoretical result confirms that weight sharing couples the learned filters to the low-dimensional patch manifold, thereby bypassing the high dimensionality of the ambient space. We further corroborate our theory by analyzing the patch geometry of natural images, showing that standard convolutional designs induce patch distributions that are highly amenable to this stability mechanism, thus providing a systematic explanation for the superior generalization of convolutional networks over fully connected baselines.


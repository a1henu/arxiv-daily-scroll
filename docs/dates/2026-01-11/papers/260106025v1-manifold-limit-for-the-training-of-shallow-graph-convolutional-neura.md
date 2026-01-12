---
layout: default
title: Manifold limit for the training of shallow graph convolutional neural networks
---

# Manifold limit for the training of shallow graph convolutional neural networks
**arXiv**：[2601.06025v1](https://arxiv.org/abs/2601.06025) · [PDF](https://arxiv.org/pdf/2601.06025.pdf)  
**作者**：Johanna Tengler, Christoph Brune, José A. Iglesias  

**一句话要点**：证明浅层图卷积神经网络在流形假设下训练的一致性与收敛性

**关键词**：图卷积神经网络, 流形学习, 离散到连续收敛, Γ收敛, 谱图理论, 参数空间正则化

## 3 点简述
- 研究浅层GCNNs在采样点云邻近图上的离散到连续一致性，基于流形假设
- 采用谱图卷积和函数分析视角，定义跨图分辨率一致的训练数据
- 证明正则化经验风险最小化泛函的Γ收敛和全局最小化器的收敛

## 摘要（原文）

> We study the discrete-to-continuum consistency of the training of shallow graph convolutional neural networks (GCNNs) on proximity graphs of sampled point clouds under a manifold assumption. Graph convolution is defined spectrally via the graph Laplacian, whose low-frequency spectrum approximates that of the Laplace-Beltrami operator of the underlying smooth manifold, and shallow GCNNs of possibly infinite width are linear functionals on the space of measures on the parameter space. From this functional-analytic perspective, graph signals are seen as spatial discretizations of functions on the manifold, which leads to a natural notion of training data consistent across graph resolutions. To enable convergence results, the continuum parameter space is chosen as a weakly compact product of unit balls, with Sobolev regularity imposed on the output weight and bias, but not on the convolutional parameter. The corresponding discrete parameter spaces inherit the corresponding spectral decay, and are additionally restricted by a frequency cutoff adapted to the informative spectral window of the graph Laplacians. Under these assumptions, we prove $Γ$-convergence of regularized empirical risk minimization functionals and corresponding convergence of their global minimizers, in the sense of weak convergence of the parameter measures and uniform convergence of the functions over compact sets. This provides a formalization of mesh and sample independence for the training of such networks.


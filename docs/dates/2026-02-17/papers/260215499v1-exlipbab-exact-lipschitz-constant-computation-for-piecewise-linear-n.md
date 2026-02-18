---
layout: default
title: ExLipBaB: Exact Lipschitz Constant Computation for Piecewise Linear Neural Networks
---

# ExLipBaB: Exact Lipschitz Constant Computation for Piecewise Linear Neural Networks
**arXiv**：[2602.15499v1](https://arxiv.org/abs/2602.15499) · [PDF](https://arxiv.org/pdf/2602.15499.pdf)  
**作者**：Tom A. Splittgerber  

**一句话要点**：提出ExLipBaB算法以精确计算任意分段线性神经网络的Lipschitz常数

**关键词**：Lipschitz常数计算, 分段线性神经网络, 精确算法, 鲁棒性保证, p-范数

## 3 点简述
- 核心问题：现有精确算法仅适用于ReLU网络，限制了在Lipschitz约束网络中的应用
- 方法要点：扩展LipBaB算法，支持任意分段线性激活函数和p-范数
- 实验或效果：未知，但旨在为小模型或敏感数据提供精确鲁棒性保证

## 摘要（原文）

> It has been shown that a neural network's Lipschitz constant can be leveraged to derive robustness guarantees, to improve generalizability via regularization or even to construct invertible networks. Therefore, a number of methods varying in the tightness of their bounds and their computational cost have been developed to approximate the Lipschitz constant for different classes of networks. However, comparatively little research exists on methods for exact computation, which has been shown to be NP-hard. Nonetheless, there are applications where one might readily accept the computational cost of an exact method. These applications could include the benchmarking of new methods or the computation of robustness guarantees for small models on sensitive data. Unfortunately, existing exact algorithms restrict themselves to only ReLU-activated networks, which are known to come with severe downsides in the context of Lipschitz-constrained networks. We therefore propose a generalization of the LipBaB algorithm to compute exact Lipschitz constants for arbitrary piecewise linear neural networks and $p$-norms. With our method, networks may contain traditional activations like ReLU or LeakyReLU, activations like GroupSort or the related MinMax and FullSort, which have been of increasing interest in the context of Lipschitz constrained networks, or even other piecewise linear functions like MaxPool.


---
layout: default
title: Generalization Bounds of Stochastic Gradient Descent in Homogeneous Neural Networks
---

# Generalization Bounds of Stochastic Gradient Descent in Homogeneous Neural Networks
**arXiv**：[2602.22936v1](https://arxiv.org/abs/2602.22936) · [PDF](https://arxiv.org/pdf/2602.22936.pdf)  
**作者**：Wenquan Ma, Yang Sui, Jiaye Teng, Bohan Wang, Jing Xu, Jingqin Yang  

**一句话要点**：在齐次神经网络中证明SGD泛化界，允许更慢步长衰减以提升优化效率

**关键词**：泛化界, 随机梯度下降, 齐次神经网络, 算法稳定性, 步长衰减, 非凸优化

## 3 点简述
- 核心问题：传统算法稳定性分析需步长快速衰减，可能阻碍优化且不实用
- 方法要点：在齐次神经网络下推导泛化界，允许步长以Ω(1/√t)衰减，扩展至非Lipschitz场景
- 实验或效果：理论结果广泛适用，涵盖全连接和卷积网络，如ReLU和LeakyReLU激活

## 摘要（原文）

> Algorithmic stability is among the most potent techniques in generalization analysis. However, its derivation usually requires a stepsize $η_t = \mathcal{O}(1/t)$ under non-convex training regimes, where $t$ denotes iterations. This rigid decay of the stepsize potentially impedes optimization and may not align with practical scenarios. In this paper, we derive the generalization bounds under the homogeneous neural network regimes, proving that this regime enables slower stepsize decay of order $Ω(1/\sqrt{t})$ under mild assumptions. We further extend the theoretical results from several aspects, e.g., non-Lipschitz regimes. This finding is broadly applicable, as homogeneous neural networks encompass fully-connected and convolutional neural networks with ReLU and LeakyReLU activations.


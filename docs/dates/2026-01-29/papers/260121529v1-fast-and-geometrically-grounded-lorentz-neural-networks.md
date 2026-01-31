---
layout: default
title: Fast and Geometrically Grounded Lorentz Neural Networks
---

# Fast and Geometrically Grounded Lorentz Neural Networks
**arXiv**：[2601.21529v1](https://arxiv.org/abs/2601.21529) · [PDF](https://arxiv.org/pdf/2601.21529.pdf)  
**作者**：Robert van der Klis, Ricardo Chávez Torres, Max van Spengler, Yuhui Ding, Thomas Hofmann, Pascal Mettes  

**一句话要点**：提出基于距离到超平面公式的Lorentz线性层，以解决输出范数对数缩放问题，提升双曲神经网络效率与几何一致性。

**关键词**：双曲神经网络, Lorentz模型, 几何深度学习, 高效计算, 表示学习

## 3 点简述
- 核心问题：现有Lorentz线性层导致输出双曲范数随梯度步数对数缩放，削弱双曲几何优势。
- 方法要点：引入新Lorentz线性层，基于距离到超平面公式，实现输出范数线性缩放，并优化激活函数与缓存策略。
- 实验或效果：新方法保持双曲几何性质，同时计算效率接近欧几里得神经网络，代码已开源。

## 摘要（原文）

> Hyperbolic space is quickly gaining traction as a promising geometry for hierarchical and robust representation learning. A core open challenge is the development of a mathematical formulation of hyperbolic neural networks that is both efficient and captures the key properties of hyperbolic space. The Lorentz model of hyperbolic space has been shown to enable both fast forward and backward propagation. However, we prove that, with the current formulation of Lorentz linear layers, the hyperbolic norms of the outputs scale logarithmically with the number of gradient descent steps, nullifying the key advantage of hyperbolic geometry. We propose a new Lorentz linear layer grounded in the well-known ``distance-to-hyperplane" formulation. We prove that our formulation results in the usual linear scaling of output hyperbolic norms with respect to the number of gradient descent steps. Our new formulation, together with further algorithmic efficiencies through Lorentzian activation functions and a new caching strategy results in neural networks fully abiding by hyperbolic geometry while simultaneously bridging the computation gap to Euclidean neural networks. Code available at: https://github.com/robertdvdk/hyperbolic-fully-connected.


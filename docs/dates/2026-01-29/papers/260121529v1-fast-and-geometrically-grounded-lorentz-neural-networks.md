---
layout: default
title: Fast and Geometrically Grounded Lorentz Neural Networks
---

# Fast and Geometrically Grounded Lorentz Neural Networks
**arXiv**：[2601.21529v1](https://arxiv.org/abs/2601.21529) · [PDF](https://arxiv.org/pdf/2601.21529.pdf)  
**作者**：Robert van der Klis, Ricardo Chávez Torres, Max van Spengler, Yuhui Ding, Thomas Hofmann, Pascal Mettes  

**一句话要点**：提出基于距离到超平面的Lorentz线性层，解决双曲神经网络输出范数缩放问题，提升计算效率。

**关键词**：双曲神经网络, Lorentz模型, 几何深度学习, 计算效率, 表示学习

## 3 点简述
- 现有Lorentz线性层导致输出双曲范数随梯度步数对数缩放，削弱双曲几何优势。
- 新层基于距离到超平面公式，实现输出范数与梯度步数的线性缩放，保持几何特性。
- 结合Lorentzian激活函数和缓存策略，提升计算效率，代码已开源。

## 摘要（原文）

> Hyperbolic space is quickly gaining traction as a promising geometry for hierarchical and robust representation learning. A core open challenge is the development of a mathematical formulation of hyperbolic neural networks that is both efficient and captures the key properties of hyperbolic space. The Lorentz model of hyperbolic space has been shown to enable both fast forward and backward propagation. However, we prove that, with the current formulation of Lorentz linear layers, the hyperbolic norms of the outputs scale logarithmically with the number of gradient descent steps, nullifying the key advantage of hyperbolic geometry. We propose a new Lorentz linear layer grounded in the well-known ``distance-to-hyperplane" formulation. We prove that our formulation results in the usual linear scaling of output hyperbolic norms with respect to the number of gradient descent steps. Our new formulation, together with further algorithmic efficiencies through Lorentzian activation functions and a new caching strategy results in neural networks fully abiding by hyperbolic geometry while simultaneously bridging the computation gap to Euclidean neural networks. Code available at: https://github.com/robertdvdk/hyperbolic-fully-connected.


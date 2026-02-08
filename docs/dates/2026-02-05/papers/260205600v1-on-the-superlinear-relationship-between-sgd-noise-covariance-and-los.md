---
layout: default
title: On the Superlinear Relationship between SGD Noise Covariance and Loss Landscape Curvature
---

# On the Superlinear Relationship between SGD Noise Covariance and Loss Landscape Curvature
**arXiv**：[2602.05600v1](https://arxiv.org/abs/2602.05600) · [PDF](https://arxiv.org/pdf/2602.05600.pdf)  
**作者**：Yikuan Zhang, Ning Yang, Yuhai Tu  

**一句话要点**：揭示SGD噪声协方差与损失景观曲率间的超线性关系，基于活动-权重对偶性提供统一理论框架。

**关键词**：随机梯度下降, 噪声协方差, 损失景观曲率, 活动-权重对偶性, 深度神经网络优化, Hessian分析

## 3 点简述
- 核心问题：先前研究假设Fisher信息矩阵与Hessian等价，导致SGD噪声协方差与Hessian成比例，但该假设在深度神经网络中通常不成立。
- 方法要点：利用活动-权重对偶性，推导出更一般的关系，表明噪声协方差与每样本Hessian平方的期望成比例，且两者近似可交换。
- 实验或效果：通过跨数据集、架构和损失函数的实验验证理论边界，噪声协方差对角元素与Hessian对角元素呈近似幂律关系，指数在1到2之间。

## 摘要（原文）

> Stochastic Gradient Descent (SGD) introduces anisotropic noise that is correlated with the local curvature of the loss landscape, thereby biasing optimization toward flat minima. Prior work often assumes an equivalence between the Fisher Information Matrix and the Hessian for negative log-likelihood losses, leading to the claim that the SGD noise covariance $\mathbf{C}$ is proportional to the Hessian $\mathbf{H}$. We show that this assumption holds only under restrictive conditions that are typically violated in deep neural networks. Using the recently discovered Activity--Weight Duality, we find a more general relationship agnostic to the specific loss formulation, showing that $\mathbf{C} \propto \mathbb{E}_p[\mathbf{h}_p^2]$, where $\mathbf{h}_p$ denotes the per-sample Hessian with $\mathbf{H} = \mathbb{E}_p[\mathbf{h}_p]$. As a consequence, $\mathbf{C}$ and $\mathbf{H}$ commute approximately rather than coincide exactly, and their diagonal elements follow an approximate power-law relation $C_{ii} \propto H_{ii}^γ$ with a theoretically bounded exponent $1 \leq γ\leq 2$, determined by per-sample Hessian spectra. Experiments across datasets, architectures, and loss functions validate these bounds, providing a unified characterization of the noise-curvature relationship in deep learning.


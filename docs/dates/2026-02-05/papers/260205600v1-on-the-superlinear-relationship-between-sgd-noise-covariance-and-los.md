---
layout: default
title: On the Superlinear Relationship between SGD Noise Covariance and Loss Landscape Curvature
---

# On the Superlinear Relationship between SGD Noise Covariance and Loss Landscape Curvature
**arXiv**：[2602.05600v1](https://arxiv.org/abs/2602.05600) · [PDF](https://arxiv.org/pdf/2602.05600.pdf)  
**作者**：Yikuan Zhang, Ning Yang, Yuhai Tu  

**一句话要点**：揭示SGD噪声协方差与损失景观曲率间的超线性关系，挑战先验假设并统一深度学习噪声-曲率表征。

**关键词**：SGD噪声协方差, 损失景观曲率, Activity-Weight Duality, 深度学习优化, Hessian矩阵, 超线性关系

## 3 点简述
- 核心问题：先前工作假设Fisher信息矩阵与Hessian等价，导致SGD噪声协方差与Hessian成比例，但此假设在深度神经网络中常不成立。
- 方法要点：利用Activity-Weight Duality，发现更一般关系，噪声协方差与每样本Hessian平方的期望成比例，且与Hessian近似可交换。
- 实验或效果：通过多数据集、架构和损失函数实验验证理论边界，指数γ在1到2之间，提供统一噪声-曲率关系描述。

## 摘要（原文）

> Stochastic Gradient Descent (SGD) introduces anisotropic noise that is correlated with the local curvature of the loss landscape, thereby biasing optimization toward flat minima. Prior work often assumes an equivalence between the Fisher Information Matrix and the Hessian for negative log-likelihood losses, leading to the claim that the SGD noise covariance $\mathbf{C}$ is proportional to the Hessian $\mathbf{H}$. We show that this assumption holds only under restrictive conditions that are typically violated in deep neural networks. Using the recently discovered Activity--Weight Duality, we find a more general relationship agnostic to the specific loss formulation, showing that $\mathbf{C} \propto \mathbb{E}_p[\mathbf{h}_p^2]$, where $\mathbf{h}_p$ denotes the per-sample Hessian with $\mathbf{H} = \mathbb{E}_p[\mathbf{h}_p]$. As a consequence, $\mathbf{C}$ and $\mathbf{H}$ commute approximately rather than coincide exactly, and their diagonal elements follow an approximate power-law relation $C_{ii} \propto H_{ii}^γ$ with a theoretically bounded exponent $1 \leq γ\leq 2$, determined by per-sample Hessian spectra. Experiments across datasets, architectures, and loss functions validate these bounds, providing a unified characterization of the noise-curvature relationship in deep learning.


---
layout: default
title: Latent-Variable Learning of SPDEs via Wiener Chaos
---

# Latent-Variable Learning of SPDEs via Wiener Chaos
**arXiv**：[2602.11794v1](https://arxiv.org/abs/2602.11794) · [PDF](https://arxiv.org/pdf/2602.11794.pdf)  
**作者**：Sebastian Zeng, Andreas Petersson, Wolfgang Bock  

**一句话要点**：提出基于Wiener混沌展开的隐变量方法，从时空观测中学习线性SPDE的随机动力学。

**关键词**：随机偏微分方程学习, 隐变量模型, Wiener混沌展开, 谱Galerkin方法, 变分学习

## 3 点简述
- 核心问题：从时空观测学习线性SPDE的随机律，无需噪声或初始条件直接访问。
- 方法要点：结合谱Galerkin投影与截断Wiener混沌展开，将SPDE降维为参数化ODE系统。
- 实验或效果：在合成数据上验证，在可比建模假设下实现最先进性能。

## 摘要（原文）

> We study the problem of learning the law of linear stochastic partial differential equations (SPDEs) with additive Gaussian forcing from spatiotemporal observations. Most existing deep learning approaches either assume access to the driving noise or initial condition, or rely on deterministic surrogate models that fail to capture intrinsic stochasticity. We propose a structured latent-variable formulation that requires only observations of solution realizations and learns the underlying randomly forced dynamics. Our approach combines a spectral Galerkin projection with a truncated Wiener chaos expansion, yielding a principled separation between deterministic evolution and stochastic forcing. This reduces the infinite-dimensional SPDE to a finite system of parametrized ordinary differential equations governing latent temporal dynamics. The latent dynamics and stochastic forcing are jointly inferred through variational learning, allowing recovery of stochastic structure without explicit observation or simulation of noise during training. Empirical evaluation on synthetic data demonstrates state-of-the-art performance under comparable modeling assumptions across bounded and unbounded one-dimensional spatial domains.


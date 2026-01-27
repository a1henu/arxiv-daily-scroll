---
layout: default
title: Riemannian AmbientFlow: Towards Simultaneous Manifold Learning and Generative Modeling from Corrupted Data
---

# Riemannian AmbientFlow: Towards Simultaneous Manifold Learning and Generative Modeling from Corrupted Data
**arXiv**：[2601.18728v1](https://arxiv.org/abs/2601.18728) · [PDF](https://arxiv.org/pdf/2601.18728.pdf)  
**作者**：Willem Diepeveen, Oscar Leong  

**一句话要点**：提出Riemannian AmbientFlow框架，从噪声数据中同时学习生成模型和底层流形结构

**关键词**：生成建模, 流形学习, 噪声数据, 黎曼几何, 变分推断, 逆问题

## 3 点简述
- 核心问题：在科学和成像应用中，仅能获取噪声或线性损坏数据，且需提取数据中的流形几何结构
- 方法要点：基于AmbientFlow变分推断框架，结合归一化流诱导的数据驱动黎曼几何，通过拉回度量和黎曼自编码器提取流形
- 实验或效果：理论保证模型恢复数据分布和流形参数化，并在合成流形和MNIST上实证验证

## 摘要（原文）

> Modern generative modeling methods have demonstrated strong performance in learning complex data distributions from clean samples. In many scientific and imaging applications, however, clean samples are unavailable, and only noisy or linearly corrupted measurements can be observed. Moreover, latent structures, such as manifold geometries, present in the data are important to extract for further downstream scientific analysis. In this work, we introduce Riemannian AmbientFlow, a framework for simultaneously learning a probabilistic generative model and the underlying, nonlinear data manifold directly from corrupted observations. Building on the variational inference framework of AmbientFlow, our approach incorporates data-driven Riemannian geometry induced by normalizing flows, enabling the extraction of manifold structure through pullback metrics and Riemannian Autoencoders. We establish theoretical guarantees showing that, under appropriate geometric regularization and measurement conditions, the learned model recovers the underlying data distribution up to a controllable error and yields a smooth, bi-Lipschitz manifold parametrization. We further show that the resulting smooth decoder can serve as a principled generative prior for inverse problems with recovery guarantees. We empirically validate our approach on low-dimensional synthetic manifolds and on MNIST.


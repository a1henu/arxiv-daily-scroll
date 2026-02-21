---
layout: default
title: Synergizing Transport-Based Generative Models and Latent Geometry for Stochastic Closure Modeling
---

# Synergizing Transport-Based Generative Models and Latent Geometry for Stochastic Closure Modeling
**arXiv**：[2602.17089v1](https://arxiv.org/abs/2602.17089) · [PDF](https://arxiv.org/pdf/2602.17089.pdf)  
**作者**：Xinghao Dong, Huchen Yang, Jin-long Wu  

**一句话要点**：提出基于流匹配与潜在几何的随机闭合模型，以解决扩散模型采样速度慢的问题。

**关键词**：随机闭合模型, 流匹配, 潜在空间, 扩散模型, 几何正则化

## 3 点简述
- 核心问题：扩散模型采样速度慢，影响随机闭合模型的实际应用。
- 方法要点：在低维潜在空间使用流匹配实现单步采样，速度提升两个数量级。
- 实验或效果：通过正则化控制潜在空间失真，确保物理保真度，减少训练数据需求。

## 摘要（原文）

> Diffusion models recently developed for generative AI tasks can produce high-quality samples while still maintaining diversity among samples to promote mode coverage, providing a promising path for learning stochastic closure models. Compared to other types of generative AI models, such as GANs and VAEs, the sampling speed is known as a key disadvantage of diffusion models. By systematically comparing transport-based generative models on a numerical example of 2D Kolmogorov flows, we show that flow matching in a lower-dimensional latent space is suited for fast sampling of stochastic closure models, enabling single-step sampling that is up to two orders of magnitude faster than iterative diffusion-based approaches. To control the latent space distortion and thus ensure the physical fidelity of the sampled closure term, we compare the implicit regularization offered by a joint training scheme against two explicit regularizers: metric-preserving (MP) and geometry-aware (GA) constraints. Besides offering a faster sampling speed, both explicitly and implicitly regularized latent spaces inherit the key topological information from the lower-dimensional manifold of the original complex dynamical system, which enables the learning of stochastic closure models without demanding a huge amount of training data.


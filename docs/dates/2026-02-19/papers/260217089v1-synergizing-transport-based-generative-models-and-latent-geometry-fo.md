---
layout: default
title: Synergizing Transport-Based Generative Models and Latent Geometry for Stochastic Closure Modeling
---

# Synergizing Transport-Based Generative Models and Latent Geometry for Stochastic Closure Modeling
**arXiv**：[2602.17089v1](https://arxiv.org/abs/2602.17089) · [PDF](https://arxiv.org/pdf/2602.17089.pdf)  
**作者**：Xinghao Dong, Huchen Yang, Jin-long Wu  

**一句话要点**：提出基于传输生成模型与潜在几何的随机闭合建模方法，以加速采样并确保物理保真度

**关键词**：随机闭合建模, 传输生成模型, 潜在空间几何, 流匹配, 采样加速, 物理保真度

## 3 点简述
- 核心问题：扩散模型采样速度慢，影响随机闭合模型的实际应用效率
- 方法要点：在低维潜在空间应用流匹配，实现单步快速采样，并比较隐式与显式正则化控制失真
- 实验或效果：在2D Kolmogorov流示例中，采样速度比迭代扩散方法快两个数量级，且潜在空间继承拓扑信息，减少数据需求

## 摘要（原文）

> Diffusion models recently developed for generative AI tasks can produce high-quality samples while still maintaining diversity among samples to promote mode coverage, providing a promising path for learning stochastic closure models. Compared to other types of generative AI models, such as GANs and VAEs, the sampling speed is known as a key disadvantage of diffusion models. By systematically comparing transport-based generative models on a numerical example of 2D Kolmogorov flows, we show that flow matching in a lower-dimensional latent space is suited for fast sampling of stochastic closure models, enabling single-step sampling that is up to two orders of magnitude faster than iterative diffusion-based approaches. To control the latent space distortion and thus ensure the physical fidelity of the sampled closure term, we compare the implicit regularization offered by a joint training scheme against two explicit regularizers: metric-preserving (MP) and geometry-aware (GA) constraints. Besides offering a faster sampling speed, both explicitly and implicitly regularized latent spaces inherit the key topological information from the lower-dimensional manifold of the original complex dynamical system, which enables the learning of stochastic closure models without demanding a huge amount of training data.


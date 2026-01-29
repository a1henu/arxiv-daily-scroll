---
layout: default
title: Supervised Guidance Training for Infinite-Dimensional Diffusion Models
---

# Supervised Guidance Training for Infinite-Dimensional Diffusion Models
**arXiv**：[2601.20756v1](https://arxiv.org/abs/2601.20756) · [PDF](https://arxiv.org/pdf/2601.20756.pdf)  
**作者**：Elizabeth L. Baker, Alexander Denker, Jes Frellsen  

**一句话要点**：提出监督引导训练方法，以解决无限维扩散模型在贝叶斯逆问题中的后验采样难题。

**关键词**：无限维扩散模型, 贝叶斯逆问题, 函数空间采样, 监督引导训练, Doob's h-变换

## 3 点简述
- 核心问题：无限维扩散模型在函数空间中的条件化采样理论未解决，阻碍其在贝叶斯逆问题中的应用。
- 方法要点：基于Doob's h-变换扩展，提出监督引导训练，通过模拟自由分数匹配实现高效稳定的后验采样。
- 实验或效果：在函数空间的贝叶斯逆问题上进行数值示例，验证方法能准确采样后验分布。

## 摘要（原文）

> Score-based diffusion models have recently been extended to infinite-dimensional function spaces, with uses such as inverse problems arising from partial differential equations. In the Bayesian formulation of inverse problems, the aim is to sample from a posterior distribution over functions obtained by conditioning a prior on noisy observations. While diffusion models provide expressive priors in function space, the theory of conditioning them to sample from the posterior remains open. We address this, assuming that either the prior lies in the Cameron-Martin space, or is absolutely continuous with respect to a Gaussian measure. We prove that the models can be conditioned using an infinite-dimensional extension of Doob's $h$-transform, and that the conditional score decomposes into an unconditional score and a guidance term. As the guidance term is intractable, we propose a simulation-free score matching objective (called Supervised Guidance Training) enabling efficient and stable posterior sampling. We illustrate the theory with numerical examples on Bayesian inverse problems in function spaces. In summary, our work offers the first function-space method for fine-tuning trained diffusion models to accurately sample from a posterior.


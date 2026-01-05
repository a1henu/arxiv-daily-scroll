---
layout: default
title: Categorical Reparameterization with Denoising Diffusion models
---

# Categorical Reparameterization with Denoising Diffusion models
**arXiv**：[2601.00781v1](https://arxiv.org/abs/2601.00781) · [PDF](https://arxiv.org/pdf/2601.00781.pdf)  
**作者**：Samson Gourevitch, Alain Durmus, Eric Moulines, Jimmy Olsson, Yazid Janati  

**一句话要点**：提出基于去噪扩散模型的分类变量重参数化方法，以优化梯度计算。

**关键词**：分类变量优化, 重参数化技巧, 去噪扩散模型, 梯度估计, 高斯噪声过程

## 3 点简述
- 核心问题：分类变量优化中梯度估计存在噪声或偏差，影响效率。
- 方法要点：引入扩散软重参数化，利用高斯噪声过程的去噪器闭式解，实现训练自由采样。
- 实验或效果：在多个基准测试中，该方法展现出竞争性或改进的优化性能。

## 摘要（原文）

> Gradient-based optimization with categorical variables typically relies on score-function estimators, which are unbiased but noisy, or on continuous relaxations that replace the discrete distribution with a smooth surrogate admitting a pathwise (reparameterized) gradient, at the cost of optimizing a biased, temperature-dependent objective. In this paper, we extend this family of relaxations by introducing a diffusion-based soft reparameterization for categorical distributions. For these distributions, the denoiser under a Gaussian noising process admits a closed form and can be computed efficiently, yielding a training-free diffusion sampler through which we can backpropagate. Our experiments show that the proposed reparameterization trick yields competitive or improved optimization performance on various benchmarks.


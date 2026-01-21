---
layout: default
title: An Elementary Approach to Scheduling in Generative Diffusion Models
---

# An Elementary Approach to Scheduling in Generative Diffusion Models
**arXiv**：[2601.13602v1](https://arxiv.org/abs/2601.13602) · [PDF](https://arxiv.org/pdf/2601.13602.pdf)  
**作者**：Qiang Sun, H. Vincent Poor, Wenyi Zhang  

**一句话要点**：提出基于KL散度的噪声调度与时间离散化优化方法，提升生成扩散模型效率

**关键词**：生成扩散模型, 噪声调度, 时间离散化, KL散度, 变分优化

## 3 点简述
- 核心问题：分析噪声调度和时间离散化对生成扩散模型性能的影响
- 方法要点：推导高斯源分布下KL散度闭式解，通过变分法优化噪声调度
- 实验或效果：在有限函数评估预算下，所选策略优于基线及搜索方法

## 摘要（原文）

> An elementary approach to characterizing the impact of noise scheduling and time discretization in generative diffusion models is developed. Considering a simplified model where the source distribution is multivariate Gaussian with a given covariance matrix, the explicit closed-form evolution trajectory of the distributions across reverse sampling steps is derived, and consequently, the Kullback-Leibler (KL) divergence between the source distribution and the reverse sampling output is obtained. The effect of the number of time discretization steps on the convergence of this KL divergence is studied via the Euler-Maclaurin expansion. An optimization problem is formulated, and its solution noise schedule is obtained via calculus of variations, shown to follow a tangent law whose coefficient is determined by the eigenvalues of the source covariance matrix. For an alternative scenario, more realistic in practice, where pretrained models have been obtained for some given noise schedules, the KL divergence also provides a measure to compare different time discretization strategies in reverse sampling. Experiments across different datasets and pretrained models demonstrate that the time discretization strategy selected by our approach consistently outperforms baseline and search-based strategies, particularly when the budget on the number of function evaluations is very tight.


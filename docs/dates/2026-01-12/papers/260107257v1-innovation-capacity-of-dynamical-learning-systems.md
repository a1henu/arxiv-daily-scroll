---
layout: default
title: Innovation Capacity of Dynamical Learning Systems
---

# Innovation Capacity of Dynamical Learning Systems
**arXiv**：[2601.07257v1](https://arxiv.org/abs/2601.07257) · [PDF](https://arxiv.org/pdf/2601.07257.pdf)  
**作者**：Anthony M. Polloreno  

**一句话要点**：提出创新容量以解释噪声物理储层中缺失的信息处理能力

**关键词**：信息处理容量, 创新容量, 噪声物理储层, 线性高斯系统, 容量守恒定律, 希尔伯特空间分解

## 3 点简述
- 核心问题：经典信息处理容量远小于观测秩，存在缺失容量
- 方法要点：引入创新容量，基于希尔伯特空间分解证明容量守恒定律
- 实验或效果：在约翰逊-奈奎斯特机制中展示温度与可预测容量的单调权衡

## 摘要（原文）

> In noisy physical reservoirs, the classical information-processing capacity $C_{\mathrm{ip}}$ quantifies how well a linear readout can realize tasks measurable from the input history, yet $C_{\mathrm{ip}}$ can be far smaller than the observed rank of the readout covariance. We explain this ``missing capacity'' by introducing the innovation capacity $C_{\mathrm{i}}$, the total capacity allocated to readout components orthogonal to the input filtration (Doob innovations, including input-noise mixing). Using a basis-free Hilbert-space formulation of the predictable/innovation decomposition, we prove the conservation law $C_{\mathrm{ip}}+C_{\mathrm{i}}=\mathrm{rank}(Σ_{XX})\le d$, so predictable and innovation capacities exactly partition the rank of the observable readout dimension covariance $Σ_{XX}\in \mathbb{R}^{\rm d\times d}$. In linear-Gaussian Johnson-Nyquist regimes, $Σ_{XX}(T)=S+T N_0$, the split becomes a generalized-eigenvalue shrinkage rule and gives an explicit monotone tradeoff between temperature and predictable capacity. Geometrically, in whitened coordinates the predictable and innovation components correspond to complementary covariance ellipsoids, making $C_{\mathrm{i}}$ a trace-controlled innovation budget. A large $C_{\mathrm{i}}$ forces a high-dimensional innovation subspace with a variance floor and under mild mixing and anti-concentration assumptions this yields extensive innovation-block differential entropy and exponentially many distinguishable histories. Finally, we give an information-theoretic lower bound showing that learning the induced innovation-block law in total variation requires a number of samples that scales with the effective innovation dimension, supporting the generative utility of noisy physical reservoirs.


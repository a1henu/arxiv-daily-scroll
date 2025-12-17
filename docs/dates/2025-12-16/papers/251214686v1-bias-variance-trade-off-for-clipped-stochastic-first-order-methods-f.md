---
layout: default
title: Bias-Variance Trade-off for Clipped Stochastic First-Order Methods: From Bounded Variance to Infinite Mean
---

# Bias-Variance Trade-off for Clipped Stochastic First-Order Methods: From Bounded Variance to Infinite Mean
**arXiv**：[2512.14686v1](https://arxiv.org/abs/2512.14686) · [PDF](https://arxiv.org/pdf/2512.14686.pdf)  
**作者**：Chuan He  

**一句话要点**：提出基于偏差-方差权衡的梯度裁剪分析，改进重尾噪声下随机一阶方法的复杂度保证

**关键词**：随机优化, 重尾噪声, 梯度裁剪, 偏差-方差权衡, 复杂度分析, 尾指数

## 3 点简述
- 研究重尾噪声下随机一阶方法的复杂度，覆盖尾指数α∈(0,2]的广泛范围
- 通过分析梯度裁剪的偏差-方差权衡，在噪声尾部对称性受控时获得改进的复杂度保证
- 数值实验验证理论结果，复杂度分析可结合轻尾噪声经典分析

## 摘要（原文）

> Stochastic optimization is fundamental to modern machine learning. Recent research has extended the study of stochastic first-order methods (SFOMs) from light-tailed to heavy-tailed noise, which frequently arises in practice, with clipping emerging as a key technique for controlling heavy-tailed gradients. Extensive theoretical advances have further shown that the oracle complexity of SFOMs depends on the tail index $α$ of the noise. Nonetheless, existing complexity results often cover only the case $α\in (1,2]$, that is, the regime where the noise has a finite mean, while the complexity bounds tend to infinity as $α$ approaches $1$. This paper tackles the general case of noise with tail index $α\in(0,2]$, covering regimes ranging from noise with bounded variance to noise with an infinite mean, where the latter case has been scarcely studied. Through a novel analysis of the bias-variance trade-off in gradient clipping, we show that when a symmetry measure of the noise tail is controlled, clipped SFOMs achieve improved complexity guarantees in the presence of heavy-tailed noise for any tail index $α\in (0,2]$. Our analysis of the bias-variance trade-off not only yields new unified complexity guarantees for clipped SFOMs across this full range of tail indices, but is also straightforward to apply and can be combined with classical analyses under light-tailed noise to establish oracle complexity guarantees under heavy-tailed noise. Finally, numerical experiments validate our theoretical findings.


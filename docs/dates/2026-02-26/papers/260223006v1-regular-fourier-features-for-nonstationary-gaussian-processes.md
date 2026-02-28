---
layout: default
title: Regular Fourier Features for Nonstationary Gaussian Processes
---

# Regular Fourier Features for Nonstationary Gaussian Processes
**arXiv**：[2602.23006v1](https://arxiv.org/abs/2602.23006) · [PDF](https://arxiv.org/pdf/2602.23006.pdf)  
**作者**：Arsalan Jawaid, Abdullah Karatas, Jörg Seewig  

**一句话要点**：提出正则傅里叶特征以解决非平稳高斯过程的模拟与核学习问题

**关键词**：非平稳高斯过程, 正则傅里叶特征, 谱表示, 核学习, 低秩近似

## 3 点简述
- 核心问题：传统谱方法依赖概率假设，不适用于非平稳过程，导致模拟效率低。
- 方法要点：直接离散化谱表示，避免概率限制，构建正半定低秩近似，支持未知谱密度下的核学习。
- 实验或效果：在局部平稳核和复值谱密度的混合核上验证了方法的有效性。

## 摘要（原文）

> Simulating a Gaussian process requires sampling from a high-dimensional Gaussian distribution, which scales cubically with the number of sample locations. Spectral methods address this challenge by exploiting the Fourier representation, treating the spectral density as a probability distribution for Monte Carlo approximation. Although this probabilistic interpretation works for stationary processes, it is overly restrictive for the nonstationary case, where spectral densities are generally not probability measures. We propose regular Fourier features for harmonizable processes that avoid this limitation. Our method discretizes the spectral representation directly, preserving the correlation structure among spectral weights without requiring probability assumptions. Under a finite spectral support assumption, this yields an efficient low-rank approximation that is positive semi-definite by construction. When the spectral density is unknown, the framework extends naturally to kernel learning from data. We demonstrate the method on locally stationary kernels and on harmonizable mixture kernels with complex-valued spectral densities.


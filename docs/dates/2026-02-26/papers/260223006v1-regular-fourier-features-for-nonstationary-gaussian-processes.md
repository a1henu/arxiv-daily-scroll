---
layout: default
title: Regular Fourier Features for Nonstationary Gaussian Processes
---

# Regular Fourier Features for Nonstationary Gaussian Processes
**arXiv**：[2602.23006v1](https://arxiv.org/abs/2602.23006) · [PDF](https://arxiv.org/pdf/2602.23006.pdf)  
**作者**：Arsalan Jawaid, Abdullah Karatas, Jörg Seewig  

**一句话要点**：提出正则傅里叶特征以解决非平稳高斯过程的谱方法限制

**关键词**：非平稳高斯过程, 谱方法, 正则傅里叶特征, 低秩近似, 核学习

## 3 点简述
- 核心问题：非平稳高斯过程的谱密度非概率测度，传统谱方法不适用
- 方法要点：直接离散化谱表示，避免概率假设，构建低秩正半定近似
- 实验或效果：应用于局部平稳核和复值谱密度的可调和混合核

## 摘要（原文）

> Simulating a Gaussian process requires sampling from a high-dimensional Gaussian distribution, which scales cubically with the number of sample locations. Spectral methods address this challenge by exploiting the Fourier representation, treating the spectral density as a probability distribution for Monte Carlo approximation. Although this probabilistic interpretation works for stationary processes, it is overly restrictive for the nonstationary case, where spectral densities are generally not probability measures. We propose regular Fourier features for harmonizable processes that avoid this limitation. Our method discretizes the spectral representation directly, preserving the correlation structure among spectral weights without requiring probability assumptions. Under a finite spectral support assumption, this yields an efficient low-rank approximation that is positive semi-definite by construction. When the spectral density is unknown, the framework extends naturally to kernel learning from data. We demonstrate the method on locally stationary kernels and on harmonizable mixture kernels with complex-valued spectral densities.


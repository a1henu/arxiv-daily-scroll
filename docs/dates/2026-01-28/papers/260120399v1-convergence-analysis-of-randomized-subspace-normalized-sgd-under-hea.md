---
layout: default
title: Convergence Analysis of Randomized Subspace Normalized SGD under Heavy-Tailed Noise
---

# Convergence Analysis of Randomized Subspace Normalized SGD under Heavy-Tailed Noise
**arXiv**：[2601.20399v1](https://arxiv.org/abs/2601.20399) · [PDF](https://arxiv.org/pdf/2601.20399.pdf)  
**作者**：Gaku Omiya, Pierre-Louis Poirion, Akiko Takeda  

**一句话要点**：提出随机子空间归一化SGD以处理重尾噪声，提升非凸优化收敛性能

**关键词**：随机子空间方法, 归一化SGD, 重尾噪声, 非凸优化, 高概率收敛, oracle复杂度

## 3 点简述
- 核心问题：随机子空间方法在非凸优化中缺乏高概率收敛分析，尤其在重尾噪声下
- 方法要点：结合方向归一化到子空间更新，假设噪声有界p阶矩，建立期望和高概率收敛保证
- 实验或效果：RS-NSGD比全维归一化SGD达到更好的oracle复杂度，未知具体实验验证

## 摘要（原文）

> Randomized subspace methods reduce per-iteration cost; however, in nonconvex optimization, most analyses are expectation-based, and high-probability bounds remain scarce even under sub-Gaussian noise. We first prove that randomized subspace SGD (RS-SGD) admits a high-probability convergence bound under sub-Gaussian noise, achieving the same order of oracle complexity as prior in-expectation results. Motivated by the prevalence of heavy-tailed gradients in modern machine learning, we then propose randomized subspace normalized SGD (RS-NSGD), which integrates direction normalization into subspace updates. Assuming the noise has bounded $p$-th moments, we establish both in-expectation and high-probability convergence guarantees, and show that RS-NSGD can achieve better oracle complexity than full-dimensional normalized SGD.


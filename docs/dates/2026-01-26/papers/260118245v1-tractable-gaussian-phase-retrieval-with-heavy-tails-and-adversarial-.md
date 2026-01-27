---
layout: default
title: Tractable Gaussian Phase Retrieval with Heavy Tails and Adversarial Corruption with Near-Linear Sample Complexity
---

# Tractable Gaussian Phase Retrieval with Heavy Tails and Adversarial Corruption with Near-Linear Sample Complexity
**arXiv**：[2601.18245v1](https://arxiv.org/abs/2601.18245) · [PDF](https://arxiv.org/pdf/2601.18245.pdf)  
**作者**：Santanu Das, Jatin Batra  

**一句话要点**：提出多项式时间算法以解决重尾噪声和对抗性损坏下的鲁棒相位恢复问题

**关键词**：相位恢复, 鲁棒统计, 对抗性损坏, 重尾噪声, 谱初始化, 鲁棒PCA

## 3 点简述
- 研究相位恢复问题，在重尾噪声和对抗性损坏下恢复信号
- 连接鲁棒谱初始化和鲁棒PCA，实现多项式时间算法
- 样本复杂度接近线性，优于先前指数时间算法

## 摘要（原文）

> Phase retrieval is the classical problem of recovering a signal $x^* \in \mathbb{R}^n$ from its noisy phaseless measurements $y_i = \langle a_i, x^* \rangle^2 + ζ_i$ (where $ζ_i$ denotes noise, and $a_i$ is the sensing vector) for $i \in [m]$. The problem of phase retrieval has a rich history, with a variety of applications such as optics, crystallography, heteroscedastic regression, astrophysics, etc. A major consideration in algorithms for phase retrieval is robustness against measurement errors. In recent breakthroughs in algorithmic robust statistics, efficient algorithms have been developed for several parameter estimation tasks such as mean estimation, covariance estimation, robust principal component analysis (PCA), etc. in the presence of heavy-tailed noise and adversarial corruptions. In this paper, we study efficient algorithms for robust phase retrieval with heavy-tailed noise when a constant fraction of both the measurements $y_i$ and the sensing vectors $a_i$ may be arbitrarily adversarially corrupted. For this problem, Buna and Rebeschini (AISTATS 2025) very recently gave an exponential time algorithm with sample complexity $O(n \log n)$. Their algorithm needs a robust spectral initialization, specifically, a robust estimate of the top eigenvector of a covariance matrix, which they deemed to be beyond known efficient algorithmic techniques (similar spectral initializations are a key ingredient of a large family of phase retrieval algorithms). In this work, we make a connection between robust spectral initialization and recent algorithmic advances in robust PCA, yielding the first polynomial-time algorithms for robust phase retrieval with both heavy-tailed noise and adversarial corruptions, in fact with near-linear (in $n$) sample complexity.


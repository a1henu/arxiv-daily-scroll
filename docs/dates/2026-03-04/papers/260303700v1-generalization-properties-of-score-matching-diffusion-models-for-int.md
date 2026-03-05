---
layout: default
title: Generalization Properties of Score-matching Diffusion Models for Intrinsically Low-dimensional Data
---

# Generalization Properties of Score-matching Diffusion Models for Intrinsically Low-dimensional Data
**arXiv**：[2603.03700v1](https://arxiv.org/abs/2603.03700) · [PDF](https://arxiv.org/pdf/2603.03700.pdf)  
**作者**：Saptarshi Chakraborty, Quentin Berthet, Peter L. Bartlett  

**一句话要点**：提出基于(p,q)-Wasserstein维度的分数匹配扩散模型泛化理论，以缓解高维数据学习中的维度诅咒。

**关键词**：扩散模型, 统计学习理论, Wasserstein距离, 维度诅咒, 泛化分析, 分数匹配

## 3 点简述
- 研究分数匹配扩散模型在有限样本下学习未知分布的统计收敛性，关注其泛化性质。
- 在温和正则条件下，推导学习分布与真实分布间Wasserstein-p距离的有限样本误差界，无需紧支撑或流形假设。
- 证明收敛率依赖于数据的(p,q)-Wasserstein维度而非环境维度，表明模型能自适应数据内在低维结构。

## 摘要（原文）

> Despite the remarkable empirical success of score-based diffusion models, their statistical guarantees remain underdeveloped. Existing analyses often provide pessimistic convergence rates that do not reflect the intrinsic low-dimensional structure common in real data, such as that arising in natural images. In this work, we study the statistical convergence of score-based diffusion models for learning an unknown distribution $μ$ from finitely many samples. Under mild regularity conditions on the forward diffusion process and the data distribution, we derive finite-sample error bounds on the learned generative distribution, measured in the Wasserstein-$p$ distance. Unlike prior results, our guarantees hold for all $p \ge 1$ and require only a finite-moment assumption on $μ$, without compact-support, manifold, or smooth-density conditions. Specifically, given $n$ i.i.d.\ samples from $μ$ with finite $q$-th moment and appropriately chosen network architectures, hyperparameters, and discretization schemes, we show that the expected Wasserstein-$p$ error between the learned distribution $\hatμ$ and $μ$ scales as $\mathbb{E}\, \mathbb{W}_p(\hatμ,μ) = \widetilde{O}\!\left(n^{-1 / d^\ast_{p,q}(μ)}\right),$ where $d^\ast_{p,q}(μ)$ is the $(p,q)$-Wasserstein dimension of $μ$. Our results demonstrate that diffusion models naturally adapt to the intrinsic geometry of data and mitigate the curse of dimensionality, since the convergence rate depends on $d^\ast_{p,q}(μ)$ rather than the ambient dimension. Moreover, our theory conceptually bridges the analysis of diffusion models with that of GANs and the sharp minimax rates established in optimal transport. The proposed $(p,q)$-Wasserstein dimension also extends classical Wasserstein dimension notions to distributions with unbounded support, which may be of independent theoretical interest.


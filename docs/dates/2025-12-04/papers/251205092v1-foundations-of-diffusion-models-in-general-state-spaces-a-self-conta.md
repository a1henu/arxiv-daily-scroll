---
layout: default
title: Foundations of Diffusion Models in General State Spaces: A Self-Contained Introduction
---

# Foundations of Diffusion Models in General State Spaces: A Self-Contained Introduction
**arXiv**：[2512.05092v1](https://arxiv.org/abs/2512.05092) · [PDF](https://arxiv.org/pdf/2512.05092.pdf)  
**作者**：Vincent Pauline, Tobias Höppe, Kirill Neklyudov, Alexander Tong, Stefan Bauer, Andrea Dittadi  

**一句话要点**：提出统一扩散模型理论框架，覆盖连续与离散状态空间，提供自包含入门指南。

**关键词**：扩散模型, 状态空间理论, 变分推断, 连续时间极限, 离散扩散, 生成建模

## 3 点简述
- 核心问题：现有扩散模型介绍多限于欧几里得数据，缺乏连续与离散状态空间的统一理论。
- 方法要点：基于马尔可夫核和变分方法，推导离散时间与连续时间极限，统一处理高斯过程和分类转移核。
- 实验或效果：未知，但提供分层内容面向不同读者，强调可重用证明和核心理论原则。

## 摘要（原文）

> Although diffusion models now occupy a central place in generative modeling, introductory treatments commonly assume Euclidean data and seldom clarify their connection to discrete-state analogues. This article is a self-contained primer on diffusion over general state spaces, unifying continuous domains and discrete/categorical structures under one lens. We develop the discrete-time view (forward noising via Markov kernels and learned reverse dynamics) alongside its continuous-time limits -- stochastic differential equations (SDEs) in $\mathbb{R}^d$ and continuous-time Markov chains (CTMCs) on finite alphabets -- and derive the associated Fokker--Planck and master equations. A common variational treatment yields the ELBO that underpins standard training losses. We make explicit how forward corruption choices -- Gaussian processes in continuous spaces and structured categorical transition kernels (uniform, masking/absorbing and more) in discrete spaces -- shape reverse dynamics and the ELBO. The presentation is layered for three audiences: newcomers seeking a self-contained intuitive introduction; diffusion practitioners wanting a global theoretical synthesis; and continuous-diffusion experts looking for an analogy-first path into discrete diffusion. The result is a unified roadmap to modern diffusion methodology across continuous domains and discrete sequences, highlighting a compact set of reusable proofs, identities, and core theoretical principles.


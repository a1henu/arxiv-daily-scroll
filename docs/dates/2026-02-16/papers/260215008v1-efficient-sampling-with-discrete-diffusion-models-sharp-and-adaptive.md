---
layout: default
title: Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees
---

# Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees
**arXiv**：[2602.15008v1](https://arxiv.org/abs/2602.15008) · [PDF](https://arxiv.org/pdf/2602.15008.pdf)  
**作者**：Daniil Dmitriev, Zhihan Huang, Yuting Wei  

**一句话要点**：提出τ-leaping采样器，为离散扩散模型提供高效采样理论保证

**关键词**：离散扩散模型, 采样效率, τ-leaping算法, KL散度收敛, 低维结构自适应, 理论保证

## 3 点简述
- 研究离散扩散模型的采样效率，基于连续时间马尔可夫链框架
- 针对均匀和掩码噪声过程，建立KL散度收敛的尖锐保证
- 采样器自适应低维结构，在隐藏马尔可夫模型等示例中实现次线性收敛

## 摘要（原文）

> Diffusion models over discrete spaces have recently shown striking empirical success, yet their theoretical foundations remain incomplete. In this paper, we study the sampling efficiency of score-based discrete diffusion models under a continuous-time Markov chain (CTMC) formulation, with a focus on $τ$-leaping-based samplers. We establish sharp convergence guarantees for attaining $\varepsilon$ accuracy in Kullback-Leibler (KL) divergence for both uniform and masking noising processes. For uniform discrete diffusion, we show that the $τ$-leaping algorithm achieves an iteration complexity of order $\tilde O(d/\varepsilon)$, with $d$ the ambient dimension of the target distribution, eliminating linear dependence on the vocabulary size $S$ and improving existing bounds by a factor of $d$; moreover, we establish a matching algorithmic lower bound showing that linear dependence on the ambient dimension is unavoidable in general. For masking discrete diffusion, we introduce a modified $τ$-leaping sampler whose convergence rate is governed by an intrinsic information-theoretic quantity, termed the effective total correlation, which is bounded by $d \log S$ but can be sublinear or even constant for structured data. As a consequence, the sampler provably adapts to low-dimensional structure without prior knowledge or algorithmic modification, yielding sublinear convergence rates for various practical examples (such as hidden Markov models, image data, and random graphs). Our analysis requires no boundedness or smoothness assumptions on the score estimator beyond control of the score entropy loss.


---
layout: default
title: Generative Drifting is Secretly Score Matching: a Spectral and Variational Perspective
---

# Generative Drifting is Secretly Score Matching: a Spectral and Variational Perspective
**arXiv**：[2603.09936v1](https://arxiv.org/abs/2603.09936) · [PDF](https://arxiv.org/pdf/2603.09936.pdf)  
**作者**：Erkan Turan, Maks Ovsjanikov  

**一句话要点**：揭示生成漂移与分数匹配的等价性，提供谱与变分视角的理论分析

**关键词**：生成模型, 分数匹配, 谱分析, 变分方法, 核方法, 梯度流

## 3 点简述
- 核心问题：生成漂移方法缺乏理论理解，如分布等价性、核选择与停止梯度算子的必要性
- 方法要点：通过高斯核下漂移算子等于平滑分布的分数差，将漂移纳入分数匹配框架，分析谱收敛与变分梯度流
- 实验或效果：提出指数带宽退火计划，将收敛时间从指数级降至对数级，并基于Sinkhorn散度构造新漂移算子

## 摘要（原文）

> Generative Modeling via Drifting has recently achieved state-of-the-art one-step image generation through a kernel-based drift operator, yet the success is largely empirical and its theoretical foundations remain poorly understood. In this paper, we make the following observation: \emph{under a Gaussian kernel, the drift operator is exactly a score difference on smoothed distributions}. This insight allows us to answer all three key questions left open in the original work: (1) whether a vanishing drift guarantees equality of distributions ($V_{p,q}=0\Rightarrow p=q$), (2) how to choose between kernels, and (3) why the stop-gradient operator is indispensable for stable training. Our observations position drifting within the well-studied score-matching family and enable a rich theoretical perspective. By linearizing the McKean-Vlasov dynamics and probing them in Fourier space, we reveal frequency-dependent convergence timescales comparable to \emph{Landau damping} in plasma kinetic theory: the Gaussian kernel suffers an exponential high-frequency bottleneck, explaining the empirical preference for the Laplacian kernel. We also propose an exponential bandwidth annealing schedule $σ(t)=σ_0 e^{-rt}$ that reduces convergence time from $\exp(O(K_{\max}^2))$ to $O(\log K_{\max})$. Finally, by formalizing drifting as a Wasserstein gradient flow of the smoothed KL divergence, we prove that the stop-gradient operator is derived directly from the frozen-field discretization mandated by the JKO scheme, and removing it severs training from any gradient-flow guarantee. This variational perspective further provides a general template for constructing novel drift operators, demonstrated with a Sinkhorn divergence drift.


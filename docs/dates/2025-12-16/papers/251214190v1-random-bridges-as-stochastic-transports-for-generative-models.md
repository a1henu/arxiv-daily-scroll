---
layout: default
title: Random-Bridges as Stochastic Transports for Generative Models
---

# Random-Bridges as Stochastic Transports for Generative Models
**arXiv**：[2512.14190v1](https://arxiv.org/abs/2512.14190) · [PDF](https://arxiv.org/pdf/2512.14190.pdf)  
**作者**：Stefano Goria, Levent A. Mengütürk, Murat C. Mengütürk, Berkan Sesen  

**一句话要点**：提出随机桥作为生成模型中的随机传输方法，以高效生成高质量样本。

**关键词**：随机桥, 生成模型, 随机传输, 高斯过程, 高效生成, 概率分布

## 3 点简述
- 核心问题：传统生成模型在样本生成中步骤多、计算成本高。
- 方法要点：利用随机桥作为概率分布间的随机传输，支持马尔可夫或非马尔可夫模式。
- 实验或效果：基于高斯随机桥的实验显示，在较少步骤内生成高质量样本，计算成本低。

## 摘要（原文）

> This paper motivates the use of random-bridges -- stochastic processes conditioned to take target distributions at fixed timepoints -- in the realm of generative modelling. Herein, random-bridges can act as stochastic transports between two probability distributions when appropriately initialized, and can display either Markovian or non-Markovian, and either continuous, discontinuous or hybrid patterns depending on the driving process. We show how one can start from general probabilistic statements and then branch out into specific representations for learning and simulation algorithms in terms of information processing. Our empirical results, built on Gaussian random bridges, produce high-quality samples in significantly fewer steps compared to traditional approaches, while achieving competitive Frechet inception distance scores. Our analysis provides evidence that the proposed framework is computationally cheap and suitable for high-speed generation tasks.


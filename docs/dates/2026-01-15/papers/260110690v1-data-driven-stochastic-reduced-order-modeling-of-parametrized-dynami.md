---
layout: default
title: Data-driven stochastic reduced-order modeling of parametrized dynamical systems
---

# Data-driven stochastic reduced-order modeling of parametrized dynamical systems
**arXiv**：[2601.10690v1](https://arxiv.org/abs/2601.10690) · [PDF](https://arxiv.org/pdf/2601.10690.pdf)  
**作者**：Andrew F. Ilersich, Kevin Course, Prasanth B. Nair  

**一句话要点**：提出基于摊销随机变分推断的数据驱动随机降阶建模框架，以解决参数化动力系统在随机动态和不确定性量化中的挑战。

**关键词**：随机降阶建模, 摊销变分推断, 参数化动力系统, 不确定性量化, 数据驱动框架, 马尔可夫高斯过程

## 3 点简述
- 核心问题：现有降阶模型难以处理随机动态和量化预测不确定性，限制了在稳健决策中的应用。
- 方法要点：利用摊销随机变分推断和重参数化技巧，联合学习概率自编码器和潜在动态的随机微分方程，无需昂贵前向求解器。
- 实验或效果：在三个测试问题中展示了对未见参数组合和强迫的优异泛化能力，相比现有方法显著提升效率。

## 摘要（原文）

> Modeling complex dynamical systems under varying conditions is computationally intensive, often rendering high-fidelity simulations intractable. Although reduced-order models (ROMs) offer a promising solution, current methods often struggle with stochastic dynamics and fail to quantify prediction uncertainty, limiting their utility in robust decision-making contexts. To address these challenges, we introduce a data-driven framework for learning continuous-time stochastic ROMs that generalize across parameter spaces and forcing conditions. Our approach, based on amortized stochastic variational inference, leverages a reparametrization trick for Markov Gaussian processes to eliminate the need for computationally expensive forward solvers during training. This enables us to jointly learn a probabilistic autoencoder and stochastic differential equations governing the latent dynamics, at a computational cost that is independent of the dataset size and system stiffness. Additionally, our approach offers the flexibility of incorporating physics-informed priors if available. Numerical studies are presented for three challenging test problems, where we demonstrate excellent generalization to unseen parameter combinations and forcings, and significant efficiency gains compared to existing approaches.


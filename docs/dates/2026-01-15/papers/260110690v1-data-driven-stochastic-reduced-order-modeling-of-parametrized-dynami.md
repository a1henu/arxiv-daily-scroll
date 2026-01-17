---
layout: default
title: Data-driven stochastic reduced-order modeling of parametrized dynamical systems
---

# Data-driven stochastic reduced-order modeling of parametrized dynamical systems
**arXiv**：[2601.10690v1](https://arxiv.org/abs/2601.10690) · [PDF](https://arxiv.org/pdf/2601.10690.pdf)  
**作者**：Andrew F. Ilersich, Kevin Course, Prasanth B. Nair  

**一句话要点**：提出基于摊销随机变分推断的数据驱动随机降阶模型框架，以解决参数化动力系统建模中的计算复杂性和不确定性量化问题。

**关键词**：随机降阶模型, 参数化动力系统, 摊销变分推断, 随机微分方程, 不确定性量化, 数据驱动建模

## 3 点简述
- 核心问题：高保真模拟参数化动力系统计算成本高，现有降阶模型难以处理随机动态和量化预测不确定性。
- 方法要点：利用摊销随机变分推断和重参数化技巧，联合学习概率自编码器和随机微分方程，无需昂贵前向求解器。
- 实验或效果：在三个测试问题中展示了对未见参数和强迫条件的优秀泛化能力，计算效率显著提升。

## 摘要（原文）

> Modeling complex dynamical systems under varying conditions is computationally intensive, often rendering high-fidelity simulations intractable. Although reduced-order models (ROMs) offer a promising solution, current methods often struggle with stochastic dynamics and fail to quantify prediction uncertainty, limiting their utility in robust decision-making contexts. To address these challenges, we introduce a data-driven framework for learning continuous-time stochastic ROMs that generalize across parameter spaces and forcing conditions. Our approach, based on amortized stochastic variational inference, leverages a reparametrization trick for Markov Gaussian processes to eliminate the need for computationally expensive forward solvers during training. This enables us to jointly learn a probabilistic autoencoder and stochastic differential equations governing the latent dynamics, at a computational cost that is independent of the dataset size and system stiffness. Additionally, our approach offers the flexibility of incorporating physics-informed priors if available. Numerical studies are presented for three challenging test problems, where we demonstrate excellent generalization to unseen parameter combinations and forcings, and significant efficiency gains compared to existing approaches.


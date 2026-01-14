---
layout: default
title: Out-of-distribution generalization of deep-learning surrogates for 2D PDE-generated dynamics in the small-data regime
---

# Out-of-distribution generalization of deep-learning surrogates for 2D PDE-generated dynamics in the small-data regime
**arXiv**：[2601.08404v1](https://arxiv.org/abs/2601.08404) · [PDF](https://arxiv.org/pdf/2601.08404.pdf)  
**作者**：Binh Duong Nguyen, Stefan Sandfeld  

**一句话要点**：提出多通道U-Net以在少量数据下提升二维PDE动力学代理模型的分布外泛化能力

**关键词**：PDE代理模型, 分布外泛化, 少量数据学习, 周期性边界条件, U-Net架构, 科学机器学习

## 3 点简述
- 研究二维周期性PDE动力学在少量数据（≤100轨迹）下的分布外初始条件泛化问题
- 引入多通道U-Net架构，结合局部性和周期性边界归纳偏置，对比多种复杂模型
- 在五个PDE数据集上，该模型匹配或超越其他架构，训练时间更少，泛化至约20个训练模拟

## 摘要（原文）

> Partial differential equations (PDEs) are a central tool for modeling the dynamics of physical, engineering, and materials systems, but high-fidelity simulations are often computationally expensive. At the same time, many scientific applications can be viewed as the evolution of spatially distributed fields, making data-driven forecasting of such fields a core task in scientific machine learning. In this work we study autoregressive deep-learning surrogates for two-dimensional PDE dynamics on periodic domains, focusing on generalization to out-of-distribution initial conditions within a fixed PDE and parameter regime and on strict small-data settings with at most $\mathcal{O}(10^2)$ simulated trajectories per system. We introduce a multi-channel U-Net [...], evaluate it on five qualitatively different PDE families and compare it to ViT, AFNO, PDE-Transformer, and KAN-UNet under a common training setup. Across all datasets, me-UNet matches or outperforms these more complex architectures in terms of field-space error, spectral similarity, and physics-based metrics for in-distribution rollouts, while requiring substantially less training time. It also generalizes qualitatively to unseen initial conditions with as few as $\approx 20$ training simulations. A data-efficiency study and Grad-CAM analysis further suggest that, in small-data periodic 2D PDE settings, convolutional architectures with inductive biases aligned to locality and periodic boundary conditions remain strong contenders for accurate and moderately out-of-distribution-robust surrogate modeling.


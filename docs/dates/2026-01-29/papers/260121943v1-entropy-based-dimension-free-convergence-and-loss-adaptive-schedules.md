---
layout: default
title: Entropy-Based Dimension-Free Convergence and Loss-Adaptive Schedules for Diffusion Models
---

# Entropy-Based Dimension-Free Convergence and Loss-Adaptive Schedules for Diffusion Models
**arXiv**：[2601.21943v1](https://arxiv.org/abs/2601.21943) · [PDF](https://arxiv.org/pdf/2601.21943.pdf)  
**作者**：Ahmad Aghapour, Erhan Bayraktar, Ziqing Zhang  

**一句话要点**：提出基于熵的无维度收敛分析与损失自适应调度以改进扩散模型采样效率

**关键词**：扩散模型, 收敛分析, 信息论, 采样调度, KL散度, 无维度假设

## 3 点简述
- 现有扩散模型收敛分析常依赖维度线性缩放或几何假设，限制了理论普适性。
- 基于信息论，推导出KL散度与熵和步数相关的无维度收敛界，避免几何限制。
- 提出轻量级损失自适应调度，仅依赖训练损失提升采样质量，无需后训练重计算。

## 摘要（原文）

> Diffusion generative models synthesize samples by discretizing reverse-time dynamics driven by a learned score (or denoiser). Existing convergence analyses of diffusion models typically scale at least linearly with the ambient dimension, and sharper rates often depend on intrinsic-dimension assumptions or other geometric restrictions on the target distribution. We develop an alternative, information-theoretic approach to dimension-free convergence that avoids any geometric assumptions. Under mild assumptions on the target distribution, we bound KL divergence between the target and generated distributions by $O(H^2/K)$ (up to endpoint factors), where $H$ is the Shannon entropy and $K$ is the number of sampling steps. Moreover, using a reformulation of the KL divergence, we propose a Loss-Adaptive Schedule (LAS) for efficient discretization of reverse SDE which is lightweight and relies only on the training loss, requiring no post-training heavy computation. Empirically, LAS improves sampling quality over common heuristic schedules.


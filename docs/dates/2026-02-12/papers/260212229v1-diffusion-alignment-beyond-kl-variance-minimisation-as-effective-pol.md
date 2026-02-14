---
layout: default
title: Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser
---

# Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser
**arXiv**：[2602.12229v1](https://arxiv.org/abs/2602.12229) · [PDF](https://arxiv.org/pdf/2602.12229.pdf)  
**作者**：Zijing Ou, Jacob Si, Junyi Zhu, Ondrej Bohdal, Mete Ozay, Taha Ceritli, Yingzhen Li  

**一句话要点**：提出方差最小化策略优化以改进扩散对齐，超越KL目标，统一现有方法并启发新设计。

**关键词**：扩散对齐, 方差最小化, 策略优化, 重要性采样, SMC解释, KL目标

## 3 点简述
- 核心问题：扩散对齐中KL目标可能不最优，需更有效策略优化方法。
- 方法要点：基于SMC视角，最小化重要性权重方差，证明与KL梯度一致，统一多种方法。
- 实验或效果：理论分析支持，VMPO框架可恢复现有方法并引导新方向，效果未知。

## 摘要（原文）

> Diffusion alignment adapts pretrained diffusion models to sample from reward-tilted distributions along the denoising trajectory. This process naturally admits a Sequential Monte Carlo (SMC) interpretation, where the denoising model acts as a proposal and reward guidance induces importance weights. Motivated by this view, we introduce Variance Minimisation Policy Optimisation (VMPO), which formulates diffusion alignment as minimising the variance of log importance weights rather than directly optimising a Kullback-Leibler (KL) based objective. We prove that the variance objective is minimised by the reward-tilted target distribution and that, under on-policy sampling, its gradient coincides with that of standard KL-based alignment. This perspective offers a common lens for understanding diffusion alignment. Under different choices of potential functions and variance minimisation strategies, VMPO recovers various existing methods, while also suggesting new design directions beyond KL.


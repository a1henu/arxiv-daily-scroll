---
layout: default
title: Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser
---

# Diffusion Alignment Beyond KL: Variance Minimisation as Effective Policy Optimiser
**arXiv**：[2602.12229v1](https://arxiv.org/abs/2602.12229) · [PDF](https://arxiv.org/pdf/2602.12229.pdf)  
**作者**：Zijing Ou, Jacob Si, Junyi Zhu, Ondrej Bohdal, Mete Ozay, Taha Ceritli, Yingzhen Li  

**一句话要点**：提出方差最小化策略优化以改进扩散对齐，超越KL目标，统一理解现有方法。

**关键词**：扩散对齐, 方差最小化, 策略优化, 重要性采样, 奖励引导, 序列蒙特卡洛

## 3 点简述
- 扩散对齐通过奖励引导适应预训练扩散模型，但传统基于KL的目标可能非最优。
- VMPO将扩散对齐视为最小化重要性权重方差，证明其梯度与KL对齐一致，提供统一视角。
- VMPO能恢复多种现有方法，并启发新设计方向，实验验证其有效性。

## 摘要（原文）

> Diffusion alignment adapts pretrained diffusion models to sample from reward-tilted distributions along the denoising trajectory. This process naturally admits a Sequential Monte Carlo (SMC) interpretation, where the denoising model acts as a proposal and reward guidance induces importance weights. Motivated by this view, we introduce Variance Minimisation Policy Optimisation (VMPO), which formulates diffusion alignment as minimising the variance of log importance weights rather than directly optimising a Kullback-Leibler (KL) based objective. We prove that the variance objective is minimised by the reward-tilted target distribution and that, under on-policy sampling, its gradient coincides with that of standard KL-based alignment. This perspective offers a common lens for understanding diffusion alignment. Under different choices of potential functions and variance minimisation strategies, VMPO recovers various existing methods, while also suggesting new design directions beyond KL.


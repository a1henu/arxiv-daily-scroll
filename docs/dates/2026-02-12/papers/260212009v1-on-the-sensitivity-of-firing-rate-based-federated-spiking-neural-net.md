---
layout: default
title: On the Sensitivity of Firing Rate-Based Federated Spiking Neural Networks to Differential Privacy
---

# On the Sensitivity of Firing Rate-Based Federated Spiking Neural Networks to Differential Privacy
**arXiv**：[2602.12009v1](https://arxiv.org/abs/2602.12009) · [PDF](https://arxiv.org/pdf/2602.12009.pdf)  
**作者**：Luiz Pereira, Mirko Perkusich, Dalton Valadares, Kyller Gorgônio  

**一句话要点**：分析差分隐私对脉冲神经网络联邦学习中发放率统计的影响，提供隐私与协调平衡的指导

**关键词**：联邦神经形态学习, 差分隐私, 脉冲神经网络, 发放率统计, 非独立同分布数据, 隐私协调平衡

## 3 点简述
- 核心问题：差分隐私机制（梯度裁剪和噪声注入）如何扰动脉冲神经网络的发放率统计，并影响基于发放率的联邦协调
- 方法要点：在非独立同分布语音识别任务中，通过隐私预算和裁剪界限的消融实验，分析发放率偏移、聚合衰减和客户端选择排名不稳定性
- 实验或效果：发现系统性的发放率偏移，并将其与稀疏性和内存指标关联，为隐私保护联邦神经形态学习提供可操作指导

## 摘要（原文）

> Federated Neuromorphic Learning (FNL) enables energy-efficient and privacy-preserving learning on devices without centralizing data. However, real-world deployments require additional privacy mechanisms that can significantly alter training signals. This paper analyzes how Differential Privacy (DP) mechanisms, specifically gradient clipping and noise injection, perturb firing-rate statistics in Spiking Neural Networks (SNNs) and how these perturbations are propagated to rate-based FNL coordination. On a speech recognition task under non-IID settings, ablations across privacy budgets and clipping bounds reveal systematic rate shifts, attenuated aggregation, and ranking instability during client selection. Moreover, we relate these shifts to sparsity and memory indicators. Our findings provide actionable guidance for privacy-preserving FNL, specifically regarding the balance between privacy strength and rate-dependent coordination.


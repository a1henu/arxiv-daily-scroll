---
layout: default
title: Rethinking LoRA for Data Heterogeneous Federated Learning: Subspace and State Alignment
---

# Rethinking LoRA for Data Heterogeneous Federated Learning: Subspace and State Alignment
**arXiv**：[2602.01746v1](https://arxiv.org/abs/2602.01746) · [PDF](https://arxiv.org/pdf/2602.01746.pdf)  
**作者**：Hongyi Peng, Han Yu, Xiaoxiao Li, Qiang Yang  

**一句话要点**：提出FedGaLore以解决非独立同分布联邦学习中LoRA性能下降问题

**关键词**：联邦学习, 低秩适应, 非独立同分布, 优化器状态同步, 梯度子空间优化

## 3 点简述
- 核心问题：非独立同分布下LoRA因更新空间和优化器状态不匹配导致性能显著低于全参数微调
- 方法要点：结合客户端梯度子空间优化与服务器端基于谱共享信号提取的投影二阶矩状态同步
- 实验或效果：在自然语言理解、视觉和自然语言生成基准上提升鲁棒性和准确性

## 摘要（原文）

> Low-Rank Adaptation (LoRA) is widely used for federated fine-tuning. Yet under non-IID settings, it can substantially underperform full-parameter fine-tuning. Through with-high-probability robustness analysis, we uncover that this gap can be attributed to two coupled mismatches: (i) update-space mismatch, where clients optimize in a low-rank subspace but aggregation occurs in the full space; and (ii) optimizer-state mismatch, where unsynchronized adaptive states amplify drift across rounds. We propose FedGaLore, which combines client-side GaLore-style gradient-subspace optimization with server-side drift-robust synchronization of projected second-moment states via spectral shared-signal extraction, to address this challenge. Across NLU, vision, and NLG benchmarks, FedGaLore improves robustness and accuracy over state-of-the-art federated LoRA baselines in non-IID settings.


---
layout: default
title: FedRot-LoRA: Mitigating Rotational Misalignment in Federated LoRA
---

# FedRot-LoRA: Mitigating Rotational Misalignment in Federated LoRA
**arXiv**：[2602.23638v1](https://arxiv.org/abs/2602.23638) · [PDF](https://arxiv.org/pdf/2602.23638.pdf)  
**作者**：Haoran Zhang, Dongjun Kim, Seohyeon Cha, Haris Vikalo  

**一句话要点**：提出FedRot-LoRA以解决联邦LoRA中的旋转错位问题

**关键词**：联邦学习, 低秩适应, 旋转对齐, 聚合误差, 自然语言处理, 通信效率

## 3 点简述
- 核心问题：联邦LoRA中因子平均导致旋转错位，引发聚合误差和不稳定训练
- 方法要点：通过正交变换对齐客户端更新，减少子空间不匹配，保持语义更新
- 实验或效果：在自然语言理解和生成任务中优于现有基线，适应不同异构性和LoRA秩

## 摘要（原文）

> Federated LoRA provides a communication-efficient mechanism for fine-tuning large language models on decentralized data. In practice, however, a discrepancy between the factor-wise averaging used to preserve low rank and the mathematically correct aggregation of local updates can cause significant aggregation error and unstable training. We argue that a major source of this problem is rotational misalignment, arising from the rotational invariance of low-rank factorizations -- semantically equivalent updates can be represented in different latent subspaces across clients since $(B_i R_i)(R_i^\top A_i) = B_i A_i$. When such misaligned factors are averaged directly, they interfere destructively and degrade the global update. To address this issue, we propose FedRot-LoRA, a federated LoRA framework that aligns client updates via orthogonal transformations prior to aggregation. This alignment preserves the semantic update while reducing cross-client subspace mismatch, without increasing communication cost or restricting model expressivity. We provide a convergence analysis that examines the aggregation error induced by factor-wise averaging and shows how rotational alignment yields a tighter upper bound on this error. Extensive experiments on natural language understanding and generative tasks demonstrate that FedRot-LoRA consistently outperforms existing federated LoRA baselines across a range of heterogeneity levels and LoRA ranks.


---
layout: default
title: Dynamics-Aligned Shared Hypernetworks for Zero-Shot Actuator Inversion
---

# Dynamics-Aligned Shared Hypernetworks for Zero-Shot Actuator Inversion
**arXiv**：[2602.06550v1](https://arxiv.org/abs/2602.06550) · [PDF](https://arxiv.org/pdf/2602.06550.pdf)  
**作者**：Jan Benad, Pradeep Kr. Banerjee, Frank Röder, Nihat Ay, Martin V. Butz, Manfred Eppe  

**一句话要点**：提出DMA*-SH框架，通过共享超网络调制解决零样本执行器反转问题。

**关键词**：零样本泛化, 上下文强化学习, 执行器反转, 超网络调制, 动态预测, 基准测试

## 3 点简述
- 核心问题：零样本泛化在上下文强化学习中面临挑战，特别是执行器反转导致相同动作产生相反物理效应。
- 方法要点：使用单一超网络生成共享适配器权重，结合输入输出归一化和随机掩码稳定上下文推断。
- 实验或效果：在Actuator Inversion Benchmark上实现零样本泛化，性能超越领域随机化和基线方法。

## 摘要（原文）

> Zero-shot generalization in contextual reinforcement learning remains a core challenge, particularly when the context is latent and must be inferred from data. A canonical failure mode is actuator inversion, where identical actions produce opposite physical effects under a latent binary context. We propose DMA*-SH, a framework where a single hypernetwork, trained solely via dynamics prediction, generates a small set of adapter weights shared across the dynamics model, policy, and action-value function. This shared modulation imparts an inductive bias matched to actuator inversion, while input/output normalization and random input masking stabilize context inference, promoting directionally concentrated representations. We provide theoretical support via an expressivity separation result for hypernetwork modulation, and a variance decomposition with policy-gradient variance bounds that formalize how within-mode compression improves learning under actuator inversion. For evaluation, we introduce the Actuator Inversion Benchmark (AIB), a suite of environments designed to isolate discontinuous context-to-dynamics interactions. On AIB's held-out actuator-inversion tasks, DMA*-SH achieves zero-shot generalization, outperforming domain randomization by 111.8% and surpassing a standard context-aware baseline by 16.1%.


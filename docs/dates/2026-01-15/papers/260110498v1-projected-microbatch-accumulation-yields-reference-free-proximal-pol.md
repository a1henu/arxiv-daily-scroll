---
layout: default
title: Projected Microbatch Accumulation yields reference-free proximal policy updates for reinforcement learning
---

# Projected Microbatch Accumulation yields reference-free proximal policy updates for reinforcement learning
**arXiv**：[2601.10498v1](https://arxiv.org/abs/2601.10498) · [PDF](https://arxiv.org/pdf/2601.10498.pdf)  
**作者**：Nilin Abrahamsen  

**一句话要点**：提出PROMA方法，用于大语言模型微调中的近端策略更新，无需参考策略或似然比裁剪。

**关键词**：近端策略优化, 大语言模型微调, 梯度投影, 策略学习稳定性, KL散度控制

## 3 点简述
- 核心问题：传统近端策略优化方法如PPO和GRPO依赖参考策略或易导致熵崩溃，影响稳定性。
- 方法要点：PROMA通过投影去除序列梯度分量，在微批次聚合前进行层间投影，实现高效近端更新。
- 实验或效果：相比GRPO，PROMA能更严格控制局部KL散度，提升策略学习稳定性，避免熵崩溃。

## 摘要（原文）

> This note introduces Projected Microbatch Accumulation (PROMA), a proximal policy update method for large language model fine-tuning. PROMA accumulates policy gradients across microbatches by projecting out sequence-wise gradient components before microbatch aggregation. The projection is applied layer-wise during the backward pass, enabling efficient implementation without additional forward or backward passes. Empirically, PROMA enforces tighter control of local KL divergence than GRPO, resulting in more stable policy learning. Unlike PPO and GRPO, PROMA achieves proximal updates without inducing entropy collapse and does not rely on a reference policy or likelihood-ratio clipping.


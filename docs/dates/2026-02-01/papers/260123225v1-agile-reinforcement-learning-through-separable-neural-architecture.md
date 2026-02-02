---
layout: default
title: Agile Reinforcement Learning through Separable Neural Architecture
---

# Agile Reinforcement Learning through Separable Neural Architecture
**arXiv**：[2601.23225v1](https://arxiv.org/abs/2601.23225) · [PDF](https://arxiv.org/pdf/2601.23225.pdf)  
**作者**：Rajib Mostakim, Reza T. Batley, Sourav Saha  

**一句话要点**：提出SPAN以解决资源受限环境中强化学习的参数和样本效率问题

**关键词**：强化学习, 参数效率, 样条网络, 资源受限环境, 样本效率

## 3 点简述
- 核心问题：多层感知机在强化学习中参数效率低，影响样本效率和策略学习
- 方法要点：基于可分离张量积B样条基和可学习预处理层，改进KHRONOS框架
- 实验或效果：在离散和连续控制任务中，样本效率提升30-50%，成功率提高1.3-9倍

## 摘要（原文）

> Deep reinforcement learning (RL) is increasingly deployed in resource-constrained environments, yet the go-to function approximators - multilayer perceptrons (MLPs) - are often parameter-inefficient due to an imperfect inductive bias for the smooth structure of many value functions. This mismatch can also hinder sample efficiency and slow policy learning in this capacity-limited regime. Although model compression techniques exist, they operate post-hoc and do not improve learning efficiency. Recent spline-based separable architectures - such as Kolmogorov-Arnold Networks (KANs) - have been shown to offer parameter efficiency but are widely reported to exhibit significant computational overhead, especially at scale.
>   In seeking to address these limitations, this work introduces SPAN (SPline-based Adaptive Networks), a novel function approximation approach to RL. SPAN adapts the low rank KHRONOS framework by integrating a learnable preprocessing layer with a separable tensor product B-spline basis. SPAN is evaluated across discrete (PPO) and high-dimensional continuous (SAC) control tasks, as well as offline settings (Minari/D4RL). Empirical results demonstrate that SPAN achieves a 30-50% improvement in sample efficiency and 1.3-9 times higher success rates across benchmarks compared to MLP baselines. Furthermore, SPAN demonstrates superior anytime performance and robustness to hyperparameter variations, suggesting it as a viable, high performance alternative for learning intrinsically efficient policies in resource-limited settings.


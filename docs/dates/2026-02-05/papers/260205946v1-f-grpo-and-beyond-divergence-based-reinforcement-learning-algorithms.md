---
layout: default
title: $f$-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment
---

# $f$-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment
**arXiv**：[2602.05946v1](https://arxiv.org/abs/2602.05946) · [PDF](https://arxiv.org/pdf/2602.05946.pdf)  
**作者**：Rajdeep Haldar, Lantao Mei, Guang Lin, Yue Xing, Qifan Song  

**一句话要点**：提出$f$-GRPO和$f$-HAL，基于$f$-散度统一框架解决通用LLM对齐问题。

**关键词**：大语言模型对齐, 强化学习, $f$-散度, 偏好对齐, 奖励优化, 变分表示

## 3 点简述
- 核心问题：将偏好对齐的散度视角扩展到通用对齐场景，如仅环境奖励的强化学习。
- 方法要点：基于$f$-散度变分表示，提出$f$-GRPO和$f$-HAL两类目标，理论保证提升平均奖励。
- 实验或效果：在数学推理和安全对齐任务上验证，性能优于现有方法，展现灵活性。

## 摘要（原文）

> Recent research shows that Preference Alignment (PA) objectives act as divergence estimators between aligned (chosen) and unaligned (rejected) response distributions. In this work, we extend this divergence-based perspective to general alignment settings, such as reinforcement learning with verifiable rewards (RLVR), where only environmental rewards are available. Within this unified framework, we propose $f$-Group Relative Policy Optimization ($f$-GRPO), a class of on-policy reinforcement learning, and $f$-Hybrid Alignment Loss ($f$-HAL), a hybrid on/off policy objectives, for general LLM alignment based on variational representation of $f$-divergences. We provide theoretical guarantees that these classes of objectives improve the average reward after alignment. Empirically, we validate our framework on both RLVR (Math Reasoning) and PA tasks (Safety Alignment), demonstrating superior performance and flexibility compared to current methods.


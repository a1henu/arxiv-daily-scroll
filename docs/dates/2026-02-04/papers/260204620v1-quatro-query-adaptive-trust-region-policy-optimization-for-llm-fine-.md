---
layout: default
title: QUATRO: Query-Adaptive Trust Region Policy Optimization for LLM Fine-tuning
---

# QUATRO: Query-Adaptive Trust Region Policy Optimization for LLM Fine-tuning
**arXiv**：[2602.04620v1](https://arxiv.org/abs/2602.04620) · [PDF](https://arxiv.org/pdf/2602.04620.pdf)  
**作者**：Doyeon Lee, Eunyi Lyou, Hyunsoo Cho, Sookyung Kim, Joonseok Lee, Jaemoo Choi  

**一句话要点**：提出QUATRO以解决GRPO风格LLM微调中启发式信任区域近似导致的优化不稳定问题

**关键词**：LLM微调, 强化学习, 信任区域优化, 策略优化, 数学推理, 熵控制

## 3 点简述
- 核心问题：GRPO风格RL微调依赖启发式信任区域近似，全局重要性比率裁剪和组归一化无法有效调控超出裁剪范围的样本，导致优化脆弱
- 方法要点：QUATRO通过原则性优化直接强制执行信任区域约束，提供清晰可解释目标，实现显式策略更新控制和稳定熵控优化
- 实验或效果：在多样化数学推理基准上验证，QUATRO在增加策略陈旧性和激进学习率下保持稳定训练，全程维持良好熵控

## 摘要（原文）

> GRPO-style reinforcement learning (RL)-based LLM fine-tuning algorithms have recently gained popularity. Relying on heuristic trust-region approximations, however, they can lead to brittle optimization behavior, as global importance-ratio clipping and group-wise normalization fail to regulate samples whose importance ratios fall outside the clipping range. We propose Query-Adaptive Trust-Region policy Optimization (QUATRO), which directly enforces trust-region constraints through a principled optimization. This yields a clear and interpretable objective that enables explicit control over policy updates and stable, entropy-controlled optimization, with a stabilizer terms arising intrinsically from the exact trust-region formulation. Empirically verified on diverse mathematical reasoning benchmarks, QUATRO shows stable training under increased policy staleness and aggressive learning rates, maintaining well-controlled entropy throughout training.


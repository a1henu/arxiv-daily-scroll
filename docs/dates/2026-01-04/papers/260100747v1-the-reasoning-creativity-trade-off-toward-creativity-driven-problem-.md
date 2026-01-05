---
layout: default
title: The Reasoning-Creativity Trade-off: Toward Creativity-Driven Problem Solving
---

# The Reasoning-Creativity Trade-off: Toward Creativity-Driven Problem Solving
**arXiv**：[2601.00747v1](https://arxiv.org/abs/2601.00747) · [PDF](https://arxiv.org/pdf/2601.00747.pdf)  
**作者**：Max Ruiz Luyten, Mihaela van der Schaar  

**一句话要点**：提出分布创造性推理框架以解决大语言模型推理与创造性的权衡问题

**关键词**：大语言模型, 创造性推理, 分布坍缩, 变分目标, 梯度流, 问题解决

## 3 点简述
- 分析现有LLM推理循环导致分布坍缩，削弱创造性问题解决能力
- 引入统一变分目标DCR，将训练建模为解迹概率测度的梯度流
- 提供理论结果与实用方法，确保模型保持正确性和创造性

## 摘要（原文）

> State-of-the-art large language model (LLM) pipelines rely on bootstrapped reasoning loops: sampling diverse chains of thought and reinforcing the highest-scoring ones, mainly optimizing correctness. We analyze how this design choice is sensitive to the collapse of the model's distribution over reasoning paths, slashing semantic entropy and undermining creative problem-solving. To analyze this failure, we introduce Distributional Creative Reasoning (DCR), a unified variational objective that casts training as gradient flow through probability measures on solution traces. STaR, GRPO, and DPO, as well as entropy bonuses, and other methods, all constitute special cases of the same loss. The framework delivers three core results: (i) the diversity decay theorem, describing how correctness-based objectives lead to distinct modes of diversity decay for STaR, GRPO, and DPO; (ii) designs that ensure convergence to a stable and diverse policy, effectively preventing collapse; and (iii) simple, actionable recipes to achieve this in practice. DCR thus offers the first principled recipe for LLMs that remain both correct and creative.


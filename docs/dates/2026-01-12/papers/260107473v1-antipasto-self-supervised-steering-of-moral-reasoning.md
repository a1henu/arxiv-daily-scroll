---
layout: default
title: AntiPaSTO: Self-Supervised Steering of Moral Reasoning
---

# AntiPaSTO: Self-Supervised Steering of Moral Reasoning
**arXiv**：[2601.07473v1](https://arxiv.org/abs/2601.07473) · [PDF](https://arxiv.org/pdf/2601.07473.pdf)  
**作者**：Michael J. Clark  

**一句话要点**：提出AntiPaSTO方法，通过自监督表征分离实现大模型道德推理的可扩展监督。

**关键词**：道德推理, 自监督学习, 表征分离, 可扩展监督, 大语言模型

## 3 点简述
- 核心问题：大模型能力增强时，人类监督难以扩展，标签不足、输出可被操控且泛化性差。
- 方法要点：引入反平行轴分离表征，通过一致性约束防止崩溃，仅需少量对比词对作为输入。
- 实验或效果：在Gemma-3-1B上使用800词对，DailyDilemmas任务性能提升6.9倍，保持双向控制。

## 摘要（原文）

> As models grow more capable, human supervision breaks down: labels don't scale, outputs can be gamed, and training doesn't generalize. Scalable oversight requires steering methods that are internal, self-supervised, and transfer out-of-distribution; existing methods satisfy some but not all three. We introduce AntiPaSTO, which separates representations along an anti-parallel axis ($α=\pm1$ produce opposite shifts), with coherence constraints preventing collapse. Human input is minimal: two contrasting words inserted into template sentences, no preference labels. Using 800 such pairs on Gemma-3-1B, AntiPaSTO beats prompting baselines by $6.9\times$ on DailyDilemmas and maintains bidirectional control where prompting triggers refusal.
>   Code is available at https://github.com/wassname/AntiPaSTO.


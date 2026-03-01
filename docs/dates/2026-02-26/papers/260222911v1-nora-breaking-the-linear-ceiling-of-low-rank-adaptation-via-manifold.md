---
layout: default
title: NoRA: Breaking the Linear Ceiling of Low-Rank Adaptation via Manifold Expansion
---

# NoRA: Breaking the Linear Ceiling of Low-Rank Adaptation via Manifold Expansion
**arXiv**：[2602.22911v1](https://arxiv.org/abs/2602.22911) · [PDF](https://arxiv.org/pdf/2602.22911.pdf)  
**作者**：Hung-Hsuan Chen  

**一句话要点**：提出NoRA以解决LoRA在复杂推理任务中的线性天花板问题

**关键词**：低秩适应, 参数高效微调, 非线性适配器, 流形扩展, 复杂推理任务

## 3 点简述
- LoRA在复杂推理任务中面临线性天花板，增加秩的收益递减
- NoRA通过SiLU门控和结构化dropout引入非线性，实现流形扩展
- 在SlimOrca和MathInstruct基准上，NoRA以更低秩超越LoRA性能

## 摘要（原文）

> Low-Rank Adaptation (LoRA) dominates parameter-efficient fine-tuning (PEFT). However, it faces a critical ``linear ceiling'' in complex reasoning tasks: simply increasing the rank yields diminishing returns due to intrinsic linear constraints. We introduce NoRA (Non-linear Rank Adaptation), a weight-level parallel adapter that injects SiLU gating and structural dropout to induce manifold expansion. On the SlimOrca benchmark, NoRA breaks this linear barrier: NoRA remarkably at rank 64 (PPL 3.89) outperforms LoRA at rank 512 (PPL 3.90), demonstrating superior spectral efficiency. This advantage generalizes to mathematical reasoning, where NoRA achieves a perplexity of 1.97 on MathInstruct, significantly surpassing LoRA's saturation point of 2.07. Mechanism analysis via Singular Value Decomposition (SVD) confirms that NoRA activates the dormant tail of the singular value spectrum, effectively preventing the rank collapse observed in linear methods.


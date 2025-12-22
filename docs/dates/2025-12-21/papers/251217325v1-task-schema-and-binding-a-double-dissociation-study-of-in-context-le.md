---
layout: default
title: Task Schema and Binding: A Double Dissociation Study of In-Context Learning
---

# Task Schema and Binding: A Double Dissociation Study of In-Context Learning
**arXiv**：[2512.17325v1](https://arxiv.org/abs/2512.17325) · [PDF](https://arxiv.org/pdf/2512.17325.pdf)  
**作者**：Chaeha Kim  

**一句话要点**：提出任务模式与绑定双重分离机制，以解释上下文学习的内在机理

**关键词**：上下文学习, 任务模式, 绑定机制, 激活修补, 双重分离, 先验知识

## 3 点简述
- 核心问题：上下文学习是否由单一机制驱动，还是可分解为不同组件
- 方法要点：通过激活修补实验，在Transformer和Mamba模型中验证任务模式与绑定的可分离性
- 实验或效果：发现任务模式完全可转移，绑定部分可转移，且机制依赖与先验知识呈负相关

## 摘要（原文）

> We provide causal mechanistic validation that in-context learning (ICL) decomposes into two separable mechanisms: Task Schema (abstract task type recognition) and Binding (specific input-output associations). Through activation patching experiments across 9 models from 7 Transformer families plus Mamba (370M-13B parameters), we establish three key findings:
>   1. Double dissociation: Task Schema transfers at 100% via late MLP patching; Binding transfers at 62% via residual stream patching -- proving separable mechanisms
>   2. Prior-Schema trade-off: Schema reliance inversely correlates with prior knowledge (Spearman rho = -0.596, p < 0.001, N=28 task-model pairs)
>   3. Architecture generality: The mechanism operates across all tested architectures including the non-Transformer Mamba
>   These findings offer a mechanistic account of the ICL puzzle that contrasts with prior views treating ICL as a monolithic mechanism (whether retrieval-based, gradient descent-like, or purely Bayesian). By establishing that Schema and Binding are neurally dissociable -- not merely behavioral modes -- we provide causal evidence for dual-process theories of ICL. Models rely on Task Schema when prior knowledge is absent, but prior knowledge interferes through attentional mis-routing (72.7% recency bias) rather than direct output competition (0%). This explains why arbitrary mappings succeed (zero prior leads to full Schema reliance) while factual overrides fail -- and reveals that the true bottleneck is attentional, not output-level. Practical implications: Understanding these dual mechanisms enables more efficient prompt engineering -- reliable schema transfer reduces required demonstrations for novel tasks, while prior-aware design can mitigate the 38% binding failure rate in high-prior scenarios, improving ICL system reliability in production deployments.


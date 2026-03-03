---
layout: default
title: Recursive Models for Long-Horizon Reasoning
---

# Recursive Models for Long-Horizon Reasoning
**arXiv**：[2603.02112v1](https://arxiv.org/abs/2603.02112) · [PDF](https://arxiv.org/pdf/2603.02112.pdf)  
**作者**：Chenxiao Yang, Nathan Srebro, Zhiyuan Li  

**一句话要点**：提出递归模型以解决语言模型在长视野推理中的上下文限制问题

**关键词**：递归模型, 长视野推理, 上下文管理, 布尔可满足性, 计算理论

## 3 点简述
- 核心问题：现代语言模型受限于有界上下文，阻碍长视野推理。
- 方法要点：基于递归原则，模型可递归调用自身在隔离上下文中解决子任务。
- 实验效果：在布尔可满足性任务上，3B递归模型显著优于前沿大语言模型。

## 摘要（原文）

> Modern language models reason within bounded context, an inherent constraint that poses a fundamental barrier to long-horizon reasoning. We identify recursion as a core principle for overcoming this barrier, and propose recursive models as a minimal realization, where the model can recursively invoke itself to solve subtasks in isolated contexts. We prove that any computable problem admits a recursive decomposition in which each subtask requires only exponentially smaller active context than standard autoregressive models; this strictly surpasses any context management approach confined to a single sequence, such as summarization. We further generalize our framework to modern agentic systems with arbitrary context processing and control flows, and prove that recursive models can achieve optimal power within this broader class. Experimentally, we train a 3B model to reason recursively and evaluate on Boolean satisfiability, a task requiring long-horizon combinatorial search, where it significantly outperforms frontier LLMs.


---
layout: default
title: Replaying pre-training data improves fine-tuning
---

# Replaying pre-training data improves fine-tuning
**arXiv**：[2603.04964v1](https://arxiv.org/abs/2603.04964) · [PDF](https://arxiv.org/pdf/2603.04964.pdf)  
**作者**：Suhas Kotha, Percy Liang  

**一句话要点**：提出在微调中重放通用数据以提升目标领域性能，提高数据效率。

**关键词**：语言模型微调, 数据重放, 目标领域适应, 预训练策略, 数据效率提升

## 3 点简述
- 核心问题：微调时仅混合通用数据防遗忘，但重放通用数据能否提升目标任务性能未知。
- 方法要点：在预训练环境中，微调或中训练时重放通用数据，分析数据调度策略。
- 实验或效果：在4B令牌和150M参数模型中，重放使目标数据效率提升最高2.06倍，并在8B参数模型中验证实际应用效果。

## 摘要（原文）

> To obtain a language model for a target domain (e.g. math), the current paradigm is to pre-train on a vast amount of generic web text and then fine-tune on the relatively limited amount of target data. Typically, generic data is only mixed in during fine-tuning to prevent catastrophic forgetting of the generic domain. We surprisingly find that replaying the generic data during fine-tuning can actually improve performance on the (less related) target task. Concretely, in a controlled pre-training environment with 4M target tokens, 4B total tokens, and 150M parameter models, generic replay increases target data efficiency by up to $1.87\times$ for fine-tuning and $2.06\times$ for mid-training. We further analyze data schedules that introduce target data during pre-training and find that replay helps more when there is less target data present in pre-training. We demonstrate the success of replay in practice for fine-tuning 8B parameter models, improving agentic web navigation success by $4.5\%$ and Basque question-answering accuracy by $2\%$.


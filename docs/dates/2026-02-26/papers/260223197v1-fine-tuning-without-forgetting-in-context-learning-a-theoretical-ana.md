---
layout: default
title: Fine-Tuning Without Forgetting In-Context Learning: A Theoretical Analysis of Linear Attention Models
---

# Fine-Tuning Without Forgetting In-Context Learning: A Theoretical Analysis of Linear Attention Models
**arXiv**：[2602.23197v1](https://arxiv.org/abs/2602.23197) · [PDF](https://arxiv.org/pdf/2602.23197.pdf)  
**作者**：Chungpa Lee, Jy-yong Sohn, Kangwook Lee  

**一句话要点**：分析线性注意力模型中微调对上下文学习的影响，提出参数更新策略以平衡零样本与少样本性能

**关键词**：线性注意力模型, 上下文学习, 微调优化, 零样本性能, 少样本学习, 理论分析

## 3 点简述
- 核心问题：微调大语言模型可能损害上下文学习能力，限制模型在未见过任务上的表现
- 方法要点：理论分析线性注意力模型，识别微调目标如何修改注意力参数及导致性能下降的条件
- 实验或效果：实证验证理论结果，显示限制值矩阵更新可改善零样本性能并保持上下文学习

## 摘要（原文）

> Transformer-based large language models exhibit in-context learning, enabling adaptation to downstream tasks via few-shot prompting with demonstrations. In practice, such models are often fine-tuned to improve zero-shot performance on downstream tasks, allowing them to solve tasks without examples and thereby reducing inference costs. However, fine-tuning can degrade in-context learning, limiting the performance of fine-tuned models on tasks not seen during fine-tuning. Using linear attention models, we provide a theoretical analysis that characterizes how fine-tuning objectives modify attention parameters and identifies conditions under which this leads to degraded few-shot performance. We show that fine-tuning all attention parameters can harm in-context learning, whereas restricting updates to the value matrix improves zero-shot performance while preserving in-context learning. We further show that incorporating an auxiliary few-shot loss enhances in-context learning primarily on the target task, at the expense of degraded in-context learning ability on tasks not seen during fine-tuning. We empirically validate our theoretical results.


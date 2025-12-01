---
layout: default
title: Adversarial Training for Process Reward Models
---

# Adversarial Training for Process Reward Models
**arXiv**：[2511.22888v1](https://arxiv.org/abs/2511.22888) · [PDF](https://arxiv.org/pdf/2511.22888.pdf)  
**作者**：Gurusha Juneja, Deepak Nathani, William Yang Wang  

**一句话要点**：提出对抗训练过程奖励模型以解决推理错误检测的泛化问题

**关键词**：过程奖励模型, 对抗训练, 推理错误检测, 数学推理, 泛化能力, 自动标注

## 3 点简述
- 核心问题：过程奖励模型依赖昂贵人工标注且对新颖错误泛化差
- 方法要点：通过生成器与奖励模型对抗训练，自动生成渐进式负样本
- 实验或效果：在数学推理基准上平均提升3.4个百分点，分布外任务提升5.3个百分点

## 摘要（原文）

> Process Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors. We introduce Adversarially Trained PRMs (\texttt{APRM}), where a Generator ($G$) learns to produce reasoning errors to deceive a PRM ($R$), while $R$ concurrently learns to detect them. This interaction yields progressively harder negatives for $R$, improving its robustness and generalization to novel errors without requiring manual step-level labels. Averaged across diverse mathematical reasoning benchmarks, \texttt{APRM} improves solver accuracy by $+3.4$ percentage points (pp) over the strongest PRM baseline. \texttt{APRM} achieves gains of $+5.3$ pp on out-of-distribution tasks.


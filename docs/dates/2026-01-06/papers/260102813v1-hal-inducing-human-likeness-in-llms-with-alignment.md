---
layout: default
title: HAL: Inducing Human-likeness in LLMs with Alignment
---

# HAL: Inducing Human-likeness in LLMs with Alignment
**arXiv**：[2601.02813v1](https://arxiv.org/abs/2601.02813) · [PDF](https://arxiv.org/pdf/2601.02813.pdf)  
**作者**：Masum Hasan, Junjie Zhao, Ehsan Hoque  

**一句话要点**：提出HAL框架，通过可解释奖励对齐LLMs以提升对话人类相似性

**关键词**：对话对齐, 可解释奖励, 人类相似性, 偏好优化, 语言模型对齐

## 3 点简述
- 核心问题：对话人类相似性难以定义、测量和优化，现有方法依赖规模或宽泛监督训练
- 方法要点：从对比对话数据提取显式对话特征，组合为紧凑标量分数，用作透明奖励信号进行对齐
- 实验或效果：对齐后模型在人类评估中更常被感知为人类相似，且不影响整体性能

## 摘要（原文）

> Conversational human-likeness plays a central role in human-AI interaction, yet it has remained difficult to define, measure, and optimize. As a result, improvements in human-like behavior are largely driven by scale or broad supervised training, rather than targeted alignment. We introduce Human Aligning LLMs (HAL), a framework for aligning language models to conversational human-likeness using an interpretable, data-driven reward. HAL derives explicit conversational traits from contrastive dialogue data, combines them into a compact scalar score, and uses this score as a transparent reward signal for alignment with standard preference optimization methods. Using this approach, we align models of varying sizes without affecting their overall performance. In large-scale human evaluations, models aligned with HAL are more frequently perceived as human-like in conversation. Because HAL operates over explicit, interpretable traits, it enables inspection of alignment behavior and diagnosis of unintended effects. More broadly, HAL demonstrates how soft, qualitative properties of language--previously outside the scope for alignment--can be made measurable and aligned in an interpretable and explainable way.


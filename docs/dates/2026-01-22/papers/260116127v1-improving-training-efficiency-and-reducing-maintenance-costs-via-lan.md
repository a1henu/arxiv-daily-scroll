---
layout: default
title: Improving Training Efficiency and Reducing Maintenance Costs via Language Specific Model Merging
---

# Improving Training Efficiency and Reducing Maintenance Costs via Language Specific Model Merging
**arXiv**：[2601.16127v1](https://arxiv.org/abs/2601.16127) · [PDF](https://arxiv.org/pdf/2601.16127.pdf)  
**作者**：Alphaeus Dmonte, Vidhi Gupta, Daniel J Perry, Mark Arehart  

**一句话要点**：提出语言特定模型合并方法以提高多语言大模型训练效率并降低维护成本

**关键词**：多语言大模型, 模型合并, 训练效率, 维护成本, 语言特定模型

## 3 点简述
- 核心问题：多语言大模型更新或添加语言时需全模型重训练，计算效率低且维护瓶颈严重。
- 方法要点：通过合并语言特定模型，减少初始训练时间和更新成本，保持质量不变。
- 实验或效果：在三个任务中验证，初始训练时间减少达50%，更新语言时训练成本降低超60%。

## 摘要（原文）

> Fine-tuning a task-specific multilingual large language model (LLM) involves training the model on a multilingual dataset with examples in all the required languages. Updating one or more supported languages with additional data or adding support for a new language involves retraining the model, which can be computationally inefficient and creates a severe maintenance bottleneck. Recent research on merging multilingual multitask models has shown promise in terms of improved quality, but its computational and maintenance efficiency remains unstudied. In this work, we provide the first focused analysis of this merging strategy from an efficiency perspective, evaluating it across three independent tasks. We demonstrate significant efficiency gains while maintaining parity in terms of quality: this merging approach reduces the initial training time by up to 50\%. We also demonstrate that updating an individual language and re-merging as part of model maintenance reduces training costs by more than 60\%, compared to re-training the full multilingual model. We show this on both public and proprietary industry datasets confirming that the approach works well for industrial use cases in addition to academic settings already studied in previous work.


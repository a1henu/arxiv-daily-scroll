---
layout: default
title: Fluent Alignment with Disfluent Judges: Post-training for Lower-resource Languages
---

# Fluent Alignment with Disfluent Judges: Post-training for Lower-resource Languages
**arXiv**：[2512.08777v1](https://arxiv.org/abs/2512.08777) · [PDF](https://arxiv.org/pdf/2512.08777.pdf)  
**作者**：David Samuel, Lilja Øvrelid, Erik Velldal, Andrey Kutuzov  

**一句话要点**：提出后训练方法以在低资源语言中实现流畅偏好对齐，无需目标语言指令数据。

**关键词**：低资源语言, 偏好对齐, 后训练, 在线策略训练, 流畅性评估, 语言模型

## 3 点简述
- 核心问题：低资源语言缺乏母语数据集和流畅生成模型，偏好对齐易受不流畅奖励模型影响。
- 方法要点：采用在线策略训练，避免依赖机器翻译或多语言微调，无需目标语言指令数据。
- 实验或效果：以挪威语为例，通过母语者评估，在线策略方法优于替代方案，提升流畅性。

## 摘要（原文）

> We propose a post-training method for lower-resource languages that preserves fluency of language models even when aligned by disfluent reward models. Preference-optimization is now a well-researched topic, but previous work has mostly addressed models for English and Chinese. Lower-resource languages lack both datasets written by native speakers and language models capable of generating fluent synthetic data. Thus, in this work, we focus on developing a fluent preference-aligned language model without any instruction-tuning data in the target language. Our approach uses an on-policy training method, which we compare with two common approaches: supervised finetuning on machine-translated data and multilingual finetuning. We conduct a case study on Norwegian Bokmål and evaluate fluency through native-speaker assessments. The results show that the on-policy aspect is crucial and outperforms the alternatives without relying on any hard-to-obtain data.


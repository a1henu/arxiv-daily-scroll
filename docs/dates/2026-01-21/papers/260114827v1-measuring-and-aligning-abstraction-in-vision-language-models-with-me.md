---
layout: default
title: Measuring and Aligning Abstraction in Vision-Language Models with Medical Taxonomies
---

# Measuring and Aligning Abstraction in Vision-Language Models with Medical Taxonomies
**arXiv**：[2601.14827v1](https://arxiv.org/abs/2601.14827) · [PDF](https://arxiv.org/pdf/2601.14827.pdf)  
**作者**：Ben Schaper, Maxime Di Folco, Bernhard Kainz, Julia A. Schnabel, Cosmin I. Bercea  

**一句话要点**：提出风险约束阈值与分类感知微调，以减少医学视觉语言模型在胸片分类中的抽象错误。

**关键词**：视觉语言模型, 医学分类法, 抽象错误, 分层评估, 胸片分类, 径向嵌入

## 3 点简述
- 核心问题：标准平坦指标无法区分临床轻微与严重错误，需量化抽象错误。
- 方法要点：利用医学分类法进行分层评估，引入灾难性抽象错误指标，并提出风险约束阈值与径向嵌入微调。
- 实验或效果：将严重抽象错误降至2%以下，同时保持竞争性性能，强调分层评估的重要性。

## 摘要（原文）

> Vision-Language Models show strong zero-shot performance for chest X-ray classification, but standard flat metrics fail to distinguish between clinically minor and severe errors. This work investigates how to quantify and mitigate abstraction errors by leveraging medical taxonomies. We benchmark several state-of-the-art VLMs using hierarchical metrics and introduce Catastrophic Abstraction Errors to capture cross-branch mistakes. Our results reveal substantial misalignment of VLMs with clinical taxonomies despite high flat performance. To address this, we propose risk-constrained thresholding and taxonomy-aware fine-tuning with radial embeddings, which reduce severe abstraction errors to below 2 per cent while maintaining competitive performance. These findings highlight the importance of hierarchical evaluation and representation-level alignment for safer and more clinically meaningful deployment of VLMs.


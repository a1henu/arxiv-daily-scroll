---
layout: default
title: Grow Up and Merge: Scaling Strategies for Efficient Language Adaptation
---

# Grow Up and Merge: Scaling Strategies for Efficient Language Adaptation
**arXiv**：[2512.10772v1](https://arxiv.org/abs/2512.10772) · [PDF](https://arxiv.org/pdf/2512.10772.pdf)  
**作者**：Kevin Glocker, Kätriin Kukk, Romina Oji, Marcel Bollmann, Marco Kuhlmann, Jenny Kunz  

**一句话要点**：提出缩放策略以高效适应新语言，提升数据效率并减少灾难性遗忘。

**关键词**：语言模型缩放, 多语言适应, 数据效率, 灾难性遗忘, 模型合并

## 3 点简述
- 核心问题：多语言模型在低资源语言上性能不足，且小规模模型适应效果差。
- 方法要点：通过缩放英语基础模型，测试其在新语言适应中的效率和性能。
- 实验或效果：缩放模型在数据效率上优于持续预训练，并探索模型合并以构建多语言系统。

## 摘要（原文）

> Achieving high-performing language models which include medium- and lower-resource languages remains a challenge. Massively multilingual models still underperform compared to language-specific adaptations, especially at smaller model scales. In this work, we investigate scaling as an efficient strategy for adapting pretrained models to new target languages. Through comprehensive scaling ablations with approximately FLOP-matched models, we test whether upscaling an English base model enables more effective and resource-efficient adaptation than standard continued pretraining. We find that, once exposed to sufficient target-language data, larger upscaled models can match or surpass the performance of smaller models continually pretrained on much more data, demonstrating the benefits of scaling for data efficiency. Scaling also helps preserve the base model's capabilities in English, thus reducing catastrophic forgetting. Finally, we explore whether such scaled, language-specific models can be merged to construct modular and flexible multilingual systems. We find that while merging remains less effective than joint multilingual training, upscaled merges perform better than smaller ones. We observe large performance differences across merging methods, suggesting potential for improvement through merging approaches specialized for language-level integration.


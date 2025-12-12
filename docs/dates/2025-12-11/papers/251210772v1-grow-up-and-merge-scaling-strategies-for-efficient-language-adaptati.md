---
layout: default
title: Grow Up and Merge: Scaling Strategies for Efficient Language Adaptation
---

# Grow Up and Merge: Scaling Strategies for Efficient Language Adaptation
**arXiv**：[2512.10772v1](https://arxiv.org/abs/2512.10772) · [PDF](https://arxiv.org/pdf/2512.10772.pdf)  
**作者**：Kevin Glocker, Kätriin Kukk, Romina Oji, Marcel Bollmann, Marco Kuhlmann, Jenny Kunz  

**一句话要点**：提出基于模型放缩的高效语言适应策略，以提升低资源语言性能并减少灾难性遗忘。

**关键词**：语言模型适应, 模型放缩, 多语言系统, 灾难性遗忘, 模型合并

## 3 点简述
- 核心问题：多语言模型在低资源语言上性能不足，且小规模模型适应效率低。
- 方法要点：通过模型放缩策略，在目标语言数据上扩展英语基础模型，替代传统持续预训练。
- 实验或效果：放缩模型在数据效率上优于小模型，能保持英语能力，合并后性能优于小规模合并。

## 摘要（原文）

> Achieving high-performing language models which include medium- and lower-resource languages remains a challenge. Massively multilingual models still underperform compared to language-specific adaptations, especially at smaller model scales. In this work, we investigate scaling as an efficient strategy for adapting pretrained models to new target languages. Through comprehensive scaling ablations with approximately FLOP-matched models, we test whether upscaling an English base model enables more effective and resource-efficient adaptation than standard continued pretraining. We find that, once exposed to sufficient target-language data, larger upscaled models can match or surpass the performance of smaller models continually pretrained on much more data, demonstrating the benefits of scaling for data efficiency. Scaling also helps preserve the base model's capabilities in English, thus reducing catastrophic forgetting. Finally, we explore whether such scaled, language-specific models can be merged to construct modular and flexible multilingual systems. We find that while merging remains less effective than joint multilingual training, upscaled merges perform better than smaller ones. We observe large performance differences across merging methods, suggesting potential for improvement through merging approaches specialized for language-level integration.


---
layout: default
title: TiME: Tiny Monolingual Encoders for Efficient NLP Pipelines
---

# TiME: Tiny Monolingual Encoders for Efficient NLP Pipelines
**arXiv**：[2512.14645v1](https://arxiv.org/abs/2512.14645) · [PDF](https://arxiv.org/pdf/2512.14645.pdf)  
**作者**：David Schulmeister, Valentin Hartmann, Lars Klein, Robert West  

**一句话要点**：提出TiME小型单语编码器，以解决NLP流水线中大型模型效率低下的问题。

**关键词**：小型语言模型, 蒸馏训练, 单语编码器, 效率优化, 低资源语言支持

## 3 点简述
- 核心问题：大型通用语言模型在NLP流水线中处理大数据或实时响应时效率不足，能耗高。
- 方法要点：采用蒸馏等现代训练技术，从多语言教师模型蒸馏单语模型，支持低资源语言。
- 实验或效果：在常见NLP任务上评估，实现性能与吞吐量、延迟、能耗之间的更好权衡。

## 摘要（原文）

> Today, a lot of research on language models is focused on large, general-purpose models. However, many NLP pipelines only require models with a well-defined, small set of capabilities. While large models are capable of performing the tasks of those smaller models, they are simply not fast enough to process large amounts of data or offer real-time responses. Furthermore, they often use unnecessarily large amounts of energy, leading to sustainability concerns and problems when deploying them on battery-powered devices. In our work, we show how to train small models for such efficiency-critical applications. As opposed to many off-the-shelf NLP pipelines, our models use modern training techniques such as distillation, and offer support for low-resource languages. We call our models TiME (Tiny Monolingual Encoders) and comprehensively evaluate them on a range of common NLP tasks, observing an improved trade-off between benchmark performance on one hand, and throughput, latency and energy consumption on the other. Along the way, we show that distilling monolingual models from multilingual teachers is possible, and likewise distilling models with absolute positional embeddings from teachers with relative positional embeddings.


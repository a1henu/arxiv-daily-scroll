---
layout: default
title: Multilingual VLM Training: Adapting an English-Trained VLM to French
---

# Multilingual VLM Training: Adapting an English-Trained VLM to French
**arXiv**：[2512.10336v1](https://arxiv.org/abs/2512.10336) · [PDF](https://arxiv.org/pdf/2512.10336.pdf)  
**作者**：Jules Lahmi, Alexis Roger  

**一句话要点**：提出多语言VLM适应方法，以解决英语训练模型在法语等非英语语言中的性能瓶颈问题。

**关键词**：多语言视觉语言模型, 模型适应, 数据集翻译, LoRA微调, 两阶段微调

## 3 点简述
- 核心问题：英语训练的VLM在非英语语言中性能受限，数据集翻译是主要瓶颈。
- 方法要点：比较翻译管道、LoRA微调和两阶段微调策略，分离视觉与语言适应。
- 实验或效果：使用翻译基准和专家评估，发现数据质量限制训练和评估效果。

## 摘要（原文）

> Artificial intelligence has made great progress in recent years, particularly in the development of Vision--Language Models (VLMs) that understand both visual and textual data. However, these advancements remain largely limited to English, reducing their accessibility for non--English speakers. It is essential to extend these capabilities to a broader range of languages. This paper explores the challenges of adapting an English-trained VLM to different languages. To this end, we will explore and compare different methods for their performance and computational cost. We consider a translation-based pipeline, LoRA finetuning, and a two-stage finetuning strategy that separates vision adaptation from language adaptation. To evaluate these methods, we use a combination of standard multimodal benchmarks translated into the target language and manual assessments by native experts. The results reveal that dataset translation remains a major bottleneck in multilingual VLM performance, with data quality limiting the effectiveness of training and evaluation. These findings suggest that future efforts should focus on native-language dataset collection and improved translation strategies.


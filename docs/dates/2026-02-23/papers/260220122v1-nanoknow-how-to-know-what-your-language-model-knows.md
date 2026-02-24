---
layout: default
title: NanoKnow: How to Know What Your Language Model Knows
---

# NanoKnow: How to Know What Your Language Model Knows
**arXiv**：[2602.20122v1](https://arxiv.org/abs/2602.20122) · [PDF](https://arxiv.org/pdf/2602.20122.pdf)  
**作者**：Lingwei Gu, Nour Jedidi, Jimmy Lin  

**一句话要点**：提出NanoKnow基准数据集以解决大语言模型知识来源难以解析的问题

**关键词**：大语言模型, 知识来源分析, 基准数据集, 参数化知识, 外部知识, 预训练数据透明度

## 3 点简述
- 核心问题：大语言模型的知识来源因预训练数据不透明而难以分析
- 方法要点：基于nanochat开放预训练数据，构建问题分割基准以区分参数化与外部知识
- 实验或效果：实验显示答案频率影响准确性，参数化与外部知识互补，非相关信息有害

## 摘要（原文）

> How do large language models (LLMs) know what they know? Answering this question has been difficult because pre-training data is often a "black box" -- unknown or inaccessible. The recent release of nanochat -- a family of small LLMs with fully open pre-training data -- addresses this as it provides a transparent view into where a model's parametric knowledge comes from. Towards the goal of understanding how knowledge is encoded by LLMs, we release NanoKnow, a benchmark dataset that partitions questions from Natural Questions and SQuAD into splits based on whether their answers are present in nanochat's pre-training corpus. Using these splits, we can now properly disentangle the sources of knowledge that LLMs rely on when producing an output. To demonstrate NanoKnow's utility, we conduct experiments using eight nanochat checkpoints. Our findings show: (1) closed-book accuracy is strongly influenced by answer frequency in the pre-training data, (2) providing external evidence can mitigate this frequency dependence, (3) even with external evidence, models are more accurate when answers were seen during pre-training, demonstrating that parametric and external knowledge are complementary, and (4) non-relevant information is harmful, with accuracy decreasing based on both the position and the number of non-relevant contexts. We release all NanoKnow artifacts at https://github.com/castorini/NanoKnow.


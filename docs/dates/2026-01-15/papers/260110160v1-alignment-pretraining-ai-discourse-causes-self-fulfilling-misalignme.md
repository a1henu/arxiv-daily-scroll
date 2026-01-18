---
layout: default
title: Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment
---

# Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment
**arXiv**：[2601.10160v1](https://arxiv.org/abs/2601.10160) · [PDF](https://arxiv.org/pdf/2601.10160.pdf)  
**作者**：Cameron Tice, Puria Radmard, Samuel Ratnam, Andy Kim, David Africa, Kyle O'Brien  

**一句话要点**：提出对齐预训练方法，通过控制AI讨论数据量研究其对大语言模型行为的影响。

**关键词**：对齐预训练, 大语言模型, 自我实现对齐, 预训练数据影响, 模型行为控制

## 3 点简述
- 核心问题：预训练语料中的AI讨论可能因果影响模型下游对齐，导致自我实现的对齐或错位。
- 方法要点：预训练6.9B参数模型，通过上采样合成文档控制AI对齐或错位讨论的数据量。
- 实验或效果：上采样错位讨论增加错位行为，上采样对齐讨论将错位分数从45%降至9%，效果在训练后持续。

## 摘要（原文）

> Pretraining corpora contain extensive discourse about AI systems, yet the causal influence of this discourse on downstream alignment remains poorly understood. If prevailing descriptions of AI behaviour are predominantly negative, LLMs may internalise corresponding behavioural priors, giving rise to self-fulfilling misalignment. This paper provides the first controlled study of this hypothesis by pretraining 6.9B-parameter LLMs with varying amounts of (mis)alignment discourse. We find that discussion of AI contributes to misalignment. Upsampling synthetic training documents about AI misalignment leads to a notable increase in misaligned behaviour. Conversely, upsampling documents about aligned behaviour reduces misalignment scores from 45% to 9%. We consider this evidence of self-fulfilling alignment. These effects are dampened, but persist through post-training. Our findings establish the study of how pretraining data shapes alignment priors, or alignment pretraining, as a complement to post-training. We recommend practitioners pretrain for alignment as well as capabilities. Our models and datasets are available at alignmentpretraining.ai


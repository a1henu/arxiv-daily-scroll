---
layout: default
title: Beyond URLs: Metadata Diversity and Position for Efficient LLM Pretraining
---

# Beyond URLs: Metadata Diversity and Position for Efficient LLM Pretraining
**arXiv**：[2511.21613v1](https://arxiv.org/abs/2511.21613) · [PDF](https://arxiv.org/pdf/2511.21613.pdf)  
**作者**：Dongyang Fan, Diba Hashemi, Sai Praneeth Karimireddy, Martin Jaggi  

**一句话要点**：提出多样化元数据与位置策略以加速大语言模型预训练

**关键词**：大语言模型预训练, 元数据多样性, 训练效率优化, 辅助任务学习, 潜在表示分析

## 3 点简述
- 核心问题：现有方法仅利用URL元数据，忽略其他类型元数据的潜在加速效果
- 方法要点：探索细粒度元数据并引入元数据前置与附加作为辅助任务
- 实验或效果：元数据可提升训练效率，并通过潜在表示分析揭示学习机制

## 摘要（原文）

> Incorporating metadata in Large Language Models (LLMs) pretraining has recently emerged as a promising approach to accelerate training. However prior work highlighted only one useful signal-URLs, leaving open the question of whether other forms of metadata could yield greater benefits. In this study, we investigate a wider range of metadata types and find other types of metadata, such as fine-grained indicators of document quality that can also accelerate pretraining when prepended. We identify a common feature among effective metadata: they encode information at a finer granularity. We further introduce metadata appending as a means of improving training efficiency, where predicting an appropriate metadata as auxiliary task can help speed up pretraining. In addition, learnable meta-tokens trained with masked loss can recover part of the speedup by inducing quality-aware latent structure. Using probing, we analyze latent representations to understand how metadata shapes learning. Together, these results yield practical guidelines for integrating metadata to improve both the efficiency and effectiveness of LLM pretraining.


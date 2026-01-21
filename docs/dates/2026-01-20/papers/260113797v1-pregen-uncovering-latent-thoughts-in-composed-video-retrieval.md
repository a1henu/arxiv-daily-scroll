---
layout: default
title: PREGEN: Uncovering Latent Thoughts in Composed Video Retrieval
---

# PREGEN: Uncovering Latent Thoughts in Composed Video Retrieval
**arXiv**：[2601.13797v1](https://arxiv.org/abs/2601.13797) · [PDF](https://arxiv.org/pdf/2601.13797.pdf)  
**作者**：Gabriele Serussi, David Vainshtein, Jonathan Kouchly, Dotan Di Castro, Chaim Baskin  

**一句话要点**：提出PREGEN框架以解决组合视频检索中视觉语言模型利用不足的问题

**关键词**：组合视频检索, 视觉语言模型, 隐藏状态提取, 轻量编码器, 零样本泛化

## 3 点简述
- 核心问题：现有组合视频检索方法未能充分利用现代视觉语言模型，存在架构过时或计算成本高的问题
- 方法要点：使用冻结预训练视觉语言模型提取隐藏状态，结合轻量编码器生成紧凑嵌入，无需微调
- 实验或效果：在标准基准上显著提升Recall@1，展示强零样本泛化能力

## 摘要（原文）

> Composed Video Retrieval (CoVR) aims to retrieve a video based on a query video and a modifying text. Current CoVR methods fail to fully exploit modern Vision-Language Models (VLMs), either using outdated architectures or requiring computationally expensive fine-tuning and slow caption generation. We introduce PREGEN (PRE GENeration extraction), an efficient and powerful CoVR framework that overcomes these limitations. Our approach uniquely pairs a frozen, pre-trained VLM with a lightweight encoding model, eliminating the need for any VLM fine-tuning. We feed the query video and modifying text into the VLM and extract the hidden state of the final token from each layer. A simple encoder is then trained on these pooled representations, creating a semantically rich and compact embedding for retrieval. PREGEN significantly advances the state of the art, surpassing all prior methods on standard CoVR benchmarks with substantial gains in Recall@1 of +27.23 and +69.59. Our method demonstrates robustness across different VLM backbones and exhibits strong zero-shot generalization to more complex textual modifications, highlighting its effectiveness and semantic capabilities.


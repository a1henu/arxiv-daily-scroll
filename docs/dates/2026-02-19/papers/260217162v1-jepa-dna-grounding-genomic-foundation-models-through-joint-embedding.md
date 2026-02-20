---
layout: default
title: JEPA-DNA: Grounding Genomic Foundation Models through Joint-Embedding Predictive Architectures
---

# JEPA-DNA: Grounding Genomic Foundation Models through Joint-Embedding Predictive Architectures
**arXiv**：[2602.17162v1](https://arxiv.org/abs/2602.17162) · [PDF](https://arxiv.org/pdf/2602.17162.pdf)  
**作者**：Ariel Larey, Elay Dahan, Amit Bleiweiss, Raizy Kellerman, Guy Leib, Omri Nayshool, Dan Ofer, Tal Zinger, Dan Dominissini, Gideon Rechavi, Nicole Bussola, Simon Lee, Shane O'Connell, Dung Hoang, Marissa Wirth, Alexander W. Charney, Nati Daniel, Yoli Shavit  

**一句话要点**：提出JEPA-DNA框架，通过联合嵌入预测架构增强基因组基础模型的全局功能表示能力。

**关键词**：基因组基础模型, 联合嵌入预测架构, 潜在空间监督, 功能表示学习, 零样本任务

## 3 点简述
- 核心问题：现有基因组基础模型依赖掩码语言建模或下一词预测，缺乏全局生物功能上下文。
- 方法要点：结合联合嵌入预测架构与生成目标，在潜在空间监督CLS令牌以预测掩码片段的高层功能嵌入。
- 实验或效果：在多种基因组基准测试中，JEPA-DNA在监督和零样本任务上表现优于仅生成基线。

## 摘要（原文）

> Genomic Foundation Models (GFMs) have largely relied on Masked Language Modeling (MLM) or Next Token Prediction (NTP) to learn the language of life. While these paradigms excel at capturing local genomic syntax and fine-grained motif patterns, they often fail to capture the broader functional context, resulting in representations that lack a global biological perspective. We introduce JEPA-DNA, a novel pre-training framework that integrates the Joint-Embedding Predictive Architecture (JEPA) with traditional generative objectives. JEPA-DNA introduces latent grounding by coupling token-level recovery with a predictive objective in the latent space by supervising a CLS token. This forces the model to predict the high-level functional embeddings of masked genomic segments rather than focusing solely on individual nucleotides. JEPA-DNA extends both NTP and MLM paradigms and can be deployed either as a standalone from-scratch objective or as a continual pre-training enhancement for existing GFMs. Our evaluations across a diverse suite of genomic benchmarks demonstrate that JEPA-DNA consistently yields superior performance in supervised and zero-shot tasks compared to generative-only baselines. By providing a more robust and biologically grounded representation, JEPA-DNA offers a scalable path toward foundation models that understand not only the genomic alphabet, but also the underlying functional logic of the sequence.


---
layout: default
title: One Instruction Does Not Fit All: How Well Do Embeddings Align Personas and Instructions in Low-Resource Indian Languages?
---

# One Instruction Does Not Fit All: How Well Do Embeddings Align Personas and Instructions in Low-Resource Indian Languages?
**arXiv**：[2601.10205v1](https://arxiv.org/abs/2601.10205) · [PDF](https://arxiv.org/pdf/2601.10205.pdf)  
**作者**：Arya Shah, Himanshu beniwal, Mayank Singh  

**一句话要点**：提出多语言嵌入模型基准以评估印度语言中人物与指令的兼容性对齐。

**关键词**：多语言嵌入模型, 人物指令对齐, 低资源语言, 检索基准, 兼容性分类, 印度语言

## 3 点简述
- 核心问题：现有基准未评估嵌入模型能否独立编码人物与指令的兼容性，尤其在低资源印度语言中。
- 方法要点：构建统一基准覆盖12种印度语言，包括检索和分类任务，评估八个多语言嵌入模型。
- 实验或效果：E5-Large-Instruct在单语检索中Recall@1达27.4%，LaBSE在分类中AUROC为75.3%。

## 摘要（原文）

> Aligning multilingual assistants with culturally grounded user preferences is essential for serving India's linguistically diverse population of over one billion speakers across multiple scripts. However, existing benchmarks either focus on a single language or conflate retrieval with generation, leaving open the question of whether current embedding models can encode persona-instruction compatibility without relying on response synthesis. We present a unified benchmark spanning 12 Indian languages and four evaluation tasks: monolingual and cross-lingual persona-to-instruction retrieval, reverse retrieval from instruction to persona, and binary compatibility classification. Eight multilingual embedding models are evaluated in a frozen-encoder setting with a thin logistic regression head for classification. E5-Large-Instruct achieves the highest Recall@1 of 27.4\% on monolingual retrieval and 20.7\% on cross-lingual transfer, while BGE-M3 leads reverse retrieval at 32.1\% Recall@1. For classification, LaBSE attains 75.3\% AUROC with strong calibration. These findings offer practical guidance for model selection in Indic multilingual retrieval and establish reproducible baselines for future work\footnote{Code, datasets, and models are publicly available at https://github.com/aryashah2k/PI-Indic-Align.

